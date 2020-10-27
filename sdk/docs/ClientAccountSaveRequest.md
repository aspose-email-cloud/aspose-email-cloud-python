# AsposeEmailCloudSdk.models.ClientAccountSaveRequest

Email client account save request             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [StorageModelOfEmailClientAccount](StorageModelOfEmailClientAccount.md)


## Example
```python
client_account_save_request = models.ClientAccountSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.EmailClientAccount(
        host='smtp.example.com',
        port=465,
        security_options='SSLAuto',
        protocol_type='SMTP',
        credentials=models.EmailClientAccountOauthCredentials(
            client_id='clientId',
            client_secret='clientSecret',
            refresh_token='refreshToken',
            login='example@example.com')))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

