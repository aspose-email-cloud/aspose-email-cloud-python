# AsposeEmailCloudSdk.EmailApi

<a name="email_as_file"></a>
# **email_as_file**
> email_as_file(self, email_as_file_request)

Converts Email model to specified format and returns as file.             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.email_as_file(
    cakePrefix_email_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailAsFileRequest**](EmailAsFileRequest.md)| Email model and format to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_as_file_async"></a>
# **email_as_file_async**
> email_as_file_async(self, email_as_file_request)

Converts Email model to specified format and returns as file.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.email_as_file_async(
    cakePrefix_email_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailAsFileRequest**](EmailAsFileRequest.md)| Email model and format to convert. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_as_mapi"></a>
# **email_as_mapi**
> email_as_mapi(self, email_as_mapi_request)

Converts EmailDto to MapiMessageDto.             

### Return type

[**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    email_dto)
```

### Usage
```python
EmailApi.email_as_mapi(
    cakePrefix_email_as_mapi_request_cakeCodePostProcessor(
        email_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_dto** | [**EmailDto**](EmailDto.md)| Email model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_as_mapi_async"></a>
# **email_as_mapi_async**
> email_as_mapi_async(self, email_as_mapi_request)

Converts EmailDto to MapiMessageDto.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_as_mapi_async(request).get() returns [**MapiMessageDto**](MapiMessageDto.md)

### Request Parameters
```python
__init__(self, 
    email_dto)
```

### Usage
```python
EmailApi.email_as_mapi_async(
    cakePrefix_email_as_mapi_request_cakeCodePostProcessor(
        email_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_dto** | [**EmailDto**](EmailDto.md)| Email model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_convert"></a>
# **email_convert**
> email_convert(self, email_convert_request)

Converts email document to specified format and returns as file             

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
EmailApi.email_convert(
    cakePrefix_email_convert_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_convert_async"></a>
# **email_convert_async**
> email_convert_async(self, email_convert_request)

Converts email document to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_convert_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
EmailApi.email_convert_async(
    cakePrefix_email_convert_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_from_file"></a>
# **email_from_file**
> email_from_file(self, email_from_file_request)

Converts email document to a model representation             

### Return type

[**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
EmailApi.email_from_file(
    cakePrefix_email_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_from_file_async"></a>
# **email_from_file_async**
> email_from_file_async(self, email_from_file_request)

Converts email document to a model representation             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_from_file_async(request).get() returns [**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
EmailApi.email_from_file_async(
    cakePrefix_email_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_get"></a>
# **email_get**
> email_get(self, email_get_request)

Get email document from storage.             

### Return type

[**EmailDto**](EmailDto.md)

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
EmailApi.email_get(
    cakePrefix_email_get_request_cakeCodePostProcessor(
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

<a name="email_get_async"></a>
# **email_get_async**
> email_get_async(self, email_get_request)

Get email document from storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_get_async(request).get() returns [**EmailDto**](EmailDto.md)

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
EmailApi.email_get_async(
    cakePrefix_email_get_request_cakeCodePostProcessor(
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

<a name="email_get_as_file"></a>
# **email_get_as_file**
> email_get_as_file(self, email_get_as_file_request)

Converts email document from storage to specified format and returns as file             

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
EmailApi.email_get_as_file(
    cakePrefix_email_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name | 
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_get_as_file_async"></a>
# **email_get_as_file_async**
> email_get_as_file_async(self, email_get_as_file_request)

Converts email document from storage to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_get_as_file_async(request).get() returns **file**

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
EmailApi.email_get_as_file_async(
    cakePrefix_email_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name | 
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_get_list"></a>
# **email_get_list**
> email_get_list(self, email_get_list_request)

Get email list from storage folder.             

### Return type

[**EmailStorageList**](EmailStorageList.md)

### Request Parameters
```python
__init__(self, 
    format, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

### Usage
```python
EmailApi.email_get_list(
    cakePrefix_email_get_list_request_cakeCodePostProcessor(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_get_list_async"></a>
# **email_get_list_async**
> email_get_list_async(self, email_get_list_request)

Get email list from storage folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_get_list_async(request).get() returns [**EmailStorageList**](EmailStorageList.md)

### Request Parameters
```python
__init__(self, 
    format, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

### Usage
```python
EmailApi.email_get_list_async(
    cakePrefix_email_get_list_request_cakeCodePostProcessor(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_save"></a>
# **email_save**
> email_save(self, email_save_request)

Save email document to storage.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.email_save(
    cakePrefix_email_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailSaveRequest**](EmailSaveRequest.md)| Email document create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_save_async"></a>
# **email_save_async**
> email_save_async(self, email_save_request)

Save email document to storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.email_save_async(
    cakePrefix_email_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailSaveRequest**](EmailSaveRequest.md)| Email document create/update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

