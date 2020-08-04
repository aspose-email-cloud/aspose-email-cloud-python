
# AsposeEmailCloudSdk.EmailConfigApi

        
<a name="discover"></a>
# discover

```python
discover(self, request: EmailConfigDiscoverRequest)
```

Discover email accounts by email address. Does not validate discovered accounts.             

### Return type

EmailAccountConfigList

### request Parameter
```python
EmailConfigDiscoverRequest(
    address: str, 
    fast_processing: bool = None)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str** | Email address. | 
 **fast_processing** | **bool** | Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.              | [optional] [default to false]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="discover_oauth"></a>
# discover_oauth

```python
discover_oauth(self, DiscoverEmailConfigOauth request)
```

Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### request Parameter

See parameter model documentation at [DiscoverEmailConfigOauth](DiscoverEmailConfigOauth.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="discover_password"></a>
# discover_password

```python
discover_password(self, DiscoverEmailConfigPassword request)
```

Discover email accounts by email address. Validates discovered accounts using login and password.             

### Return type

[**EmailAccountConfigList**](EmailAccountConfigList.md)

### request Parameter

See parameter model documentation at [DiscoverEmailConfigPassword](DiscoverEmailConfigPassword.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

