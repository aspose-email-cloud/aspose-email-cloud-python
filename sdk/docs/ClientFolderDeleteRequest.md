# AsposeEmailCloudSdk.models.ClientFolderDeleteRequest

Email client delete folder request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** |**str** |Path to folder to delete.              |

Parent class: [ClientAccountBaseRequest](ClientAccountBaseRequest.md)


## Example
```python
client_folder_delete_request = models.ClientFolderDeleteRequest(
    folder='INBOX/SubFolder/FolderToDelete',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

