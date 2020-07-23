# AsposeEmailCloudSdk.models.MapiMessageItemBaseDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**list[MapiAttachmentDto]**](MapiAttachmentDto.md) | Message item attachments.              | [optional] 
**billing** | **str** | Billing information associated with an item.              | [optional] 
**body** | **str** | Message text.              | [optional] 
**body_html** | **str** | Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.              | [optional] 
**body_rtf** | **str** | RTF formatted message text.              | [optional] 
**body_type** | **str** | The content type of message body. Enum, available values: PlainText, Html, Rtf | 
**categories** | **list[str]** | Contains keywords or categories for the message object.              | [optional] 
**companies** | **list[str]** | Contains the names of the companies that are associated with an item.              | [optional] 
**item_id** | **str** | The item id, uses with a server.              | [optional] 
**message_class** | **str** | Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.              | [optional] 
**mileage** | **str** | Contains the mileage information that is associated with an item.              | [optional] 
**recipients** | [**list[MapiRecipientDto]**](MapiRecipientDto.md) | Recipients of the message.              | [optional] 
**sensitivity** | **str** | Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential | 
**subject** | **str** | Subject of the message.              | [optional] 
**subject_prefix** | **str** | Subject prefix that typically indicates some action on a message, such as \&quot;FW: \&quot; for forwarding.              | [optional] 
**properties** | [**list[MapiPropertyDto]**](MapiPropertyDto.md) | List of MAPI properties              | [optional] 
**discriminator** | **str** |  | 



[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


