# AsposeEmailCloudSdk.StorageApi

        
<a name="get_disc_usage"></a>
# get_disc_usage

```python
get_disc_usage(self, request: GetDiscUsageRequest)
```



### Return type

DiscUsage

### request Parameter
```python
GetDiscUsageRequest(
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_file_versions"></a>
# get_file_versions

```python
get_file_versions(self, request: GetFileVersionsRequest)
```



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
 **path** | **str** |  | 
 **storage_name** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="object_exists"></a>
# object_exists

```python
object_exists(self, request: ObjectExistsRequest)
```



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
 **path** | **str** |  | 
 **storage_name** | **str** |  | [optional] 
 **version_id** | **str** |  | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="exists"></a>
# exists

```python
exists(self, request: StorageExistsRequest)
```



### Return type

StorageExist

### request Parameter
```python
StorageExistsRequest(
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str** |  | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

