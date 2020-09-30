# AsposeEmailCloudSdk.models.FilesList

Files list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** |[**list[StorageFile]**](StorageFile.md) |Files and folders contained by folder StorageFile. |[optional] 



## Example
```python
files_list = models.FilesList(
    value=[
        models.StorageFile(
            name='file.ext',
            modified_date=datetime.today(),
            size=1024,
            path='/path/to/file/on/storage')])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

