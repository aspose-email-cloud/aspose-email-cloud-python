# AsposeEmailCloudSdk.models.ContactAsFileRequest

Convert contact model to file request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Enumerates contact formats. Enum, available values: VCard, WebDav, Msg |
**value** |[**ContactDto**](ContactDto.md) |Contact model.              |



## Example
```python
contact_as_file_request = models.ContactAsFileRequest(
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


[[Back to Model list]](Models.md) [[Back to README]](README.md)

