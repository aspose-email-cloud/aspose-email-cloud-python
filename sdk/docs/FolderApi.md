
# AsposeEmailCloudSdk.FolderApi

        
<a name="copy_folder"></a>
# copy_folder

```python
copy_folder(self, request: CopyFolderRequest)
```

Copy folder

### Return type

None

### request Parameter
```python
CopyFolderRequest(
    src_path,
    dest_path,
    src_storage_name,
    dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str** | Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str** | Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str** | Source storage name | [optional] 
 **dest_storage_name** | **str** | Destination storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="create_folder"></a>
# create_folder

```python
create_folder(self, request: CreateFolderRequest)
```

Create the folder

### Return type

None

### request Parameter
```python
CreateFolderRequest(
    path,
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="delete_folder"></a>
# delete_folder

```python
delete_folder(self, request: DeleteFolderRequest)
```

Delete folder

### Return type

None

### request Parameter
```python
DeleteFolderRequest(
    path,
    storage_name,
    recursive)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str** | Storage name | [optional] 
 **recursive** | **bool** | Enable to delete folders, subfolders and files | [optional] [default to false]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_files_list"></a>
# get_files_list

```python
get_files_list(self, request: GetFilesListRequest)
```

Get all files and folders within a folder

### Return type

FilesList

### request Parameter
```python
GetFilesListRequest(
    path,
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="move_folder"></a>
# move_folder

```python
move_folder(self, request: MoveFolderRequest)
```

Move folder

### Return type

None

### request Parameter
```python
MoveFolderRequest(
    src_path,
    dest_path,
    src_storage_name,
    dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str** | Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str** | Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str** | Source storage name | [optional] 
 **dest_storage_name** | **str** | Destination storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

