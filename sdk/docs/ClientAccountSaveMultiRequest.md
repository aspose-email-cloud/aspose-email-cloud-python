# AsposeEmailCloudSdk.models.ClientAccountSaveMultiRequest

Email client multi account save request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [StorageModelOfEmailClientMultiAccount](StorageModelOfEmailClientMultiAccount.md)


## Example
```python
client_account_save_multi_request = models.ClientAccountSaveMultiRequest(
    storage_file=models.StorageFileLocation(
        file_name='email.multi.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.EmailClientMultiAccount(
        receive_accounts=[
            models.EmailClientAccount(
                host='imap.gmail.com',
                port=993,
                security_options='SSLAuto',
                credentials=models.EmailClientAccountPasswordCredentials(
                    password='password',
                    login='example@gmail.com')),
            models.EmailClientAccount(
                host='exchange@outlook.com',
                port=443,
                protocol_type='EWS',
                credentials=models.EmailClientAccountOauthCredentials(
                    client_id='clientId',
                    client_secret='clientSecret',
                    refresh_token='refreshToken',
                    login='example@outlook.com'))],
        send_account=models.EmailClientAccount(
            host='smtp.gmail.com',
            port=465,
            security_options='SSLAuto',
            protocol_type='SMTP',
            credentials=models.EmailClientAccountPasswordCredentials(
                password='password',
                login='example@gmail.com'))))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

