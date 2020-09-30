# AsposeEmailCloudSdk.models.AiBcrParseStorageRequest

Parse business card images from Storage request             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_folder** |[**StorageFolderLocation**](StorageFolderLocation.md) |Parse output folder location on storage              |
**images** |[**list[AiBcrImageStorageFile]**](AiBcrImageStorageFile.md) |Images to parse.              |
**options** |[**AiBcrOptions**](AiBcrOptions.md) |Recognition options.              |[optional] 



## Example
```python
ai_bcr_parse_storage_request = models.AiBcrParseStorageRequest(
    out_folder=models.StorageFolderLocation(
        storage='First Storage',
        folder_path='VCard/files/produced/by/parser/will/be/placed/here'),
    images=[
        models.AiBcrImageStorageFile(
            file=models.StorageFileLocation(
                file_name='VCardScanImage.jpg',
                storage='First Storage',
                folder_path='image/location/on/storage'),
            is_single=True)])
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

