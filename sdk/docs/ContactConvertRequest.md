# ContactConvertRequest

Request model for ContactApi.convert

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**to_format** |**str** |File format to convert to Enum, available values: VCard, WebDav, Msg |
**from_format** |**str** |File format to convert from Enum, available values: VCard, WebDav, Msg |
**file** |**str** |File to convert |

## Example
```python
request = models.ContactConvertRequest(
    to_format='VCard',
    from_format='Msg',
    file='/path/to/contact.msg')
```
