# CalendarGetRequest

Request model for CalendarApi.get

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |iCalendar file name in storage. |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.CalendarGetRequest(
    file_name='calendar.ics',
    folder='calendar/location/on/storage',
    storage='First Storage')
```
