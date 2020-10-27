# ClientAccountGetRequest

Request model for ClientAccountApi.get

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |File name on storage. |
**folder** |**str** |Folder on storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.ClientAccountGetRequest(
    file_name='email.account',
    folder='email/account/location/on/storage',
    storage='First Storage')
```
