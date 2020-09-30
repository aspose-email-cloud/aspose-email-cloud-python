# AsposeEmailCloudSdk.AiBcrApi (EmailCloud.ai.bcr)

AI Business card recognition operations.

<a name="parse"></a>
## parse

Description: Parse images to vCard document models             

Returns: List of vCards

Method call example:
```python
result = api.ai.bcr.parse(request)
```

### Parameter: request

Description: parse method request.

See parameter model documentation at [AiBcrParseRequest](AiBcrParseRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.AiBcrParseRequest(
    file='/path/to/image.png',
    countries='us',
    languages='en',
    is_single=True)
```

</details>

### Result

Description: List of vCards

Return type: [**ContactList**](ContactList.md)

<details>
    <summary>Result example</summary>

```python
result = models.ContactList(
    value=[
        models.ContactDto(
            attachments=[
                models.Attachment(
                    name='attachment.txt',
                    base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
            display_name='Alex Thomas',
            email_addresses=[
                models.EmailAddress(
                    category=models.EnumWithCustom<EmailAddressCategory>(
                        value='Custom',
                        description='Partners'),
                    display_name='Alex Thomas Partners',
                    preferred=True,
                    address='email@aspose.com')],
            gender='Male',
            given_name='Alex',
            phone_numbers=[
                models.PhoneNumber(
                    category=models.EnumWithCustom<PhoneNumberCategory>(
                        value='Office'),
                    number='+49 211 4247 21',
                    preferred=True)],
            profession='GENERAL DIRECTOR',
            surname='Thomas',
            urls=[
                models.Url(
                    category=models.EnumWithCustom<UrlCategory>(
                        value='Work'),
                    preferred=True,
                    href='www.aspose.com')])])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.AiBcrParseRequest(
    file='/path/to/image.png',
    countries='us',
    languages='en',
    is_single=True)

// Call method:
result = api.ai.bcr.parse(request)

// Result example:
result = models.ContactList(
    value=[
        models.ContactDto(
            attachments=[
                models.Attachment(
                    name='attachment.txt',
                    base64_data='U29tZSBmaWxlIGNvbnRlbnQ=')],
            display_name='Alex Thomas',
            email_addresses=[
                models.EmailAddress(
                    category=models.EnumWithCustom<EmailAddressCategory>(
                        value='Custom',
                        description='Partners'),
                    display_name='Alex Thomas Partners',
                    preferred=True,
                    address='email@aspose.com')],
            gender='Male',
            given_name='Alex',
            phone_numbers=[
                models.PhoneNumber(
                    category=models.EnumWithCustom<PhoneNumberCategory>(
                        value='Office'),
                    number='+49 211 4247 21',
                    preferred=True)],
            profession='GENERAL DIRECTOR',
            surname='Thomas',
            urls=[
                models.Url(
                    category=models.EnumWithCustom<UrlCategory>(
                        value='Work'),
                    preferred=True,
                    href='www.aspose.com')])])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="parse_storage"></a>
## parse_storage

Description: Parse images from storage to vCard files             

Returns: List of vCard files located on storage

Method call example:
```python
result = api.ai.bcr.parse_storage(request)
```

### Parameter: request

Description: Request with images located on storage

See parameter model documentation at [AiBcrParseStorageRequest](AiBcrParseStorageRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.AiBcrParseStorageRequest(
    out_folder=models.StorageFolderLocation(
        storage='First Storage',
        folder_path='VCard/files/produced/by/parser/will/be/placed/here'),
    images=[
        models.AiBcrImageStorageFile(
            file=models.StorageFileLocation(
                file_name='VCardScanImage.jpg',
                storage='First Storage',
                folder_path='image/location/on/storage'),
            is_single=True)])
```

</details>

### Result

Description: List of vCard files located on storage

Return type: [**StorageFileLocationList**](StorageFileLocationList.md)

<details>
    <summary>Result example</summary>

```python
result = models.StorageFileLocationList(
    value=[
        models.StorageFileLocation(
            file_name='fileOnStorage.txt',
            storage='First Storage',
            folder_path='file/location/folder/on/storage')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.AiBcrParseStorageRequest(
    out_folder=models.StorageFolderLocation(
        storage='First Storage',
        folder_path='VCard/files/produced/by/parser/will/be/placed/here'),
    images=[
        models.AiBcrImageStorageFile(
            file=models.StorageFileLocation(
                file_name='VCardScanImage.jpg',
                storage='First Storage',
                folder_path='image/location/on/storage'),
            is_single=True)])

// Call method:
result = api.ai.bcr.parse_storage(request)

// Result example:
result = models.StorageFileLocationList(
    value=[
        models.StorageFileLocation(
            file_name='fileOnStorage.txt',
            storage='First Storage',
            folder_path='file/location/folder/on/storage')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

