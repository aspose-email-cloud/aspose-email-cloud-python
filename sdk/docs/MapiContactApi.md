# AsposeEmailCloudSdk.MapiContactApi (EmailCloud.mapi.contact)

MAPI contact operations

<a name="as_contact_dto"></a>
## as_contact_dto

Description: Converts MAPI contact model to ContactDto model.             

Returns: Contact model.

Method call example:
```python
result = api.mapi.contact.as_contact_dto(mapi_contact_dto)
```

### Parameter: mapi_contact_dto

Description: MAPI contact model to convert.

See parameter model documentation at [MapiContactDto](MapiContactDto.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
mapi_contact_dto = models.MapiContactDto(
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

### Result

Description: Contact model.

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
mapi_contact_dto = models.MapiContactDto(
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

// Call method:
result = api.mapi.contact.as_contact_dto(mapi_contact_dto)

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
<a name="as_file"></a>
## as_file

Description: Converts MAPI contact model to specified format and returns as file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.mapi.contact.as_file(request)
```

### Parameter: request

Description: MAPI contact model to convert.

See parameter model documentation at [MapiContactAsFileRequest](MapiContactAsFileRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiContactAsFileRequest(
    format='Msg',
    value=models.MapiContactDto(
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
            primary_telephone_number='+49 211 4247 21')))
```

</details>

### Result

Description: File stream in specified format.

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.MapiContactAsFileRequest(
    format='Msg',
    value=models.MapiContactDto(
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
            primary_telephone_number='+49 211 4247 21')))

// Call method:
result = api.mapi.contact.as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="from_file"></a>
## from_file

Description: Converts contact file to a MAPI model representation.             

Returns: MAPI model

Method call example:
```python
result = api.mapi.contact.from_file(request)
```

### Parameter: request

Description: from_file method request.

See parameter model documentation at [MapiContactFromFileRequest](MapiContactFromFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')
```

</details>

### Result

Description: MAPI model

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
request = models.MapiContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')

// Call method:
result = api.mapi.contact.from_file(request)

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
<a name="get"></a>
## get

Description: Get MAPI contact document.             

Returns: Contact model.

Method call example:
```python
result = api.mapi.contact.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [MapiContactGetRequest](MapiContactGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiContactGetRequest(
    format='VCard',
    file_name='contact.vcf',
    folder='folder/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: Contact model.

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
request = models.MapiContactGetRequest(
    format='VCard',
    file_name='contact.vcf',
    folder='folder/on/storage',
    storage='First Storage')

// Call method:
result = api.mapi.contact.get(request)

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
<a name="save"></a>
## save

Description: Save MAPI Contact to storage.             

Method call example:
```python
api.mapi.contact.save(request)
```

### Parameter: request

Description: Create/Update contact request.

See parameter model documentation at [MapiContactSaveRequest](MapiContactSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiContactSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='contact.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiContactDto(
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
            primary_telephone_number='+49 211 4247 21')))
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
request = models.MapiContactSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='contact.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiContactDto(
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
            primary_telephone_number='+49 211 4247 21')))

// Call method:
api.mapi.contact.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

