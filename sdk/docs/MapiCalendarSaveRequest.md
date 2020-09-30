# AsposeEmailCloudSdk.models.MapiCalendarSaveRequest

Save MapiCalendar to storage request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Calendar file format Enum, available values: Ics, Msg |

Parent class: [StorageModelOfMapiCalendarDto](StorageModelOfMapiCalendarDto.md)


## Example
```python
mapi_calendar_save_request = models.MapiCalendarSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='calendar.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiCalendarDto(
        attendees=models.MapiCalendarAttendeesDto(
            appointment_recipients=[
                models.MapiRecipientDto(
                    email_address='organizer@aspose.com',
                    address_type='SMTP',
                    display_name='Organizer Name',
                    recipient_type='MapiTo'),
                models.MapiRecipientDto(
                    email_address='attendee@aspose.com',
                    address_type='SMTP',
                    display_name='Attendee Name',
                    recipient_type='MapiTo')]),
        busy_status='Tentative',
        client_intent=[
            'Manager'],
        end_date=datetime.today(),
        location='Some location',
        recurrence=models.MapiCalendarEventRecurrenceDto(
            recurrence_pattern=models.MapiCalendarDailyRecurrencePatternDto(
                frequency='Daily',
                occurrence_count=10,
                week_start_day='Monday')),
        start_date=datetime.today(),
        organizer=models.MapiElectronicAddressDto(
            email_address='organizer@aspose.com'),
        body='Some description',
        subject='Some summary'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

