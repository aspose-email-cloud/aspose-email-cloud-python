# AsposeEmailCloudSdk.MapiCalendarApi

<a name="mapi_calendar_as_calendar_dto"></a>
# **mapi_calendar_as_calendar_dto**
> mapi_calendar_as_calendar_dto(self, mapi_calendar_as_calendar_dto_request)

Converts MAPI calendar model to CalendarDto model.             

### Return type

[**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_calendar_dto)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_as_calendar_dto(
    cakePrefix_mapi_calendar_as_calendar_dto_request_cakeCodePostProcessor(
        mapi_calendar_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_calendar_dto** | [**MapiCalendarDto**](MapiCalendarDto.md)| MAPI calendar model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_as_calendar_dto_async"></a>
# **mapi_calendar_as_calendar_dto_async**
> mapi_calendar_as_calendar_dto_async(self, mapi_calendar_as_calendar_dto_request)

Converts MAPI calendar model to CalendarDto model.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_calendar_as_calendar_dto_async(request).get() returns [**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_calendar_dto)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_as_calendar_dto_async(
    cakePrefix_mapi_calendar_as_calendar_dto_request_cakeCodePostProcessor(
        mapi_calendar_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_calendar_dto** | [**MapiCalendarDto**](MapiCalendarDto.md)| MAPI calendar model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_as_file"></a>
# **mapi_calendar_as_file**
> mapi_calendar_as_file(self, mapi_calendar_as_file_request)

Converts MAPI calendar model to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_as_file(
    cakePrefix_mapi_calendar_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiCalendarAsFileRequest**](MapiCalendarAsFileRequest.md)| MAPI calendar model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_as_file_async"></a>
# **mapi_calendar_as_file_async**
> mapi_calendar_as_file_async(self, mapi_calendar_as_file_request)

Converts MAPI calendar model to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_calendar_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_as_file_async(
    cakePrefix_mapi_calendar_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiCalendarAsFileRequest**](MapiCalendarAsFileRequest.md)| MAPI calendar model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_from_file"></a>
# **mapi_calendar_from_file**
> mapi_calendar_from_file(self, mapi_calendar_from_file_request)

Converts calendar file to a MAPI model representation.             

### Return type

[**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_from_file(
    cakePrefix_mapi_calendar_from_file_request_cakeCodePostProcessor(
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_from_file_async"></a>
# **mapi_calendar_from_file_async**
> mapi_calendar_from_file_async(self, mapi_calendar_from_file_request)

Converts calendar file to a MAPI model representation.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_calendar_from_file_async(request).get() returns [**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_from_file_async(
    cakePrefix_mapi_calendar_from_file_request_cakeCodePostProcessor(
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_get"></a>
# **mapi_calendar_get**
> mapi_calendar_get(self, mapi_calendar_get_request)

Get MAPI calendar document.             

### Return type

[**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_get(
    cakePrefix_mapi_calendar_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar file name in storage. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_get_async"></a>
# **mapi_calendar_get_async**
> mapi_calendar_get_async(self, mapi_calendar_get_request)

Get MAPI calendar document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_calendar_get_async(request).get() returns [**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_get_async(
    cakePrefix_mapi_calendar_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar file name in storage. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_save"></a>
# **mapi_calendar_save**
> mapi_calendar_save(self, mapi_calendar_save_request)

Save MAPI Calendar to storage.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_save(
    cakePrefix_mapi_calendar_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiCalendarSaveRequest**](MapiCalendarSaveRequest.md)| Calendar create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_calendar_save_async"></a>
# **mapi_calendar_save_async**
> mapi_calendar_save_async(self, mapi_calendar_save_request)

Save MAPI Calendar to storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_calendar_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiCalendarApi.mapi_calendar_save_async(
    cakePrefix_mapi_calendar_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiCalendarSaveRequest**](MapiCalendarSaveRequest.md)| Calendar create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

