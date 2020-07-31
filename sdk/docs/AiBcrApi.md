# AsposeEmailCloudSdk.AiBcrApi

<a name="ai_bcr_parse"></a>
# **ai_bcr_parse**
> ai_bcr_parse(self, ai_bcr_parse_request)

Parse images to vCard document models             

### Return type

[**ContactList**](ContactList.md)

### Request Parameters
```python
__init__(self, 
    file, 
    countries=countries, 
    languages=languages, 
    is_single=is_single)
```

### Usage
```python
AiBcrApi.ai_bcr_parse(
    cakePrefix_ai_bcr_parse_request_cakeCodePostProcessor(
        file, 
        countries=countries, 
        languages=languages, 
        is_single=is_single))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to parse | 
 **countries** | **str**| Comma-separated codes of countries. | [optional] [default to ]
 **languages** | **str**| Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \&quot;it\&quot; or \&quot;ita\&quot; for Italian); it&#39;s \&quot;\&quot; by default.              | [optional] [default to ]
 **is_single** | **bool**| Determines that image contains single VCard or more. | [optional] [default to true]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_async"></a>
# **ai_bcr_parse_async**
> ai_bcr_parse_async(self, ai_bcr_parse_request)

Parse images to vCard document models             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_async(request).get() returns [**ContactList**](ContactList.md)

### Request Parameters
```python
__init__(self, 
    file, 
    countries=countries, 
    languages=languages, 
    is_single=is_single)
```

### Usage
```python
AiBcrApi.ai_bcr_parse_async(
    cakePrefix_ai_bcr_parse_request_cakeCodePostProcessor(
        file, 
        countries=countries, 
        languages=languages, 
        is_single=is_single))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to parse | 
 **countries** | **str**| Comma-separated codes of countries. | [optional] [default to ]
 **languages** | **str**| Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \&quot;it\&quot; or \&quot;ita\&quot; for Italian); it&#39;s \&quot;\&quot; by default.              | [optional] [default to ]
 **is_single** | **bool**| Determines that image contains single VCard or more. | [optional] [default to true]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_storage"></a>
# **ai_bcr_parse_storage**
> ai_bcr_parse_storage(self, ai_bcr_parse_storage_request)

Parse images from storage to vCard files             

### Return type

[**StorageFileLocationList**](StorageFileLocationList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiBcrApi.ai_bcr_parse_storage(
    cakePrefix_ai_bcr_parse_storage_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiBcrParseStorageRequest**](AiBcrParseStorageRequest.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_bcr_parse_storage_async"></a>
# **ai_bcr_parse_storage_async**
> ai_bcr_parse_storage_async(self, ai_bcr_parse_storage_request)

Parse images from storage to vCard files             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_bcr_parse_storage_async(request).get() returns [**StorageFileLocationList**](StorageFileLocationList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiBcrApi.ai_bcr_parse_storage_async(
    cakePrefix_ai_bcr_parse_storage_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiBcrParseStorageRequest**](AiBcrParseStorageRequest.md)| Request with images located on storage | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

