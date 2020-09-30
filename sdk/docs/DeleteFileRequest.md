# DeleteFileRequest

Request model for FileApi.delete_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |File path e.g. '/folder/file.ext' |
**storage_name** |**str** |Storage name |[optional] 
**version_id** |**str** |File version ID to delete |[optional] 

## Example
```python
request = models.DeleteFileRequest(
    path='/storage/path/to/file.ext',
    storage_name='First Storage',)
```
