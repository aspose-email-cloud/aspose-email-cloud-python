# AsposeEmailCloudSdk.models.MapiCalendarAsFileRequest

Convert MapiCalendar to file request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Calendar file format Enum, available values: Ics, Msg |
**value** |[**MapiCalendarDto**](MapiCalendarDto.md) |MAPI calendar model.              |



## Example
```python
mapi_calendar_as_file_request = models.MapiCalendarAsFileRequest(
    format='Msg',
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

