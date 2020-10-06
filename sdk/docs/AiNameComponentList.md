# AsposeEmailCloudSdk.models.AiNameComponentList

List of name components             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

Parent class: [ListResponseOfAiNameComponent](ListResponseOfAiNameComponent.md)


## Example
```python
ai_name_component_list = models.AiNameComponentList(
    value=[
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

