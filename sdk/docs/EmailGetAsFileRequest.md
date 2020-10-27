# EmailGetAsFileRequest

Request model for EmailApi.get_as_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |Email document file name |
**format** |**str** |File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**storage** |**str** |Storage name |[optional] 
**folder** |**str** |Path to folder in storage |[optional] 

## Example
```python
request = models.EmailGetAsFileRequest(
    file_name='email.eml',
    format='Mhtml',
    storage='First Storage',
    folder='folder/on/storage')
```
