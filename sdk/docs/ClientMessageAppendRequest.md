# AsposeEmailCloudSdk.models.ClientMessageAppendRequest

Email client append message request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** |**str** |Path to folder on email server to append message to.              |[optional] 
**message** |[**MailMessageBase**](MailMessageBase.md) |Message to append.              |
**mark_as_sent** |**bool** |Determines that appended message should be market as sent or not.              |

Parent class: [ClientAccountBaseRequest](ClientAccountBaseRequest.md)


## Example
```python
client_message_append_request = models.ClientMessageAppendRequest(
    folder='INBOX/SubFolder',
    message=models.MailMessageDto(
        value=models.EmailDto(
            attachments=[
                models.Attachment(
                    name='some-file.txt',
                    base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
            body='Some body',
            body_type='Html',
            delivery_notification_options=[
                'OnSuccess',
                'Delay'],
            _from=models.MailAddress(
                display_name='From Address',
                address='from@aspose.com'),
            html_body='<b>Some body</b>',
            is_body_html=True,
            is_draft=True,
            subject='Re: Some subject',
            to=[
                models.MailAddress(
                    display_name='To Address',
                    address='to@aspose.com')])),
    mark_as_sent=True,
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

