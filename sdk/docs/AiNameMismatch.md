# AsposeEmailCloudSdk.models.AiNameMismatch

Names mismatch detailed description             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** |**str** |Mismatch type. Enum, available values: Unknown, FirstName, MiddleName, MiddleLastName, MiddleNickname, Gender, Context |
**similarity** |**float** |Similarity score              |
**explanation** |**str** |Explanation or mismatch subtype              |[optional] 



## Example
```python
ai_name_mismatch = models.AiNameMismatch(
    category='Gender',
    explanation='no_match')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

