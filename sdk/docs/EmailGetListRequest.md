# EmailGetListRequest

Request model for EmailApi.get_list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**format** |**str** |Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft |
**folder** |**str** |Path to folder in storage. |[optional] 
**storage** |**str** |Storage name. |[optional] 
**items_per_page** |**int** |Count of items on page. |[optional] [default to 10]
**page_number** |**int** |Page number. |[optional] [default to 0]

## Example
```python
request = models.EmailGetListRequest(
    format='Eml',
    folder='folder/on/storage',
    storage='First Storage',
    items_per_page=10,
    page_number=0)
```
