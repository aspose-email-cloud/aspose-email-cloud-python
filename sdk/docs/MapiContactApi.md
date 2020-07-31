# AsposeEmailCloudSdk.MapiContactApi

<a name="mapi_contact_as_contact_dto"></a>
# **mapi_contact_as_contact_dto**
> mapi_contact_as_contact_dto(self, mapi_contact_as_contact_dto_request)

Converts MAPI contact model to ContactDto model.             

### Return type

[**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_contact_dto)
```

### Usage
```python
MapiContactApi.mapi_contact_as_contact_dto(
    cakePrefix_mapi_contact_as_contact_dto_request_cakeCodePostProcessor(
        mapi_contact_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_contact_dto** | [**MapiContactDto**](MapiContactDto.md)| MAPI contact model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_as_contact_dto_async"></a>
# **mapi_contact_as_contact_dto_async**
> mapi_contact_as_contact_dto_async(self, mapi_contact_as_contact_dto_request)

Converts MAPI contact model to ContactDto model.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_contact_as_contact_dto_async(request).get() returns [**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    mapi_contact_dto)
```

### Usage
```python
MapiContactApi.mapi_contact_as_contact_dto_async(
    cakePrefix_mapi_contact_as_contact_dto_request_cakeCodePostProcessor(
        mapi_contact_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapi_contact_dto** | [**MapiContactDto**](MapiContactDto.md)| MAPI contact model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_as_file"></a>
# **mapi_contact_as_file**
> mapi_contact_as_file(self, mapi_contact_as_file_request)

Converts MAPI contact model to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiContactApi.mapi_contact_as_file(
    cakePrefix_mapi_contact_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiContactAsFileRequest**](MapiContactAsFileRequest.md)| MAPI contact model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_as_file_async"></a>
# **mapi_contact_as_file_async**
> mapi_contact_as_file_async(self, mapi_contact_as_file_request)

Converts MAPI contact model to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_contact_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiContactApi.mapi_contact_as_file_async(
    cakePrefix_mapi_contact_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiContactAsFileRequest**](MapiContactAsFileRequest.md)| MAPI contact model to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_from_file"></a>
# **mapi_contact_from_file**
> mapi_contact_from_file(self, mapi_contact_from_file_request)

Converts contact file to a MAPI model representation.             

### Return type

[**MapiContactDto**](MapiContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
MapiContactApi.mapi_contact_from_file(
    cakePrefix_mapi_contact_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_from_file_async"></a>
# **mapi_contact_from_file_async**
> mapi_contact_from_file_async(self, mapi_contact_from_file_request)

Converts contact file to a MAPI model representation.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_contact_from_file_async(request).get() returns [**MapiContactDto**](MapiContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
MapiContactApi.mapi_contact_from_file_async(
    cakePrefix_mapi_contact_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_get"></a>
# **mapi_contact_get**
> mapi_contact_get(self, mapi_contact_get_request)

Get MAPI contact document.             

### Return type

[**MapiContactDto**](MapiContactDto.md)

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
MapiContactApi.mapi_contact_get(
    cakePrefix_mapi_contact_get_request_cakeCodePostProcessor(
        format, 
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **file_name** | **str**| Contact document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_get_async"></a>
# **mapi_contact_get_async**
> mapi_contact_get_async(self, mapi_contact_get_request)

Get MAPI contact document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_contact_get_async(request).get() returns [**MapiContactDto**](MapiContactDto.md)

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
MapiContactApi.mapi_contact_get_async(
    cakePrefix_mapi_contact_get_request_cakeCodePostProcessor(
        format, 
        file_name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **file_name** | **str**| Contact document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_save"></a>
# **mapi_contact_save**
> mapi_contact_save(self, mapi_contact_save_request)

Save MAPI Contact to storage.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiContactApi.mapi_contact_save(
    cakePrefix_mapi_contact_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiContactSaveRequest**](MapiContactSaveRequest.md)| Create/Update contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="mapi_contact_save_async"></a>
# **mapi_contact_save_async**
> mapi_contact_save_async(self, mapi_contact_save_request)

Save MAPI Contact to storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
mapi_contact_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
MapiContactApi.mapi_contact_save_async(
    cakePrefix_mapi_contact_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MapiContactSaveRequest**](MapiContactSaveRequest.md)| Create/Update contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

