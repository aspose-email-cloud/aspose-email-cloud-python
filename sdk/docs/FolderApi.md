# AsposeEmailCloudSdk.FolderApi (EmailCloud.cloud_storage.folder)

Folder operations controller

<a name="copy_folder"></a>
## copy_folder

Description: Copy folder

Method call example:
```python
api.cloud_storage.folder.copy_folder(request)
```

### Parameter: request

Description: copy_folder method request.

See parameter model documentation at [CopyFolderRequest](CopyFolderRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CopyFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')
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
request = models.CopyFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')

// Call method:
api.cloud_storage.folder.copy_folder(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="create_folder"></a>
## create_folder

Description: Create the folder

Method call example:
```python
api.cloud_storage.folder.create_folder(request)
```

### Parameter: request

Description: create_folder method request.

See parameter model documentation at [CreateFolderRequest](CreateFolderRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CreateFolderRequest(
    path='/storage/path/to/new/folder',
    storage_name='First Storage')
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
request = models.CreateFolderRequest(
    path='/storage/path/to/new/folder',
    storage_name='First Storage')

// Call method:
api.cloud_storage.folder.create_folder(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="delete_folder"></a>
## delete_folder

Description: Delete folder

Method call example:
```python
api.cloud_storage.folder.delete_folder(request)
```

### Parameter: request

Description: delete_folder method request.

See parameter model documentation at [DeleteFolderRequest](DeleteFolderRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.DeleteFolderRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage',
    recursive=True)
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
request = models.DeleteFolderRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage',
    recursive=True)

// Call method:
api.cloud_storage.folder.delete_folder(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_files_list"></a>
## get_files_list

Description: Get all files and folders within a folder

Returns: Returns all files and folders contained by the folder.

Method call example:
```python
result = api.cloud_storage.folder.get_files_list(request)
```

### Parameter: request

Description: get_files_list method request.

See parameter model documentation at [GetFilesListRequest](GetFilesListRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.GetFilesListRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage')
```

</details>

### Result

Description: Returns all files and folders contained by the folder.

Return type: [**FilesList**](FilesList.md)

<details>
    <summary>Result example</summary>

```python
result = models.FilesList(
    value=[
        models.StorageFile(
            name='file.ext',
            modified_date=datetime.today(),
            size=1024,
            path='/path/to/file/on/storage')])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.GetFilesListRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage')

// Call method:
result = api.cloud_storage.folder.get_files_list(request)

// Result example:
result = models.FilesList(
    value=[
        models.StorageFile(
            name='file.ext',
            modified_date=datetime.today(),
            size=1024,
            path='/path/to/file/on/storage')])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="move_folder"></a>
## move_folder

Description: Move folder

Method call example:
```python
api.cloud_storage.folder.move_folder(request)
```

### Parameter: request

Description: move_folder method request.

See parameter model documentation at [MoveFolderRequest](MoveFolderRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MoveFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')
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
request = models.MoveFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')

// Call method:
api.cloud_storage.folder.move_folder(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

