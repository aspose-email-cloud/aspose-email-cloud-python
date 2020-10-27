# CalendarConvertRequest

Request model for CalendarApi.convert

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |File format. Enum, available values: Ics, Msg |
**file** |**str** |File to convert |

## Example
```python
request = models.CalendarConvertRequest(
    format='Ics',
    file='/path/to/calendar.msg')
```
