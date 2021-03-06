# AiNameParseEmailAddressRequest

Request model for AiNameApi.parse_email_address

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**email_address** |**str** |Email address to parse. |
**language** |**str** |An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian).              |[optional] [default to ]
**location** |**str** |A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France.              |[optional] [default to ]
**encoding** |**str** |A character encoding name. |[optional] [default to ]
**script** |**str** |A writing system code; starts with the ISO-15924 script name. |[optional] [default to ]
**style** |**str** |Name writing style. Enum, available values: Formal, Informal, Legal, Academic |[optional] [default to 0]

## Example
```python
request = models.AiNameParseEmailAddressRequest(
    email_address='john-cane@gmail.com')
```
