# AsposeEmailCloudSdk.models.AiNameMatchResult

Two names match result             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**similarity** |**float** |Similarity score              |
**mismatches** |[**list[AiNameMismatch]**](AiNameMismatch.md) |Detailed description of mismatches              |[optional] 



## Example
```python
ai_name_match_result = models.AiNameMatchResult(
    similarity=0.6,
    mismatches=[
        models.AiNameMismatch(
            category='Gender',
            explanation='no_match')])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

