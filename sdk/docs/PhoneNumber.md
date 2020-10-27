# AsposeEmailCloudSdk.models.PhoneNumber

A phone number.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** |[**EnumWithCustomOfPhoneNumberCategory**](EnumWithCustomOfPhoneNumberCategory.md) |Phone number category.              |[optional] 
**number** |**str** |Phone number.              |[optional] 
**preferred** |**bool** |Defines whether phone number is preferred.              |



## Example
```python
phone_number = models.PhoneNumber(
    category=models.EnumWithCustomOfPhoneNumberCategory(
        value='Company'),
    number='+44 141 628 8900',
    preferred=True)
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

