# EmailGetRequest

Request model for EmailApi.get

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**file_name** |**str** |Email document file name. |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.EmailGetRequest(
    format='Eml',
    file_name='email.eml',
    folder='folder/on/storage',
    storage='First Storage')
```
