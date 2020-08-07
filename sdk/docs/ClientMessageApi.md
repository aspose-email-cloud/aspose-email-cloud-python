# AsposeEmailCloudSdk.ClientMessageApi

        
<a name="append"></a>
# append

```python
append(self, ClientMessageAppendRequest request)
```

Add email message to specified folder in email account.             

### Return type

[**ValueTOfString**](ValueTOfString.md)

### request Parameter

See parameter model documentation at [ClientMessageAppendRequest](ClientMessageAppendRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="append_file"></a>
# append_file

```python
append_file(self, request: ClientMessageAppendFileRequest)
```

Add email message from file to specified folder in email account.             

### Return type

ValueTOfString

### request Parameter
```python
ClientMessageAppendFileRequest(
    account,
    file,
    storage,
    account_storage_folder,
    format,
    folder,
    mark_as_sent)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str** | Email account. | 
 **file** | **str** | Message file to append. | 
 **storage** | **str** | Storage name where account file located. | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located. | [optional] 
 **format** | **str** | Email file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | [optional] [default to 0]
 **folder** | **str** | Path to folder on email server to append message to. | [optional] 
 **mark_as_sent** | **bool** | Determines that appended message should be market as sent or not. | [optional] [default to true]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="delete"></a>
# delete

```python
delete(self, ClientMessageDeleteRequest request)
```

Delete message.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientMessageDeleteRequest](ClientMessageDeleteRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="fetch"></a>
# fetch

```python
fetch(self, request: ClientMessageFetchRequest)
```

Fetch message from email account             

### Return type

MailMessageBase

### request Parameter
```python
ClientMessageFetchRequest(
    message_id,
    account,
    folder,
    storage,
    account_storage_folder,
    type,
    format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str** | Message identifier | 
 **account** | **str** | Email account | 
 **folder** | **str** | Account folder to fetch from (should be specified for some protocols such as IMAP)              | [optional] 
 **storage** | **str** | Storage name where account file located. | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located. | [optional] 
 **type** | **str** | MailMessageBase type. Using this property you can fetch message in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64 | [optional] [default to 0]
 **format** | **str** | Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="fetch_file"></a>
# fetch_file

```python
fetch_file(self, request: ClientMessageFetchFileRequest)
```

Fetch message as file from email account             

### Return type

str

### request Parameter
```python
ClientMessageFetchFileRequest(
    message_id,
    account,
    folder,
    storage,
    account_storage_folder,
    format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str** | Message identifier | 
 **account** | **str** | Email account | 
 **folder** | **str** | Account folder to fetch from (should be specified for some protocols such as IMAP)              | [optional] 
 **storage** | **str** | Storage name where account file located. | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located. | [optional] 
 **format** | **str** | Fetched message file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="list"></a>
# list

```python
list(self, request: ClientMessageListRequest)
```

Get messages from folder, filtered by query             

The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

### Return type

MailMessageBaseList

### request Parameter
```python
ClientMessageListRequest(
    folder,
    account,
    query_string,
    storage,
    account_storage_folder,
    recursive,
    type,
    format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str** | A folder in email account | 
 **account** | **str** | Email account | 
 **query_string** | **str** | A MailQuery search string | [optional] 
 **storage** | **str** | Storage name where account file located | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located | [optional] 
 **recursive** | **bool** | Specifies that should message be searched in subfolders recursively | [optional] [default to false]
 **type** | **str** | MailMessageBase type. Using this property you can get messages in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64 | [optional] [default to 0]
 **format** | **str** | Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="move"></a>
# move

```python
move(self, ClientMessageMoveRequest request)
```

Move message to another folder.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientMessageMoveRequest](ClientMessageMoveRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="send"></a>
# send

```python
send(self, ClientMessageSendRequest request)
```

Send an email specified by model in request.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientMessageSendRequest](ClientMessageSendRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="send_file"></a>
# send_file

```python
send_file(self, request: ClientMessageSendFileRequest)
```

Send an email file.             

### Return type

None

### request Parameter
```python
ClientMessageSendFileRequest(
    account,
    file,
    storage,
    account_storage_folder,
    format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str** | Email account | 
 **file** | **str** | File to send | 
 **storage** | **str** | Storage name where account file located. | [optional] 
 **account_storage_folder** | **str** | Folder in storage where account file located. | [optional] 
 **format** | **str** | Email file format Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef | [optional] [default to 0]

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
        
<a name="set_is_read"></a>
# set_is_read

```python
set_is_read(self, ClientMessageSetIsReadRequest request)
```

Mark message as read or unread.             

### Return type

void (empty response body)

### request Parameter

See parameter model documentation at [ClientMessageSetIsReadRequest](ClientMessageSetIsReadRequest.md)

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

