# AsposeEmailCloudSdk.models.EmailConfigDiscoverOauthRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** |**str** |OAuth client id.              |
**client_secret** |**str** |OAuth client secret.              |
**refresh_token** |**str** |OAuth refresh token.              |
**request_url** |**str** |The url to obtain access token. If not specified, will be discovered from email configuration.              |[optional] 

Parent class: [DiscoverEmailConfigRequest](DiscoverEmailConfigRequest.md)


## Example
```python
email_config_discover_oauth_request = models.EmailConfigDiscoverOauthRequest(
    client_id='ClientId',
    client_secret='ClientSecret',
    refresh_token='RefreshToken',
    address='example@aspose.com',
    fast_processing=True)
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

