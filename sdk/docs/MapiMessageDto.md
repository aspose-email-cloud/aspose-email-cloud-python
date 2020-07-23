# AsposeEmailCloudSdk.models.MapiMessageDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_body** | **str** | Message text              | [optional] 
**client_submit_time** | **datetime** | Date and time the message sender submitted a message.              | 
**conversation_topic** | **str** | Topic of the first message in a conversation thread.              | [optional] 
**delivery_time** | **datetime** | Date and time a message was delivered.              | 
**display_bcc** | **str** | List of the display names of any blind carbon copy (BCC) message recipients, separated by semicolons (;).              | [optional] 
**display_cc** | **str** | List of the display names of any carbon copy (CC) message recipients, separated by semicolons (;).              | [optional] 
**display_name** | **str** | Display name for the message.              | [optional] 
**display_name_prefix** | **str** | Prefix of the display name.              | [optional] 
**display_to** | **str** | List of the display names of the primary (To) message recipients, separated by semicolons (;).              | [optional] 
**flags** | **list[str]** | Message flags.              Items: Mapi message flags. Enum, available values: MsgFlagZero, MsgFlagRead, MsgFlagUnmodified, MsgFlagSubmit, MsgFlagUnsent, MsgFlagHasAttach, MsgFlagFromMe, MsgFlagAssociated, MsgFlagResend, MsgFlagNotifyRead, MsgFlagNotifyUnread, MsgFlagEverRead, MsgFlagOriginX400, MsgFlagOriginInternet, MsgFlagOriginMiscExt | [optional] 
**headers** | **dict(str, str)** | Transport message headers              | [optional] 
**internet_message_id** | **str** | Internet message id of the message.              | [optional] 
**message_format** | **str** | Represents outlook message format. Enum, available values: Ascii, Unicode | 
**normalized_subject** | **str** | Normalized subject of the message.              | [optional] 
**read_receipt_requested** | **bool** | Value indicating whether the read receipt is requested. | 
**reply_to** | **str** | Reply to names. | [optional] 
**sender_address_type** | **str** | Message sender&#39;s e-mail address type. | [optional] 
**sender_email_address** | **str** | Message sender&#39;s e-mail address. | [optional] 
**sender_name** | **str** | Message sender&#39;s display name. | [optional] 
**sender_smtp_address** | **str** | Message sender&#39;s e-mail address. | [optional] 
**sent_representing_address_type** | **str** | Address type for the messaging user represented by the sender. | [optional] 
**sent_representing_email_address** | **str** | E-mail address for the messaging user represented by the sender. | [optional] 
**sent_representing_name** | **str** | Display name for the messaging user represented by the sender. | [optional] 
**sent_representing_smtp_address** | **str** | E-mail address for the messaging user represented by the sender. | [optional] 
**transport_message_headers** | **str** | Transport-specific message envelope information. | [optional] 

 Parent class: [MapiMessageItemBaseDto](MapiMessageItemBaseDto.md)

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


