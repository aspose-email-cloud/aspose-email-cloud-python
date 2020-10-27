# MapiCalendarGetRequest

Request model for MapiCalendarApi.get

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |Calendar file name in storage. |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.MapiCalendarGetRequest(
    file_name='calendar.msg',
    folder='calendar/location/on/storage',
    storage='First Storage')
```
