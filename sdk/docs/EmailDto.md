# AsposeEmailCloudSdk.models.EmailDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_views** | [**list[AlternateView]**](AlternateView.md) | Collection of alternate views of message.              | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Email message attachments.              | [optional] 
**bcc** | [**list[MailAddress]**](MailAddress.md) | BCC recipients.              | [optional] 
**body** | **str** | Email message body as plain text.              | [optional] 
**body_encoding** | **str** | Body encoding.              | [optional] 
**body_type** | **str** | The content type of message body. Enum, available values: PlainText, Html, Rtf | 
**cc** | [**list[MailAddress]**](MailAddress.md) | CC recipients.              | [optional] 
**_date** | **datetime** | Message date.              | 
**delivery_notification_options** | **list[str]** | Delivery notifications.              | [optional] 
**_from** | [**MailAddress**](MailAddress.md) | From address.              | [optional] 
**headers** | **dict(str, str)** | Document headers.              | [optional] 
**html_body** | **str** | HTML body.              | [optional] 
**html_body_text** | **str** | Html body as plain text. Read only.              | [optional] 
**is_body_html** | **bool** | Indicates whether the message body is in Html.              | 
**is_draft** | **bool** | Indicates whether or not a message has been sent.              | 
**is_encrypted** | **bool** | Indicates whether the message is encrypted. Read only.              | 
**is_signed** | **bool** | Indicates whether the message is signed. Read only.              | 
**linked_resources** | [**list[LinkedResource]**](LinkedResource.md) | Linked resources of message.              | [optional] 
**message_id** | **str** | Message id.              | [optional] 
**original_is_tnef** | **bool** | Indicates whether original EML message is in TNEF format. Read only.              | 
**preferred_text_encoding** | **str** | Preferred encoding.              | [optional] 
**priority** | **str** | Email priority status. Enum, available values: High, Low, Normal | 
**read_receipt_to** | [**list[MailAddress]**](MailAddress.md) | Read receipt addresses.              | [optional] 
**reply_to_list** | [**list[MailAddress]**](MailAddress.md) | The list of addresses to reply to for the mail message.              | [optional] 
**reverse_path** | [**MailAddress**](MailAddress.md) | ReversePath address.              | [optional] 
**sender** | [**MailAddress**](MailAddress.md) | Sender address.              | [optional] 
**sensitivity** | **str** | Specifies the sensitivity of a MailMessage. Enum, available values: None, Normal, Personal, Private, CompanyConfidential | 
**subject** | **str** | Message subject.              | [optional] 
**subject_encoding** | **str** | Subject encoding.              | [optional] 
**time_zone_offset** | **int** | Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the local time and UTC represented as count of ticks (10 000 per millisecond).              | [optional] 
**to** | [**list[MailAddress]**](MailAddress.md) | The address collection that contains the recipients of message.              | [optional] 
**x_mailer** | **str** | The X-Mailer the software that created the e-mail message.              | [optional] 



[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


