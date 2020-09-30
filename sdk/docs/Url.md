# AsposeEmailCloudSdk.models.Url

Url and its category.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** |[**EnumWithCustomOfUrlCategory**](EnumWithCustomOfUrlCategory.md) |Url category.              |[optional] 
**preferred** |**bool** |Defines whether url is preferred.              |
**href** |**str** |URL.              |[optional] 



## Example
```python
url = models.Url(
    category=models.EnumWithCustom<UrlCategory>(
        value='Work'),
    preferred=True,
    href='https://products.aspose.cloud/email')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

