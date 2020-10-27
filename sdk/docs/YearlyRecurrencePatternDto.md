# AsposeEmailCloudSdk.models.YearlyRecurrencePatternDto

Yearly recurrence pattern.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_day** |**str** |Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay |
**start_month** |**str** |Represents a calendar month. Enum, available values: None, January, February, March, April, May, June, July, August, September, October, November, December |
**start_offset** |**int** |Start offset.              |
**start_position** |**str** |Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last |

Parent class: [RecurrencePatternDto](RecurrencePatternDto.md)


## Example
```python
yearly_recurrence_pattern_dto = models.YearlyRecurrencePatternDto(
    start_month='January',
    start_offset=30,
    interval=-1,
    week_start='Monday')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

