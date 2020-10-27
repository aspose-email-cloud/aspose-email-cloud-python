# AsposeEmailCloudSdk.models.ClientMessageMoveRequest

Email client move message request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_folder** |**str** |Folder to move message from.              |[optional] 
**destination_folder** |**str** |Folder to move message to.              |

Parent class: [ClientMessageBaseRequest](ClientMessageBaseRequest.md)


## Example
```python
client_message_move_request = models.ClientMessageMoveRequest(
    source_folder='INBOX',
    destination_folder='INBOX/SubFolder',
    message_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

