# AsposeEmailCloudSdk.models.AlternateView

Represents the format to view a message.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_uri** |**str** |Base URI.              |[optional] 
**linked_resources** |[**list[LinkedResource]**](LinkedResource.md) |Embedded resources referred to by this alternate view.              |[optional] 

Parent class: [AttachmentBase](AttachmentBase.md)


## Example
```python
alternate_view = models.AlternateView(
    base64_data='<File content represented as Base64 string>',
    content_id='fa7a8948-4af1-432a-b4d9-ee0c28542e75',
    content_type=models.ContentType(
        char_set='utf-8',
        media_type='text/calendar',
        name='meeting.ics',
        parameters=[
            models.ContentTypeParameter(
                name='Method',
                value='REQUEST'),
            models.ContentTypeParameter(
                name='Name',
                value='meeting.ics'),
            models.ContentTypeParameter(
                name='charset',
                value='utf-8')]))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

