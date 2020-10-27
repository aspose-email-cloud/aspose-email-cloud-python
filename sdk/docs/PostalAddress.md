# AsposeEmailCloudSdk.models.PostalAddress

A postal address             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** |**str** |Address.              |[optional] 
**category** |[**EnumWithCustomOfPostalAddressCategory**](EnumWithCustomOfPostalAddressCategory.md) |Address category.              |[optional] 
**city** |**str** |Address&#39;s city.              |[optional] 
**country** |**str** |Address&#39;s country.              |[optional] 
**country_code** |**str** |Country code.              |[optional] 
**is_mailing_address** |**bool** |Defines whether address may be used for mailing.              |
**postal_code** |**str** |Postal code.              |[optional] 
**post_office_box** |**str** |Post Office box.              |[optional] 
**preferred** |**bool** |Defines whether postal address is preferred.              |
**state_or_province** |**str** |Address&#39;s region.              |[optional] 
**street** |**str** |Address&#39;s street.              |[optional] 



## Example
```python
postal_address = models.PostalAddress(
    address='221b',
    category=models.EnumWithCustomOfPostalAddressCategory(
        ),
    city='London',
    country='United Kingdom',
    is_mailing_address=True,
    postal_code='NW1 6XE',
    preferred=True,
    street='Baker St')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

