# AsposeEmailCloudSdk.models.AiBcrImageStorageFile

Image from storage for recognition             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** |[**StorageFileLocation**](StorageFileLocation.md) |Image location              |

Parent class: [AiBcrImage](AiBcrImage.md)


## Example
```python
ai_bcr_image_storage_file = models.AiBcrImageStorageFile(
    file=models.StorageFileLocation(
        file_name='VCardScanImage.jpg',
        storage='First Storage',
        folder_path='image/location/on/storage'),
    is_single=True)
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

