# AsposeEmailCloudSdk.models.CalendarStorageList

iCalendar models list with corresponding storage locations.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [ListResponseOfStorageModelOfCalendarDto](ListResponseOfStorageModelOfCalendarDto.md)


## Example
```python
calendar_storage_list = models.CalendarStorageList(
    value=[
        models.StorageModelOfCalendarDto(
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
                summary='Some summary'))])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

