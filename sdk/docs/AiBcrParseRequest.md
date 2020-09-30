# AiBcrParseRequest

Request model for AiBcrApi.parse

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**file** |**str** |File to parse |
**countries** |**str** |Comma-separated codes of countries. |[optional] [default to ]
**languages** |**str** |Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \"it\" or \"ita\" for Italian); it's \"\" by default.              |[optional] [default to ]
**is_single** |**bool** |Determines that image contains single VCard or more. |[optional] [default to true]

## Example
```python
request = models.AiBcrParseRequest(
    file='/path/to/image.png',
    countries='us',
    languages='en',
    is_single=True)
```
