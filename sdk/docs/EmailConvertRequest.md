# EmailConvertRequest

Request model for EmailApi.convert

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**from_format** |**str** |File format to convert to Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**to_format** |**str** |File format to convert from Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**file** |**str** |File to convert |

## Example
```python
request = models.EmailConvertRequest(
    from_format='Msg',
    to_format='Mhtml',
    file='/path/to/message.msg')
```
