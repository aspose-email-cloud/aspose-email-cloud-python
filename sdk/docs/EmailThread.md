# AsposeEmailCloudSdk.models.EmailThread

Email messages thread             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** |**str** |Thread identifier              |[optional] 
**subject** |**str** |Thread subject              |[optional] 
**messages** |[**list[EmailDto]**](EmailDto.md) |List of messages in thread              |[optional] 
**folder** |**str** |Thread folder location              |[optional] 



## Example
```python
email_thread = models.EmailThread(
    id='5',
    subject='Some subject',
    messages=[
        models.EmailDto(
            attachments=[
                models.Attachment(
                    name='some-file.txt',
                    base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
            body='Some body',
            body_type='Html',
            date=datetime.today(),
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
                    address='to@aspose.com')]),
        models.EmailDto(
            attachments=[
                models.Attachment(
                    name='some-file.txt',
                    base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
            body='Other body',
            body_type='Html',
            date=datetime.today(),
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
                    address='to@aspose.com')])])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

