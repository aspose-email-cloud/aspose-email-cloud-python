# AsposeEmailCloudSdk.StorageApi

<a name="get_disc_usage"></a>
# **get_disc_usage**
> get_disc_usage(self, get_disc_usage_request)

Get disc usage

### Return type

[**DiscUsage**](DiscUsage.md)

### Request Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

### Usage
```python
StorageApi.get_disc_usage(
    cakePrefix_get_disc_usage_request_cakeCodePostProcessor(
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_disc_usage_async"></a>
# **get_disc_usage_async**
> get_disc_usage_async(self, get_disc_usage_request)

Get disc usage

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_disc_usage_async(request).get() returns [**DiscUsage**](DiscUsage.md)

### Request Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

### Usage
```python
StorageApi.get_disc_usage_async(
    cakePrefix_get_disc_usage_request_cakeCodePostProcessor(
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_file_versions"></a>
# **get_file_versions**
> get_file_versions(self, get_file_versions_request)

Get file versions

### Return type

[**FileVersions**](FileVersions.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
StorageApi.get_file_versions(
    cakePrefix_get_file_versions_request_cakeCodePostProcessor(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_file_versions_async"></a>
# **get_file_versions_async**
> get_file_versions_async(self, get_file_versions_request)

Get file versions

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_file_versions_async(request).get() returns [**FileVersions**](FileVersions.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
StorageApi.get_file_versions_async(
    cakePrefix_get_file_versions_request_cakeCodePostProcessor(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="object_exists"></a>
# **object_exists**
> object_exists(self, object_exists_request)

Check if file or folder exists

### Return type

[**ObjectExist**](ObjectExist.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
StorageApi.object_exists(
    cakePrefix_object_exists_request_cakeCodePostProcessor(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="object_exists_async"></a>
# **object_exists_async**
> object_exists_async(self, object_exists_request)

Check if file or folder exists

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
object_exists_async(request).get() returns [**ObjectExist**](ObjectExist.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
StorageApi.object_exists_async(
    cakePrefix_object_exists_request_cakeCodePostProcessor(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="storage_exists"></a>
# **storage_exists**
> storage_exists(self, storage_exists_request)

Check if storage exists

### Return type

[**StorageExist**](StorageExist.md)

### Request Parameters
```python
__init__(self, 
    storage_name)
```

### Usage
```python
StorageApi.storage_exists(
    cakePrefix_storage_exists_request_cakeCodePostProcessor(
        storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="storage_exists_async"></a>
# **storage_exists_async**
> storage_exists_async(self, storage_exists_request)

Check if storage exists

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
storage_exists_async(request).get() returns [**StorageExist**](StorageExist.md)

### Request Parameters
```python
__init__(self, 
    storage_name)
```

### Usage
```python
StorageApi.storage_exists_async(
    cakePrefix_storage_exists_request_cakeCodePostProcessor(
        storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

