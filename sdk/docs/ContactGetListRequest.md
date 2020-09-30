# ContactGetListRequest

Request model for ContactApi.get_list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |Contact document format. Enum, available values: VCard, WebDav, Msg |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 
**items_per_page** |**int** |Count of items on page. |[optional] [default to 10]
**page_number** |**int** |Page number. |[optional] [default to 0]

## Example
```python
request = models.ContactGetListRequest(
    format='VCard',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)
```
