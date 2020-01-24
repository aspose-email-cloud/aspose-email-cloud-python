import sys, os, pytest, uuid, base64, functools, dateutil.parser
sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import api, models
from AsposeEmailCloudSdk.models import requests
from datetime import timedelta, datetime
from conftest import TestData
from dateutil import tz

@pytest.mark.pipeline
def test_hierarchical(td: TestData):
    """
    HierarchicalObject serialization and deserialization test.
    This test checks that BaseObject.Type field filled automatically by SDK
    and properly used in serialization and deserialization
    """
    calendarFile = _create_calendar(td)
    calendar = td.email.get_calendar(requests.GetCalendarRequest(calendarFile, td.folder, td.storage))
    assert calendar.name == 'CALENDAR'
    assert calendar.type == 'HierarchicalObject'
    primitive_properties = list(filter(lambda x: x.type == 'PrimitiveObject', calendar.internal_properties))
    assert len(primitive_properties) >= 3
    assert primitive_properties[0].value is not None

@pytest.mark.pipeline
def test_async(td: TestData):
    """
    Asynchronous API call test
    """
    calendarFile = _create_calendar(td)
    calendar = td.email.get_calendar_async(requests.GetCalendarRequest(calendarFile, td.folder, td.storage)).get()
    assert calendar.name == 'CALENDAR'

@pytest.mark.pipeline
def test_file(td: TestData):
    """
    File support test
    """
    sample = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.ics')
    file_name = str(uuid.uuid4()) + ".ics"
    storage_location = td.folder + "/" + file_name
    td.email.upload_file(requests.UploadFileRequest(storage_location, sample, td.storage))
    rq = requests.UploadFileRequest(storage_location, sample, td.storage)
    downloaded = td.email.download_file(requests.DownloadFileRequest(storage_location, td.storage))
    with open(downloaded, 'r') as f:
        filedata = f.read()
        assert 'Broadway' in filedata

@pytest.mark.pipeline
def test_contact_format(td: TestData):
    """
    Contact format specified as Enum, but SDK represents it as a string.
    Test checks that value parsing works properly
    """
    for contact_format in ['vcard', 'msg']:
        extension = '.vcf' if contact_format == 'vcard' else '.msg'
        name = str(uuid.uuid4()) + extension
        td.email.create_contact(
            requests.CreateContactRequest(
                contact_format,
                name,
                models.HierarchicalObjectRequest(
                    models.HierarchicalObject('CONTACT', internal_properties=[]),
                    models.StorageFolderLocation(td.storage, td.folder))))
        object_exist = td.email.object_exists(requests.ObjectExistsRequest(
            td.folder + "/" + name,
            td.storage))
        assert object_exist.exists
    pass

@pytest.mark.pipeline
def test_date_time(td: TestData):
    """
    Test datetime serialization and deserialization.
    Checks that SDK and Backend do not change datetime during processing.
    In most cases developer should carefully serialize and deserialize datetime
    """
    start_date = datetime.today() + timedelta(days=1)
    start_date = start_date.replace(microsecond=0, tzinfo=tz.tzutc())
    calendar_storage = _create_calendar(td, start_date)
    calendar = td.email.get_calendar(requests.GetCalendarRequest(
        calendar_storage,
        td.folder,
        td.storage)) # type: models.HierarchicalObject
    start_date_property = list(filter(lambda item: item.name == 'STARTDATE', calendar.internal_properties))[0]
    fact_start_date = dateutil.parser.parse(start_date_property.value)
    assert start_date == fact_start_date

@pytest.mark.ai
def test_ai_bcr_parse_storage(td: TestData):
    file_name = str(uuid.uuid4())+ ".png"
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    # 1) Upload business card image to storage
    storage_location = td.folder + "/" + file_name
    td.email.upload_file(requests.UploadFileRequest(storage_location, image_file, td.storage))

    out_folder = str(uuid.uuid4())
    out_folder_path = td.folder + "/" + out_folder
    td.email.create_folder(requests.CreateFolderRequest(out_folder_path, td.storage))
    # 2) Call business card recognition action
    result = td.email.ai_bcr_parse_storage(requests.AiBcrParseStorageRequest(
        models.AiBcrParseStorageRq(
            images=[models.AiBcrImageStorageFile(True, models.StorageFileLocation(td.storage, td.folder, file_name))],
            out_folder=models.StorageFolderLocation(td.storage, out_folder_path)))) # type: models.ListResponseOfStorageFileLocation
    # Check that only one file produced
    assert len(result.value) == 1
    # 3) Get file name from recognition result
    contact_file = result.value[0] # type: models.StorageFileLocation
    # 4) Download VCard file, produced by recognition method, check it contains text "Thomas"
    downloaded = td.email.download_file(requests.DownloadFileRequest(
        contact_file.folder_path + "/" + contact_file.file_name,
        td.storage))
    with open(downloaded, 'r') as f:
        filedata = f.read()
        assert 'Thomas' in filedata
    # 5) Get VCard object properties list, check that there are 3 properties or more
    contact_properties = td.email.get_contact_properties(requests.GetContactPropertiesRequest(
        'VCard', contact_file.file_name, contact_file.folder_path, contact_file.storage)) # type: models.HierarchicalObject
    assert len(contact_properties.internal_properties) >= 3

