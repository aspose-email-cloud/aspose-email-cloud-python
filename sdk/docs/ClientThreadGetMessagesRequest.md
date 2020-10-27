# ClientThreadGetMessagesRequest

Request model for ClientThreadApi.get_messages

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**thread_id** |**str** |Thread identifier |
**account** |**str** |Email account |
**folder** |**str** |Specifies account folder to get thread from              |[optional] 
**storage** |**str** |Storage name where account file located |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located |[optional] 

## Example
```python
request = models.ClientThreadGetMessagesRequest(
    thread_id='5',
    account='email.account',
    folder='INBOX',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage')
```
