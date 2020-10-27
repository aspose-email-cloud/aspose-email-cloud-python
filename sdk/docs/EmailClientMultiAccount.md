# AsposeEmailCloudSdk.models.EmailClientMultiAccount

Email client virtual account, which contains several accounts             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receive_accounts** |[**list[EmailClientAccount]**](EmailClientAccount.md) |Email client receive accounts              |
**send_account** |[**EmailClientAccount**](EmailClientAccount.md) |Email client send account              |[optional] 



## Example
```python
email_client_multi_account = models.EmailClientMultiAccount(
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
            login='example@gmail.com')))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

