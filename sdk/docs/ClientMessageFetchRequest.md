# ClientMessageFetchRequest

Request model for ClientMessageApi.fetch

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**message_id** |**str** |Message identifier |
**account** |**str** |Email account |
**folder** |**str** |Account folder to fetch from (should be specified for some protocols such as IMAP)              |[optional] 
**storage** |**str** |Storage name where account file located. |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located. |[optional] 
**type** |**str** |MailMessageBase type. Using this property you can fetch message in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64 |[optional] [default to 0]
**format** |**str** |Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |[optional] [default to 0]

## Example
```python
request = models.ClientMessageFetchRequest(
    message_id='<put your message identifier here>',
    account='email.multi.account',
    folder='INBOX',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    type='Dto',
    format='Eml')
```
