# CalendarGetAsAlternateRequest

Request model for CalendarApi.get_as_alternate

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |iCalendar file name in storage |
**calendar_action** |**str** |iCalendar method type Enum, available values: Create, Update, Cancel |
**sequence_id** |**str** |The sequence id |[optional] 
**folder** |**str** |Path to folder in storage |[optional] 
**storage** |**str** |Storage name |[optional] 

## Example
```python
request = models.CalendarGetAsAlternateRequest(
    file_name='calendar.ics',
    calendar_action='Create',
    folder='calendar/location/on/storage',
    storage='First Storage')
```
