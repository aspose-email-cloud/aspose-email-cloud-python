# AsposeEmailCloudSdk.models.AiNameMatchParsedRequest

Two parsed names to match request             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other_parsed_name** |[**list[AiNameComponent]**](AiNameComponent.md) |Other parsed name to match              |

Parent class: [AiNameParsedRequest](AiNameParsedRequest.md)


## Example
```python
ai_name_match_parsed_request = models.AiNameMatchParsedRequest(
    other_parsed_name=[
        models.AiNameComponent(
            value='J',
            category='FirstInitial',
            score=1),
        models.AiNameComponent(
            value='Cane',
            category='LastName',
            score=0.5,
            position=3),
        models.AiNameComponent(
            value='%f%L',
            category='Format'),
        models.AiNameComponent(
            value='0.5',
            category='Score',
            score=0.5)],
    parsed_name=[
        models.AiNameComponent(
            value='John',
            category='FirstName',
            score=0.95),
        models.AiNameComponent(
            value='Cane',
            category='LastName',
            score=0.5,
            position=5),
        models.AiNameComponent(
            value='%F%L',
            category='Format'),
        models.AiNameComponent(
            value='0.5',
            category='Score',
            score=0.5)])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

