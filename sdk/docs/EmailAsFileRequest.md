# AsposeEmailCloudSdk.models.EmailAsFileRequest

Convert email model to file request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**value** |[**EmailDto**](EmailDto.md) |Email model.              |



## Example
```python
email_as_file_request = models.EmailAsFileRequest(
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
                address='to@aspose.com')]))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

