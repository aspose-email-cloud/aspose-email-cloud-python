# ClientMessageListRequest

Request model for ClientMessageApi.list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**folder** |**str** |A folder in email account |
**account** |**str** |Email account |
**query_string** |**str** |A MailQuery search string |[optional] 
**storage** |**str** |Storage name where account file located |[optional] 
**account_storage_folder** |**str** |Folder in storage where account file located |[optional] 
**recursive** |**bool** |Specifies that should message be searched in subfolders recursively |[optional] [default to false]
**type** |**str** |MailMessageBase type. Using this property you can get messages in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64 |[optional] [default to 0]
**format** |**str** |Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |[optional] [default to 0]

## Example
```python
request = models.ClientMessageListRequest(
    folder='INBOX',
    account='email.multi.account',
    query_string='('From' Contains '.com')',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    recursive=True,
    type='Dto',
    format='Eml')
```