@pytest.mark.ai
def test_ai_bcr_parse(td: TestData):
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    image_data = None
    with open(image_file, 'rb') as f:
        filedata = f.read()
        image_data = str(base64.b64encode(filedata), 'utf-8')
    result = td.email.ai_bcr_parse(requests.AiBcrParseRequest(
        models.AiBcrBase64Rq(images=[models.AiBcrBase64Image(True, image_data)]))) # type: models.ListResponseOfHierarchicalObject
    assert len(result.value) == 1
    display_name = list(filter(
        lambda prop: prop.type == 'PrimitiveObject' and prop.name == 'DISPLAYNAME',
        result.value[0].internal_properties))[0]
    assert 'Thomas' in display_name.value

@pytest.mark.ai
def test_ai_name_genderize(td: TestData):
    """ Test name gender detection """
    result = td.email.ai_name_genderize(
        requests.AiNameGenderizeRequest('John Cane')) # type: models.ListResponseOfAiNameGenderHypothesis
    assert len(result.value) >= 1
    assert result.value[0].gender == 'Male'

@pytest.mark.ai
def test_ai_name_format(td: TestData):
    result = td.email.ai_name_format(
        requests.AiNameFormatRequest(
            'Mr. John Michael Cane',
            format='%t%L%f%m')) # type: models.AiNameFormatted
    assert result.name == 'Mr. Cane J. M.'

@pytest.mark.ai
def test_ai_name_match(td: TestData):
    first = 'John Michael Cane'
    second = 'Cane J.'
    result = td.email.ai_name_match(
        requests.AiNameMatchRequest(first, second)) # type: models.AiNameMatchResult
    assert result.similarity >= 0.5

@pytest.mark.ai
def test_ai_name_expand(td: TestData):
    name = 'Smith Bobby'
    result = td.email.ai_name_expand(
        requests.AiNameExpandRequest(name)) # type: models.AiNameWeightedVariants
    expandedNames = list(weighted.name for weighted in result.names)
    assert 'Mr. Smith' in expandedNames
    assert 'B. Smith' in expandedNames

@pytest.mark.ai
def test_ai_name_complete(td: TestData):
    prefix = 'Dav'
    result = td.email.ai_name_complete(
        requests.AiNameCompleteRequest(prefix)) # type: models.AiNameWeightedVariants
    names = list(prefix + weighted.name for weighted in result.names)
    assert 'David' in names
    assert 'Dave' in names
    assert 'Davis' in names

@pytest.mark.ai
def test_ai_name_parse_email_address(td: TestData):
    address = 'john-cane@gmail.com'
    result = td.email.ai_name_parse_email_address(
        requests.AiNameParseEmailAddressRequest(address))
    names = (extracted.name for extracted in result.value)
    extracted_values = list(functools.reduce(lambda a,b: a+b, names))
    given_name = next((x for x in extracted_values if x.category == 'GivenName'))
    surname = next((x for x in extracted_values if x.category == 'Surname'))
    assert given_name.value == 'John'
    assert surname.value == 'Cane'

