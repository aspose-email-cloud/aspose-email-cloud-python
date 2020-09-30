# GetFilesListRequest

Request model for FolderApi.get_files_list

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |Folder path e.g. '/folder' |
**storage_name** |**str** |Storage name |[optional] 

## Example
```python
request = models.GetFilesListRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage')
```
