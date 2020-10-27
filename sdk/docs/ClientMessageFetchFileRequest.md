# ClientMessageFetchFileRequest

Request model for ClientMessageApi.fetch_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**message_id** |**str** |Message identifier |
**account** |**str** |Email account |
**folder** |**str** |Account folder to fetch from (should be specified for some protocols such as IMAP)              |[optional] 
**storage** |**str** |Storage name where account file located. |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located. |[optional] 
**format** |**str** |Fetched message file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |[optional] [default to 0]

## Example
```python
request = models.ClientMessageFetchFileRequest(
    message_id='<put your message identifier here>',
    account='email.multi.account',
    folder='INBOX',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    format='Eml')
```
