import os
import sys
import uuid

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from conftest import EmailApiData
from datetime import timedelta, datetime


@pytest.mark.pipeline
def test_create_calendar_email(td: EmailApiData):
    calendar = calendar_dto()
    calendar_file = str(uuid.uuid4()) + '.ics'
    td.api.calendar.save(
        models.CalendarSaveRequest(
            models.StorageFileLocation(td.storage, td.folder, calendar_file),
            calendar, "Ics"))
    exist_result = td.api.cloud_storage.storage.object_exists(
        models.ObjectExistsRequest(td.folder + '/' + calendar_file, td.storage))
    assert exist_result.exists

    alternate = td.api.calendar.as_alternate(models.CalendarAsAlternateRequest(calendar, "Create"))

    email = models.EmailDto(
        alternate_views=[alternate],
        # 'from' is reserved, so from field is named '_from':
        _from=models.MailAddress('From Name', 'organizer@aspose.com'),
        to=[models.MailAddress('To Name', 'attendee@aspose.com')],
        subject='Some subject',
        body='Some body')

    email_file = str(uuid.uuid4()) + '.eml'
    td.api.email.save(models.EmailSaveRequest(
        models.StorageFileLocation(td.storage, td.folder, email_file),
        email, 'Eml'))

    downloaded = td.api.cloud_storage.file.download_file(
        models.DownloadFileRequest(
            td.folder + '/' + email_file,
            td.storage))
    with open(downloaded, 'r') as f:
        file_data = f.read()
        assert 'attendee@aspose.com' in file_data


@pytest.mark.pipeline
def test_calendar_converter(td: EmailApiData):
    email = td.api
    # Create DTO with specified location:
    calendar = calendar_dto()
    # We can convert this DTO to a MAPI or ICS file
    mapi = email.calendar.as_file(models.CalendarAsFileRequest('Msg', calendar))
    # Let's convert this file to ICS format:
    ics = email.calendar.convert(models.CalendarConvertRequest('Ics', mapi))
    # ICS is a text format. We can read the file to a string and check that it
    # contains specified location as a substring:
    with open(ics, 'r') as f:
        file_data = f.read()
        assert calendar.location in file_data
    # We can also convert the file back to a CalendarDto
    dto = email.calendar.from_file(models.CalendarFromFileRequest(ics))
    assert calendar.location == dto.location


@pytest.mark.pipeline
def test_convert_model_to_mapi_model(td: EmailApiData):
    calendar = calendar_dto()
    mapi_calendar = td.api.calendar.as_mapi(calendar)
    assert calendar.location == mapi_calendar.location
    assert 'MapiCalendarDailyRecurrencePatternDto' == mapi_calendar.recurrence.recurrence_pattern.discriminator


def calendar_dto():
    calendar = models.CalendarDto()
    calendar.attendees = [models.MailAddress('Attendee Name', 'attendee@aspose.com', 'Accepted')]
    calendar.description = 'Some description'
    calendar.summary = 'Some summary'
    calendar.organizer = models.MailAddress('Organizer Name', 'organizer@aspose.com', 'Accepted')
    calendar.start_date = datetime.today() + timedelta(days=1)
    calendar.end_date = calendar.start_date + timedelta(hours=1)
    calendar.location = 'Some location'
    calendar.recurrence = models.DailyRecurrencePatternDto(None, 10, None, 'Monday')
    return calendar
