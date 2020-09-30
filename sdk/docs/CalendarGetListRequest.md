# CalendarGetListRequest

Request model for CalendarApi.get_list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**folder** |**str** |Path to folder in storage. |
**items_per_page** |**int** |Count of items on page. |[optional] [default to 10]
**page_number** |**int** |Page number. |[optional] [default to 0]
**storage** |**str** |Storage name. |[optional] 

## Example
```python
request = models.CalendarGetListRequest(
    folder='some/folder/on/storage',
    items_per_page=10,
    page_number=0,
    storage='First Storage')
```
