# UploadFileRequest

Request model for FileApi.upload_file

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**path** |**str** |Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              |
**file** |**str** |File to upload |
**storage_name** |**str** |Storage name |[optional] 

## Example
```python
request = models.UploadFileRequest(
    path='/storage/path/to/file.ext',
    file='/local/file/system/path/to/file.ext',
    storage_name='First Storage')
```
