# MoveFolderRequest

Request model for FolderApi.move_folder

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**src_path** |**str** |Folder path to move e.g. '/folder' |
**dest_path** |**str** |Destination folder path to move to e.g '/dst' |
**src_storage_name** |**str** |Source storage name |[optional] 
**dest_storage_name** |**str** |Destination storage name |[optional] 

## Example
```python
request = models.MoveFolderRequest(
    src_path='/storage/path/to/source/folder',
    dest_path='/storage/path/to/destination/folder',
    src_storage_name='First Storage',
    dest_storage_name='Other Storage')
```
