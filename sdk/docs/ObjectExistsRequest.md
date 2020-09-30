# ObjectExistsRequest

Request model for StorageApi.object_exists

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |File or folder path e.g. '/file.ext' or '/folder' |
**storage_name** |**str** |Storage name |[optional] 
**version_id** |**str** |File version ID |[optional] 

## Example
```python
request = models.ObjectExistsRequest(
    path='/storage/path/to/folder/or/file.ext',
    storage_name='First Storage',)
```
