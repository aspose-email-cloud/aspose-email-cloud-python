# ClientFolderGetListRequest

Request model for ClientFolderApi.get_list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**account** |**str** |Email account |
**storage** |**str** |Storage name where account file located |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located |[optional] 
**parent_folder** |**str** |Folder in which subfolders should be listed |[optional] 

## Example
```python
request = models.ClientFolderGetListRequest(
    account='email.multi.account',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    parent_folder='INBOX')
```
