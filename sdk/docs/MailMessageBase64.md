# AsposeEmailCloudSdk.models.MailMessageBase64

Email message represented as file, encoded to Base64 format.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_base64** |**str** |Email message file data encoded to Base64 string.              |
**format** |**str** |Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |

Parent class: [MailMessageBase](MailMessageBase.md)


## Example
```python
mail_message_base64 = models.MailMessageBase64(
    value_base64='RnJvbTogZkBmLnVzClRvOiB0QHQudXMKU3ViamVjdDogUwoKQm9keQ==')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

