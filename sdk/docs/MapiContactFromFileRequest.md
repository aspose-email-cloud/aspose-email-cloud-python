# MapiContactFromFileRequest

Request model for MapiContactApi.from_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |File format Enum, available values: VCard, WebDav, Msg |
**file** |**str** |File to convert |

## Example
```python
request = models.MapiContactFromFileRequest(
    format='Msg',
    file='/path/to/contact.msg')
```
