# AsposeEmailCloudSdk.CalendarApi

        
<a name="as_alternate"></a>
# as_alternate

```python
as_alternate(self, CalendarAsAlternateRequest request)
```

Convert iCalendar to AlternateView             

### Return type

[**AlternateView**](AlternateView.md)

### request Parameter

See parameter model documentation at [CalendarAsAlternateRequest](CalendarAsAlternateRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_file"></a>
# as_file

```python
as_file(self, CalendarAsFileRequest request)
```

Converts calendar model to specified format and returns as file.             

### Return type

**Stream**

### request Parameter

See parameter model documentation at [CalendarAsFileRequest](CalendarAsFileRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="as_mapi"></a>
# as_mapi

```python
as_mapi(self, CalendarDto calendar_dto)
```

Converts CalendarDto to MapiCalendarDto.             

### Return type

[**MapiCalendarDto**](MapiCalendarDto.md)

### calendar_dto Parameter

See parameter model documentation at [CalendarDto](CalendarDto.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="convert"></a>
# convert

```python
convert(self, request: CalendarConvertRequest)
```

Converts calendar document to specified format and returns as file.             

### Return type

str

### request Parameter
```python
CalendarConvertRequest(
    format,
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str** | File format. Enum, available values: Ics, Msg | 
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="from_file"></a>
# from_file

```python
from_file(self, request: CalendarFromFileRequest)
```

Converts calendar document to a model representation.             

### Return type

CalendarDto

### request Parameter
```python
CalendarFromFileRequest(
    file)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str** | File to convert | 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get"></a>
# get

```python
get(self, request: CalendarGetRequest)
```

Get calendar file from storage.             

### Return type

CalendarDto

### request Parameter
```python
CalendarGetRequest(
    file_name,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | iCalendar file name in storage. | 
 **folder** | **str** | Path to folder in storage. | [optional] 
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_as_alternate"></a>
# get_as_alternate

```python
get_as_alternate(self, request: CalendarGetAsAlternateRequest)
```

Get iCalendar from storage as AlternateView             

### Return type

AlternateView

### request Parameter
```python
CalendarGetAsAlternateRequest(
    file_name,
    calendar_action,
    sequence_id,
    folder,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | iCalendar file name in storage | 
 **calendar_action** | **str** | iCalendar method type Enum, available values: Create, Update, Cancel | 
 **sequence_id** | **str** | The sequence id | [optional] 
 **folder** | **str** | Path to folder in storage | [optional] 
 **storage** | **str** | Storage name | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_as_file"></a>
# get_as_file

```python
get_as_file(self, request: CalendarGetAsFileRequest)
```

Converts calendar document from storage to specified format and returns as file.             

### Return type

str

### request Parameter
```python
CalendarGetAsFileRequest(
    file_name,
    format,
    storage,
    folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str** | Calendar document file name. | 
 **format** | **str** | File format. Enum, available values: Ics, Msg | 
 **storage** | **str** | Storage name. | [optional] 
 **folder** | **str** | Path to folder in storage. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="get_list"></a>
# get_list

```python
get_list(self, request: CalendarGetListRequest)
```

Get iCalendar list from storage folder.             

### Return type

CalendarStorageList

### request Parameter
```python
CalendarGetListRequest(
    folder,
    items_per_page,
    page_number,
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str** | Path to folder in storage. | 
 **items_per_page** | **int** | Count of items on page. | [optional] [default to 10]
 **page_number** | **int** | Page number. | [optional] [default to 0]
 **storage** | **str** | Storage name. | [optional] 

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="save"></a>
# save

```python
save(self, CalendarSaveRequest request)
```

Save iCalendar             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [CalendarSaveRequest](CalendarSaveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

