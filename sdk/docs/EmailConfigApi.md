# AsposeEmailCloudSdk.EmailConfigApi

<a name="email_config_discover"></a>
# **email_config_discover**
> email_config_discover(self, email_config_discover_request)

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
EmailConfigApi.email_config_discover(
    cakePrefix_email_config_discover_request_cakeCodePostProcessor(
        address, 
        fast_processing=fast_processing))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Email address. | 
 **fast_processing** | **bool**| Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.              | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_config_discover_async"></a>
# **email_config_discover_async**
> email_config_discover_async(self, email_config_discover_request)

Discover email accounts by email address. Does not validate discovered accounts.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_config_discover_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    address, 
    fast_processing=fast_processing)
```

### Usage
```python
EmailConfigApi.email_config_discover_async(
    cakePrefix_email_config_discover_request_cakeCodePostProcessor(
        address, 
        fast_processing=fast_processing))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Email address. | 
 **fast_processing** | **bool**| Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.              | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_config_discover_oauth"></a>
# **email_config_discover_oauth**
> email_config_discover_oauth(self, email_config_discover_oauth_request)

Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailConfigApi.email_config_discover_oauth(
    cakePrefix_email_config_discover_oauth_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DiscoverEmailConfigOauth**](DiscoverEmailConfigOauth.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_config_discover_oauth_async"></a>
# **email_config_discover_oauth_async**
> email_config_discover_oauth_async(self, email_config_discover_oauth_request)

Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_config_discover_oauth_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailConfigApi.email_config_discover_oauth_async(
    cakePrefix_email_config_discover_oauth_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DiscoverEmailConfigOauth**](DiscoverEmailConfigOauth.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_config_discover_password"></a>
# **email_config_discover_password**
> email_config_discover_password(self, email_config_discover_password_request)

Discover email accounts by email address. Validates discovered accounts using login and password.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailConfigApi.email_config_discover_password(
    cakePrefix_email_config_discover_password_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DiscoverEmailConfigPassword**](DiscoverEmailConfigPassword.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="email_config_discover_password_async"></a>
# **email_config_discover_password_async**
> email_config_discover_password_async(self, email_config_discover_password_request)

Discover email accounts by email address. Validates discovered accounts using login and password.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
email_config_discover_password_async(request).get() returns [**EmailAccountConfigList**](EmailAccountConfigList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
EmailConfigApi.email_config_discover_password_async(
    cakePrefix_email_config_discover_password_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DiscoverEmailConfigPassword**](DiscoverEmailConfigPassword.md)| Discover email configuration request. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

