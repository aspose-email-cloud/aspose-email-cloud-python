import sys, os, pytest, uuid
sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import api, models
from AsposeEmailCloudSdk.models import requests
from datetime import timedelta, datetime
from conftest import TestData
from dateutil import tz
import dateutil.parser


def test_hierarchical(test_data: TestData):
    """
    HierarchicalObject serialization and deserialization test.
    This test checks that BaseObject.Type field filled automatically by SDK
    and properly used in serialization and deserialization
    """
    calendarFile = _create_calendar(test_data)
    calendar = test_data.email.get_calendar(requests.GetCalendarRequest(calendarFile, test_data.folder, test_data.storage))
    assert calendar.name == 'CALENDAR'
    assert calendar.type == 'HierarchicalObject'
    primitive_properties = list(filter(lambda x: x.type == 'PrimitiveObject', calendar.internal_properties))
    assert len(primitive_properties) >= 3

def test_async(test_data: TestData):
    """
    Asynchronous API call test
    """
    calendarFile = _create_calendar(test_data)
    calendar = test_data.email.get_calendar_async(requests.GetCalendarRequest(calendarFile, test_data.folder, test_data.storage)).get()
    assert calendar.name == 'CALENDAR'

def test_file(test_data: TestData):
    """
    File support test
    """
    sample = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.ics')
    fileName = str(uuid.uuid4()) + ".ics"
    storageLocation = test_data.folder + "/" + fileName
    test_data.email.upload_file(requests.UploadFileRequest(storageLocation, sample, test_data.storage))
    downloaded = test_data.email.download_file(requests.DownloadFileRequest(storageLocation, test_data.storage))
    with open(downloaded, 'r') as f:
        filedata = f.read()
        assert 'Broadway' in filedata

def test_contact_format(test_data: TestData):
    """
    Contact format specified as Enum, but SDK represents it as a string.
    Test checks that value parsing works properly
    """
    for contact_format in ['vcard', 'msg']:
        extension = '.vcf' if contact_format == 'vcard' else '.msg'
        name = str(uuid.uuid4()) + extension
        test_data.email.create_contact(
            requests.CreateContactRequest(
                contact_format,
                name,
                models.HierarchicalObjectRequest(
                    models.HierarchicalObject('CONTACT', internal_properties=[]),
                    models.StorageFolderLocation(test_data.storage, test_data.folder))))
        object_exist = test_data.email.object_exists(requests.ObjectExistsRequest(
            test_data.folder + "/" + name,
            test_data.storage))
        assert object_exist.exists
    pass

def test_date_time(test_data: TestData):
    """
    Test datetime serialization and deserialization.
    Checks that SDK and Backend do not change datetime during processing.
    In most cases developer should carefully serialize and deserialize datetime
    """
    start_date = datetime.today() + timedelta(days=1)
    start_date = start_date.replace(microsecond=0, tzinfo=tz.tzutc())
    calendar_storage = _create_calendar(test_data, start_date)
    calendar = test_data.email.get_calendar(requests.GetCalendarRequest(
        calendar_storage,
        test_data.folder,
        test_data.storage)) # type: models.HierarchicalObject
    start_date_property = list(filter(lambda item: item.name == 'STARTDATE', calendar.internal_properties))[0]
    fact_start_date = dateutil.parser.parse(start_date_property.value)
    assert start_date == fact_start_date

def _create_calendar(test_data, start_date_param=None):
    name = str(uuid.uuid4())+ ".ics"
    start_date = start_date_param if start_date_param is not None else datetime.today() + timedelta(days=1)
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
        models.StorageFolderLocation(test_data.storage, test_data.folder)
    ))
    test_data.email.create_calendar(request)
    return name