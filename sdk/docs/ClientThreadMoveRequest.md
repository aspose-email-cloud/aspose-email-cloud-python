# AsposeEmailCloudSdk.models.ClientThreadMoveRequest

Email client move thread request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_folder** |**str** |Email account folder to move thread to.              |
**source_folder** |**str** |Email account folder to move thread from.              |[optional] 

Parent class: [ClientThreadBaseRequest](ClientThreadBaseRequest.md)


## Example
```python
client_thread_move_request = models.ClientThreadMoveRequest(
    destination_folder='INBOX/SubFolder',
    source_folder='INBOX',
    thread_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

