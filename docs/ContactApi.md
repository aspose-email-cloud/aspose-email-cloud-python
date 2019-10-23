# AsposeEmailCloudSdk.ContactApi

<a name="add_contact_attachment"></a>
# **add_contact_attachment**
> add_contact_attachment(self, add_contact_attachment_request)

Add attachment to contact document

### Return type

void (empty response body)

<a name="add_contact_attachment_async"></a>
# **add_contact_attachment_async**
> add_contact_attachment_async(self, add_contact_attachment_request)

Add attachment to contact document

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    attachment, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **attachment** | **str**| Attachment name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_contact"></a>
# **create_contact**
> create_contact(self, create_contact_request)

Create contact document

### Return type

void (empty response body)

<a name="create_contact_async"></a>
# **create_contact_async**
> create_contact_async(self, create_contact_request)

Create contact document

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create contact request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_contact_property"></a>
# **delete_contact_property**
> delete_contact_property(self, delete_contact_property_request)

Delete property from indexed property list

### Return type

void (empty response body)

<a name="delete_contact_property_async"></a>
# **delete_contact_property_async**
> delete_contact_property_async(self, delete_contact_property_request)

Delete property from indexed property list

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    member_name, 
    index, 
    folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **member_name** | **str**| Indexed property name | 
 **index** | **int**| Property index | 
 **folder** | [**StorageFolder**](StorageFolder.md)| Calendar document location in storage information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_attachment"></a>
# **get_contact_attachment**
> get_contact_attachment(self, get_contact_attachment_request)

Get attachment file by name

### Return type

[**file**](file.md)

<a name="get_contact_attachment_async"></a>
# **get_contact_attachment_async**
> get_contact_attachment_async(self, get_contact_attachment_request)

Get attachment file by name

Performs operation asynchronously.

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_list"></a>
# **get_contact_list**
> get_contact_list(self, get_contact_list_request)

Get contact list from storage folder

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

<a name="get_contact_list_async"></a>
# **get_contact_list_async**
> get_contact_list_async(self, get_contact_list_request)

Get contact list from storage folder

Performs operation asynchronously.

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    format, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_properties"></a>
# **get_contact_properties**
> get_contact_properties(self, get_contact_properties_request)

Get contact document properties

### Return type

[**HierarchicalObject**](HierarchicalObject.md)

<a name="get_contact_properties_async"></a>
# **get_contact_properties_async**
> get_contact_properties_async(self, get_contact_properties_request)

Get contact document properties

Performs operation asynchronously.

### Return type

[**HierarchicalObject**](HierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_contact_properties"></a>
# **update_contact_properties**
> update_contact_properties(self, update_contact_properties_request)

Update contact document properties

### Return type

void (empty response body)

<a name="update_contact_properties_async"></a>
# **update_contact_properties_async**
> update_contact_properties_async(self, update_contact_properties_request)

Update contact document properties

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **int**| Contact document format | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

