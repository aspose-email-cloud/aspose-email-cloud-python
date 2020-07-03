import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from AsposeEmailCloudSdk.models import requests
from conftest import EmailApiData
from datetime import timedelta, datetime
import dateutil.parser
from dateutil import tz


@pytest.mark.pipeline
def test_hierarchical(td: EmailApiData):
    """
    HierarchicalObject serialization and deserialization test.
    This test checks that BaseObject.Type field filled automatically by SDK
    and properly used in serialization and deserialization
    """
    calendar_file = td.create_calendar()
    calendar = td.email.get_calendar(requests.GetCalendarRequest(calendar_file, td.folder, td.storage))
    assert calendar.name == 'CALENDAR'
    assert calendar.type == 'HierarchicalObject'
    primitive_properties = list(filter(lambda x: x.type == 'PrimitiveObject', calendar.internal_properties))
    assert len(primitive_properties) >= 3
    # noinspection PyTypeChecker
    first = primitive_properties[0]  # type: models.PrimitiveObject
    assert first.value is not None


@pytest.mark.pipeline
def test_async(td: EmailApiData):
    """
    Asynchronous API call test
    """
    calendar_file = td.create_calendar()
    calendar = td.email.get_calendar_async(requests.GetCalendarRequest(calendar_file, td.folder, td.storage)).get()
    assert calendar.name == 'CALENDAR'


@pytest.mark.pipeline
def test_date_time(td: EmailApiData):
    """
    Test datetime serialization and deserialization.
    Checks that SDK and Backend do not change datetime during processing.
    In most cases developer should carefully serialize and deserialize datetime
    """
    start_date = datetime.today() + timedelta(days=1)
    start_date = start_date.replace(microsecond=0, tzinfo=tz.tzutc())
    calendar_storage = td.create_calendar(start_date)
    calendar = td.email.get_calendar(requests.GetCalendarRequest(
        calendar_storage,
        td.folder,
        td.storage))  # type: models.HierarchicalObject
    # noinspection PyTypeChecker
    start_date_property = list(
        filter(lambda item: item.name == 'STARTDATE', calendar.internal_properties))[0]  # type: models.PrimitiveObject
    fact_start_date = dateutil.parser.parse(start_date_property.value)
    assert start_date == fact_start_date


@pytest.mark.pipeline
def test_create_calendar_email(td: EmailApiData):
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

    email_file = str(uuid.uuid4()) + '.eml'
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
def test_calendar_converter(td: EmailApiData):
    email = td.email
    location = 'Some location'
    # Create DTO with specified location:
    calendar_dto = models.CalendarDto()
    calendar_dto.location = location
    calendar_dto.summary = 'Some summary'
    calendar_dto.description = 'Some description'
    calendar_dto.start_date = datetime.today()
    calendar_dto.end_date = datetime.today()
    calendar_dto.organizer = models.MailAddress(address='organizer@aspose.com')
    calendar_dto.attendees = [models.MailAddress(address='attendee@aspose.com')]
    # We can convert this DTO to a MAPI or ICS file
    mapi = email.convert_calendar_model_to_file(requests.ConvertCalendarModelToFileRequest('Msg', calendar_dto))
    # Let's convert this file to ICS format:
    ics = email.convert_calendar(requests.ConvertCalendarRequest('Ics', mapi))
    # ICS is a text format. We can read the file to a string and check that it
    # contains specified location as a substring:
    with open(ics, 'r') as f:
        file_data = f.read()
        assert location in file_data
    # We can also convert the file back to a CalendarDto
    dto = email.get_calendar_file_as_model(requests.GetCalendarFileAsModelRequest(ics))
    assert location == dto.location
