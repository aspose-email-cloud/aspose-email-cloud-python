# AsposeEmailCloudSdk.models.MapiContactAsFileRequest

Convert MapiContact to file request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** |**str** |Enumerates contact formats. Enum, available values: VCard, WebDav, Msg |
**value** |[**MapiContactDto**](MapiContactDto.md) |MAPI contact model.              |



## Example
```python
mapi_contact_as_file_request = models.MapiContactAsFileRequest(
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


[[Back to Model list]](Models.md) [[Back to README]](README.md)

