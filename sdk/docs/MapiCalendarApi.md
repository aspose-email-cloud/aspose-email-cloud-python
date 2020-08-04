
# AsposeEmailCloudSdk.MapiCalendarApi

        
<a name="as_calendar_dto"></a>
# as_calendar_dto

```python
as_calendar_dto(self, MapiCalendarDto mapi_calendar_dto)
```

Converts MAPI calendar model to CalendarDto model.             

### Return type

[**CalendarDto**](CalendarDto.md)

### mapi_calendar_dto Parameter

See parameter model documentation at [MapiCalendarDto](MapiCalendarDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_file"></a>
# as_file

```python
as_file(self, MapiCalendarAsFileRequest request)
```

Converts MAPI calendar model to specified format and returns as file.             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [MapiCalendarAsFileRequest](MapiCalendarAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: MapiCalendarFromFileRequest)
```

Converts calendar file to a MAPI model representation.             

### Return type

MapiCalendarDto

### request Parameter
```python
MapiCalendarFromFileRequest(
    file: str)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get"></a>
# get

```python
get(self, request: MapiCalendarGetRequest)
```

Get MAPI calendar document.             

### Return type

MapiCalendarDto

### request Parameter
```python
MapiCalendarGetRequest(
    file_name: str, 
    folder: str = None, 
    storage: str = None)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | Calendar file name in storage. | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save"></a>
# save

```python
save(self, MapiCalendarSaveRequest request)
```

Save MAPI Calendar to storage.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [MapiCalendarSaveRequest](MapiCalendarSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

