# AsposeEmailCloudSdk.FileApi

<a name="copy_file"></a>
# **copy_file**
> copy_file(self, copy_file_request)

Copy file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="copy_file_async"></a>
# **copy_file_async**
> copy_file_async(self, copy_file_request)

Copy file

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_file"></a>
# **delete_file**
> delete_file(self, delete_file_request)

Delete file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_file_async"></a>
# **delete_file_async**
> delete_file_async(self, delete_file_request)

Delete file

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="download_file"></a>
# **download_file**
> download_file(self, download_file_request)

Download file

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="download_file_async"></a>
# **download_file_async**
> download_file_async(self, download_file_request)

Download file

Performs operation asynchronously.

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_file"></a>
# **move_file**
> move_file(self, move_file_request)

Move file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_file_async"></a>
# **move_file_async**
> move_file_async(self, move_file_request)

Move file

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="upload_file"></a>
# **upload_file**
> upload_file(self, upload_file_request)

Upload file

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Request Parameters
```python
__init__(self, 
    path, 
    file, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="upload_file_async"></a>
# **upload_file_async**
> upload_file_async(self, upload_file_request)

Upload file

Performs operation asynchronously.

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Request Parameters
```python
__init__(self, 
    path, 
    file, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

