# AsposeEmailCloudSdk.ContactApi (EmailCloud.contact)

Contact document operations. Supported formats: VCard, MSG, WebDav

<a name="as_file"></a>
## as_file

Description: Converts contact model to specified format and returns as file             

Returns: File stream in specified format

Method call example:
```python
result = api.contact.as_file(request)
```

### Parameter: request

Description: Contact model and format to convert

See parameter model documentation at [ContactAsFileRequest](ContactAsFileRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactAsFileRequest(
    value=models.ContactDto(
        attachments=[
            models.Attachment(
                name='attachment.txt',
                base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
        display_name='Alex Thomas',
        email_addresses=[
            models.EmailAddress(
                category=models.EnumWithCustomOfEmailAddressCategory(
                    value='Custom',
                    description='Partners'),
                display_name='Alex Thomas Partners',
                preferred=True,
                address='email@aspose.com')],
        gender='Male',
        given_name='Alex',
        phone_numbers=[
            models.PhoneNumber(
                category=models.EnumWithCustomOfPhoneNumberCategory(
                    value='Office'),
                number='+49 211 4247 21',
                preferred=True)],
        profession='GENERAL DIRECTOR',
        surname='Thomas',
        urls=[
            models.Url(
                category=models.EnumWithCustomOfUrlCategory(
                    value='Work'),
                preferred=True,
                href='www.aspose.com')]))
```

</details>

### Result

Description: File stream in specified format

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactAsFileRequest(
    value=models.ContactDto(
        attachments=[
            models.Attachment(
                name='attachment.txt',
                base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
        display_name='Alex Thomas',
        email_addresses=[
            models.EmailAddress(
                category=models.EnumWithCustomOfEmailAddressCategory(
                    value='Custom',
                    description='Partners'),
                display_name='Alex Thomas Partners',
                preferred=True,
                address='email@aspose.com')],
        gender='Male',
        given_name='Alex',
        phone_numbers=[
            models.PhoneNumber(
                category=models.EnumWithCustomOfPhoneNumberCategory(
                    value='Office'),
                number='+49 211 4247 21',
                preferred=True)],
        profession='GENERAL DIRECTOR',
        surname='Thomas',
        urls=[
            models.Url(
                category=models.EnumWithCustomOfUrlCategory(
                    value='Work'),
                preferred=True,
                href='www.aspose.com')]))

// Call method:
result = api.contact.as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="as_mapi"></a>
## as_mapi

Description: Converts ContactDto to MapiContactDto.             

Returns: MAPI model contact representation

Method call example:
```python
result = api.contact.as_mapi(contact_dto)
```

### Parameter: contact_dto

Description: Contact model to convert

See parameter model documentation at [ContactDto](ContactDto.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
contact_dto = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])
```

</details>

### Result

Description: MAPI model contact representation

Return type: [**MapiContactDto**](MapiContactDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.MapiContactDto(
    electronic_addresses=models.MapiContactElectronicAddressPropertySetDto(
        default_email_address=models.MapiContactElectronicAddressDto(
            email_address='email@aspose.com')),
    name_info=models.MapiContactNamePropertySetDto(
        given_name='Alex',
        surname='Thomas'),
    personal_info=models.MapiContactPersonalInfoPropertySetDto(
        business_home_page='www.aspose.com'),
    professional_info=models.MapiContactProfessionalPropertySetDto(
        profession='GENERAL DIRECTOR'),
    telephones=models.MapiContactTelephonePropertySetDto(
        primary_telephone_number='+49 211 4247 21'))
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
contact_dto = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])

// Call method:
result = api.contact.as_mapi(contact_dto)

// Result example:
result = models.MapiContactDto(
    electronic_addresses=models.MapiContactElectronicAddressPropertySetDto(
        default_email_address=models.MapiContactElectronicAddressDto(
            email_address='email@aspose.com')),
    name_info=models.MapiContactNamePropertySetDto(
        given_name='Alex',
        surname='Thomas'),
    personal_info=models.MapiContactPersonalInfoPropertySetDto(
        business_home_page='www.aspose.com'),
    professional_info=models.MapiContactProfessionalPropertySetDto(
        profession='GENERAL DIRECTOR'),
    telephones=models.MapiContactTelephonePropertySetDto(
        primary_telephone_number='+49 211 4247 21'))
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="convert"></a>
## convert

Description: Converts contact document to specified format and returns as file             

Returns: File stream in specified destination format

Method call example:
```python
result = api.contact.convert(request)
```

### Parameter: request

Description: convert method request.

See parameter model documentation at [ContactConvertRequest](ContactConvertRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactConvertRequest(
    to_format='VCard',
    from_format='Msg',
    file='/path/to/contact.msg')
```

</details>

### Result

Description: File stream in specified destination format

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactConvertRequest(
    to_format='VCard',
    from_format='Msg',
    file='/path/to/contact.msg')

// Call method:
result = api.contact.convert(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="from_file"></a>
## from_file

Description: Converts contact document to a model representation             

Returns: Contact model

Method call example:
```python
result = api.contact.from_file(request)
```

### Parameter: request

Description: from_file method request.

See parameter model documentation at [ContactFromFileRequest](ContactFromFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')
```

</details>

### Result

Description: Contact model

Return type: [**ContactDto**](ContactDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')

// Call method:
result = api.contact.from_file(request)

// Result example:
result = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get"></a>
## get

Description: Get contact document from storage.             

Returns: Contact document.

Method call example:
```python
result = api.contact.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [ContactGetRequest](ContactGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactGetRequest(
    format='VCard',
    file_name='contact.vcf',
    folder='folder/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: Contact document.

Return type: [**ContactDto**](ContactDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactGetRequest(
    format='VCard',
    file_name='contact.vcf',
    folder='folder/on/storage',
    storage='First Storage')

// Call method:
result = api.contact.get(request)

// Result example:
result = models.ContactDto(
    attachments=[
        models.Attachment(
            name='attachment.txt',
            base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
    display_name='Alex Thomas',
    email_addresses=[
        models.EmailAddress(
            category=models.EnumWithCustomOfEmailAddressCategory(
                value='Custom',
                description='Partners'),
            display_name='Alex Thomas Partners',
            preferred=True,
            address='email@aspose.com')],
    gender='Male',
    given_name='Alex',
    phone_numbers=[
        models.PhoneNumber(
            category=models.EnumWithCustomOfPhoneNumberCategory(
                value='Office'),
            number='+49 211 4247 21',
            preferred=True)],
    profession='GENERAL DIRECTOR',
    surname='Thomas',
    urls=[
        models.Url(
            category=models.EnumWithCustomOfUrlCategory(
                value='Work'),
            preferred=True,
            href='www.aspose.com')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_as_file"></a>
## get_as_file

Description: Converts contact document from storage to specified format and returns as file             

Returns: File stream in specified format

Method call example:
```python
result = api.contact.get_as_file(request)
```

### Parameter: request

Description: get_as_file method request.

See parameter model documentation at [ContactGetAsFileRequest](ContactGetAsFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactGetAsFileRequest(
    file_name='contact.msg',
    to_format='VCard',
    from_format='Msg',
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
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactGetAsFileRequest(
    file_name='contact.msg',
    to_format='VCard',
    from_format='Msg',
    storage='First Storage',
    folder='folder/on/storage')

// Call method:
result = api.contact.get_as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_list"></a>
## get_list

Description: Get contact list from storage folder.             

Returns: Contact list.

Method call example:
```python
result = api.contact.get_list(request)
```

### Parameter: request

Description: get_list method request.

See parameter model documentation at [ContactGetListRequest](ContactGetListRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactGetListRequest(
    format='VCard',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)
```

</details>

### Result

Description: Contact list.

Return type: [**ContactStorageList**](ContactStorageList.md)

<details>
    <summary>Result example</summary>

```python
result = models.ContactStorageList(
    value=[
        models.StorageModelOfContactDto(
            storage_file=models.StorageFileLocation(
                file_name='contact.vcf',
                storage='First Storage',
                folder_path='file/location/folder/on/storage'),
            value=models.ContactDto(
                attachments=[
                    models.Attachment(
                        name='attachment.txt',
                        base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
                display_name='Alex Thomas',
                email_addresses=[
                    models.EmailAddress(
                        category=models.EnumWithCustomOfEmailAddressCategory(
                            value='Custom',
                            description='Partners'),
                        display_name='Alex Thomas Partners',
                        preferred=True,
                        address='email@aspose.com')],
                gender='Male',
                given_name='Alex',
                phone_numbers=[
                    models.PhoneNumber(
                        category=models.EnumWithCustomOfPhoneNumberCategory(
                            value='Office'),
                        number='+49 211 4247 21',
                        preferred=True)],
                profession='GENERAL DIRECTOR',
                surname='Thomas',
                urls=[
                    models.Url(
                        category=models.EnumWithCustomOfUrlCategory(
                            value='Work'),
                        preferred=True,
                        href='www.aspose.com')]))])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactGetListRequest(
    format='VCard',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)

// Call method:
result = api.contact.get_list(request)

// Result example:
result = models.ContactStorageList(
    value=[
        models.StorageModelOfContactDto(
            storage_file=models.StorageFileLocation(
                file_name='contact.vcf',
                storage='First Storage',
                folder_path='file/location/folder/on/storage'),
            value=models.ContactDto(
                attachments=[
                    models.Attachment(
                        name='attachment.txt',
                        base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
                display_name='Alex Thomas',
                email_addresses=[
                    models.EmailAddress(
                        category=models.EnumWithCustomOfEmailAddressCategory(
                            value='Custom',
                            description='Partners'),
                        display_name='Alex Thomas Partners',
                        preferred=True,
                        address='email@aspose.com')],
                gender='Male',
                given_name='Alex',
                phone_numbers=[
                    models.PhoneNumber(
                        category=models.EnumWithCustomOfPhoneNumberCategory(
                            value='Office'),
                        number='+49 211 4247 21',
                        preferred=True)],
                profession='GENERAL DIRECTOR',
                surname='Thomas',
                urls=[
                    models.Url(
                        category=models.EnumWithCustomOfUrlCategory(
                            value='Work'),
                        preferred=True,
                        href='www.aspose.com')]))])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="save"></a>
## save

Description: Save contact to storage.             

Method call example:
```python
api.contact.save(request)
```

### Parameter: request

Description: Create/Update contact request.

See parameter model documentation at [ContactSaveRequest](ContactSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ContactSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='contact.vcf',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.ContactDto(
        attachments=[
            models.Attachment(
                name='attachment.txt',
                base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
        display_name='Alex Thomas',
        email_addresses=[
            models.EmailAddress(
                category=models.EnumWithCustomOfEmailAddressCategory(
                    value='Custom',
                    description='Partners'),
                display_name='Alex Thomas Partners',
                preferred=True,
                address='email@aspose.com')],
        gender='Male',
        given_name='Alex',
        phone_numbers=[
            models.PhoneNumber(
                category=models.EnumWithCustomOfPhoneNumberCategory(
                    value='Office'),
                number='+49 211 4247 21',
                preferred=True)],
        profession='GENERAL DIRECTOR',
        surname='Thomas',
        urls=[
            models.Url(
                category=models.EnumWithCustomOfUrlCategory(
                    value='Work'),
                preferred=True,
                href='www.aspose.com')]))
```

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ContactSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='contact.vcf',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.ContactDto(
        attachments=[
            models.Attachment(
                name='attachment.txt',
                base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
        display_name='Alex Thomas',
        email_addresses=[
            models.EmailAddress(
                category=models.EnumWithCustomOfEmailAddressCategory(
                    value='Custom',
                    description='Partners'),
                display_name='Alex Thomas Partners',
                preferred=True,
                address='email@aspose.com')],
        gender='Male',
        given_name='Alex',
        phone_numbers=[
            models.PhoneNumber(
                category=models.EnumWithCustomOfPhoneNumberCategory(
                    value='Office'),
                number='+49 211 4247 21',
                preferred=True)],
        profession='GENERAL DIRECTOR',
        surname='Thomas',
        urls=[
            models.Url(
                category=models.EnumWithCustomOfUrlCategory(
                    value='Work'),
                preferred=True,
                href='www.aspose.com')]))

// Call method:
api.contact.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

