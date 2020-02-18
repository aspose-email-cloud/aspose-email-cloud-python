# AsposeEmailCloudSdk.models.EmailAccountConfig
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Email account display name              | [optional] 
**protocol_type** | **str** | Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav | 
**host** | **str** | Email account host.              | [optional] 
**port** | **int** | Port.              | [optional] 
**socket_type** | **str** | Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto | 
**authentication_types** | **list[str]** | Supported authentication types.              Items: Email account authentication types. Enum, available values: NoAuth, OAuth2, PasswordCleartext, PasswordEncrypted, SmtpAfterPop, ClientIpAddress | [optional] 
**extra_info** | [**list[NameValuePair]**](NameValuePair.md) | Extra account information.              | [optional] 
**is_validated** | **bool** | Determines that configuration validated. Set to false if validation skipped.              | 



[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


