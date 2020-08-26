# AsposeEmailCloudSdk.FileApi

        
<a name="copy_file"></a>
# copy_file

```python
copy_file(self, request: CopyFileRequest)
```



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
 **src_path** | **str** |  | 
 **dest_path** | **str** |  | 
 **src_storage_name** | **str** |  | [optional] 
 **dest_storage_name** | **str** |  | [optional] 
 **version_id** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="delete_file"></a>
# delete_file

```python
delete_file(self, request: DeleteFileRequest)
```



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
 **path** | **str** |  | 
 **storage_name** | **str** |  | [optional] 
 **version_id** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="download_file"></a>
# download_file

```python
download_file(self, request: DownloadFileRequest)
```



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
 **path** | **str** |  | 
 **storage_name** | **str** |  | [optional] 
 **version_id** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="move_file"></a>
# move_file

```python
move_file(self, request: MoveFileRequest)
```



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
 **src_path** | **str** |  | 
 **dest_path** | **str** |  | 
 **src_storage_name** | **str** |  | [optional] 
 **dest_storage_name** | **str** |  | [optional] 
 **version_id** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="upload_file"></a>
# upload_file

```python
upload_file(self, request: UploadFileRequest)
```



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
 **path** | **str** |  | 
 **file** | **str** | File to upload | 
 **storage_name** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

