# AsposeEmailCloudSdk.models.AiNameParsedRequest

Parsed name request model             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cultural_context** |[**AiNameCulturalContext**](AiNameCulturalContext.md) |AiName parser cultural context              |[optional] 
**format** |**str** |Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (&#x3D; &#39;%t%F%m%N%L%p&#39;)     /format/FN+LN/ (&#x3D; &#39;%F%L&#39;)     /format/title+FN+LN/ (&#x3D; &#39;%t%F%L&#39;)     /format/FN+MN+LN/ (&#x3D; &#39;%F%M%N%L&#39;)     /format/title+FN+MN+LN/ (&#x3D; &#39;%t%F%M%N%L&#39;)     /format/FN+MI+LN/ (&#x3D; &#39;%F%m%N%L&#39;)     /format/title+FN+MI+LN/ (&#x3D; &#39;%t%F%m%N%L&#39;)     /format/LN/ (&#x3D; &#39;%L&#39;)     /format/title+LN/ (&#x3D; &#39;%t%L&#39;)     /format/LN+FN+MN/ (&#x3D; &#39;%L,%F%M%N&#39;)     /format/LN+title+FN+MN/ (&#x3D; &#39;%L,%t%F%M%N&#39;)     /format/LN+FN+MI/ (&#x3D; &#39;%L,%F%m%N&#39;)     /format/LN+title+FN+MI/ (&#x3D; &#39;%L,%t%F%m%N&#39;)  Custom format string - custom combination of characters and the next term placeholders:      &#39;%t&#39; - Title (prefix)     &#39;%F&#39; - First name     &#39;%f&#39; - First initial     &#39;%M&#39; - Middle name(s)     &#39;%m&#39; - Middle initial(s)     &#39;%N&#39; - Nickname     &#39;%L&#39; - Last name     &#39;%l&#39; - Last initial     &#39;%p&#39; - Postfix  If no value for format option was provided, its default value is &#39;%t%F%m%N%L%p&#39;              |[optional] 
**parsed_name** |[**list[AiNameComponent]**](AiNameComponent.md) |Parsed name              |



## Example
```python
ai_name_parsed_request = models.AiNameParsedRequest(
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

