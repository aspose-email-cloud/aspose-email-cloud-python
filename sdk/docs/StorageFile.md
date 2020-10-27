# AsposeEmailCloudSdk.models.StorageFile

File or folder information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** |**str** |File or folder name. |[optional] 
**is_folder** |**bool** |True if it is a folder. |
**modified_date** |**datetime** |File or folder last modified DateTime. |[optional] 
**size** |**int** |File or folder size. |
**path** |**str** |File or folder path. |[optional] 



## Example
```python
storage_file = models.StorageFile(
    name='file.ext',
    modified_date=datetime.today(),
    size=4096,
    path='/storage/path/to')
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

