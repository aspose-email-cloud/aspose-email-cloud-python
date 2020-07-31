# AsposeEmailCloudSdk.MapiMessageApi

<a name="mapi_message_as_email_dto"></a>
# **mapi_message_as_email_dto**
> mapi_message_as_email_dto(self, mapi_message_as_email_dto_request)

Converts MAPI message model to EmailDto model             

### Return type

[**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_message)
```

### Usage
```python
MapiMessageApi.mapi_message_as_email_dto(
    cakePrefix_mapi_message_as_email_dto_request_cakeCodePostProcessor(
        mapi_message))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_message** | [**MapiMessageDto**](MapiMessageDto.md)| MAPI message model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_as_email_dto_async"></a>
# **mapi_message_as_email_dto_async**
> mapi_message_as_email_dto_async(self, mapi_message_as_email_dto_request)

Converts MAPI message model to EmailDto model             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_message_as_email_dto_async(request).get() returns [**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_message)
```

### Usage
```python
MapiMessageApi.mapi_message_as_email_dto_async(
    cakePrefix_mapi_message_as_email_dto_request_cakeCodePostProcessor(
        mapi_message))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_message** | [**MapiMessageDto**](MapiMessageDto.md)| MAPI message model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_as_file"></a>
# **mapi_message_as_file**
> mapi_message_as_file(self, mapi_message_as_file_request)

Converts MAPI message model to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiMessageApi.mapi_message_as_file(
    cakePrefix_mapi_message_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiMessageAsFileRequest**](MapiMessageAsFileRequest.md)| MAPI message model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_as_file_async"></a>
# **mapi_message_as_file_async**
> mapi_message_as_file_async(self, mapi_message_as_file_request)

Converts MAPI message model to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_message_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiMessageApi.mapi_message_as_file_async(
    cakePrefix_mapi_message_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiMessageAsFileRequest**](MapiMessageAsFileRequest.md)| MAPI message model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_from_file"></a>
# **mapi_message_from_file**
> mapi_message_from_file(self, mapi_message_from_file_request)

Converts email file to a MAPI model representation             

### Return type

[**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
MapiMessageApi.mapi_message_from_file(
    cakePrefix_mapi_message_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_from_file_async"></a>
# **mapi_message_from_file_async**
> mapi_message_from_file_async(self, mapi_message_from_file_request)

Converts email file to a MAPI model representation             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_message_from_file_async(request).get() returns [**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
MapiMessageApi.mapi_message_from_file_async(
    cakePrefix_mapi_message_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_get"></a>
# **mapi_message_get**
> mapi_message_get(self, mapi_message_get_request)

Get MAPI message document.             

### Return type

[**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
MapiMessageApi.mapi_message_get(
    cakePrefix_mapi_message_get_request_cakeCodePostProcessor(
        format, 
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file_name** | **str**| Email document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_get_async"></a>
# **mapi_message_get_async**
> mapi_message_get_async(self, mapi_message_get_request)

Get MAPI message document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_message_get_async(request).get() returns [**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file_name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
MapiMessageApi.mapi_message_get_async(
    cakePrefix_mapi_message_get_request_cakeCodePostProcessor(
        format, 
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file_name** | **str**| Email document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_save"></a>
# **mapi_message_save**
> mapi_message_save(self, mapi_message_save_request)

Save MAPI message to storage.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiMessageApi.mapi_message_save(
    cakePrefix_mapi_message_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiMessageSaveRequest**](MapiMessageSaveRequest.md)| Message create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_message_save_async"></a>
# **mapi_message_save_async**
> mapi_message_save_async(self, mapi_message_save_request)

Save MAPI message to storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_message_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiMessageApi.mapi_message_save_async(
    cakePrefix_mapi_message_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiMessageSaveRequest**](MapiMessageSaveRequest.md)| Message create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

