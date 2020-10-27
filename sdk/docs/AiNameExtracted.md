# AsposeEmailCloudSdk.models.AiNameExtracted

Extracted name             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** |[**list[AiNameExtractedComponent]**](AiNameExtractedComponent.md) |Extracted name components              |[optional] 
**score** |**float** |Extracted name score              |



## Example
```python
ai_name_extracted = models.AiNameExtracted(
    name=[
        models.AiNameExtractedComponent(
            category='Surname',
            value='Cane'),
        models.AiNameExtractedComponent(
            category='SomeName',
            value='John')],
    score=0.5)
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

