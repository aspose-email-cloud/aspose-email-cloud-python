# EmailFromFileRequest

Request model for EmailApi.from_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** | Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**file** |**str** |File to convert |

## Example
```python
request = models.EmailFromFileRequest(
    format='Eml',
    file='/path/to/message.eml')
```
