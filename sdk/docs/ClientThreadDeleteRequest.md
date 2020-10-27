# AsposeEmailCloudSdk.models.ClientThreadDeleteRequest

Delete email client thread request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** |**str** |Folder on email server, where thread is stored.              |[optional] 

Parent class: [ClientThreadBaseRequest](ClientThreadBaseRequest.md)


## Example
```python
client_thread_delete_request = models.ClientThreadDeleteRequest(
    folder='INBOX/SubFolder',
    thread_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

