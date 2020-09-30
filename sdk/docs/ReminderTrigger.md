# AsposeEmailCloudSdk.models.ReminderTrigger

Specifies when an alarm will trigger.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** |**datetime** |A trigger set to an absolute date/time. |
**duration** |**int** |Specifies a relative time in ticks for the trigger of the alarm.              |[optional] 
**related** |**str** |Specify the relationship of the alarm trigger with respect to the start or end of the event. Enum, available values: Start, End |



## Example
```python
reminder_trigger = models.ReminderTrigger(
    date_time=datetime.today(),
    duration=600000000)
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

