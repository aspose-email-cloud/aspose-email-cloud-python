# AsposeEmailCloudSdk.CalendarApi

<a name="calendar_as_alternate"></a>
# **calendar_as_alternate**
> calendar_as_alternate(self, calendar_as_alternate_request)

Convert iCalendar to AlternateView             

### Return type

[**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_as_alternate(
    cakePrefix_calendar_as_alternate_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarAsAlternateRequest**](CalendarAsAlternateRequest.md)| iCalendar to AlternateView request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_as_alternate_async"></a>
# **calendar_as_alternate_async**
> calendar_as_alternate_async(self, calendar_as_alternate_request)

Convert iCalendar to AlternateView             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_as_alternate_async(request).get() returns [**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_as_alternate_async(
    cakePrefix_calendar_as_alternate_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarAsAlternateRequest**](CalendarAsAlternateRequest.md)| iCalendar to AlternateView request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_as_file"></a>
# **calendar_as_file**
> calendar_as_file(self, calendar_as_file_request)

Converts calendar model to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_as_file(
    cakePrefix_calendar_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarAsFileRequest**](CalendarAsFileRequest.md)| Calendar model and format to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_as_file_async"></a>
# **calendar_as_file_async**
> calendar_as_file_async(self, calendar_as_file_request)

Converts calendar model to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_as_file_async(
    cakePrefix_calendar_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarAsFileRequest**](CalendarAsFileRequest.md)| Calendar model and format to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_as_mapi"></a>
# **calendar_as_mapi**
> calendar_as_mapi(self, calendar_as_mapi_request)

Converts CalendarDto to MapiCalendarDto.             

### Return type

[**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    calendar_dto)
```

### Usage
```python
CalendarApi.calendar_as_mapi(
    cakePrefix_calendar_as_mapi_request_cakeCodePostProcessor(
        calendar_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_dto** | [**CalendarDto**](CalendarDto.md)| iCalendar model calendar representation. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_as_mapi_async"></a>
# **calendar_as_mapi_async**
> calendar_as_mapi_async(self, calendar_as_mapi_request)

Converts CalendarDto to MapiCalendarDto.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_as_mapi_async(request).get() returns [**MapiCalendarDto**](MapiCalendarDto.md)

### Request Parameters
```python
__init__(self, 
    calendar_dto)
```

### Usage
```python
CalendarApi.calendar_as_mapi_async(
    cakePrefix_calendar_as_mapi_request_cakeCodePostProcessor(
        calendar_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_dto** | [**CalendarDto**](CalendarDto.md)| iCalendar model calendar representation. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_convert"></a>
# **calendar_convert**
> calendar_convert(self, calendar_convert_request)

Converts calendar document to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
CalendarApi.calendar_convert(
    cakePrefix_calendar_convert_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format. Enum, available values: Ics, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_convert_async"></a>
# **calendar_convert_async**
> calendar_convert_async(self, calendar_convert_request)

Converts calendar document to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_convert_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
CalendarApi.calendar_convert_async(
    cakePrefix_calendar_convert_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format. Enum, available values: Ics, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_from_file"></a>
# **calendar_from_file**
> calendar_from_file(self, calendar_from_file_request)

Converts calendar document to a model representation.             

### Return type

[**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file)
```

### Usage
```python
CalendarApi.calendar_from_file(
    cakePrefix_calendar_from_file_request_cakeCodePostProcessor(
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_from_file_async"></a>
# **calendar_from_file_async**
> calendar_from_file_async(self, calendar_from_file_request)

Converts calendar document to a model representation.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_from_file_async(request).get() returns [**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file)
```

### Usage
```python
CalendarApi.calendar_from_file_async(
    cakePrefix_calendar_from_file_request_cakeCodePostProcessor(
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get"></a>
# **calendar_get**
> calendar_get(self, calendar_get_request)

Get calendar file from storage.             

### Return type

[**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get(
    cakePrefix_calendar_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| iCalendar file name in storage. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_async"></a>
# **calendar_get_async**
> calendar_get_async(self, calendar_get_request)

Get calendar file from storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_get_async(request).get() returns [**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get_async(
    cakePrefix_calendar_get_request_cakeCodePostProcessor(
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| iCalendar file name in storage. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_as_alternate"></a>
# **calendar_get_as_alternate**
> calendar_get_as_alternate(self, calendar_get_as_alternate_request)

Get iCalendar from storage as AlternateView             

### Return type

[**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    calendar_action, 
    sequence_id=sequence_id, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get_as_alternate(
    cakePrefix_calendar_get_as_alternate_request_cakeCodePostProcessor(
        file_name, 
        calendar_action, 
        sequence_id=sequence_id, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| iCalendar file name in storage | 
 **calendar_action** | **str**| iCalendar method type Enum, available values: Create, Update, Cancel | 
 **sequence_id** | **str**| The sequence id | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_as_alternate_async"></a>
# **calendar_get_as_alternate_async**
> calendar_get_as_alternate_async(self, calendar_get_as_alternate_request)

Get iCalendar from storage as AlternateView             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_get_as_alternate_async(request).get() returns [**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    calendar_action, 
    sequence_id=sequence_id, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get_as_alternate_async(
    cakePrefix_calendar_get_as_alternate_request_cakeCodePostProcessor(
        file_name, 
        calendar_action, 
        sequence_id=sequence_id, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| iCalendar file name in storage | 
 **calendar_action** | **str**| iCalendar method type Enum, available values: Create, Update, Cancel | 
 **sequence_id** | **str**| The sequence id | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_as_file"></a>
# **calendar_get_as_file**
> calendar_get_as_file(self, calendar_get_as_file_request)

Converts calendar document from storage to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    file_name, 
    format, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
CalendarApi.calendar_get_as_file(
    cakePrefix_calendar_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar document file name. | 
 **format** | **str**| File format. Enum, available values: Ics, Msg | 
 **storage** | **str**| Storage name. | [optional] 
 **folder** | **str**| Path to folder in storage. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_as_file_async"></a>
# **calendar_get_as_file_async**
> calendar_get_as_file_async(self, calendar_get_as_file_request)

Converts calendar document from storage to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_get_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    file_name, 
    format, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
CalendarApi.calendar_get_as_file_async(
    cakePrefix_calendar_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar document file name. | 
 **format** | **str**| File format. Enum, available values: Ics, Msg | 
 **storage** | **str**| Storage name. | [optional] 
 **folder** | **str**| Path to folder in storage. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_list"></a>
# **calendar_get_list**
> calendar_get_list(self, calendar_get_list_request)

Get iCalendar list from storage folder.             

### Return type

[**CalendarStorageList**](CalendarStorageList.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    items_per_page=items_per_page, 
    page_number=page_number, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get_list(
    cakePrefix_calendar_get_list_request_cakeCodePostProcessor(
        folder, 
        items_per_page=items_per_page, 
        page_number=page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage. | 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_get_list_async"></a>
# **calendar_get_list_async**
> calendar_get_list_async(self, calendar_get_list_request)

Get iCalendar list from storage folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_get_list_async(request).get() returns [**CalendarStorageList**](CalendarStorageList.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    items_per_page=items_per_page, 
    page_number=page_number, 
    storage=storage)
```

### Usage
```python
CalendarApi.calendar_get_list_async(
    cakePrefix_calendar_get_list_request_cakeCodePostProcessor(
        folder, 
        items_per_page=items_per_page, 
        page_number=page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage. | 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_save"></a>
# **calendar_save**
> calendar_save(self, calendar_save_request)

Save iCalendar             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_save(
    cakePrefix_calendar_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarSaveRequest**](CalendarSaveRequest.md)| iCalendar create/update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="calendar_save_async"></a>
# **calendar_save_async**
> calendar_save_async(self, calendar_save_request)

Save iCalendar             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
calendar_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
CalendarApi.calendar_save_async(
    cakePrefix_calendar_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CalendarSaveRequest**](CalendarSaveRequest.md)| iCalendar create/update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