@pytest.mark.pipeline
def test_create_calendar_email(td: TestData):
    calendar = models.CalendarDto()
    calendar.attendees = [models.MailAddress('Attendee Name', 'attendee@aspose.com', 'Accepted')]
    calendar.description = 'Some description'
    calendar.summary = 'Some summary'
    calendar.organizer = models.MailAddress('Organizer Name', 'organizer@aspose.com', 'Accepted')
    calendar.start_date = datetime.today() + timedelta(days=1)
    calendar.end_date = calendar.start_date + timedelta(hours=1)
    calendar.location = 'Some location'

    folder_location = models.StorageFolderLocation(td.storage, td.folder)
    calendar_file = str(uuid.uuid4()) + '.ics'
    td.email.save_calendar_model(
        requests.SaveCalendarModelRequest(
            calendar_file,
            models.StorageModelRqOfCalendarDto(calendar, folder_location)))
    exist_result = td.email.object_exists(
        requests.ObjectExistsRequest(td.folder + '/' + calendar_file, td.storage))
    assert exist_result.exists

    alternate = td.email.convert_calendar_model_to_alternate(
        requests.ConvertCalendarModelToAlternateRequest(
            models.CalendarDtoAlternateRq(calendar, 'Create')))

    email = models.EmailDto(
        alternate_views=[alternate],
        # 'from' is reserved, so from field is named '_from':
        _from=models.MailAddress('From Name', 'organizer@aspose.com'),
        to=[models.MailAddress('To Name', 'attendee@aspose.com')],
        subject='Some subject',
        body='Some body')

    email_file = str(uuid.uuid4())+ '.eml'
    td.email.save_email_model(
        requests.SaveEmailModelRequest(
            'Eml', email_file,
            models.StorageModelRqOfEmailDto(email, folder_location)))

    downloaded = td.email.download_file(
        requests.DownloadFileRequest(
            td.folder + '/' + email_file,
            td.storage))
    with open(downloaded, 'r') as f:
        file_data = f.read()
        assert 'attendee@aspose.com' in file_data


@pytest.mark.pipeline
def test_contact_model(td: TestData):
    contact = models.ContactDto(
        gender='Male',
        surname='Thomas',
        given_name='Alex',
        email_addresses=[
            models.EmailAddress(
                models.EnumWithCustomOfEmailAddressCategory('Work'),
                'Alex Thomas', True, address='alex.thomas@work.com')],
        phone_numbers=[
            models.PhoneNumber(
                models.EnumWithCustomOfPhoneNumberCategory('Work'),
                '+49211424721', True)])

    contact_file = str(uuid.uuid4())+ '.vcf'
    td.email.save_contact_model(
        requests.SaveContactModelRequest(
            'VCard', contact_file,
            models.StorageModelRqOfContactDto(
                contact,
                models.StorageFolderLocation(td.storage, td.folder))))
    exist_result = td.email.object_exists(
        requests.ObjectExistsRequest(td.folder + '/' + contact_file, td.storage))
    assert exist_result.exists

@pytest.mark.ai
def test_ai_bcr_parse_model(td: TestData):
    image_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_single_0001.png')
    image_data = None
    with open(image_file, 'rb') as f:
        filedata = f.read()
        image_data = str(base64.b64encode(filedata), 'utf-8')
    result = td.email.ai_bcr_parse_model(requests.AiBcrParseModelRequest(
        models.AiBcrBase64Rq(images=[models.AiBcrBase64Image(True, image_data)])))
    assert len(result.value) == 1
    first_vcard = result.value[0]
    assert 'Thomas' in first_vcard.display_name

def _create_calendar(td, start_date_param=None):
    name = str(uuid.uuid4())+ '.ics'
    start_date = (
        start_date_param if start_date_param is not None
        else datetime.today() + timedelta(days=1))
    end_date = start_date + timedelta(hours=1)
    request = requests.CreateCalendarRequest(
        name,
        models.HierarchicalObjectRequest(
            models.HierarchicalObject('CALENDAR', internal_properties=[
                models.PrimitiveObject(name="LOCATION", value="location"),
                models.PrimitiveObject("STARTDATE", None, start_date.isoformat()),
                models.PrimitiveObject("ENDDATE", None, end_date.isoformat()),
                models.HierarchicalObject("ORGANIZER", None, internal_properties=[
                    models.PrimitiveObject("ADDRESS", value="organizer@am.ru"),
                    models.PrimitiveObject("DISPLAYNAME", value="Piu Man")
                ]),
                models.HierarchicalObject("ATTENDEES", internal_properties=[
                    models.IndexedHierarchicalObject("ATTENDEE", index=0, internal_properties=[
                        models.PrimitiveObject("ADDRESS", value="attendee@am.ru"),
                        models.PrimitiveObject("DISPLAYNAME", value="Attendee Name")
                    ])
                ])
            ]),
        models.StorageFolderLocation(td.storage, td.folder)
    ))
    td.email.create_calendar(request)
    return name