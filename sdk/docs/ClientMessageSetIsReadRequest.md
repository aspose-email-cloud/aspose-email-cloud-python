# AsposeEmailCloudSdk.models.ClientMessageSetIsReadRequest

Email client mark message is read/unread request.             

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_read** |**bool** |Message is read flag.              |

Parent class: [ClientMessageBaseRequest](ClientMessageBaseRequest.md)


## Example
```python
client_message_set_is_read_request = models.ClientMessageSetIsReadRequest(
    is_read=True,
    message_id='5',
    account_location=models.StorageFileLocation(
        file_name='email.account',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'))
```


[[Back to Model list]](Models.md) [[Back to README]](README.md)

