# AsposeEmailCloudSdk.MapiApi

<a name="add_mapi_attachment"></a>
# **add_mapi_attachment**
> add_mapi_attachment(self, add_mapi_attachment_request)

Add attachment to document

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_mapi_attachment_async"></a>
# **add_mapi_attachment_async**
> add_mapi_attachment_async(self, add_mapi_attachment_request)

Add attachment to document

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_mapi"></a>
# **create_mapi**
> create_mapi(self, create_mapi_request)

Create new document

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create document request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_mapi_async"></a>
# **create_mapi_async**
> create_mapi_async(self, create_mapi_request)

Create new document

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create document request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_mapi_attachment"></a>
# **delete_mapi_attachment**
> delete_mapi_attachment(self, delete_mapi_attachment_request)

Remove attachment from document

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment name or index | 
 **storage** | [**StorageFolderLocation**](StorageFolderLocation.md)| Document file storage location info | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_mapi_attachment_async"></a>
# **delete_mapi_attachment_async**
> delete_mapi_attachment_async(self, delete_mapi_attachment_request)

Remove attachment from document

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment name or index | 
 **storage** | [**StorageFolderLocation**](StorageFolderLocation.md)| Document file storage location info | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_mapi_properties"></a>
# **delete_mapi_properties**
> delete_mapi_properties(self, delete_mapi_properties_request)

Delete document properties

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be deleted | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_mapi_properties_async"></a>
# **delete_mapi_properties_async**
> delete_mapi_properties_async(self, delete_mapi_properties_request)

Delete document properties

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be deleted | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_attachment"></a>
# **get_mapi_attachment**
> get_mapi_attachment(self, get_mapi_attachment_request)

Get document attachment as file stream

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_attachment_async"></a>
# **get_mapi_attachment_async**
> get_mapi_attachment_async(self, get_mapi_attachment_request)

Get document attachment as file stream

Performs operation asynchronously.

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_attachments"></a>
# **get_mapi_attachments**
> get_mapi_attachments(self, get_mapi_attachments_request)

Get document attachment list

### Return type

[**ListResponseOfString**](ListResponseOfString.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_attachments_async"></a>
# **get_mapi_attachments_async**
> get_mapi_attachments_async(self, get_mapi_attachments_request)

Get document attachment list

Performs operation asynchronously.

### Return type

[**ListResponseOfString**](ListResponseOfString.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_list"></a>
# **get_mapi_list**
> get_mapi_list(self, get_mapi_list_request)

Get document list from storage folder

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_list_async"></a>
# **get_mapi_list_async**
> get_mapi_list_async(self, get_mapi_list_request)

Get document list from storage folder

Performs operation asynchronously.

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_properties"></a>
# **get_mapi_properties**
> get_mapi_properties(self, get_mapi_properties_request)

Get document properties

### Return type

[**HierarchicalObjectResponse**](HierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_properties_async"></a>
# **get_mapi_properties_async**
> get_mapi_properties_async(self, get_mapi_properties_request)

Get document properties

Performs operation asynchronously.

### Return type

[**HierarchicalObjectResponse**](HierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_mapi_properties"></a>
# **update_mapi_properties**
> update_mapi_properties(self, update_mapi_properties_request)

Update document properties

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_mapi_properties_async"></a>
# **update_mapi_properties_async**
> update_mapi_properties_async(self, update_mapi_properties_request)

Update document properties

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

