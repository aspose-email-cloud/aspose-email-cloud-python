# CalendarGetAsFileRequest

Request model for CalendarApi.get_as_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |Calendar document file name. |
**format** |**str** |File format. Enum, available values: Ics, Msg |
**storage** |**str** |Storage name. |[optional] 
**folder** |**str** |Path to folder in storage. |[optional] 

## Example
```python
request = models.CalendarGetAsFileRequest(
    file_name='calendar.msg',
    format='Ics',
    storage='First Storage',
    folder='calendar/file/location/on/storage')
```
