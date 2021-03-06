# AsposeEmailCloudSdk.models.MapiContactDto

Represents outlook contact information.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**electronic_addresses** |[**MapiContactElectronicAddressPropertySetDto**](MapiContactElectronicAddressPropertySetDto.md) |Specify properties for up to three different e-mail addresses and three different fax addresses.              |[optional] 
**events** |[**MapiContactEventPropertySetDto**](MapiContactEventPropertySetDto.md) |Specify events associated with a contact.              |[optional] 
**name_info** |[**MapiContactNamePropertySetDto**](MapiContactNamePropertySetDto.md) |The properties are used to specify the name of the person represented by the contact.              |[optional] 
**other_fields** |[**MapiContactOtherPropertySetDto**](MapiContactOtherPropertySetDto.md) |Specify other fields of contact.              |[optional] 
**personal_info** |[**MapiContactPersonalInfoPropertySetDto**](MapiContactPersonalInfoPropertySetDto.md) |Specify other additional contact information.              |[optional] 
**photo** |[**MapiContactPhotoDto**](MapiContactPhotoDto.md) |Contact photo.              |[optional] 
**physical_addresses** |[**MapiContactPhysicalAddressPropertySetDto**](MapiContactPhysicalAddressPropertySetDto.md) |Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address.              |[optional] 
**professional_info** |[**MapiContactProfessionalPropertySetDto**](MapiContactProfessionalPropertySetDto.md) |Properties are used to store professional details for the person represented by the contact.              |[optional] 
**telephones** |[**MapiContactTelephonePropertySetDto**](MapiContactTelephonePropertySetDto.md) |Specify telephone numbers for the contact.              |[optional] 

Parent class: [MapiMessageItemBaseDto](MapiMessageItemBaseDto.md)


## Example
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


[[Back to Model list]](Models.md) [[Back to README]](README.md)

