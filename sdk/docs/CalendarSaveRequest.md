# AsposeEmailCloudSdk.models.CalendarSaveRequest

Save iCalendar to storage request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Calendar file format Enum, available values: Ics, Msg |

Parent class: [StorageModelOfCalendarDto](StorageModelOfCalendarDto.md)


## Example
```python
calendar_save_request = models.CalendarSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='calendar.ics',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
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

