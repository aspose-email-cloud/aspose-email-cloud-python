# AsposeEmailCloudSdk.models.AiNameWeightedVariants

Name variants             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** |[**list[AiNameWeighted]**](AiNameWeighted.md) |List of name variations              |[optional] 
**comments** |**str** |Usually empty; can contain extra message describing some issue occurred during processing              |[optional] 



## Example
```python
ai_name_weighted_variants = models.AiNameWeightedVariants(
    names=[
        models.AiNameWeighted(
            name='J. Cane',
            score=1),
        models.AiNameWeighted(
            name='Mr. Cane',
            score=0.75)])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

