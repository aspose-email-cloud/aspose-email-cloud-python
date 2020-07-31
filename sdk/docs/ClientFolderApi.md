# AsposeEmailCloudSdk.ClientFolderApi

<a name="client_folder_create"></a>
# **client_folder_create**
> client_folder_create(self, client_folder_create_request)

Create new folder in email account             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientFolderApi.client_folder_create(
    cakePrefix_client_folder_create_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientFolderCreateRequest**](ClientFolderCreateRequest.md)| Create folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_folder_create_async"></a>
# **client_folder_create_async**
> client_folder_create_async(self, client_folder_create_request)

Create new folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_folder_create_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientFolderApi.client_folder_create_async(
    cakePrefix_client_folder_create_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientFolderCreateRequest**](ClientFolderCreateRequest.md)| Create folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_folder_delete"></a>
# **client_folder_delete**
> client_folder_delete(self, client_folder_delete_request)

Delete a folder in email account             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientFolderApi.client_folder_delete(
    cakePrefix_client_folder_delete_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientFolderDeleteRequest**](ClientFolderDeleteRequest.md)| Delete folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_folder_delete_async"></a>
# **client_folder_delete_async**
> client_folder_delete_async(self, client_folder_delete_request)

Delete a folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_folder_delete_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientFolderApi.client_folder_delete_async(
    cakePrefix_client_folder_delete_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientFolderDeleteRequest**](ClientFolderDeleteRequest.md)| Delete folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_folder_get_list"></a>
# **client_folder_get_list**
> client_folder_get_list(self, client_folder_get_list_request)

Get folders list in email account             

### Return type

[**MailServerFolderList**](MailServerFolderList.md)

### Request Parameters
```python
__init__(self, 
    account, 
    storage=storage, 
    account_storage_folder=account_storage_folder, 
    parent_folder=parent_folder)
```

### Usage
```python
ClientFolderApi.client_folder_get_list(
    cakePrefix_client_folder_get_list_request_cakeCodePostProcessor(
        account, 
        storage=storage, 
        account_storage_folder=account_storage_folder, 
        parent_folder=parent_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Email account | 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 
 **parent_folder** | **str**| Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_folder_get_list_async"></a>
# **client_folder_get_list_async**
> client_folder_get_list_async(self, client_folder_get_list_request)

Get folders list in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_folder_get_list_async(request).get() returns [**MailServerFolderList**](MailServerFolderList.md)

### Request Parameters
```python
__init__(self, 
    account, 
    storage=storage, 
    account_storage_folder=account_storage_folder, 
    parent_folder=parent_folder)
```

### Usage
```python
ClientFolderApi.client_folder_get_list_async(
    cakePrefix_client_folder_get_list_request_cakeCodePostProcessor(
        account, 
        storage=storage, 
        account_storage_folder=account_storage_folder, 
        parent_folder=parent_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Email account | 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 
 **parent_folder** | **str**| Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

