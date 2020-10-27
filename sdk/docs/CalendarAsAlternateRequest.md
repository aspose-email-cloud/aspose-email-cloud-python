# AsposeEmailCloudSdk.models.CalendarAsAlternateRequest

Convert iCalendar to AlternateView request             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** |[**CalendarDto**](CalendarDto.md) |iCalendar document model              |
**action** |**str** |iCalendar actions. Enum, available values: Create, Update, Cancel |
**sequence_id** |**str** |iCalendar sequence id              |[optional] 



## Example
```python
calendar_as_alternate_request = models.CalendarAsAlternateRequest(
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'),
    sequence_id='cf4ffb6c-895d-4e58-bdb4-0a3918e96a43')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

