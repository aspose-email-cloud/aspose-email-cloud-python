# AsposeEmailCloudSdk.ClientThreadApi

<a name="client_thread_delete"></a>
# **client_thread_delete**
> client_thread_delete(self, client_thread_delete_request)

Delete thread by id. All messages from thread will also be deleted.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_delete(
    cakePrefix_client_thread_delete_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadDeleteRequest**](ClientThreadDeleteRequest.md)| Delete email thread request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_delete_async"></a>
# **client_thread_delete_async**
> client_thread_delete_async(self, client_thread_delete_request)

Delete thread by id. All messages from thread will also be deleted.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_thread_delete_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_delete_async(
    cakePrefix_client_thread_delete_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadDeleteRequest**](ClientThreadDeleteRequest.md)| Delete email thread request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_get_list"></a>
# **client_thread_get_list**
> client_thread_get_list(self, client_thread_get_list_request)

Get message threads from folder. All messages are partly fetched (without email body and some other fields).             

### Return type

[**EmailThreadList**](EmailThreadList.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    account, 
    storage=storage, 
    account_storage_folder=account_storage_folder, 
    update_folder_cache=update_folder_cache, 
    messages_cache_limit=messages_cache_limit)
```

### Usage
```python
ClientThreadApi.client_thread_get_list(
    cakePrefix_client_thread_get_list_request_cakeCodePostProcessor(
        folder, 
        account, 
        storage=storage, 
        account_storage_folder=account_storage_folder, 
        update_folder_cache=update_folder_cache, 
        messages_cache_limit=messages_cache_limit))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account.              | 
 **account** | **str**| Email account | 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 
 **update_folder_cache** | **bool**| This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account              | [optional] [default to true]
 **messages_cache_limit** | **int**| Limit messages cache size if CacheFile is used. Ignored in accounts without limits support              | [optional] [default to 200]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_get_list_async"></a>
# **client_thread_get_list_async**
> client_thread_get_list_async(self, client_thread_get_list_request)

Get message threads from folder. All messages are partly fetched (without email body and some other fields).             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_thread_get_list_async(request).get() returns [**EmailThreadList**](EmailThreadList.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    account, 
    storage=storage, 
    account_storage_folder=account_storage_folder, 
    update_folder_cache=update_folder_cache, 
    messages_cache_limit=messages_cache_limit)
```

### Usage
```python
ClientThreadApi.client_thread_get_list_async(
    cakePrefix_client_thread_get_list_request_cakeCodePostProcessor(
        folder, 
        account, 
        storage=storage, 
        account_storage_folder=account_storage_folder, 
        update_folder_cache=update_folder_cache, 
        messages_cache_limit=messages_cache_limit))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account.              | 
 **account** | **str**| Email account | 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 
 **update_folder_cache** | **bool**| This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account              | [optional] [default to true]
 **messages_cache_limit** | **int**| Limit messages cache size if CacheFile is used. Ignored in accounts without limits support              | [optional] [default to 200]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_get_messages"></a>
# **client_thread_get_messages**
> client_thread_get_messages(self, client_thread_get_messages_request)

Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             

### Return type

[**EmailList**](EmailList.md)

### Request Parameters
```python
__init__(self, 
    thread_id, 
    account, 
    folder=folder, 
    storage=storage, 
    account_storage_folder=account_storage_folder)
```

### Usage
```python
ClientThreadApi.client_thread_get_messages(
    cakePrefix_client_thread_get_messages_request_cakeCodePostProcessor(
        thread_id, 
        account, 
        folder=folder, 
        storage=storage, 
        account_storage_folder=account_storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Thread identifier | 
 **account** | **str**| Email account | 
 **folder** | **str**| Specifies account folder to get thread from              | [optional] 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_get_messages_async"></a>
# **client_thread_get_messages_async**
> client_thread_get_messages_async(self, client_thread_get_messages_request)

Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_thread_get_messages_async(request).get() returns [**EmailList**](EmailList.md)

### Request Parameters
```python
__init__(self, 
    thread_id, 
    account, 
    folder=folder, 
    storage=storage, 
    account_storage_folder=account_storage_folder)
```

### Usage
```python
ClientThreadApi.client_thread_get_messages_async(
    cakePrefix_client_thread_get_messages_request_cakeCodePostProcessor(
        thread_id, 
        account, 
        folder=folder, 
        storage=storage, 
        account_storage_folder=account_storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Thread identifier | 
 **account** | **str**| Email account | 
 **folder** | **str**| Specifies account folder to get thread from              | [optional] 
 **storage** | **str**| Storage name where account file located | [optional] 
 **account_storage_folder** | **str**| Folder in storage where account file located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_move"></a>
# **client_thread_move**
> client_thread_move(self, client_thread_move_request)

Move thread to another folder.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_move(
    cakePrefix_client_thread_move_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadMoveRequest**](ClientThreadMoveRequest.md)| Move thread request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_move_async"></a>
# **client_thread_move_async**
> client_thread_move_async(self, client_thread_move_request)

Move thread to another folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_thread_move_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_move_async(
    cakePrefix_client_thread_move_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadMoveRequest**](ClientThreadMoveRequest.md)| Move thread request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_set_is_read"></a>
# **client_thread_set_is_read**
> client_thread_set_is_read(self, client_thread_set_is_read_request)

Mark all messages in thread as read or unread.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_set_is_read(
    cakePrefix_client_thread_set_is_read_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadSetIsReadRequest**](ClientThreadSetIsReadRequest.md)| Email account specifier and IsRead flag. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="client_thread_set_is_read_async"></a>
# **client_thread_set_is_read_async**
> client_thread_set_is_read_async(self, client_thread_set_is_read_request)

Mark all messages in thread as read or unread.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
client_thread_set_is_read_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ClientThreadApi.client_thread_set_is_read_async(
    cakePrefix_client_thread_set_is_read_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ClientThreadSetIsReadRequest**](ClientThreadSetIsReadRequest.md)| Email account specifier and IsRead flag. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

