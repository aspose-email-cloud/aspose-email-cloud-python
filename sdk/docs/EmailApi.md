# AsposeEmailCloudSdk.EmailApi (EmailCloud.email)

Email document (*.eml) operations.

<a name="as_file"></a>
## as_file

Description: Converts Email model to a specified format and returns as a file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.email.as_file(request)
```

### Parameter: request

Description: Email model and format to convert.

See parameter model documentation at [EmailAsFileRequest](EmailAsFileRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailAsFileRequest(
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

</details>

### Result

Description: File stream in specified format.

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailAsFileRequest(
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

// Call method:
result = api.email.as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="as_mapi"></a>
## as_mapi

Description: Converts EmailDto to MapiMessageDto.             

Returns: MAPI model message representation

Method call example:
```python
result = api.email.as_mapi(email_dto)
```

### Parameter: email_dto

Description: Email model to convert

See parameter model documentation at [EmailDto](EmailDto.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
email_dto = models.EmailDto(
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
            address='to@aspose.com')])
```

</details>

### Result

Description: MAPI model message representation

Return type: [**MapiMessageDto**](MapiMessageDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.MapiMessageDto(
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
    subject_prefix='Re: ')
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
email_dto = models.EmailDto(
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
            address='to@aspose.com')])

// Call method:
result = api.email.as_mapi(email_dto)

// Result example:
result = models.MapiMessageDto(
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
    subject_prefix='Re: ')
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="convert"></a>
## convert

Description: Converts email document to specified format and returns as file             

Returns: File stream in specified format

Method call example:
```python
result = api.email.convert(request)
```

### Parameter: request

Description: convert method request.

See parameter model documentation at [EmailConvertRequest](EmailConvertRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailConvertRequest(
    from_format='Msg',
    to_format='Mhtml',
    file='/path/to/message.msg')
```

</details>

### Result

Description: File stream in specified format

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailConvertRequest(
    from_format='Msg',
    to_format='Mhtml',
    file='/path/to/message.msg')

// Call method:
result = api.email.convert(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="from_file"></a>
## from_file

Description: Converts email document to a model representation             

Returns: Email document model

Method call example:
```python
result = api.email.from_file(request)
```

### Parameter: request

Description: from_file method request.

See parameter model documentation at [EmailFromFileRequest](EmailFromFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailFromFileRequest(
    format='Eml',
    file='/path/to/message.eml')
```

</details>

### Result

Description: Email document model

Return type: [**EmailDto**](EmailDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.EmailDto(
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
            address='to@aspose.com')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailFromFileRequest(
    format='Eml',
    file='/path/to/message.eml')

// Call method:
result = api.email.from_file(request)

// Result example:
result = models.EmailDto(
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
            address='to@aspose.com')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get"></a>
## get

Description: Get email document from storage.             

Returns: Email document.

Method call example:
```python
result = api.email.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [EmailGetRequest](EmailGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailGetRequest(
    format='Eml',
    file_name='email.eml',
    folder='folder/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: Email document.

Return type: [**EmailDto**](EmailDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.EmailDto(
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
            address='to@aspose.com')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailGetRequest(
    format='Eml',
    file_name='email.eml',
    folder='folder/on/storage',
    storage='First Storage')

// Call method:
result = api.email.get(request)

// Result example:
result = models.EmailDto(
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
            address='to@aspose.com')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_as_file"></a>
## get_as_file

Description: Converts email document from storage to specified format and returns as file             

Returns: File stream in specified format

Method call example:
```python
result = api.email.get_as_file(request)
```

### Parameter: request

Description: get_as_file method request.

See parameter model documentation at [EmailGetAsFileRequest](EmailGetAsFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailGetAsFileRequest(
    file_name='email.eml',
    format='Mhtml',
    storage='First Storage',
    folder='folder/on/storage')
```

</details>

### Result

Description: File stream in specified format

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailGetAsFileRequest(
    file_name='email.eml',
    format='Mhtml',
    storage='First Storage',
    folder='folder/on/storage')

// Call method:
result = api.email.get_as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_list"></a>
## get_list

Description: Get email list from storage folder.             

Returns: Email document list.

Method call example:
```python
result = api.email.get_list(request)
```

### Parameter: request

Description: get_list method request.

See parameter model documentation at [EmailGetListRequest](EmailGetListRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailGetListRequest(
    format='Eml',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)
```

</details>

### Result

Description: Email document list.

Return type: [**EmailStorageList**](EmailStorageList.md)

<details>
    <summary>Result example</summary>

```python
result = models.EmailStorageList(
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
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailGetListRequest(
    format='Eml',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)

// Call method:
result = api.email.get_list(request)

// Result example:
result = models.EmailStorageList(
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

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="save"></a>
## save

Description: Save email document to storage.             

Method call example:
```python
api.email.save(request)
```

### Parameter: request

Description: Email document create/update request.

See parameter model documentation at [EmailSaveRequest](EmailSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.EmailSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='email.eml',
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
                address='to@aspose.com')]))
```

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.EmailSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='email.eml',
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
                address='to@aspose.com')]))

// Call method:
api.email.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

