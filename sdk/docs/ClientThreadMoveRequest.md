# AsposeEmailCloudSdk.models.ClientThreadMoveRequest

Email client move thread request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_folder** |**str** |Email account folder to move thread to.              |

Parent class: [ClientThreadBaseRequest](ClientThreadBaseRequest.md)


## Example
```python
client_thread_move_request = models.ClientThreadMoveRequest(
    destination_folder='INBOX/SubFolder',
    thread_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

