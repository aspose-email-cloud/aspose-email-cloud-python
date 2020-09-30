# ClientMessageAppendFileRequest

Request model for ClientMessageApi.append_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**account** |**str** |Email account. |
**file** |**str** |Message file to append. |
**storage** |**str** |Storage name where account file located. |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located. |[optional] 
**format** |**str** |Email file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |[optional] [default to 0]
**folder** |**str** |Path to folder on email server to append message to. |[optional] 
**mark_as_sent** |**bool** |Determines that appended message should be market as sent or not. |[optional] [default to true]

## Example
```python
request = models.ClientMessageAppendFileRequest(
    account='email.multi.account',
    file='/path/to/message.eml',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    format='Eml',
    folder='INBOX',)
```
