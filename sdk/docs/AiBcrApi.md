
# AsposeEmailCloudSdk.AiBcrApi

        
<a name="parse"></a>
# parse

```python
parse(self, request: AiBcrParseRequest)
```

Parse images to vCard document models             

### Return type

ContactList

### request Parameter
```python
AiBcrParseRequest(
    file,
    countries,
    languages,
    is_single)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str** | File to parse | 
 **countries** | **str** | Comma-separated codes of countries. | [optional] [default to ]
 **languages** | **str** | Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \&quot;it\&quot; or \&quot;ita\&quot; for Italian); it&#39;s \&quot;\&quot; by default.              | [optional] [default to ]
 **is_single** | **bool** | Determines that image contains single VCard or more. | [optional] [default to true]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="parse_storage"></a>
# parse_storage

```python
parse_storage(self, AiBcrParseStorageRequest request)
```

Parse images from storage to vCard files             

### Return type

[**StorageFileLocationList**](StorageFileLocationList.md)

### request Parameter

See parameter model documentation at [AiBcrParseStorageRequest](AiBcrParseStorageRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

