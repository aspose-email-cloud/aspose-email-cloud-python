# AsposeEmailCloudSdk.FileApi

        
<a name="copy_file"></a>
# copy_file

```python
copy_file(self, request: CopyFileRequest)
```

Copy file

### Return type

None

### request Parameter
```python
CopyFileRequest(
    src_path,
    dest_path,
    src_storage_name,
    dest_storage_name,
    version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str** | Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str** | Destination file path | 
 **src_storage_name** | **str** | Source storage name | [optional] 
 **dest_storage_name** | **str** | Destination storage name | [optional] 
 **version_id** | **str** | File version ID to copy | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="delete_file"></a>
# delete_file

```python
delete_file(self, request: DeleteFileRequest)
```

Delete file

### Return type

None

### request Parameter
```python
DeleteFileRequest(
    path,
    storage_name,
    version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str** | Storage name | [optional] 
 **version_id** | **str** | File version ID to delete | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="download_file"></a>
# download_file

```python
download_file(self, request: DownloadFileRequest)
```

Download file

### Return type

str

### request Parameter
```python
DownloadFileRequest(
    path,
    storage_name,
    version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str** | Storage name | [optional] 
 **version_id** | **str** | File version ID to download | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="move_file"></a>
# move_file

```python
move_file(self, request: MoveFileRequest)
```

Move file

### Return type

None

### request Parameter
```python
MoveFileRequest(
    src_path,
    dest_path,
    src_storage_name,
    dest_storage_name,
    version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str** | Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str** | Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str** | Source storage name | [optional] 
 **dest_storage_name** | **str** | Destination storage name | [optional] 
 **version_id** | **str** | File version ID to move | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="upload_file"></a>
# upload_file

```python
upload_file(self, request: UploadFileRequest)
```

Upload file

### Return type

FilesUploadResult

### request Parameter
```python
UploadFileRequest(
    path,
    file,
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **str** | File to upload | 
 **storage_name** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

