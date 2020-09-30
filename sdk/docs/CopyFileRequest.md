# CopyFileRequest

Request model for FileApi.copy_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**src_path** |**str** |Source file path e.g. '/folder/file.ext' |
**dest_path** |**str** |Destination file path |
**src_storage_name** |**str** |Source storage name |[optional] 
**dest_storage_name** |**str** |Destination storage name |[optional] 
**version_id** |**str** |File version ID to copy |[optional] 

## Example
```python
request = models.CopyFileRequest(
    src_path='/storage/path/to/source/file.ext',
    dest_path='/storage/path/to/destination/file.ext',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage',)
```
