# ClientAccountGetMultiRequest

Request model for ClientAccountApi.get_multi

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file_name** |**str** |File name on storage |
**folder** |**str** |Folder on storage |[optional] 
**storage** |**str** |Storage name |[optional] 

## Example
```python
request = models.ClientAccountGetMultiRequest(
    file_name='email.multi.account',
    folder='email/account/location/on/storage',
    storage='First Storage')
```
