import os
import sys
import uuid
from datetime import datetime

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../sdk"))
from AsposeEmailCloudSdk import models
from conftest import EmailApiData


@pytest.mark.pipeline
def test_mapi_model_to_general_model(td: EmailApiData):
    mapi_calendar = mapi_calendar_dto()
    calendar = td.api.mapi.calendar.as_calendar_dto(mapi_calendar)
    assert mapi_calendar.subject == calendar.summary
    assert mapi_calendar.location == calendar.location


@pytest.mark.pipeline
def test_mapi_model_to_file(td: EmailApiData):
    mapi_calendar = mapi_calendar_dto()
    ics_file = td.api.mapi.calendar.as_file(models.MapiCalendarAsFileRequest('Ics', mapi_calendar))
    with open(ics_file, 'r') as f:
        file_data = f.read()
        assert mapi_calendar.location in file_data
    mapi_calendar_converted = td.api.mapi.calendar.from_file(models.MapiCalendarFromFileRequest(ics_file))
    assert mapi_calendar.location == mapi_calendar_converted.location


@pytest.mark.pipeline
def test_storage_support(td: EmailApiData):
    file_name = str(uuid.uuid4()) + '.msg'
    mapi_calendar = mapi_calendar_dto()
    td.api.mapi.calendar.save(models.MapiCalendarSaveRequest(
        models.StorageFileLocation(td.storage, td.folder, file_name),
        mapi_calendar, 'Msg'))
    mapi_calendar_from_storage = td.api.mapi.calendar.get(
        models.MapiCalendarGetRequest(file_name, td.folder, td.storage))
    assert mapi_calendar.location == mapi_calendar_from_storage.location


def mapi_calendar_dto():
    mapi_calendar = models.MapiCalendarDto()
    mapi_calendar.attendees = models.MapiCalendarAttendeesDto([mapi_recipient_dto()])
    mapi_calendar.client_intent = ['Manager']
    mapi_calendar.recurrence = recurrence_dto()
    mapi_calendar.organizer = models.MapiElectronicAddressDto(None, 'organizer@aspose.com')
    mapi_calendar.busy_status = 'Tentative'
    mapi_calendar.start_date = datetime.today()
    mapi_calendar.end_date = datetime.today()
    mapi_calendar.location = 'Some location'
    mapi_calendar.body = 'Some description'
    mapi_calendar.body_type = 'PlainText'
    mapi_calendar.subject = 'Some summary'
    return mapi_calendar


def recurrence_dto():
    recurrence = models.MapiCalendarEventRecurrenceDto()
    recurrence_pattern = models.MapiCalendarDailyRecurrencePatternDto()
    recurrence_pattern.occurrence_count = 10
    recurrence_pattern.week_start_day = 'Monday'
    recurrence.recurrence_pattern = recurrence_pattern
    return recurrence


def mapi_recipient_dto():
    mapi_recipient = models.MapiRecipientDto()
    mapi_recipient.address_type = 'SMTP'
    mapi_recipient.display_name = 'Attendee Name'
    mapi_recipient.email_address = 'attendee@aspose.com'
    mapi_recipient.recipient_type = 'MapiTo'
    return mapi_recipient
