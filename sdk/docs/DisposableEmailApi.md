# AsposeEmailCloudSdk.DisposableEmailApi

<a name="disposable_email_is_disposable"></a>
# **disposable_email_is_disposable**
> disposable_email_is_disposable(self, disposable_email_is_disposable_request)

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
DisposableEmailApi.disposable_email_is_disposable(
    cakePrefix_disposable_email_is_disposable_request_cakeCodePostProcessor(
        address))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| An email address to check | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="disposable_email_is_disposable_async"></a>
# **disposable_email_is_disposable_async**
> disposable_email_is_disposable_async(self, disposable_email_is_disposable_request)

Check email address is disposable             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
disposable_email_is_disposable_async(request).get() returns [**ValueTOfBoolean**](ValueTOfBoolean.md)

### Request Parameters
```python
__init__(self, 
    address)
```

### Usage
```python
DisposableEmailApi.disposable_email_is_disposable_async(
    cakePrefix_disposable_email_is_disposable_request_cakeCodePostProcessor(
        address))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| An email address to check | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

