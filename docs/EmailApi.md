# AsposeEmailCloudSdk.EmailApi

<a name="add_email_attachment"></a>
# **add_email_attachment**
> add_email_attachment(self, add_email_attachment_request)

Adds an attachment to Email document

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

<a name="add_email_attachment_async"></a>
# **add_email_attachment_async**
> add_email_attachment_async(self, add_email_attachment_request)

Adds an attachment to Email document

Performs operation asynchronously.

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    attachment_name, 
    file_name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_name** | **str**| Attachment file name | 
 **file_name** | **str**| Email document file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage info to specify location of email document and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email"></a>
# **create_email**
> create_email(self, create_email_request)

Create an email document

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

<a name="create_email_async"></a>
# **create_email_async**
> create_email_async(self, create_email_request)

Create an email document

Performs operation asynchronously.

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **request** | [**CreateEmailRequest**](CreateEmailRequest.md)| An email document and optional Storage info to specify where the file should be located | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email"></a>
# **get_email**
> get_email(self, get_email_request)

Get email document

### Return type

[**EmailDocument**](EmailDocument.md)

<a name="get_email_async"></a>
# **get_email_async**
> get_email_async(self, get_email_request)

Get email document

Performs operation asynchronously.

### Return type

[**EmailDocument**](EmailDocument.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    storage=storage, 
    folder=folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_attachment"></a>
# **get_email_attachment**
> get_email_attachment(self, get_email_attachment_request)

Get email attachment by name

### Return type

[**file**](file.md)

<a name="get_email_attachment_async"></a>
# **get_email_attachment_async**
> get_email_attachment_async(self, get_email_attachment_request)

Get email attachment by name

Performs operation asynchronously.

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    attachment, 
    file_name, 
    storage=storage, 
    folder=folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **str**| Attachment name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_property"></a>
# **get_email_property**
> get_email_property(self, get_email_property_request)

Get an email document property by its name

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

<a name="get_email_property_async"></a>
# **get_email_property_async**
> get_email_property_async(self, get_email_property_request)

Get an email document property by its name

Performs operation asynchronously.

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    property_name, 
    file_name, 
    storage=storage, 
    folder=folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_property"></a>
# **set_email_property**
> set_email_property(self, set_email_property_request)

Set email document property value

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

<a name="set_email_property_async"></a>
# **set_email_property_async**
> set_email_property_async(self, set_email_property_request)

Set email document property value

Performs operation asynchronously.

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    property_name, 
    file_name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name that should be changed | 
 **file_name** | **str**| Email document file name | 
 **request** | [**SetEmailPropertyRequest**](SetEmailPropertyRequest.md)| A property that should be changed and optional Storage info to specify             where the file located | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

