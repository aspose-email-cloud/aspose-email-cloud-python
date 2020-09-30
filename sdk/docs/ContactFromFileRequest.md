# ContactFromFileRequest

Request model for ContactApi.from_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |File format Enum, available values: VCard, WebDav, Msg |
**file** |**str** |File to convert |

## Example
```python
request = models.ContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')
```
