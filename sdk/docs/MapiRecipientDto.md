# AsposeEmailCloudSdk.models.MapiRecipientDto

Represents the recipient information in the Microsoft Outlook Message.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** |**str** |Email address of the message recipient or sender.              |[optional] 
**address_type** |**str** |Type of the address of the message recipient or sender.              |[optional] 
**display_name** |**str** |Display name of the message recipient or sender.              |[optional] 
**recipient_type** |**str** |Represent the PR_RECIPIENT_TYPE property which contains the recipient type for a message recipient. Enum, available values: Unknown, MapiBcc, MapiCc, MapiP1, MapiSubmitted, MapiTo |



## Example
```python
mapi_recipient_dto = models.MapiRecipientDto(
    email_address='to@aspose.com',
    address_type='SMTP',
    display_name='To Address',
    recipient_type='MapiTo')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

