# AsposeEmailCloudSdk.ClientAccountApi

        
<a name="get"></a>
# get

```python
get(self, request: ClientAccountGetRequest)
```

Get email client account from storage.             

### Return type

EmailClientAccount

### request Parameter
```python
ClientAccountGetRequest(
    file_name,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | File name on storage. | 
 **folder** | **str** | Folder on storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_multi"></a>
# get_multi

```python
get_multi(self, request: ClientAccountGetMultiRequest)
```

Get email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

### Return type

EmailClientMultiAccount

### request Parameter
```python
ClientAccountGetMultiRequest(
    file_name,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | File name on storage | 
 **folder** | **str** | Folder on storage | [optional] 
 **storage** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save"></a>
# save

```python
save(self, ClientAccountSaveRequest request)
```

Create/update email client account file (*.account) with credentials             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientAccountSaveRequest](ClientAccountSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save_multi"></a>
# save_multi

```python
save_multi(self, ClientAccountSaveMultiRequest request)
```

Create email client multi account file (*.multi.account). Will respond error if file extension is not \".multi.account\".             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientAccountSaveMultiRequest](ClientAccountSaveMultiRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

