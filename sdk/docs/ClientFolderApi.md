# AsposeEmailCloudSdk.ClientFolderApi (EmailCloud.client.folder)

Email client folder operations.

<a name="create"></a>
## create

Description: Create new folder in email account             

Method call example:
```python
api.client.folder.create(request)
```

### Parameter: request

Description: Create folder request

See parameter model documentation at [ClientFolderCreateRequest](ClientFolderCreateRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientFolderCreateRequest(
    parent_folder='INBOX/SubFolder/ParentFolder',
    folder_name='NewFolder',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.ClientFolderCreateRequest(
    parent_folder='INBOX/SubFolder/ParentFolder',
    folder_name='NewFolder',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))

// Call method:
api.client.folder.create(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="delete"></a>
## delete

Description: Delete a folder in email account             

Method call example:
```python
api.client.folder.delete(request)
```

### Parameter: request

Description: Delete folder request

See parameter model documentation at [ClientFolderDeleteRequest](ClientFolderDeleteRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientFolderDeleteRequest(
    folder='INBOX/SubFolder/FolderToDelete',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.ClientFolderDeleteRequest(
    folder='INBOX/SubFolder/FolderToDelete',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))

// Call method:
api.client.folder.delete(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_list"></a>
## get_list

Description: Get folders list in email account             

Returns: Folders list

Method call example:
```python
result = api.client.folder.get_list(request)
```

### Parameter: request

Description: get_list method request.

See parameter model documentation at [ClientFolderGetListRequest](ClientFolderGetListRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.ClientFolderGetListRequest(
    account='email.multi.account',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    parent_folder='INBOX')
```

</details>

### Result

Description: Folders list

Return type: [**MailServerFolderList**](MailServerFolderList.md)

<details>
    <summary>Result example</summary>

```python
result = 
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.ClientFolderGetListRequest(
    account='email.multi.account',
    storage='First Storage',
    account_storage_folder='email/account/location/on/storage',
    parent_folder='INBOX')

// Call method:
result = api.client.folder.get_list(request)

// Result example:
result = 
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

