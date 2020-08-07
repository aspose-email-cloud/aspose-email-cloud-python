# AsposeEmailCloudSdk.StorageApi

        
<a name="get_disc_usage"></a>
# get_disc_usage

```python
get_disc_usage(self, request: GetDiscUsageRequest)
```

Get disc usage

### Return type

DiscUsage

### request Parameter
```python
GetDiscUsageRequest(
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_file_versions"></a>
# get_file_versions

```python
get_file_versions(self, request: GetFileVersionsRequest)
```

Get file versions

### Return type

FileVersions

### request Parameter
```python
GetFileVersionsRequest(
    path,
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="object_exists"></a>
# object_exists

```python
object_exists(self, request: ObjectExistsRequest)
```

Check if file or folder exists

### Return type

ObjectExist

### request Parameter
```python
ObjectExistsRequest(
    path,
    storage_name,
    version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str** | File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str** | Storage name | [optional] 
 **version_id** | **str** | File version ID | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="exists"></a>
# exists

```python
exists(self, request: StorageExistsRequest)
```

Check if storage exists

### Return type

StorageExist

### request Parameter
```python
StorageExistsRequest(
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str** | Storage name | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

