# AsposeEmailCloudSdk.ClientAccountApi (EmailCloud.client.account)

Email server account for built-in client operations.

<a name="get"></a>
## get

Description: Get email client account from storage.             

Returns: Email client account from storage.

Method call example:
```python
result = api.client.account.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [ClientAccountGetRequest](ClientAccountGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientAccountGetRequest(
    file_name='email.account',
    folder='email/account/location/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: Email client account from storage.

Return type: [**EmailClientAccount**](EmailClientAccount.md)

<details>
    <summary>Result example</summary>

```python
result = models.EmailClientAccount(
    host='smtp.example.com',
    port=465,
    security_options='SSLAuto',
    protocol_type='SMTP',
    credentials=models.EmailClientAccountOauthCredentials(
        client_id='clientId',
        client_secret='clientSecret',
        refresh_token='refreshToken',
        login='example@example.com'))
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ClientAccountGetRequest(
    file_name='email.account',
    folder='email/account/location/on/storage',
    storage='First Storage')

// Call method:
result = api.client.account.get(request)

// Result example:
result = models.EmailClientAccount(
    host='smtp.example.com',
    port=465,
    security_options='SSLAuto',
    protocol_type='SMTP',
    credentials=models.EmailClientAccountOauthCredentials(
        client_id='clientId',
        client_secret='clientSecret',
        refresh_token='refreshToken',
        login='example@example.com'))
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_multi"></a>
## get_multi

Description: Get email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

Returns: Email client multi account from storage

Method call example:
```python
result = api.client.account.get_multi(request)
```

### Parameter: request

Description: get_multi method request.

See parameter model documentation at [ClientAccountGetMultiRequest](ClientAccountGetMultiRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientAccountGetMultiRequest(
    file_name='email.multi.account',
    folder='email/account/location/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: Email client multi account from storage

Return type: [**EmailClientMultiAccount**](EmailClientMultiAccount.md)

<details>
    <summary>Result example</summary>

```python
result = models.EmailClientMultiAccount(
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
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ClientAccountGetMultiRequest(
    file_name='email.multi.account',
    folder='email/account/location/on/storage',
    storage='First Storage')

// Call method:
result = api.client.account.get_multi(request)

// Result example:
result = models.EmailClientMultiAccount(
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

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="save"></a>
## save

Description: Create/update email client account file (*.account) with credentials             

Method call example:
```python
api.client.account.save(request)
```

### Parameter: request

Description: Email account information

See parameter model documentation at [ClientAccountSaveRequest](ClientAccountSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientAccountSaveRequest(
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

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ClientAccountSaveRequest(
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

// Call method:
api.client.account.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="save_multi"></a>
## save_multi

Description: Create email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

Method call example:
```python
api.client.account.save_multi(request)
```

### Parameter: request

Description: Email accounts information.

See parameter model documentation at [ClientAccountSaveMultiRequest](ClientAccountSaveMultiRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientAccountSaveMultiRequest(
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

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(app_key, app_sid)

// Prepare parameters:
request = models.ClientAccountSaveMultiRequest(
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

// Call method:
api.client.account.save_multi(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

