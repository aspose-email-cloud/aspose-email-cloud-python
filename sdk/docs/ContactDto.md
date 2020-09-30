# AsposeEmailCloudSdk.models.ContactDto

VCard document representation.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_persons** |[**list[AssociatedPerson]**](AssociatedPerson.md) |Associated persons.              |[optional] 
**attachments** |[**list[Attachment]**](Attachment.md) |Document attachments.              |[optional] 
**company_name** |**str** |Company name.              |[optional] 
**computer_network_name** |**str** |Computer network.              |[optional] 
**customer_id** |**str** |Customer id.              |[optional] 
**department_name** |**str** |Department name.              |[optional] 
**display_name** |**str** |Display name.              |[optional] 
**email_addresses** |[**list[EmailAddress]**](EmailAddress.md) |Person&#39;s email addresses.              |[optional] 
**events** |[**list[CustomerEvent]**](CustomerEvent.md) |Person&#39;s events.              |[optional] 
**file_as** |**str** |A name used for sorting.              |[optional] 
**file_as_mapping** |**str** |Specifies how to generate and recompute the value of the dispidFileAs property when other contact name properties change. Coincides MS-OXPROPS revision 16.2 from 7/31/2014. Enum, available values: Empty, DisplayName, FirstName, LastName, Organization, LastFirstMiddle, OrgLastFirstMiddle, LastFirstMiddleOrg, LastFirstMiddle2, LastFirstMiddle3, OrgLastFirstMiddle2, OrgLastFirstMiddle3, LastFirstMiddleOrg2, LastFirstMiddleOrg3, LastFirstMiddleGen, FirstMiddleLastGen, LastFirstMiddleGen2, BestMatch, AccordingToLocale, None |
**free_busy_location** |**str** |URL path from which a client can retrieve free/busy information for the contact as an iCal file.              |[optional] 
**gender** |**str** |Enum defines gender of a person. Enum, available values: Unspecified, Female, Male |
**given_name** |**str** |Person&#39;s given name.              |[optional] 
**government_id_number** |**str** |Government id number.              |[optional] 
**hobbies** |**str** |Person&#39;s hobbies.              |[optional] 
**initials** |**str** |Person&#39;s initials.              |[optional] 
**instant_messengers** |[**list[InstantMessengerAddress]**](InstantMessengerAddress.md) |Person&#39;s instant messenger addresses.              |[optional] 
**job_title** |**str** |Person&#39;s job title.              |[optional] 
**language** |**str** |Language.              |[optional] 
**location** |**str** |Person&#39;s location.              |[optional] 
**middle_name** |**str** |Person&#39;s middle name.              |[optional] 
**nickname** |**str** |Person&#39;s nickname.              |[optional] 
**notes** |**str** |Notes.              |[optional] 
**notes_format** |**str** |Defines format of a text. Enum, available values: Text, Html |
**office_location** |**str** |Office location.              |[optional] 
**organizational_id_number** |**str** |Contains an identifier for the mail user used within the mail user&#39;s organization.              |[optional] 
**phone_numbers** |[**list[PhoneNumber]**](PhoneNumber.md) |Person&#39;s phone numbers.              |[optional] 
**photo** |[**ContactPhoto**](ContactPhoto.md) |Person&#39;s photo.              |[optional] 
**physical_addresses** |[**list[PostalAddress]**](PostalAddress.md) |Person&#39;s physical addresses.              |[optional] 
**preferred_text_encoding** |**str** |Encoding for all text properties.              |[optional] 
**prefix** |**str** |A prefix of a full name such like Mr.(mister), Dr.(doctor) and so on.              |[optional] 
**profession** |**str** |A job position of a person in a company.              |[optional] 
**suffix** |**str** |A suffix of a full name such like Jr.(junior), Sr.(senior) and so on.              |[optional] 
**surname** |**str** |Person&#39;s surname.              |[optional] 
**urls** |[**list[Url]**](Url.md) |Person&#39;s urls.              |[optional] 



## Example
```python
contact_dto = models.ContactDto(
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
            href='www.aspose.com')])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

