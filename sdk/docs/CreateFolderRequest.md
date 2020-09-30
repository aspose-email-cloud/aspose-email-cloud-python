# CreateFolderRequest

Request model for FolderApi.create_folder

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |Folder path to create e.g. 'folder_1/folder_2/' |
**storage_name** |**str** |Storage name |[optional] 

## Example
```python
request = models.CreateFolderRequest(
    path='/storage/path/to/new/folder',
    storage_name='First Storage')
```
