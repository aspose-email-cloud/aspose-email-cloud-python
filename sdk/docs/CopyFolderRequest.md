# CopyFolderRequest

Request model for FolderApi.copy_folder

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**src_path** |**str** |Source folder path e.g. '/src' |
**dest_path** |**str** |Destination folder path e.g. '/dst' |
**src_storage_name** |**str** |Source storage name |[optional] 
**dest_storage_name** |**str** |Destination storage name |[optional] 

## Example
```python
request = models.CopyFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')
```
