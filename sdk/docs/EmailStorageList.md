# AsposeEmailCloudSdk.models.EmailStorageList

Email models list with corresponding storage locations.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [ListResponseOfStorageModelOfEmailDto](ListResponseOfStorageModelOfEmailDto.md)


## Example
```python
email_storage_list = models.EmailStorageList(
    value=[
        models.EmailSaveRequest(
            storage_file=models.StorageFileLocation(
                file_name='message.eml',
                storage='First Storage',
                folder_path='file/location/folder/on/storage'),
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
                        address='to@aspose.com')]))])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

