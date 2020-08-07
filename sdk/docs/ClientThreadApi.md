# AsposeEmailCloudSdk.ClientThreadApi

        
<a name="delete"></a>
# delete

```python
delete(self, ClientThreadDeleteRequest request)
```

Delete thread by id. All messages from thread will also be deleted.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientThreadDeleteRequest](ClientThreadDeleteRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_list"></a>
# get_list

```python
get_list(self, request: ClientThreadGetListRequest)
```

Get message threads from folder. All messages are partly fetched (without email body and some other fields).             

### Return type

EmailThreadList

### request Parameter
```python
ClientThreadGetListRequest(
    folder,
    account,
    storage,
    account_storage_folder,
    update_folder_cache,
    messages_cache_limit)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str** | A folder in email account.              | 
 **account** | **str** | Email account | 
 **storage** | **str** | Storage name where account file located | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located | [optional] 
 **update_folder_cache** | **bool** | This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account              | [optional] [default to true]
 **messages_cache_limit** | **int** | Limit messages cache size if CacheFile is used. Ignored in accounts without limits support              | [optional] [default to 200]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_messages"></a>
# get_messages

```python
get_messages(self, request: ClientThreadGetMessagesRequest)
```

Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             

### Return type

EmailList

### request Parameter
```python
ClientThreadGetMessagesRequest(
    thread_id,
    account,
    folder,
    storage,
    account_storage_folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str** | Thread identifier | 
 **account** | **str** | Email account | 
 **folder** | **str** | Specifies account folder to get thread from              | [optional] 
 **storage** | **str** | Storage name where account file located | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="move"></a>
# move

```python
move(self, ClientThreadMoveRequest request)
```

Move thread to another folder.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientThreadMoveRequest](ClientThreadMoveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="set_is_read"></a>
# set_is_read

```python
set_is_read(self, ClientThreadSetIsReadRequest request)
```

Mark all messages in thread as read or unread.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientThreadSetIsReadRequest](ClientThreadSetIsReadRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

