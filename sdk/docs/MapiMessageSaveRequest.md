# AsposeEmailCloudSdk.models.MapiMessageSaveRequest

MapiMessage save to storage request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |

Parent class: [StorageModelOfMapiMessageDto](StorageModelOfMapiMessageDto.md)


## Example
```python
mapi_message_save_request = models.MapiMessageSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='message.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiMessageDto(
        message_body='Some body',
        client_submit_time=datetime.today(),
        delivery_time=datetime.today(),
        display_to='To Address',
        flags=[
            'MsgFlagRead',
            'MsgFlagUnsent',
            'MsgFlagHasAttach'],
        normalized_subject='Some subject',
        sender_address_type='SMTP',
        sender_email_address='from@aspose.com',
        sender_name='From Address',
        sender_smtp_address='from@aspose.com',
        attachments=[
            models.MapiAttachmentDto(
                name='some-file.txt',
                data_base64='U29tZSBmaWxlIHRleHQ=')],
        body='Some body',
        message_class='IPM.Note',
        recipients=[
            models.MapiRecipientDto(
                email_address='to@aspose.com',
                address_type='SMTP',
                display_name='To Address',
                recipient_type='MapiTo')],
        subject='Re: Some subject',
        subject_prefix='Re: '))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

