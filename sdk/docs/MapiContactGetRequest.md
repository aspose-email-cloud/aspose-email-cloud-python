# MapiContactGetRequest

Request model for MapiContactApi.get

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |Contact document format. Enum, available values: VCard, WebDav, Msg |
**file_name** |**str** |Contact document file name. |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.MapiContactGetRequest(
    format='VCard',
    file_name='contact.vcf',
    folder='folder/on/storage',
    storage='First Storage')
```
