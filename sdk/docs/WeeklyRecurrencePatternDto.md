# AsposeEmailCloudSdk.models.WeeklyRecurrencePatternDto

Weekly recurrence pattern.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_days** |**list[str]** |Start days              Items: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay |[optional] 

Parent class: [RecurrencePatternDto](RecurrencePatternDto.md)


## Example
```python
weekly_recurrence_pattern_dto = models.WeeklyRecurrencePatternDto(
    start_days=[
        'Tuesday',
        'Thursday'],
    interval=-1,
    occurs=10,
    week_start='Sunday')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

