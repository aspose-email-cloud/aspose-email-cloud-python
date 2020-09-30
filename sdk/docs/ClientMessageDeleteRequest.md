# AsposeEmailCloudSdk.models.ClientMessageDeleteRequest

Email client delete message request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** |**str** |Folder to delete message from.              |[optional] 

Parent class: [ClientMessageBaseRequest](ClientMessageBaseRequest.md)


## Example
```python
client_message_delete_request = models.ClientMessageDeleteRequest(
    folder='INBOX',
    message_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

