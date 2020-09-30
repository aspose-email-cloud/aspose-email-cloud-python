# ContactGetAsFileRequest

Request model for ContactApi.get_as_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |Calendar document file name |
**to_format** |**str** |File format Enum, available values: VCard, WebDav, Msg |
**from_format** |**str** |File format to convert from Enum, available values: VCard, WebDav, Msg |
**storage** |**str** |Storage name |[optional] 
**folder** |**str** |Path to folder in storage |[optional] 

## Example
```python
request = models.ContactGetAsFileRequest(
    file_name='contact.msg',
    to_format='VCard',
    from_format='Msg',
    storage='First Storage',
    folder='folder/on/storage')
```
