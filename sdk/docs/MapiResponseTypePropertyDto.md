# AsposeEmailCloudSdk.models.MapiResponseTypePropertyDto

Mapi property with response type value             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** |**str** |Represents the types of recipient responses that are received for a meeting. Enum, available values: Unknown, Organizer, Tentative, Accept, Decline, NoResponseReceived |

Parent class: [MapiPropertyDto](MapiPropertyDto.md)


## Example
```python
mapi_response_type_property_dto = models.MapiResponseTypePropertyDto(
    value='Accept',
    descriptor=models.MapiKnownPropertyDescriptor(
        name='ResponseStatus'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

