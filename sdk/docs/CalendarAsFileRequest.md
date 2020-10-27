# AsposeEmailCloudSdk.models.CalendarAsFileRequest

iCalendar model to file request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Calendar file format Enum, available values: Ics, Msg |
**value** |[**CalendarDto**](CalendarDto.md) |iCalendar model              |



## Example
```python
calendar_as_file_request = models.CalendarAsFileRequest(
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
        summary='Some summary'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

