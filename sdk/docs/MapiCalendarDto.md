# AsposeEmailCloudSdk.models.MapiCalendarDto

Represents the mapi calendar object             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment_counter_proposal** |**bool** |Value indicating whether a Meeting Response object is a counter proposal.              |
**attendees** |[**MapiCalendarAttendeesDto**](MapiCalendarAttendeesDto.md) |Attendees              |[optional] 
**busy_status** |**str** |Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice |
**client_intent** |**list[str]** |Actions the user has taken on this Meeting object.              Items: Enumerates the actions the user can taken on the Meeting object Enum, available values: Manager, Delegate, DeletedWithNoResponse, DeletedExceptionWithNoResponse, RespondedTentative, RespondedAccept, RespondedDecline, ModifiedStartTime, ModifiedEndTime, ModifiedLocation, RespondedExceptionDecline, Canceled, ExceptionCanceled |[optional] 
**end_date** |**datetime** |End date and time of the event. If the date is not set, default value for DateTime is returned.              |
**end_date_time_zone** |[**MapiCalendarTimeZoneDto**](MapiCalendarTimeZoneDto.md) |Time zone information that indicates the time zone of the EndDate property.              |[optional] 
**is_all_day** |**bool** |Value indicating whether the event is an all-day event.              |
**key_words** |**str** |Categories of the calendar object.              |[optional] 
**location** |**str** |Location of the event.              |[optional] 
**recurrence** |[**MapiCalendarEventRecurrenceDto**](MapiCalendarEventRecurrenceDto.md) |Recurrence properties.              |[optional] 
**reminder_delta** |**int** |Interval, in minutes, between the time at which the reminder first becomes overdue and the start time of the Calendar object.              |
**reminder_file_parameter** |**str** |Full path of the sound that a client SHOULD play when the reminder becomes overdue.              |[optional] 
**reminder_set** |**bool** |Value indicating whether a reminder is set on the object.              |
**sequence** |**int** |Sequence number.              |
**start_date** |**datetime** |Start date and time of the event. If the date is not set, default value for DateTime is returned.              |
**start_date_time_zone** |[**MapiCalendarTimeZoneDto**](MapiCalendarTimeZoneDto.md) |Time zone information that indicates the time zone of the StartDate property.              |[optional] 
**uid** |**str** |Unique identifier.              |[optional] 
**organizer** |[**MapiElectronicAddressDto**](MapiElectronicAddressDto.md) |Organizer              |[optional] 

Parent class: [MapiMessageItemBaseDto](MapiMessageItemBaseDto.md)


## Example
```python
mapi_calendar_dto = models.MapiCalendarDto(
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
    subject='Some summary')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

