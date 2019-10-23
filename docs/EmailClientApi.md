# AsposeEmailCloudSdk.EmailClientApi

<a name="append_email_message"></a>
# **append_email_message**
> append_email_message(self, append_email_message_request)

Adds an email from *.eml file to specified folder in email account

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

<a name="append_email_message_async"></a>
# **append_email_message_async**
> append_email_message_async(self, append_email_message_request)

Adds an email from *.eml file to specified folder in email account

Performs operation asynchronously.

### Return type

[**EmailPropertyResponse**](EmailPropertyResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailBaseRequest**](AppendEmailBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="append_mime_message"></a>
# **append_mime_message**
> append_mime_message(self, append_mime_message_request)

Adds an email from MIME to specified folder in email account

### Return type

[**ValueResponse**](ValueResponse.md)

<a name="append_mime_message_async"></a>
# **append_mime_message_async**
> append_mime_message_async(self, append_mime_message_request)

Adds an email from MIME to specified folder in email account

Performs operation asynchronously.

### Return type

[**ValueResponse**](ValueResponse.md)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AppendEmailMimeBaseRequest**](AppendEmailMimeBaseRequest.md)| Append email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_email_folder"></a>
# **create_email_folder**
> create_email_folder(self, create_email_folder_request)

Create new folder in email account

### Return type

void (empty response body)

<a name="create_email_folder_async"></a>
# **create_email_folder_async**
> create_email_folder_async(self, create_email_folder_request)

Create new folder in email account

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateFolderBaseRequest**](CreateFolderBaseRequest.md)| Create folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_folder"></a>
# **delete_email_folder**
> delete_email_folder(self, delete_email_folder_request)

Delete a folder in email account

### Return type

void (empty response body)

<a name="delete_email_folder_async"></a>
# **delete_email_folder_async**
> delete_email_folder_async(self, delete_email_folder_request)

Delete a folder in email account

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteFolderBaseRequest**](DeleteFolderBaseRequest.md)| Delete folder request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_email_message"></a>
# **delete_email_message**
> delete_email_message(self, delete_email_message_request)

Delete message from email account by id

### Return type

void (empty response body)

<a name="delete_email_message_async"></a>
# **delete_email_message_async**
> delete_email_message_async(self, delete_email_message_request)

Delete message from email account by id

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DeleteMessageBaseRequest**](DeleteMessageBaseRequest.md)| Delete message request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="fetch_email_message"></a>
# **fetch_email_message**
> fetch_email_message(self, fetch_email_message_request)

Fetch message mime from email account

### Return type

[**MimeResponse**](MimeResponse.md)

<a name="fetch_email_message_async"></a>
# **fetch_email_message_async**
> fetch_email_message_async(self, fetch_email_message_request)

Fetch message mime from email account

Performs operation asynchronously.

### Return type

[**MimeResponse**](MimeResponse.md)

### Request Parameters
```python
__init__(self, 
    message_id, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message identifier | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account) | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_folders"></a>
# **list_email_folders**
> list_email_folders(self, list_email_folders_request)

Get folders list in email account

### Return type

[**ListFoldersResponse**](ListFoldersResponse.md)

<a name="list_email_folders_async"></a>
# **list_email_folders_async**
> list_email_folders_async(self, list_email_folders_request)

Get folders list in email account

Performs operation asynchronously.

### Return type

[**ListFoldersResponse**](ListFoldersResponse.md)

### Request Parameters
```python
__init__(self, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    parent_folder=parent_folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account) | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **parent_folder** | **str**| Folder in which subfolders should be listed | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="list_email_messages"></a>
# **list_email_messages**
> list_email_messages(self, list_email_messages_request)

Get messages from folder, filtered by query

The query string should have the following view.  The example of a simple expression:   '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.  The number of simple expressions can make a compound one, ex.: (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator  At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message  Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message  Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item  Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once  The field value (<Field value>) can take the following values: For text fields - any string, For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\", For flags (fields of boolean type) - either \"True\", or \"False\"

### Return type

[**ListMessagesResponse**](ListMessagesResponse.md)

<a name="list_email_messages_async"></a>
# **list_email_messages_async**
> list_email_messages_async(self, list_email_messages_request)

Get messages from folder, filtered by query

Performs operation asynchronously.

The query string should have the following view.  The example of a simple expression:   '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.  The number of simple expressions can make a compound one, ex.: (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator  At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message  Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message  Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item  Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once  The field value (<Field value>) can take the following values: For text fields - any string, For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\", For flags (fields of boolean type) - either \"True\", or \"False\"

### Return type

[**ListMessagesResponse**](ListMessagesResponse.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    query_string, 
    first_account, 
    second_account=second_account, 
    storage=storage, 
    storage_folder=storage_folder, 
    recursive=recursive)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| A folder in email account | 
 **query_string** | **str**| A MailQuery search string | 
 **first_account** | **str**| Email account | 
 **second_account** | **str**| Additional email account (should be specified for POP/IMAP accounts and should be SMTP account) | [optional] 
 **storage** | **str**| Storage name where account file(s) located | [optional] 
 **storage_folder** | **str**| Folder in storage where account file(s) located | [optional] 
 **recursive** | **bool**| Specifies that should message be searched in subfolders recursively | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_account"></a>
# **save_mail_account**
> save_mail_account(self, save_mail_account_request)

Create email account file (*.account) with login/password authentication

### Return type

void (empty response body)

<a name="save_mail_account_async"></a>
# **save_mail_account_async**
> save_mail_account_async(self, save_mail_account_request)

Create email account file (*.account) with login/password authentication

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveEmailAccountRequest**](SaveEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="save_mail_o_auth_account"></a>
# **save_mail_o_auth_account**
> save_mail_o_auth_account(self, save_mail_o_auth_account_request)

Create email account file (*.account) with OAuth

### Return type

void (empty response body)

<a name="save_mail_o_auth_account_async"></a>
# **save_mail_o_auth_account_async**
> save_mail_o_auth_account_async(self, save_mail_o_auth_account_request)

Create email account file (*.account) with OAuth

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SaveOAuthEmailAccountRequest**](SaveOAuthEmailAccountRequest.md)| Email account information | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email"></a>
# **send_email**
> send_email(self, send_email_request)

Send an email from *.eml file located on storage

### Return type

void (empty response body)

<a name="send_email_async"></a>
# **send_email_async**
> send_email_async(self, send_email_request)

Send an email from *.eml file located on storage

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailBaseRequest**](SendEmailBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="send_email_mime"></a>
# **send_email_mime**
> send_email_mime(self, send_email_mime_request)

Send an email specified by MIME in request

### Return type

void (empty response body)

<a name="send_email_mime_async"></a>
# **send_email_mime_async**
> send_email_mime_async(self, send_email_mime_request)

Send an email specified by MIME in request

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SendEmailMimeBaseRequest**](SendEmailMimeBaseRequest.md)| Send email request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="set_email_read_flag"></a>
# **set_email_read_flag**
> set_email_read_flag(self, set_email_read_flag_request)

Sets \"Message is read\" flag

### Return type

void (empty response body)

<a name="set_email_read_flag_async"></a>
# **set_email_read_flag_async**
> set_email_read_flag_async(self, set_email_read_flag_request)

Sets \"Message is read\" flag

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetMessageReadFlagAccountBaseRequest**](SetMessageReadFlagAccountBaseRequest.md)| Message is read request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

