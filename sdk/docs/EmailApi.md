# AsposeEmailCloudSdk.EmailApi

<a name="add_calendar_attachment"></a>
# **add_calendar_attachment**
> add_calendar_attachment(self, add_calendar_attachment_request)

Adds an attachment to iCalendar file             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

### Usage
```python
EmailApi.add_calendar_attachment(
    AddCalendarAttachmentRequest(
        name, 
        attachment, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **attachment** | **str**| Attachment file name in storage | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage name and folder path for calendar and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_calendar_attachment_async"></a>
# **add_calendar_attachment_async**
> add_calendar_attachment_async(self, add_calendar_attachment_request)

Adds an attachment to iCalendar file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
add_calendar_attachment_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

### Usage
```python
EmailApi.add_calendar_attachment_async(
    AddCalendarAttachmentRequest(
        name, 
        attachment, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **attachment** | **str**| Attachment file name in storage | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage name and folder path for calendar and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_contact_attachment"></a>
# **add_contact_attachment**
> add_contact_attachment(self, add_contact_attachment_request)

Add attachment to contact document             

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

### Usage
```python
EmailApi.add_contact_attachment(
    AddContactAttachmentRequest(
        format, 
        name, 
        attachment, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **attachment** | **str**| Attachment name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_contact_attachment_async"></a>
# **add_contact_attachment_async**
> add_contact_attachment_async(self, add_contact_attachment_request)

Add attachment to contact document             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
add_contact_attachment_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    attachment, 
    request)
```

### Usage
```python
EmailApi.add_contact_attachment_async(
    AddContactAttachmentRequest(
        format, 
        name, 
        attachment, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **attachment** | **str**| Attachment name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_email_attachment"></a>
# **add_email_attachment**
> add_email_attachment(self, add_email_attachment_request)

Adds an attachment to Email document             

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    attachment_name, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.add_email_attachment(
    AddEmailAttachmentRequest(
        attachment_name, 
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_name** | **str**| Attachment file name | 
 **file_name** | **str**| Email document file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage info to specify location of email document and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="add_email_attachment_async"></a>
# **add_email_attachment_async**
> add_email_attachment_async(self, add_email_attachment_request)

Adds an attachment to Email document             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
add_email_attachment_async(request).get() returns [**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    attachment_name, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.add_email_attachment_async(
    AddEmailAttachmentRequest(
        attachment_name, 
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_name** | **str**| Attachment file name | 
 **file_name** | **str**| Email document file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage info to specify location of email document and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

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

### Usage
```python
EmailApi.add_mapi_attachment(
    AddMapiAttachmentRequest(
        name, 
        attachment, 
        request))
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

Returns multiprocessing.pool.AsyncResult.
add_mapi_attachment_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

### Usage
```python
EmailApi.add_mapi_attachment_async(
    AddMapiAttachmentRequest(
        name, 
        attachment, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **attachment** | **str**| Attachment file name | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Add attachment request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_ocr"></a>
# **ai_bcr_ocr**
> ai_bcr_ocr(self, ai_bcr_ocr_request)

Ocr images             

### Return type

[**ListResponseOfAiBcrOcrData**](ListResponseOfAiBcrOcrData.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_ocr(
    AiBcrOcrRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_ocr_async"></a>
# **ai_bcr_ocr_async**
> ai_bcr_ocr_async(self, ai_bcr_ocr_request)

Ocr images             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_ocr_async(request).get() returns [**ListResponseOfAiBcrOcrData**](ListResponseOfAiBcrOcrData.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_ocr_async(
    AiBcrOcrRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_ocr_storage"></a>
# **ai_bcr_ocr_storage**
> ai_bcr_ocr_storage(self, ai_bcr_ocr_storage_request)

Ocr images from storage             

### Return type

[**ListResponseOfAiBcrOcrData**](ListResponseOfAiBcrOcrData.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_ocr_storage(
    AiBcrOcrStorageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrStorageImageRq**](AiBcrStorageImageRq.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_ocr_storage_async"></a>
# **ai_bcr_ocr_storage_async**
> ai_bcr_ocr_storage_async(self, ai_bcr_ocr_storage_request)

Ocr images from storage             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_ocr_storage_async(request).get() returns [**ListResponseOfAiBcrOcrData**](ListResponseOfAiBcrOcrData.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_ocr_storage_async(
    AiBcrOcrStorageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrStorageImageRq**](AiBcrStorageImageRq.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse"></a>
# **ai_bcr_parse**
> ai_bcr_parse(self, ai_bcr_parse_request)

Parse images to vCard properties             

### Return type

[**ListResponseOfHierarchicalObject**](ListResponseOfHierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse(
    AiBcrParseRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_async"></a>
# **ai_bcr_parse_async**
> ai_bcr_parse_async(self, ai_bcr_parse_request)

Parse images to vCard properties             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_async(request).get() returns [**ListResponseOfHierarchicalObject**](ListResponseOfHierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_async(
    AiBcrParseRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_model"></a>
# **ai_bcr_parse_model**
> ai_bcr_parse_model(self, ai_bcr_parse_model_request)

Parse images to vCard document models             

### Return type

[**ListResponseOfContactDto**](ListResponseOfContactDto.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_model(
    AiBcrParseModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_model_async"></a>
# **ai_bcr_parse_model_async**
> ai_bcr_parse_model_async(self, ai_bcr_parse_model_request)

Parse images to vCard document models             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_model_async(request).get() returns [**ListResponseOfContactDto**](ListResponseOfContactDto.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_model_async(
    AiBcrParseModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrBase64Rq**](AiBcrBase64Rq.md)| Request with base64 images data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_ocr_data_model"></a>
# **ai_bcr_parse_ocr_data_model**
> ai_bcr_parse_ocr_data_model(self, ai_bcr_parse_ocr_data_model_request)

Parse OCR data to vCard document models             

### Return type

[**ListResponseOfContactDto**](ListResponseOfContactDto.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_ocr_data_model(
    AiBcrParseOcrDataModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrParseOcrDataRq**](AiBcrParseOcrDataRq.md)|  | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_ocr_data_model_async"></a>
# **ai_bcr_parse_ocr_data_model_async**
> ai_bcr_parse_ocr_data_model_async(self, ai_bcr_parse_ocr_data_model_request)

Parse OCR data to vCard document models             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_ocr_data_model_async(request).get() returns [**ListResponseOfContactDto**](ListResponseOfContactDto.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_ocr_data_model_async(
    AiBcrParseOcrDataModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrParseOcrDataRq**](AiBcrParseOcrDataRq.md)|  | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_storage"></a>
# **ai_bcr_parse_storage**
> ai_bcr_parse_storage(self, ai_bcr_parse_storage_request)

Parse images from storage to vCard files             

### Return type

[**ListResponseOfStorageFileLocation**](ListResponseOfStorageFileLocation.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_storage(
    AiBcrParseStorageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrParseStorageRq**](AiBcrParseStorageRq.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_storage_async"></a>
# **ai_bcr_parse_storage_async**
> ai_bcr_parse_storage_async(self, ai_bcr_parse_storage_request)

Parse images from storage to vCard files             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_storage_async(request).get() returns [**ListResponseOfStorageFileLocation**](ListResponseOfStorageFileLocation.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_bcr_parse_storage_async(
    AiBcrParseStorageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiBcrParseStorageRq**](AiBcrParseStorageRq.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_complete"></a>
# **ai_name_complete**
> ai_name_complete(self, ai_name_complete_request)

The call proposes k most probable names for given starting characters             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_complete(
    AiNameCompleteRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to complete (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_complete_async"></a>
# **ai_name_complete_async**
> ai_name_complete_async(self, ai_name_complete_request)

The call proposes k most probable names for given starting characters             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_complete_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_complete_async(
    AiNameCompleteRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to complete (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand"></a>
# **ai_name_expand**
> ai_name_expand(self, ai_name_expand_request)

Expands a person's name into a list of possible alternatives using options for expanding instructions             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_expand(
    AiNameExpandRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_async"></a>
# **ai_name_expand_async**
> ai_name_expand_async(self, ai_name_expand_request)

Expands a person's name into a list of possible alternatives using options for expanding instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_expand_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_expand_async(
    AiNameExpandRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_parsed"></a>
# **ai_name_expand_parsed**
> ai_name_expand_parsed(self, ai_name_expand_parsed_request)

Expands a person's parsed name into a list of possible alternatives using options for expanding instructions             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_expand_parsed(
    AiNameExpandParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Parsed name with options | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_parsed_async"></a>
# **ai_name_expand_parsed_async**
> ai_name_expand_parsed_async(self, ai_name_expand_parsed_request)

Expands a person's parsed name into a list of possible alternatives using options for expanding instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_expand_parsed_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_expand_parsed_async(
    AiNameExpandParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Parsed name with options | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format"></a>
# **ai_name_format**
> ai_name_format(self, ai_name_format_request)

Formats a person's name in correct case and name order using options for formatting instructions             

### Return type

[**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    format=format, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_format(
    AiNameFormatRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        format=format, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **format** | **str**| Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (&#x3D; &#39;%t%F%m%N%L%p&#39;)     /format/FN+LN/ (&#x3D; &#39;%F%L&#39;)     /format/title+FN+LN/ (&#x3D; &#39;%t%F%L&#39;)     /format/FN+MN+LN/ (&#x3D; &#39;%F%M%N%L&#39;)     /format/title+FN+MN+LN/ (&#x3D; &#39;%t%F%M%N%L&#39;)     /format/FN+MI+LN/ (&#x3D; &#39;%F%m%N%L&#39;)     /format/title+FN+MI+LN/ (&#x3D; &#39;%t%F%m%N%L&#39;)     /format/LN/ (&#x3D; &#39;%L&#39;)     /format/title+LN/ (&#x3D; &#39;%t%L&#39;)     /format/LN+FN+MN/ (&#x3D; &#39;%L,%F%M%N&#39;)     /format/LN+title+FN+MN/ (&#x3D; &#39;%L,%t%F%M%N&#39;)     /format/LN+FN+MI/ (&#x3D; &#39;%L,%F%m%N&#39;)     /format/LN+title+FN+MI/ (&#x3D; &#39;%L,%t%F%m%N&#39;)  Custom format string - custom combination of characters and the next term placeholders:      &#39;%t&#39; - Title (prefix)     &#39;%F&#39; - First name     &#39;%f&#39; - First initial     &#39;%M&#39; - Middle name(s)     &#39;%m&#39; - Middle initial(s)     &#39;%N&#39; - Nickname     &#39;%L&#39; - Last name     &#39;%l&#39; - Last initial     &#39;%p&#39; - Postfix  If no value for format option was provided, its default value is &#39;%t%F%m%N%L%p&#39;              | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_async"></a>
# **ai_name_format_async**
> ai_name_format_async(self, ai_name_format_request)

Formats a person's name in correct case and name order using options for formatting instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_format_async(request).get() returns [**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    format=format, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_format_async(
    AiNameFormatRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        format=format, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **format** | **str**| Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (&#x3D; &#39;%t%F%m%N%L%p&#39;)     /format/FN+LN/ (&#x3D; &#39;%F%L&#39;)     /format/title+FN+LN/ (&#x3D; &#39;%t%F%L&#39;)     /format/FN+MN+LN/ (&#x3D; &#39;%F%M%N%L&#39;)     /format/title+FN+MN+LN/ (&#x3D; &#39;%t%F%M%N%L&#39;)     /format/FN+MI+LN/ (&#x3D; &#39;%F%m%N%L&#39;)     /format/title+FN+MI+LN/ (&#x3D; &#39;%t%F%m%N%L&#39;)     /format/LN/ (&#x3D; &#39;%L&#39;)     /format/title+LN/ (&#x3D; &#39;%t%L&#39;)     /format/LN+FN+MN/ (&#x3D; &#39;%L,%F%M%N&#39;)     /format/LN+title+FN+MN/ (&#x3D; &#39;%L,%t%F%M%N&#39;)     /format/LN+FN+MI/ (&#x3D; &#39;%L,%F%m%N&#39;)     /format/LN+title+FN+MI/ (&#x3D; &#39;%L,%t%F%m%N&#39;)  Custom format string - custom combination of characters and the next term placeholders:      &#39;%t&#39; - Title (prefix)     &#39;%F&#39; - First name     &#39;%f&#39; - First initial     &#39;%M&#39; - Middle name(s)     &#39;%m&#39; - Middle initial(s)     &#39;%N&#39; - Nickname     &#39;%L&#39; - Last name     &#39;%l&#39; - Last initial     &#39;%p&#39; - Postfix  If no value for format option was provided, its default value is &#39;%t%F%m%N%L%p&#39;              | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_parsed"></a>
# **ai_name_format_parsed**
> ai_name_format_parsed(self, ai_name_format_parsed_request)

Formats a person's parsed name in correct case and name order using options for formatting instructions             

### Return type

[**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_format_parsed(
    AiNameFormatParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Parsed name with options | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_parsed_async"></a>
# **ai_name_format_parsed_async**
> ai_name_format_parsed_async(self, ai_name_format_parsed_request)

Formats a person's parsed name in correct case and name order using options for formatting instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_format_parsed_async(request).get() returns [**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_format_parsed_async(
    AiNameFormatParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Parsed name with options | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize"></a>
# **ai_name_genderize**
> ai_name_genderize(self, ai_name_genderize_request)

Detect person's gender from name string             

### Return type

[**ListResponseOfAiNameGenderHypothesis**](ListResponseOfAiNameGenderHypothesis.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_genderize(
    AiNameGenderizeRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_async"></a>
# **ai_name_genderize_async**
> ai_name_genderize_async(self, ai_name_genderize_request)

Detect person's gender from name string             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_genderize_async(request).get() returns [**ListResponseOfAiNameGenderHypothesis**](ListResponseOfAiNameGenderHypothesis.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_genderize_async(
    AiNameGenderizeRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_parsed"></a>
# **ai_name_genderize_parsed**
> ai_name_genderize_parsed(self, ai_name_genderize_parsed_request)

Detect person's gender from parsed name             

### Return type

[**ListResponseOfAiNameGenderHypothesis**](ListResponseOfAiNameGenderHypothesis.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_genderize_parsed(
    AiNameGenderizeParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Gender detection request data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_parsed_async"></a>
# **ai_name_genderize_parsed_async**
> ai_name_genderize_parsed_async(self, ai_name_genderize_parsed_request)

Detect person's gender from parsed name             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_genderize_parsed_async(request).get() returns [**ListResponseOfAiNameGenderHypothesis**](ListResponseOfAiNameGenderHypothesis.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_genderize_parsed_async(
    AiNameGenderizeParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedRq**](AiNameParsedRq.md)| Gender detection request data | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match"></a>
# **ai_name_match**
> ai_name_match(self, ai_name_match_request)

Compare people's names. Uses options for comparing instructions             

### Return type

[**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    name, 
    other_name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_match(
    AiNameMatchRequest(
        name, 
        other_name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to match (required) | 
 **other_name** | **str**| Another name to match (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_async"></a>
# **ai_name_match_async**
> ai_name_match_async(self, ai_name_match_request)

Compare people's names. Uses options for comparing instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_match_async(request).get() returns [**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    name, 
    other_name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_match_async(
    AiNameMatchRequest(
        name, 
        other_name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to match (required) | 
 **other_name** | **str**| Another name to match (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_parsed"></a>
# **ai_name_match_parsed**
> ai_name_match_parsed(self, ai_name_match_parsed_request)

Compare people's parsed names and attributes. Uses options for comparing instructions             

### Return type

[**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_match_parsed(
    AiNameMatchParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedMatchRq**](AiNameParsedMatchRq.md)| Parsed names to match | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_parsed_async"></a>
# **ai_name_match_parsed_async**
> ai_name_match_parsed_async(self, ai_name_match_parsed_request)

Compare people's parsed names and attributes. Uses options for comparing instructions             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_match_parsed_async(request).get() returns [**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.ai_name_match_parsed_async(
    AiNameMatchParsedRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AiNameParsedMatchRq**](AiNameParsedMatchRq.md)| Parsed names to match | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse"></a>
# **ai_name_parse**
> ai_name_parse(self, ai_name_parse_request)

Parse name to components             

### Return type

[**ListResponseOfAiNameComponent**](ListResponseOfAiNameComponent.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_parse(
    AiNameParseRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_async"></a>
# **ai_name_parse_async**
> ai_name_parse_async(self, ai_name_parse_request)

Parse name to components             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_parse_async(request).get() returns [**ListResponseOfAiNameComponent**](ListResponseOfAiNameComponent.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_parse_async(
    AiNameParseRequest(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_email_address"></a>
# **ai_name_parse_email_address**
> ai_name_parse_email_address(self, ai_name_parse_email_address_request)

Parse person's name out of an email address             

### Return type

[**ListResponseOfAiNameExtracted**](ListResponseOfAiNameExtracted.md)

### Request Parameters
```python
__init__(self, 
    email_address, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_parse_email_address(
    AiNameParseEmailAddressRequest(
        email_address, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email address to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_email_address_async"></a>
# **ai_name_parse_email_address_async**
> ai_name_parse_email_address_async(self, ai_name_parse_email_address_request)

Parse person's name out of an email address             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_parse_email_address_async(request).get() returns [**ListResponseOfAiNameExtracted**](ListResponseOfAiNameExtracted.md)

### Request Parameters
```python
__init__(self, 
    email_address, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
EmailApi.ai_name_parse_email_address_async(
    AiNameParseEmailAddressRequest(
        email_address, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email address to parse (required) | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian) | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France | [optional] [default to ]
 **encoding** | **str**| A character encoding name | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_email_message"></a>
# **append_email_message**
> append_email_message(self, append_email_message_request)

Adds an email from *.eml file to specified folder in email account             

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.append_email_message(
    AppendEmailMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailBaseRequest**](AppendEmailBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_email_message_async"></a>
# **append_email_message_async**
> append_email_message_async(self, append_email_message_request)

Adds an email from *.eml file to specified folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
append_email_message_async(request).get() returns [**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.append_email_message_async(
    AppendEmailMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailBaseRequest**](AppendEmailBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_email_model_message"></a>
# **append_email_model_message**
> append_email_model_message(self, append_email_model_message_request)

Adds an email from model to specified folder in email account             

### Return type

[**ValueResponse**](ValueResponse.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.append_email_model_message(
    AppendEmailModelMessageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AppendEmailModelRq**](AppendEmailModelRq.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_email_model_message_async"></a>
# **append_email_model_message_async**
> append_email_model_message_async(self, append_email_model_message_request)

Adds an email from model to specified folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
append_email_model_message_async(request).get() returns [**ValueResponse**](ValueResponse.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.append_email_model_message_async(
    AppendEmailModelMessageRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**AppendEmailModelRq**](AppendEmailModelRq.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_mime_message"></a>
# **append_mime_message**
> append_mime_message(self, append_mime_message_request)

Adds an email from MIME to specified folder in email account             

### Return type

[**ValueResponse**](ValueResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.append_mime_message(
    AppendMimeMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailMimeBaseRequest**](AppendEmailMimeBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_mime_message_async"></a>
# **append_mime_message_async**
> append_mime_message_async(self, append_mime_message_request)

Adds an email from MIME to specified folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
append_mime_message_async(request).get() returns [**ValueResponse**](ValueResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.append_mime_message_async(
    AppendMimeMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailMimeBaseRequest**](AppendEmailMimeBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="convert_calendar_model_to_alternate"></a>
# **convert_calendar_model_to_alternate**
> convert_calendar_model_to_alternate(self, convert_calendar_model_to_alternate_request)

Convert iCalendar to AlternateView             

### Return type

[**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.convert_calendar_model_to_alternate(
    ConvertCalendarModelToAlternateRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**CalendarDtoAlternateRq**](CalendarDtoAlternateRq.md)| iCalendar to AlternateView request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="convert_calendar_model_to_alternate_async"></a>
# **convert_calendar_model_to_alternate_async**
> convert_calendar_model_to_alternate_async(self, convert_calendar_model_to_alternate_request)

Convert iCalendar to AlternateView             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
convert_calendar_model_to_alternate_async(request).get() returns [**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.convert_calendar_model_to_alternate_async(
    ConvertCalendarModelToAlternateRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**CalendarDtoAlternateRq**](CalendarDtoAlternateRq.md)| iCalendar to AlternateView request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="convert_email"></a>
# **convert_email**
> convert_email(self, convert_email_request)

Converts email document to specified format and returns as file             

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
EmailApi.convert_email(
    ConvertEmailRequest(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **file** | **file**| File to upload | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="convert_email_async"></a>
# **convert_email_async**
> convert_email_async(self, convert_email_request)

Converts email document to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
convert_email_async(request).get() returns [**file**](file.md)

### Request Parameters
```python
__init__(self, 
    format, 
    file)
```

### Usage
```python
EmailApi.convert_email_async(
    ConvertEmailRequest(
        format, 
        file))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **file** | **file**| File to upload | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="copy_file"></a>
# **copy_file**
> copy_file(self, copy_file_request)

Copy file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.copy_file(
    CopyFileRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="copy_file_async"></a>
# **copy_file_async**
> copy_file_async(self, copy_file_request)

Copy file

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
copy_file_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.copy_file_async(
    CopyFileRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="copy_folder"></a>
# **copy_folder**
> copy_folder(self, copy_folder_request)

Copy folder

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

### Usage
```python
EmailApi.copy_folder(
    CopyFolderRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="copy_folder_async"></a>
# **copy_folder_async**
> copy_folder_async(self, copy_folder_request)

Copy folder

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
copy_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

### Usage
```python
EmailApi.copy_folder_async(
    CopyFolderRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_calendar"></a>
# **create_calendar**
> create_calendar(self, create_calendar_request)

Create calendar file             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.create_calendar(
    CreateCalendarRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)|  | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_calendar_async"></a>
# **create_calendar_async**
> create_calendar_async(self, create_calendar_request)

Create calendar file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
create_calendar_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.create_calendar_async(
    CreateCalendarRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)|  | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_contact"></a>
# **create_contact**
> create_contact(self, create_contact_request)

Create contact document             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

### Usage
```python
EmailApi.create_contact(
    CreateContactRequest(
        format, 
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create contact request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_contact_async"></a>
# **create_contact_async**
> create_contact_async(self, create_contact_request)

Create contact document             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
create_contact_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

### Usage
```python
EmailApi.create_contact_async(
    CreateContactRequest(
        format, 
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create contact request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email"></a>
# **create_email**
> create_email(self, create_email_request)

Create an email document             

### Return type

[**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.create_email(
    CreateEmailRequest(
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **request** | [**CreateEmailRequest**](CreateEmailRequest.md)| An email document and optional Storage info to specify where the file should be located              | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email_async"></a>
# **create_email_async**
> create_email_async(self, create_email_request)

Create an email document             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
create_email_async(request).get() returns [**EmailDocumentResponse**](EmailDocumentResponse.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.create_email_async(
    CreateEmailRequest(
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **request** | [**CreateEmailRequest**](CreateEmailRequest.md)| An email document and optional Storage info to specify where the file should be located              | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email_folder"></a>
# **create_email_folder**
> create_email_folder(self, create_email_folder_request)

Create new folder in email account             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.create_email_folder(
    CreateEmailFolderRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateFolderBaseRequest**](CreateFolderBaseRequest.md)| Create folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email_folder_async"></a>
# **create_email_folder_async**
> create_email_folder_async(self, create_email_folder_request)

Create new folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
create_email_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.create_email_folder_async(
    CreateEmailFolderRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateFolderBaseRequest**](CreateFolderBaseRequest.md)| Create folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_folder"></a>
# **create_folder**
> create_folder(self, create_folder_request)

Create the folder

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.create_folder(
    CreateFolderRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_folder_async"></a>
# **create_folder_async**
> create_folder_async(self, create_folder_request)

Create the folder

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
create_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.create_folder_async(
    CreateFolderRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

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

### Usage
```python
EmailApi.create_mapi(
    CreateMapiRequest(
        name, 
        request))
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

Returns multiprocessing.pool.AsyncResult.
create_mapi_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.create_mapi_async(
    CreateMapiRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Create document request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_calendar_property"></a>
# **delete_calendar_property**
> delete_calendar_property(self, delete_calendar_property_request)

Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    member_name, 
    index, 
    request)
```

### Usage
```python
EmailApi.delete_calendar_property(
    DeleteCalendarPropertyRequest(
        name, 
        member_name, 
        index, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **member_name** | **str**| Indexed property name | 
 **index** | **str**| Property index path | 
 **request** | [**StorageFolderLocation**](StorageFolderLocation.md)| Storage detail to specify iCalendar file location | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_calendar_property_async"></a>
# **delete_calendar_property_async**
> delete_calendar_property_async(self, delete_calendar_property_request)

Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_calendar_property_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    member_name, 
    index, 
    request)
```

### Usage
```python
EmailApi.delete_calendar_property_async(
    DeleteCalendarPropertyRequest(
        name, 
        member_name, 
        index, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **member_name** | **str**| Indexed property name | 
 **index** | **str**| Property index path | 
 **request** | [**StorageFolderLocation**](StorageFolderLocation.md)| Storage detail to specify iCalendar file location | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_contact_property"></a>
# **delete_contact_property**
> delete_contact_property(self, delete_contact_property_request)

Delete property from indexed property list             

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

### Usage
```python
EmailApi.delete_contact_property(
    DeleteContactPropertyRequest(
        format, 
        name, 
        member_name, 
        index, 
        folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **member_name** | **str**| Indexed property name | 
 **index** | **int**| Property index | 
 **folder** | [**StorageFolderLocation**](StorageFolderLocation.md)| Calendar document location in storage information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_contact_property_async"></a>
# **delete_contact_property_async**
> delete_contact_property_async(self, delete_contact_property_request)

Delete property from indexed property list             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_contact_property_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    member_name, 
    index, 
    folder)
```

### Usage
```python
EmailApi.delete_contact_property_async(
    DeleteContactPropertyRequest(
        format, 
        name, 
        member_name, 
        index, 
        folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **member_name** | **str**| Indexed property name | 
 **index** | **int**| Property index | 
 **folder** | [**StorageFolderLocation**](StorageFolderLocation.md)| Calendar document location in storage information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_folder"></a>
# **delete_email_folder**
> delete_email_folder(self, delete_email_folder_request)

Delete a folder in email account             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.delete_email_folder(
    DeleteEmailFolderRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteFolderBaseRequest**](DeleteFolderBaseRequest.md)| Delete folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_folder_async"></a>
# **delete_email_folder_async**
> delete_email_folder_async(self, delete_email_folder_request)

Delete a folder in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_email_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.delete_email_folder_async(
    DeleteEmailFolderRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteFolderBaseRequest**](DeleteFolderBaseRequest.md)| Delete folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_message"></a>
# **delete_email_message**
> delete_email_message(self, delete_email_message_request)

Delete message from email account by id             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.delete_email_message(
    DeleteEmailMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteMessageBaseRequest**](DeleteMessageBaseRequest.md)| Delete message request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_message_async"></a>
# **delete_email_message_async**
> delete_email_message_async(self, delete_email_message_request)

Delete message from email account by id             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_email_message_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.delete_email_message_async(
    DeleteEmailMessageRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteMessageBaseRequest**](DeleteMessageBaseRequest.md)| Delete message request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_file"></a>
# **delete_file**
> delete_file(self, delete_file_request)

Delete file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.delete_file(
    DeleteFileRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_file_async"></a>
# **delete_file_async**
> delete_file_async(self, delete_file_request)

Delete file

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_file_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.delete_file_async(
    DeleteFileRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_folder"></a>
# **delete_folder**
> delete_folder(self, delete_folder_request)

Delete folder

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    recursive=recursive)
```

### Usage
```python
EmailApi.delete_folder(
    DeleteFolderRequest(
        path, 
        storage_name=storage_name, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_folder_async"></a>
# **delete_folder_async**
> delete_folder_async(self, delete_folder_request)

Delete folder

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
delete_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    recursive=recursive)
```

### Usage
```python
EmailApi.delete_folder_async(
    DeleteFolderRequest(
        path, 
        storage_name=storage_name, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

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

### Usage
```python
EmailApi.delete_mapi_attachment(
    DeleteMapiAttachmentRequest(
        name, 
        attachment, 
        storage))
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

Returns multiprocessing.pool.AsyncResult.
delete_mapi_attachment_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    storage)
```

### Usage
```python
EmailApi.delete_mapi_attachment_async(
    DeleteMapiAttachmentRequest(
        name, 
        attachment, 
        storage))
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

### Usage
```python
EmailApi.delete_mapi_properties(
    DeleteMapiPropertiesRequest(
        name, 
        request))
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

Returns multiprocessing.pool.AsyncResult.
delete_mapi_properties_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.delete_mapi_properties_async(
    DeleteMapiPropertiesRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be deleted | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config"></a>
# **discover_email_config**
> discover_email_config(self, discover_email_config_request)

Discover email accounts by email address. Does not validate discovered accounts.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    address, 
    fast_processing=fast_processing)
```

### Usage
```python
EmailApi.discover_email_config(
    DiscoverEmailConfigRequest(
        address, 
        fast_processing=fast_processing))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Email address | 
 **fast_processing** | **bool**| Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned              | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config_async"></a>
# **discover_email_config_async**
> discover_email_config_async(self, discover_email_config_request)

Discover email accounts by email address. Does not validate discovered accounts.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
discover_email_config_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    address, 
    fast_processing=fast_processing)
```

### Usage
```python
EmailApi.discover_email_config_async(
    DiscoverEmailConfigRequest(
        address, 
        fast_processing=fast_processing))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Email address | 
 **fast_processing** | **bool**| Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned              | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config_oauth"></a>
# **discover_email_config_oauth**
> discover_email_config_oauth(self, discover_email_config_oauth_request)

Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.discover_email_config_oauth(
    DiscoverEmailConfigOauthRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**DiscoverEmailConfigOauth**](DiscoverEmailConfigOauth.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config_oauth_async"></a>
# **discover_email_config_oauth_async**
> discover_email_config_oauth_async(self, discover_email_config_oauth_request)

Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
discover_email_config_oauth_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.discover_email_config_oauth_async(
    DiscoverEmailConfigOauthRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**DiscoverEmailConfigOauth**](DiscoverEmailConfigOauth.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config_password"></a>
# **discover_email_config_password**
> discover_email_config_password(self, discover_email_config_password_request)

Discover email accounts by email address. Validates discovered accounts using login and password.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.discover_email_config_password(
    DiscoverEmailConfigPasswordRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**DiscoverEmailConfigPassword**](DiscoverEmailConfigPassword.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="discover_email_config_password_async"></a>
# **discover_email_config_password_async**
> discover_email_config_password_async(self, discover_email_config_password_request)

Discover email accounts by email address. Validates discovered accounts using login and password.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
discover_email_config_password_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.discover_email_config_password_async(
    DiscoverEmailConfigPasswordRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**DiscoverEmailConfigPassword**](DiscoverEmailConfigPassword.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="download_file"></a>
# **download_file**
> download_file(self, download_file_request)

Download file

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.download_file(
    DownloadFileRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="download_file_async"></a>
# **download_file_async**
> download_file_async(self, download_file_request)

Download file

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
download_file_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.download_file_async(
    DownloadFileRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="fetch_email_message"></a>
# **fetch_email_message**
> fetch_email_message(self, fetch_email_message_request)

Fetch message mime from email account             

### Return type

[**MimeResponse**](MimeResponse.md)

### Request Parameters
```python
__init__(self, 
    message_id, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder)
```

### Usage
```python
EmailApi.fetch_email_message(
    FetchEmailMessageRequest(
        message_id, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message identifier | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="fetch_email_message_async"></a>
# **fetch_email_message_async**
> fetch_email_message_async(self, fetch_email_message_request)

Fetch message mime from email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
fetch_email_message_async(request).get() returns [**MimeResponse**](MimeResponse.md)

### Request Parameters
```python
__init__(self, 
    message_id, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder)
```

### Usage
```python
EmailApi.fetch_email_message_async(
    FetchEmailMessageRequest(
        message_id, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message identifier | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="fetch_email_model"></a>
# **fetch_email_model**
> fetch_email_model(self, fetch_email_model_request)

Fetch message model from email account             

### Return type

[**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    message_id, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder)
```

### Usage
```python
EmailApi.fetch_email_model(
    FetchEmailModelRequest(
        message_id, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message identifier | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="fetch_email_model_async"></a>
# **fetch_email_model_async**
> fetch_email_model_async(self, fetch_email_model_request)

Fetch message model from email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
fetch_email_model_async(request).get() returns [**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    message_id, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder)
```

### Usage
```python
EmailApi.fetch_email_model_async(
    FetchEmailModelRequest(
        message_id, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message identifier | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar"></a>
# **get_calendar**
> get_calendar(self, get_calendar_request)

Get calendar file properties             

### Return type

[**HierarchicalObject**](HierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar(
    GetCalendarRequest(
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_async"></a>
# **get_calendar_async**
> get_calendar_async(self, get_calendar_request)

Get calendar file properties             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_async(request).get() returns [**HierarchicalObject**](HierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_async(
    GetCalendarRequest(
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_attachment"></a>
# **get_calendar_attachment**
> get_calendar_attachment(self, get_calendar_attachment_request)

Get iCalendar document attachment by name             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_attachment(
    GetCalendarAttachmentRequest(
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_attachment_async"></a>
# **get_calendar_attachment_async**
> get_calendar_attachment_async(self, get_calendar_attachment_request)

Get iCalendar document attachment by name             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_attachment_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_attachment_async(
    GetCalendarAttachmentRequest(
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_list"></a>
# **get_calendar_list**
> get_calendar_list(self, get_calendar_list_request)

Get iCalendar files list in folder on storage             

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    items_per_page, 
    page_number, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_list(
    GetCalendarListRequest(
        folder, 
        items_per_page, 
        page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | 
 **items_per_page** | **int**| Count of items on page | 
 **page_number** | **int**| Page number | 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_list_async"></a>
# **get_calendar_list_async**
> get_calendar_list_async(self, get_calendar_list_request)

Get iCalendar files list in folder on storage             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_list_async(request).get() returns [**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    items_per_page, 
    page_number, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_list_async(
    GetCalendarListRequest(
        folder, 
        items_per_page, 
        page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | 
 **items_per_page** | **int**| Count of items on page | 
 **page_number** | **int**| Page number | 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model"></a>
# **get_calendar_model**
> get_calendar_model(self, get_calendar_model_request)

Get calendar file             

### Return type

[**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_model(
    GetCalendarModelRequest(
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model_async"></a>
# **get_calendar_model_async**
> get_calendar_model_async(self, get_calendar_model_request)

Get calendar file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_model_async(request).get() returns [**CalendarDto**](CalendarDto.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_model_async(
    GetCalendarModelRequest(
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model_as_alternate"></a>
# **get_calendar_model_as_alternate**
> get_calendar_model_as_alternate(self, get_calendar_model_as_alternate_request)

Get iCalendar from storage as AlternateView             

### Return type

[**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    name, 
    calendar_action, 
    sequence_id=sequence_id, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_model_as_alternate(
    GetCalendarModelAsAlternateRequest(
        name, 
        calendar_action, 
        sequence_id=sequence_id, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **calendar_action** | **str**| iCalendar method type Enum, available values: Create, Update, Cancel | 
 **sequence_id** | **str**| The sequence id | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model_as_alternate_async"></a>
# **get_calendar_model_as_alternate_async**
> get_calendar_model_as_alternate_async(self, get_calendar_model_as_alternate_request)

Get iCalendar from storage as AlternateView             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_model_as_alternate_async(request).get() returns [**AlternateView**](AlternateView.md)

### Request Parameters
```python
__init__(self, 
    name, 
    calendar_action, 
    sequence_id=sequence_id, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_calendar_model_as_alternate_async(
    GetCalendarModelAsAlternateRequest(
        name, 
        calendar_action, 
        sequence_id=sequence_id, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **calendar_action** | **str**| iCalendar method type Enum, available values: Create, Update, Cancel | 
 **sequence_id** | **str**| The sequence id | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model_list"></a>
# **get_calendar_model_list**
> get_calendar_model_list(self, get_calendar_model_list_request)

Get iCalendar list from storage folder             

### Return type

[**CalendarDtoList**](CalendarDtoList.md)

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
EmailApi.get_calendar_model_list(
    GetCalendarModelListRequest(
        folder, 
        items_per_page=items_per_page, 
        page_number=page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_model_list_async"></a>
# **get_calendar_model_list_async**
> get_calendar_model_list_async(self, get_calendar_model_list_request)

Get iCalendar list from storage folder             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_calendar_model_list_async(request).get() returns [**CalendarDtoList**](CalendarDtoList.md)

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
EmailApi.get_calendar_model_list_async(
    GetCalendarModelListRequest(
        folder, 
        items_per_page=items_per_page, 
        page_number=page_number, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_attachment"></a>
# **get_contact_attachment**
> get_contact_attachment(self, get_contact_attachment_request)

Get attachment file by name             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_contact_attachment(
    GetContactAttachmentRequest(
        format, 
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_attachment_async"></a>
# **get_contact_attachment_async**
> get_contact_attachment_async(self, get_contact_attachment_request)

Get attachment file by name             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_contact_attachment_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_contact_attachment_async(
    GetContactAttachmentRequest(
        format, 
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
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
EmailApi.get_contact_list(
    GetContactListRequest(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_list_async"></a>
# **get_contact_list_async**
> get_contact_list_async(self, get_contact_list_request)

Get contact list from storage folder             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_contact_list_async(request).get() returns [**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

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
EmailApi.get_contact_list_async(
    GetContactListRequest(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 
 **items_per_page** | **int**| Count of items on page | [optional] [default to 10]
 **page_number** | **int**| Page number | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_model"></a>
# **get_contact_model**
> get_contact_model(self, get_contact_model_request)

Get contact document.             

### Return type

[**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_contact_model(
    GetContactModelRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_model_async"></a>
# **get_contact_model_async**
> get_contact_model_async(self, get_contact_model_request)

Get contact document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_contact_model_async(request).get() returns [**ContactDto**](ContactDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_contact_model_async(
    GetContactModelRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_model_list"></a>
# **get_contact_model_list**
> get_contact_model_list(self, get_contact_model_list_request)

Get contact list from storage folder.             

### Return type

[**ContactDtoList**](ContactDtoList.md)

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
EmailApi.get_contact_model_list(
    GetContactModelListRequest(
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

<a name="get_contact_model_list_async"></a>
# **get_contact_model_list_async**
> get_contact_model_list_async(self, get_contact_model_list_request)

Get contact list from storage folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_contact_model_list_async(request).get() returns [**ContactDtoList**](ContactDtoList.md)

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
EmailApi.get_contact_model_list_async(
    GetContactModelListRequest(
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

<a name="get_contact_properties"></a>
# **get_contact_properties**
> get_contact_properties(self, get_contact_properties_request)

Get contact document properties             

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

### Usage
```python
EmailApi.get_contact_properties(
    GetContactPropertiesRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_contact_properties_async"></a>
# **get_contact_properties_async**
> get_contact_properties_async(self, get_contact_properties_request)

Get contact document properties             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_contact_properties_async(request).get() returns [**HierarchicalObject**](HierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_contact_properties_async(
    GetContactPropertiesRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_disc_usage"></a>
# **get_disc_usage**
> get_disc_usage(self, get_disc_usage_request)

Get disc usage

### Return type

[**DiscUsage**](DiscUsage.md)

### Request Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_disc_usage(
    GetDiscUsageRequest(
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_disc_usage_async"></a>
# **get_disc_usage_async**
> get_disc_usage_async(self, get_disc_usage_request)

Get disc usage

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_disc_usage_async(request).get() returns [**DiscUsage**](DiscUsage.md)

### Request Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_disc_usage_async(
    GetDiscUsageRequest(
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email"></a>
# **get_email**
> get_email(self, get_email_request)

Get email document             

### Return type

[**EmailDocument**](EmailDocument.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
EmailApi.get_email(
    GetEmailRequest(
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_async"></a>
# **get_email_async**
> get_email_async(self, get_email_request)

Get email document             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_async(request).get() returns [**EmailDocument**](EmailDocument.md)

### Request Parameters
```python
__init__(self, 
    file_name, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
EmailApi.get_email_async(
    GetEmailRequest(
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name in storage | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_as_file"></a>
# **get_email_as_file**
> get_email_as_file(self, get_email_as_file_request)

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
EmailApi.get_email_as_file(
    GetEmailAsFileRequest(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name | 
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_as_file_async"></a>
# **get_email_as_file_async**
> get_email_as_file_async(self, get_email_as_file_request)

Converts email document from storage to specified format and returns as file             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_as_file_async(request).get() returns **file**

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
EmailApi.get_email_as_file_async(
    GetEmailAsFileRequest(
        file_name, 
        format, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Email document file name | 
 **format** | **str**| File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_attachment"></a>
# **get_email_attachment**
> get_email_attachment(self, get_email_attachment_request)

Get email attachment by name             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    attachment, 
    file_name, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
EmailApi.get_email_attachment(
    GetEmailAttachmentRequest(
        attachment, 
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **str**| Attachment name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_attachment_async"></a>
# **get_email_attachment_async**
> get_email_attachment_async(self, get_email_attachment_request)

Get email attachment by name             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_attachment_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    attachment, 
    file_name, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
EmailApi.get_email_attachment_async(
    GetEmailAttachmentRequest(
        attachment, 
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **str**| Attachment name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_model"></a>
# **get_email_model**
> get_email_model(self, get_email_model_request)

Get email document.             

### Return type

[**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_email_model(
    GetEmailModelRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **name** | **str**| Email document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_model_async"></a>
# **get_email_model_async**
> get_email_model_async(self, get_email_model_request)

Get email document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_model_async(request).get() returns [**EmailDto**](EmailDto.md)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_email_model_async(
    GetEmailModelRequest(
        format, 
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **name** | **str**| Email document file name. | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_model_list"></a>
# **get_email_model_list**
> get_email_model_list(self, get_email_model_list_request)

Get email list from storage folder.             

### Return type

[**EmailDtoList**](EmailDtoList.md)

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
EmailApi.get_email_model_list(
    GetEmailModelListRequest(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_model_list_async"></a>
# **get_email_model_list_async**
> get_email_model_list_async(self, get_email_model_list_request)

Get email list from storage folder.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_model_list_async(request).get() returns [**EmailDtoList**](EmailDtoList.md)

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
EmailApi.get_email_model_list_async(
    GetEmailModelListRequest(
        format, 
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **folder** | **str**| Path to folder in storage. | [optional] 
 **storage** | **str**| Storage name. | [optional] 
 **items_per_page** | **int**| Count of items on page. | [optional] [default to 10]
 **page_number** | **int**| Page number. | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_property"></a>
# **get_email_property**
> get_email_property(self, get_email_property_request)

Get an email document property by its name             

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

### Usage
```python
EmailApi.get_email_property(
    GetEmailPropertyRequest(
        property_name, 
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_email_property_async"></a>
# **get_email_property_async**
> get_email_property_async(self, get_email_property_request)

Get an email document property by its name             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_email_property_async(request).get() returns [**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    property_name, 
    file_name, 
    storage=storage, 
    folder=folder)
```

### Usage
```python
EmailApi.get_email_property_async(
    GetEmailPropertyRequest(
        property_name, 
        file_name, 
        storage=storage, 
        folder=folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name | 
 **file_name** | **str**| Email document file name | 
 **storage** | **str**| Storage name | [optional] 
 **folder** | **str**| Path to folder in storage | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_file_versions"></a>
# **get_file_versions**
> get_file_versions(self, get_file_versions_request)

Get file versions

### Return type

[**FileVersions**](FileVersions.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_file_versions(
    GetFileVersionsRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_file_versions_async"></a>
# **get_file_versions_async**
> get_file_versions_async(self, get_file_versions_request)

Get file versions

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_file_versions_async(request).get() returns [**FileVersions**](FileVersions.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_file_versions_async(
    GetFileVersionsRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_files_list"></a>
# **get_files_list**
> get_files_list(self, get_files_list_request)

Get all files and folders within a folder

### Return type

[**FilesList**](FilesList.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_files_list(
    GetFilesListRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_files_list_async"></a>
# **get_files_list_async**
> get_files_list_async(self, get_files_list_request)

Get all files and folders within a folder

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
get_files_list_async(request).get() returns [**FilesList**](FilesList.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.get_files_list_async(
    GetFilesListRequest(
        path, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_mapi_attachment"></a>
# **get_mapi_attachment**
> get_mapi_attachment(self, get_mapi_attachment_request)

Get document attachment as file stream             

### Return type

**file**

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_mapi_attachment(
    GetMapiAttachmentRequest(
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
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

Returns multiprocessing.pool.AsyncResult.
get_mapi_attachment_async(request).get() returns **file**

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_mapi_attachment_async(
    GetMapiAttachmentRequest(
        name, 
        attachment, 
        folder=folder, 
        storage=storage))
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

### Usage
```python
EmailApi.get_mapi_attachments(
    GetMapiAttachmentsRequest(
        name, 
        folder=folder, 
        storage=storage))
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

Returns multiprocessing.pool.AsyncResult.
get_mapi_attachments_async(request).get() returns [**ListResponseOfString**](ListResponseOfString.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_mapi_attachments_async(
    GetMapiAttachmentsRequest(
        name, 
        folder=folder, 
        storage=storage))
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

### Usage
```python
EmailApi.get_mapi_list(
    GetMapiListRequest(
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
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

Returns multiprocessing.pool.AsyncResult.
get_mapi_list_async(request).get() returns [**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder=folder, 
    storage=storage, 
    items_per_page=items_per_page, 
    page_number=page_number)
```

### Usage
```python
EmailApi.get_mapi_list_async(
    GetMapiListRequest(
        folder=folder, 
        storage=storage, 
        items_per_page=items_per_page, 
        page_number=page_number))
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

### Usage
```python
EmailApi.get_mapi_properties(
    GetMapiPropertiesRequest(
        name, 
        folder=folder, 
        storage=storage))
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

Returns multiprocessing.pool.AsyncResult.
get_mapi_properties_async(request).get() returns [**HierarchicalObjectResponse**](HierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

### Usage
```python
EmailApi.get_mapi_properties_async(
    GetMapiPropertiesRequest(
        name, 
        folder=folder, 
        storage=storage))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="is_email_address_disposable"></a>
# **is_email_address_disposable**
> is_email_address_disposable(self, is_email_address_disposable_request)

Check email address is disposable             

### Return type

[**ValueTOfBoolean**](ValueTOfBoolean.md)

### Request Parameters
```python
__init__(self, 
    address)
```

### Usage
```python
EmailApi.is_email_address_disposable(
    IsEmailAddressDisposableRequest(
        address))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| An email address to check | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="is_email_address_disposable_async"></a>
# **is_email_address_disposable_async**
> is_email_address_disposable_async(self, is_email_address_disposable_request)

Check email address is disposable             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
is_email_address_disposable_async(request).get() returns [**ValueTOfBoolean**](ValueTOfBoolean.md)

### Request Parameters
```python
__init__(self, 
    address)
```

### Usage
```python
EmailApi.is_email_address_disposable_async(
    IsEmailAddressDisposableRequest(
        address))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| An email address to check | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_folders"></a>
# **list_email_folders**
> list_email_folders(self, list_email_folders_request)

Get folders list in email account             

### Return type

[**ListResponseOfMailServerFolder**](ListResponseOfMailServerFolder.md)

### Request Parameters
```python
__init__(self, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    parent_folder=parent_folder)
```

### Usage
```python
EmailApi.list_email_folders(
    ListEmailFoldersRequest(
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        parent_folder=parent_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **parent_folder** | **str**| Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_folders_async"></a>
# **list_email_folders_async**
> list_email_folders_async(self, list_email_folders_request)

Get folders list in email account             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
list_email_folders_async(request).get() returns [**ListResponseOfMailServerFolder**](ListResponseOfMailServerFolder.md)

### Request Parameters
```python
__init__(self, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    parent_folder=parent_folder)
```

### Usage
```python
EmailApi.list_email_folders_async(
    ListEmailFoldersRequest(
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        parent_folder=parent_folder))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **parent_folder** | **str**| Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_messages"></a>
# **list_email_messages**
> list_email_messages(self, list_email_messages_request)

Get messages from folder, filtered by query             

The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

### Return type

[**ListResponseOfString**](ListResponseOfString.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    query_string, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    recursive=recursive)
```

### Usage
```python
EmailApi.list_email_messages(
    ListEmailMessagesRequest(
        folder, 
        query_string, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account | 
 **query_string** | **str**| A MailQuery search string | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **recursive** | **bool**| Specifies that should message be searched in subfolders recursively | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_messages_async"></a>
# **list_email_messages_async**
> list_email_messages_async(self, list_email_messages_request)

Get messages from folder, filtered by query             

Performs operation asynchronously.

The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

### Return type

Returns multiprocessing.pool.AsyncResult.
list_email_messages_async(request).get() returns [**ListResponseOfString**](ListResponseOfString.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    query_string, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    recursive=recursive)
```

### Usage
```python
EmailApi.list_email_messages_async(
    ListEmailMessagesRequest(
        folder, 
        query_string, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account | 
 **query_string** | **str**| A MailQuery search string | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **recursive** | **bool**| Specifies that should message be searched in subfolders recursively | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_models"></a>
# **list_email_models**
> list_email_models(self, list_email_models_request)

Get messages from folder, filtered by query             

The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

### Return type

[**ListResponseOfEmailDto**](ListResponseOfEmailDto.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    query_string, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    recursive=recursive)
```

### Usage
```python
EmailApi.list_email_models(
    ListEmailModelsRequest(
        folder, 
        query_string, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account | 
 **query_string** | **str**| A MailQuery search string | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **recursive** | **bool**| Specifies that should message be searched in subfolders recursively | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_models_async"></a>
# **list_email_models_async**
> list_email_models_async(self, list_email_models_request)

Get messages from folder, filtered by query             

Performs operation asynchronously.

The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

### Return type

Returns multiprocessing.pool.AsyncResult.
list_email_models_async(request).get() returns [**ListResponseOfEmailDto**](ListResponseOfEmailDto.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    query_string, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    recursive=recursive)
```

### Usage
```python
EmailApi.list_email_models_async(
    ListEmailModelsRequest(
        folder, 
        query_string, 
        first_account, 
        second_account=second_account, 
        storage=storage, 
        storage_folder=storage_folder, 
        recursive=recursive))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account | 
 **query_string** | **str**| A MailQuery search string | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)              | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **recursive** | **bool**| Specifies that should message be searched in subfolders recursively | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_file"></a>
# **move_file**
> move_file(self, move_file_request)

Move file

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.move_file(
    MoveFileRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_file_async"></a>
# **move_file_async**
> move_file_async(self, move_file_request)

Move file

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
move_file_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.move_file_async(
    MoveFileRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_folder"></a>
# **move_folder**
> move_folder(self, move_folder_request)

Move folder

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

### Usage
```python
EmailApi.move_folder(
    MoveFolderRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="move_folder_async"></a>
# **move_folder_async**
> move_folder_async(self, move_folder_request)

Move folder

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
move_folder_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

### Usage
```python
EmailApi.move_folder_async(
    MoveFolderRequest(
        src_path, 
        dest_path, 
        src_storage_name=src_storage_name, 
        dest_storage_name=dest_storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="object_exists"></a>
# **object_exists**
> object_exists(self, object_exists_request)

Check if file or folder exists

### Return type

[**ObjectExist**](ObjectExist.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.object_exists(
    ObjectExistsRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="object_exists_async"></a>
# **object_exists_async**
> object_exists_async(self, object_exists_request)

Check if file or folder exists

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
object_exists_async(request).get() returns [**ObjectExist**](ObjectExist.md)

### Request Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

### Usage
```python
EmailApi.object_exists_async(
    ObjectExistsRequest(
        path, 
        storage_name=storage_name, 
        version_id=version_id))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_calendar_model"></a>
# **save_calendar_model**
> save_calendar_model(self, save_calendar_model_request)

Save iCalendar             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_calendar_model(
    SaveCalendarModelRequest(
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **rq** | [**StorageModelRqOfCalendarDto**](StorageModelRqOfCalendarDto.md)| Calendar properties update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_calendar_model_async"></a>
# **save_calendar_model_async**
> save_calendar_model_async(self, save_calendar_model_request)

Save iCalendar             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
save_calendar_model_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_calendar_model_async(
    SaveCalendarModelRequest(
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **rq** | [**StorageModelRqOfCalendarDto**](StorageModelRqOfCalendarDto.md)| Calendar properties update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_contact_model"></a>
# **save_contact_model**
> save_contact_model(self, save_contact_model_request)

Save contact.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_contact_model(
    SaveContactModelRequest(
        format, 
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name. | 
 **rq** | [**StorageModelRqOfContactDto**](StorageModelRqOfContactDto.md)| Create contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_contact_model_async"></a>
# **save_contact_model_async**
> save_contact_model_async(self, save_contact_model_request)

Save contact.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
save_contact_model_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_contact_model_async(
    SaveContactModelRequest(
        format, 
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format. Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name. | 
 **rq** | [**StorageModelRqOfContactDto**](StorageModelRqOfContactDto.md)| Create contact request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_email_model"></a>
# **save_email_model**
> save_email_model(self, save_email_model_request)

Save email document.             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_email_model(
    SaveEmailModelRequest(
        format, 
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **name** | **str**| iCalendar file name in storage. | 
 **rq** | [**StorageModelRqOfEmailDto**](StorageModelRqOfEmailDto.md)| Calendar properties update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_email_model_async"></a>
# **save_email_model_async**
> save_email_model_async(self, save_email_model_request)

Save email document.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
save_email_model_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    rq)
```

### Usage
```python
EmailApi.save_email_model_async(
    SaveEmailModelRequest(
        format, 
        name, 
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| File format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html | 
 **name** | **str**| iCalendar file name in storage. | 
 **rq** | [**StorageModelRqOfEmailDto**](StorageModelRqOfEmailDto.md)| Calendar properties update request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_account"></a>
# **save_mail_account**
> save_mail_account(self, save_mail_account_request)

Create email account file (*.account) with login/password authentication             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.save_mail_account(
    SaveMailAccountRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveEmailAccountRequest**](SaveEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_account_async"></a>
# **save_mail_account_async**
> save_mail_account_async(self, save_mail_account_request)

Create email account file (*.account) with login/password authentication             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
save_mail_account_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.save_mail_account_async(
    SaveMailAccountRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveEmailAccountRequest**](SaveEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_o_auth_account"></a>
# **save_mail_o_auth_account**
> save_mail_o_auth_account(self, save_mail_o_auth_account_request)

Create email account file (*.account) with OAuth             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.save_mail_o_auth_account(
    SaveMailOAuthAccountRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveOAuthEmailAccountRequest**](SaveOAuthEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_o_auth_account_async"></a>
# **save_mail_o_auth_account_async**
> save_mail_o_auth_account_async(self, save_mail_o_auth_account_request)

Create email account file (*.account) with OAuth             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
save_mail_o_auth_account_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.save_mail_o_auth_account_async(
    SaveMailOAuthAccountRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveOAuthEmailAccountRequest**](SaveOAuthEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email"></a>
# **send_email**
> send_email(self, send_email_request)

Send an email from *.eml file located on storage             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.send_email(
    SendEmailRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailBaseRequest**](SendEmailBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_async"></a>
# **send_email_async**
> send_email_async(self, send_email_request)

Send an email from *.eml file located on storage             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
send_email_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.send_email_async(
    SendEmailRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailBaseRequest**](SendEmailBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_mime"></a>
# **send_email_mime**
> send_email_mime(self, send_email_mime_request)

Send an email specified by MIME in request             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.send_email_mime(
    SendEmailMimeRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailMimeBaseRequest**](SendEmailMimeBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_mime_async"></a>
# **send_email_mime_async**
> send_email_mime_async(self, send_email_mime_request)

Send an email specified by MIME in request             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
send_email_mime_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.send_email_mime_async(
    SendEmailMimeRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailMimeBaseRequest**](SendEmailMimeBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_model"></a>
# **send_email_model**
> send_email_model(self, send_email_model_request)

Send an email specified by model in request             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.send_email_model(
    SendEmailModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**SendEmailModelRq**](SendEmailModelRq.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_model_async"></a>
# **send_email_model_async**
> send_email_model_async(self, send_email_model_request)

Send an email specified by model in request             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
send_email_model_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    rq)
```

### Usage
```python
EmailApi.send_email_model_async(
    SendEmailModelRequest(
        rq))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rq** | [**SendEmailModelRq**](SendEmailModelRq.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_property"></a>
# **set_email_property**
> set_email_property(self, set_email_property_request)

Set email document property value             

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    property_name, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.set_email_property(
    SetEmailPropertyRequest(
        property_name, 
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name that should be changed | 
 **file_name** | **str**| Email document file name | 
 **request** | [**SetEmailPropertyRequest**](SetEmailPropertyRequest.md)| A property that should be changed and optional Storage info to specify where the file located              | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_property_async"></a>
# **set_email_property_async**
> set_email_property_async(self, set_email_property_request)

Set email document property value             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
set_email_property_async(request).get() returns [**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    property_name, 
    file_name, 
    request)
```

### Usage
```python
EmailApi.set_email_property_async(
    SetEmailPropertyRequest(
        property_name, 
        file_name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **str**| A property name that should be changed | 
 **file_name** | **str**| Email document file name | 
 **request** | [**SetEmailPropertyRequest**](SetEmailPropertyRequest.md)| A property that should be changed and optional Storage info to specify where the file located              | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_read_flag"></a>
# **set_email_read_flag**
> set_email_read_flag(self, set_email_read_flag_request)

Sets \"Message is read\" flag             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.set_email_read_flag(
    SetEmailReadFlagRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetMessageReadFlagAccountBaseRequest**](SetMessageReadFlagAccountBaseRequest.md)| Message is read request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_read_flag_async"></a>
# **set_email_read_flag_async**
> set_email_read_flag_async(self, set_email_read_flag_request)

Sets \"Message is read\" flag             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
set_email_read_flag_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailApi.set_email_read_flag_async(
    SetEmailReadFlagRequest(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetMessageReadFlagAccountBaseRequest**](SetMessageReadFlagAccountBaseRequest.md)| Message is read request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="storage_exists"></a>
# **storage_exists**
> storage_exists(self, storage_exists_request)

Check if storage exists

### Return type

[**StorageExist**](StorageExist.md)

### Request Parameters
```python
__init__(self, 
    storage_name)
```

### Usage
```python
EmailApi.storage_exists(
    StorageExistsRequest(
        storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="storage_exists_async"></a>
# **storage_exists_async**
> storage_exists_async(self, storage_exists_request)

Check if storage exists

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
storage_exists_async(request).get() returns [**StorageExist**](StorageExist.md)

### Request Parameters
```python
__init__(self, 
    storage_name)
```

### Usage
```python
EmailApi.storage_exists_async(
    StorageExistsRequest(
        storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_calendar_properties"></a>
# **update_calendar_properties**
> update_calendar_properties(self, update_calendar_properties_request)

Update calendar file properties             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.update_calendar_properties(
    UpdateCalendarPropertiesRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Calendar properties update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_calendar_properties_async"></a>
# **update_calendar_properties_async**
> update_calendar_properties_async(self, update_calendar_properties_request)

Update calendar file properties             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
update_calendar_properties_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.update_calendar_properties_async(
    UpdateCalendarPropertiesRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Calendar properties update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_contact_properties"></a>
# **update_contact_properties**
> update_contact_properties(self, update_contact_properties_request)

Update contact document properties             

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

### Usage
```python
EmailApi.update_contact_properties(
    UpdateContactPropertiesRequest(
        format, 
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_contact_properties_async"></a>
# **update_contact_properties_async**
> update_contact_properties_async(self, update_contact_properties_request)

Update contact document properties             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
update_contact_properties_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    format, 
    name, 
    request)
```

### Usage
```python
EmailApi.update_contact_properties_async(
    UpdateContactPropertiesRequest(
        format, 
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Contact document format Enum, available values: VCard, WebDav, Msg | 
 **name** | **str**| Contact document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

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

### Usage
```python
EmailApi.update_mapi_properties(
    UpdateMapiPropertiesRequest(
        name, 
        request))
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

Returns multiprocessing.pool.AsyncResult.
update_mapi_properties_async(request).get() returns void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

### Usage
```python
EmailApi.update_mapi_properties_async(
    UpdateMapiPropertiesRequest(
        name, 
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document file name | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Properties that should be updated/added | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="upload_file"></a>
# **upload_file**
> upload_file(self, upload_file_request)

Upload file

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Request Parameters
```python
__init__(self, 
    path, 
    file, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.upload_file(
    UploadFileRequest(
        path, 
        file, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="upload_file_async"></a>
# **upload_file_async**
> upload_file_async(self, upload_file_request)

Upload file

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
upload_file_async(request).get() returns [**FilesUploadResult**](FilesUploadResult.md)

### Request Parameters
```python
__init__(self, 
    path, 
    file, 
    storage_name=storage_name)
```

### Usage
```python
EmailApi.upload_file_async(
    UploadFileRequest(
        path, 
        file, 
        storage_name=storage_name))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

