# AsposeEmailCloudSdk.models.TaskRegeneratingPatternDto

Represents the regenerating recurrence pattern that specifies how many days, weeks, months or years after the completion of the current task the next occurrence will be due.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regenerating_type** |**str** |Enumerates the types of regenerating pattern. Enum, available values: Daily, Weekly, Monthly, Yearly |

Parent class: [RecurrencePatternDto](RecurrencePatternDto.md)


## Example
```python
task_regenerating_pattern_dto = models.TaskRegeneratingPatternDto(
    interval=1,
    occurs=2,
    end_date=datetime.today(),
    week_start='Sunday')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

