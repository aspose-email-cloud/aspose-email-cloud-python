# AsposeEmailCloudSdk.models.RecurrencePatternDto

iCalendar recurrence pattern.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** |**int** |Number of recurrence units.              |
**occurs** |**int** |Number of occurrences of the recurrence pattern.              |
**end_date** |**datetime** |End date.              |
**week_start** |**str** |Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay |
**discriminator** |**str** | |



## Example
```python
recurrence_pattern_dto = models.RecurrencePatternDto(
    interval=-1,
    week_start='Monday')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

