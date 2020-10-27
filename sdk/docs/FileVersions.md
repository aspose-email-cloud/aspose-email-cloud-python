# AsposeEmailCloudSdk.models.FileVersions

File versions FileVersion.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** |[**list[FileVersion]**](FileVersion.md) |File versions FileVersion. |[optional] 



## Example
```python
file_versions = models.FileVersions(
    value=[
        models.FileVersion(
            version_id='d5afd857-8797-4ca0-b806-a03fdfc3831f',
            is_latest=True,
            name='file.ext',
            modified_date=datetime.today(),
            size=4096,
            path='/storage/path/to')])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

