# AsposeEmailCloudSdk.models.MailMessageDto

Represents email message, stored as an EmailDto object.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** |[**EmailDto**](EmailDto.md) |Message document object.              |

Parent class: [MailMessageBase](MailMessageBase.md)


## Example
```python
mail_message_dto = models.MailMessageDto(
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

