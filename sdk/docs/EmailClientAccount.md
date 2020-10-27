# AsposeEmailCloudSdk.models.EmailClientAccount
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Mail server host name or IP address              | 
**port** | **int** | Mail server port              | 
**security_options** | **str** | Email account security mode Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto | 
**protocol_type** | **str** | Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav | 
**credentials** | [**EmailClientAccountCredentials**](EmailClientAccountCredentials.md) | Email client account credentials              | 
**cache_file** | [**StorageFileLocation**](StorageFileLocation.md) | File with messages cache. Used to provide extra functions, which are not supported by account              | [optional] 



[[Back to Model list]](Models.md) [[Back to README]](README.md)


