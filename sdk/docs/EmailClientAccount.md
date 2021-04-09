# AsposeEmailCloudSdk.models.EmailClientAccount

A universal email client account             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** |**str** |Mail server host name or IP address              |
**port** |**int** |Mail server port              |
**security_options** |**str** |Email account security mode Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto |
**protocol_type** |**str** |Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav |
**credentials** |[**EmailClientAccountCredentials**](EmailClientAccountCredentials.md) |Email client account credentials              |
**cache_file** |[**StorageFileLocation**](StorageFileLocation.md) |File with messages cache. Used to provide extra functions, which are not supported by account              |[optional] 



## Example
```python
email_client_account = models.EmailClientAccount(
    host='smtp.example.com',
    port=465,
    security_options='SSLAuto',
    protocol_type='SMTP',
    credentials=models.EmailClientAccountOauthCredentials(
        client_id='clientId',
        client_secret='clientSecret',
        refresh_token='refreshToken',
        login='example@example.com'),
    cache_file=models.StorageFileLocation(
        file_name='account.cache',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

