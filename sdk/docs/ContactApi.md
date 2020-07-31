# AsposeEmailCloudSdk.ContactApi

<a name="contact_as_file"></a>
# **contact_as_file**
> contact_as_file(self, contact_as_file_request)

Converts contact model to specified format and returns as file             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ContactApi.contact_as_file(
    cakePrefix_contact_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ContactAsFileRequest**](ContactAsFileRequest.md)| Contact model and format to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_as_file_async"></a>
# **contact_as_file_async**
> contact_as_file_async(self, contact_as_file_request)

Converts contact model to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ContactApi.contact_as_file_async(
    cakePrefix_contact_as_file_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ContactAsFileRequest**](ContactAsFileRequest.md)| Contact model and format to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_as_mapi"></a>
# **contact_as_mapi**
> contact_as_mapi(self, contact_as_mapi_request)

Converts ContactDto to MapiContactDto.             

### Return type

[**MapiContactDto**](MapiContactDto.md)

### Request Parameters
```python
__init__(self, 
    contact_dto)
```

### Usage
```python
ContactApi.contact_as_mapi(
    cakePrefix_contact_as_mapi_request_cakeCodePostProcessor(
        contact_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_dto** | [**ContactDto**](ContactDto.md)| Contact model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_as_mapi_async"></a>
# **contact_as_mapi_async**
> contact_as_mapi_async(self, contact_as_mapi_request)

Converts ContactDto to MapiContactDto.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_as_mapi_async(request).get() returns [**MapiContactDto**](MapiContactDto.md)

### Request Parameters
```python
__init__(self, 
    contact_dto)
```

### Usage
```python
ContactApi.contact_as_mapi_async(
    cakePrefix_contact_as_mapi_request_cakeCodePostProcessor(
        contact_dto))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_dto** | [**ContactDto**](ContactDto.md)| Contact model to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_convert"></a>
# **contact_convert**
> contact_convert(self, contact_convert_request)

Converts contact document to specified format and returns as file             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    to_format, 
    from_format, 
    file)
```

### Usage
```python
ContactApi.contact_convert(
    cakePrefix_contact_convert_request_cakeCodePostProcessor(
        to_format, 
        from_format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_format** | **str**| File format to convert to Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str**| File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_convert_async"></a>
# **contact_convert_async**
> contact_convert_async(self, contact_convert_request)

Converts contact document to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_convert_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    to_format, 
    from_format, 
    file)
```

### Usage
```python
ContactApi.contact_convert_async(
    cakePrefix_contact_convert_request_cakeCodePostProcessor(
        to_format, 
        from_format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_format** | **str**| File format to convert to Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str**| File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_from_file"></a>
# **contact_from_file**
> contact_from_file(self, contact_from_file_request)

Converts contact document to a model representation             

### Return type

[**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
ContactApi.contact_from_file(
    cakePrefix_contact_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_from_file_async"></a>
# **contact_from_file_async**
> contact_from_file_async(self, contact_from_file_request)

Converts contact document to a model representation             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_from_file_async(request).get() returns [**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
ContactApi.contact_from_file_async(
    cakePrefix_contact_from_file_request_cakeCodePostProcessor(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **file** | **file**| File to convert | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_get"></a>
# **contact_get**
> contact_get(self, contact_get_request)

Get contact document from storage.             

### Return type

[**ContactDto**](ContactDto.md)

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
ContactApi.contact_get(
    cakePrefix_contact_get_request_cakeCodePostProcessor(
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

<a name="contact_get_async"></a>
# **contact_get_async**
> contact_get_async(self, contact_get_request)

Get contact document from storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_get_async(request).get() returns [**ContactDto**](ContactDto.md)

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
ContactApi.contact_get_async(
    cakePrefix_contact_get_request_cakeCodePostProcessor(
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

<a name="contact_get_as_file"></a>
# **contact_get_as_file**
> contact_get_as_file(self, contact_get_as_file_request)

Converts contact document from storage to specified format and returns as file             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    file_name, 
    to_format, 
    from_format, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
ContactApi.contact_get_as_file(
    cakePrefix_contact_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        to_format, 
        from_format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar document file name | 
 **to_format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str**| File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_get_as_file_async"></a>
# **contact_get_as_file_async**
> contact_get_as_file_async(self, contact_get_as_file_request)

Converts contact document from storage to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_get_as_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    file_name, 
    to_format, 
    from_format, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
ContactApi.contact_get_as_file_async(
    cakePrefix_contact_get_as_file_request_cakeCodePostProcessor(
        file_name, 
        to_format, 
        from_format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Calendar document file name | 
 **to_format** | **str**| File format Enum, available values: VCard, WebDav, Msg | 
 **from_format** | **str**| File format to convert from Enum, available values: VCard, WebDav, Msg | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_get_list"></a>
# **contact_get_list**
> contact_get_list(self, contact_get_list_request)

Get contact list from storage folder.             

### Return type

[**ContactStorageList**](ContactStorageList.md)

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
ContactApi.contact_get_list(
    cakePrefix_contact_get_list_request_cakeCodePostProcessor(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_get_list_async"></a>
# **contact_get_list_async**
> contact_get_list_async(self, contact_get_list_request)

Get contact list from storage folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_get_list_async(request).get() returns [**ContactStorageList**](ContactStorageList.md)

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
ContactApi.contact_get_list_async(
    cakePrefix_contact_get_list_request_cakeCodePostProcessor(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_save"></a>
# **contact_save**
> contact_save(self, contact_save_request)

Save contact to storage.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ContactApi.contact_save(
    cakePrefix_contact_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ContactSaveRequest**](ContactSaveRequest.md)| Create/Update contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="contact_save_async"></a>
# **contact_save_async**
> contact_save_async(self, contact_save_request)

Save contact to storage.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
contact_save_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
ContactApi.contact_save_async(
    cakePrefix_contact_save_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ContactSaveRequest**](ContactSaveRequest.md)| Create/Update contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

