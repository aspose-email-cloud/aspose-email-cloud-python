# AsposeEmailCloudSdk.models.ClientThreadSetIsReadRequest

Mark thread messages as read or unread request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_read** |**bool** |Message is read flag.              |
**folder** |**str** |Folder on email server, where thread is stored.              |[optional] 

Parent class: [ClientThreadBaseRequest](ClientThreadBaseRequest.md)


## Example
```python
client_thread_set_is_read_request = models.ClientThreadSetIsReadRequest(
    is_read=True,
    folder='INBOX',
    thread_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

