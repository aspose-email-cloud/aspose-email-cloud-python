# AsposeEmailCloudSdk.models.ClientFolderCreateRequest

Email Client create folder request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_folder** |**str** |Path to parent folder.              |[optional] 
**folder_name** |**str** |Folder name.              |

Parent class: [ClientAccountBaseRequest](ClientAccountBaseRequest.md)


## Example
```python
client_folder_create_request = models.ClientFolderCreateRequest(
    parent_folder='INBOX/SubFolder/ParentFolder',
    folder_name='NewFolder',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

