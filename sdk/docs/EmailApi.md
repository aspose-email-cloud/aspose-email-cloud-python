# AsposeEmailCloudSdk.EmailApi

        
<a name="as_file"></a>
# as_file

```python
as_file(self, EmailAsFileRequest request)
```

Converts Email model to specified format and returns as file.             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [EmailAsFileRequest](EmailAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_mapi"></a>
# as_mapi

```python
as_mapi(self, EmailDto email_dto)
```

Converts EmailDto to MapiMessageDto.             

### Return type

[**MapiMessageDto**](MapiMessageDto.md)

### email_dto Parameter

See parameter model documentation at [EmailDto](EmailDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="convert"></a>
# convert

```python
convert(self, request: EmailConvertRequest)
```

Converts email document to specified format and returns as file             

### Return type

str

### request Parameter
```python
EmailConvertRequest(
    from_format,
    to_format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_format** | **str** | File format to convert to Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **to_format** | **str** | File format to convert from Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: EmailFromFileRequest)
```

Converts email document to a model representation             

### Return type

EmailDto

### request Parameter
```python
EmailFromFileRequest(
    format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** |  Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get"></a>
# get

```python
get(self, request: EmailGetRequest)
```

Get email document from storage.             

### Return type

EmailDto

### request Parameter
```python
EmailGetRequest(
    format,
    file_name,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **file_name** | **str** | Email document file name. | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_as_file"></a>
# get_as_file

```python
get_as_file(self, request: EmailGetAsFileRequest)
```

Converts email document from storage to specified format and returns as file             

### Return type

str

### request Parameter
```python
EmailGetAsFileRequest(
    file_name,
    format,
    storage,
    folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | Email document file name | 
 **format** | **str** | File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **storage** | **str** | Storage name | [optional] 
 **folder** | **str** | Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_list"></a>
# get_list

```python
get_list(self, request: EmailGetListRequest)
```

Get email list from storage folder.             

### Return type

EmailStorageList

### request Parameter
```python
EmailGetListRequest(
    format,
    folder,
    storage,
    items_per_page,
    page_number)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 
 **items_per_page** | **int** | Count of items on page. | [optional] [default to 10]
 **page_number** | **int** | Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save"></a>
# save

```python
save(self, EmailSaveRequest request)
```

Save email document to storage.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [EmailSaveRequest](EmailSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

