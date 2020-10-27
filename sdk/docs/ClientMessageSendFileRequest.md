# ClientMessageSendFileRequest

Request model for ClientMessageApi.send_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**account** |**str** |Email account |
**file** |**str** |File to send |
**storage** |**str** |Storage name where account file located. |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located. |[optional] 
**format** |**str** |Email file format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |[optional] [default to 0]

## Example
```python
request = models.ClientMessageSendFileRequest(
    account='email.multi.account',
    file='/path/to/message.eml',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    format='Eml')
```
