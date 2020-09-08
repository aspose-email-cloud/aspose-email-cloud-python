# AsposeEmailCloudSdk.MapiMessageApi

        
<a name="as_email_dto"></a>
# as_email_dto

```python
as_email_dto(self, MapiMessageDto mapi_message)
```

Converts MAPI message model to EmailDto model             

### Return type

[**EmailDto**](EmailDto.md)

### mapi_message Parameter

See parameter model documentation at [MapiMessageDto](MapiMessageDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_file"></a>
# as_file

```python
as_file(self, MapiMessageAsFileRequest request)
```

Converts MAPI message model to specified format and returns as file.             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [MapiMessageAsFileRequest](MapiMessageAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: MapiMessageFromFileRequest)
```

Converts email file to a MAPI model representation             

### Return type

MapiMessageDto

### request Parameter
```python
MapiMessageFromFileRequest(
    format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get"></a>
# get

```python
get(self, request: MapiMessageGetRequest)
```

Get MAPI message document.             

### Return type

MapiMessageDto

### request Parameter
```python
MapiMessageGetRequest(
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
        
<a name="save"></a>
# save

```python
save(self, MapiMessageSaveRequest request)
```

Save MAPI message to storage.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [MapiMessageSaveRequest](MapiMessageSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

