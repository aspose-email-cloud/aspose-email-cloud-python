# DeleteFolderRequest

Request model for FolderApi.delete_folder

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |Folder path e.g. '/folder' |
**storage_name** |**str** |Storage name |[optional] 
**recursive** |**bool** |Enable to delete folders, subfolders and files |[optional] [default to false]

## Example
```python
request = models.DeleteFolderRequest(
    path='/storage/path/to/folder',
    storage_name='First Storage',
    recursive=True)
```
