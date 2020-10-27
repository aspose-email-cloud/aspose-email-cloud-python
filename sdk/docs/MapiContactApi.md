# AsposeEmailCloudSdk.MapiContactApi

        
<a name="as_contact_dto"></a>
# as_contact_dto

```python
as_contact_dto(self, MapiContactDto mapi_contact_dto)
```

Converts MAPI contact model to ContactDto model.             

### Return type

[**ContactDto**](ContactDto.md)

### mapi_contact_dto Parameter

See parameter model documentation at [MapiContactDto](MapiContactDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_file"></a>
# as_file

```python
as_file(self, MapiContactAsFileRequest request)
```

Converts MAPI contact model to specified format and returns as file.             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [MapiContactAsFileRequest](MapiContactAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: MapiContactFromFileRequest)
```

Converts contact file to a MAPI model representation.             

### Return type

MapiContactDto

### request Parameter
```python
MapiContactFromFileRequest(
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
get(self, request: MapiContactGetRequest)
```

Get MAPI contact document.             

### Return type

MapiContactDto

### request Parameter
```python
MapiContactGetRequest(
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
        
<a name="save"></a>
# save

```python
save(self, MapiContactSaveRequest request)
```

Save MAPI Contact to storage.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [MapiContactSaveRequest](MapiContactSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

