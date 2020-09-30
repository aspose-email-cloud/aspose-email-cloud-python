# DownloadFileRequest

Request model for FileApi.download_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |File path e.g. '/folder/file.ext' |
**storage_name** |**str** |Storage name |[optional] 
**version_id** |**str** |File version ID to download |[optional] 

## Example
```python
request = models.DownloadFileRequest(
    path='/storage/path/to/file.ext',
    storage_name='First Storage',)
```
