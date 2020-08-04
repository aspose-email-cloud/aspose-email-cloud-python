
# AsposeEmailCloudSdk.ContactApi

        
<a name="as_file"></a>
# as_file

```python
as_file(self, ContactAsFileRequest request)
```

Converts contact model to specified format and returns as file             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [ContactAsFileRequest](ContactAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_mapi"></a>
# as_mapi

```python
as_mapi(self, ContactDto contact_dto)
```

Converts ContactDto to MapiContactDto.             

### Return type

[**MapiContactDto**](MapiContactDto.md)

### contact_dto Parameter

See parameter model documentation at [ContactDto](ContactDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="convert"></a>
# convert

```python
convert(self, request: ContactConvertRequest)
```

Converts contact document to specified format and returns as file             

### Return type

str

### request Parameter
```python
ContactConvertRequest(
    to_format,
    from_format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_format** | **str** | File format to convert to Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str** | File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: ContactFromFileRequest)
```

Converts contact document to a model representation             

### Return type

ContactDto

### request Parameter
```python
ContactFromFileRequest(
    format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | File format Enum, available values: VCard, WebDav, Msg | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get"></a>
# get

```python
get(self, request: ContactGetRequest)
```

Get contact document from storage.             

### Return type

ContactDto

### request Parameter
```python
ContactGetRequest(
    format,
    file_name,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **file_name** | **str** | Contact document file name. | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_as_file"></a>
# get_as_file

```python
get_as_file(self, request: ContactGetAsFileRequest)
```

Converts contact document from storage to specified format and returns as file             

### Return type

str

### request Parameter
```python
ContactGetAsFileRequest(
    file_name,
    to_format,
    from_format,
    storage,
    folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | Calendar document file name | 
 **to_format** | **str** | File format Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str** | File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **storage** | **str** | Storage name | [optional] 
 **folder** | **str** | Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_list"></a>
# get_list

```python
get_list(self, request: ContactGetListRequest)
```

Get contact list from storage folder.             

### Return type

ContactStorageList

### request Parameter
```python
ContactGetListRequest(
    format,
    folder,
    storage,
    items_per_page,
    page_number)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 
 **items_per_page** | **int** | Count of items on page. | [optional] [default to 10]
 **page_number** | **int** | Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save"></a>
# save

```python
save(self, ContactSaveRequest request)
```

Save contact to storage.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ContactSaveRequest](ContactSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

