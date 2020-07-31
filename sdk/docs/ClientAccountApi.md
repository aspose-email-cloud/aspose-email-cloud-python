# AsposeEmailCloudSdk.ClientAccountApi

<a name="client_account_get"></a>
# **client_account_get**
> client_account_get(self, client_account_get_request)

Get email client account from storage.             

### Return type

[**EmailClientAccount**](EmailClientAccount.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
ClientAccountApi.client_account_get(
    cakePrefix_client_account_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name on storage. | 
 **folder** | **str**| Folder on storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_get_async"></a>
# **client_account_get_async**
> client_account_get_async(self, client_account_get_request)

Get email client account from storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_account_get_async(request).get() returns [**EmailClientAccount**](EmailClientAccount.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
ClientAccountApi.client_account_get_async(
    cakePrefix_client_account_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name on storage. | 
 **folder** | **str**| Folder on storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_get_multi"></a>
# **client_account_get_multi**
> client_account_get_multi(self, client_account_get_multi_request)

Get email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

### Return type

[**EmailClientMultiAccount**](EmailClientMultiAccount.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
ClientAccountApi.client_account_get_multi(
    cakePrefix_client_account_get_multi_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name on storage | 
 **folder** | **str**| Folder on storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_get_multi_async"></a>
# **client_account_get_multi_async**
> client_account_get_multi_async(self, client_account_get_multi_request)

Get email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_account_get_multi_async(request).get() returns [**EmailClientMultiAccount**](EmailClientMultiAccount.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
ClientAccountApi.client_account_get_multi_async(
    cakePrefix_client_account_get_multi_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name on storage | 
 **folder** | **str**| Folder on storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_save"></a>
# **client_account_save**
> client_account_save(self, client_account_save_request)

Create/update email client account file (*.account) with credentials             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientAccountApi.client_account_save(
    cakePrefix_client_account_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailClientAccountSaveRequest**](EmailClientAccountSaveRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_save_async"></a>
# **client_account_save_async**
> client_account_save_async(self, client_account_save_request)

Create/update email client account file (*.account) with credentials             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_account_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientAccountApi.client_account_save_async(
    cakePrefix_client_account_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailClientAccountSaveRequest**](EmailClientAccountSaveRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_save_multi"></a>
# **client_account_save_multi**
> client_account_save_multi(self, client_account_save_multi_request)

Create email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientAccountApi.client_account_save_multi(
    cakePrefix_client_account_save_multi_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailClientMultiAccountSaveRequest**](EmailClientMultiAccountSaveRequest.md)| Email accounts information. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_account_save_multi_async"></a>
# **client_account_save_multi_async**
> client_account_save_multi_async(self, client_account_save_multi_request)

Create email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_account_save_multi_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientAccountApi.client_account_save_multi_async(
    cakePrefix_client_account_save_multi_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailClientMultiAccountSaveRequest**](EmailClientMultiAccountSaveRequest.md)| Email accounts information. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

