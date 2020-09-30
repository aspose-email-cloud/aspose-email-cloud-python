# MapiMessageFromFileRequest

Request model for MapiMessageApi.from_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |File format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**file** |**str** |File to convert |

## Example
```python
request = models.MapiMessageFromFileRequest(
    format='Msg',
    file='/path/to/message.msg')
```
