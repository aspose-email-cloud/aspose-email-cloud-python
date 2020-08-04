
# AsposeEmailCloudSdk.ClientFolderApi

        
<a name="create"></a>
# create

```python
create(self, ClientFolderCreateRequest request)
```

Create new folder in email account             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientFolderCreateRequest](ClientFolderCreateRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="delete"></a>
# delete

```python
delete(self, ClientFolderDeleteRequest request)
```

Delete a folder in email account             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientFolderDeleteRequest](ClientFolderDeleteRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_list"></a>
# get_list

```python
get_list(self, request: ClientFolderGetListRequest)
```

Get folders list in email account             

### Return type

MailServerFolderList

### request Parameter
```python
ClientFolderGetListRequest(
    account,
    storage,
    account_storage_folder,
    parent_folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str** | Email account | 
 **storage** | **str** | Storage name where account file located | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located | [optional] 
 **parent_folder** | **str** | Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

