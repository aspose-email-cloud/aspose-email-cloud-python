# GetFileVersionsRequest

Request model for StorageApi.get_file_versions

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |File path e.g. '/file.ext' |
**storage_name** |**str** |Storage name |[optional] 

## Example
```python
request = models.GetFileVersionsRequest(
    path='/storage/path/to/file.ext',
    storage_name='First Storage')
```
