# AsposeEmailCloudSdk.CalendarApi

<a name="add_calendar_attachment"></a>
# **add_calendar_attachment**
> add_calendar_attachment(self, add_calendar_attachment_request)

Adds an attachment to iCalendar file

### Return type

void (empty response body)

<a name="add_calendar_attachment_async"></a>
# **add_calendar_attachment_async**
> add_calendar_attachment_async(self, add_calendar_attachment_request)

Adds an attachment to iCalendar file

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **attachment** | **str**| Attachment file name in storage | 
 **request** | [**AddAttachmentRequest**](AddAttachmentRequest.md)| Storage name and folder path for calendar and attachment files | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="create_calendar"></a>
# **create_calendar**
> create_calendar(self, create_calendar_request)

Create calendar file

### Return type

void (empty response body)

<a name="create_calendar_async"></a>
# **create_calendar_async**
> create_calendar_async(self, create_calendar_request)

Create calendar file

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Calendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)|  | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="delete_calendar_property"></a>
# **delete_calendar_property**
> delete_calendar_property(self, delete_calendar_property_request)

Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}

### Return type

void (empty response body)

<a name="delete_calendar_property_async"></a>
# **delete_calendar_property_async**
> delete_calendar_property_async(self, delete_calendar_property_request)

Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    member_name, 
    index, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **member_name** | **str**| Indexed property name | 
 **index** | **str**| Property index path | 
 **request** | [**StorageFolder**](StorageFolder.md)| Storage detail to specify iCalendar file location | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar"></a>
# **get_calendar**
> get_calendar(self, get_calendar_request)

Get calendar file properties

### Return type

[**HierarchicalObject**](HierarchicalObject.md)

<a name="get_calendar_async"></a>
# **get_calendar_async**
> get_calendar_async(self, get_calendar_request)

Get calendar file properties

Performs operation asynchronously.

### Return type

[**HierarchicalObject**](HierarchicalObject.md)

### Request Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_attachment"></a>
# **get_calendar_attachment**
> get_calendar_attachment(self, get_calendar_attachment_request)

Get iCalendar document attachment by name

### Return type

[**file**](file.md)

<a name="get_calendar_attachment_async"></a>
# **get_calendar_attachment_async**
> get_calendar_attachment_async(self, get_calendar_attachment_request)

Get iCalendar document attachment by name

Performs operation asynchronously.

### Return type

[**file**](file.md)

### Request Parameters
```python
__init__(self, 
    name, 
    attachment, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar document file name | 
 **attachment** | **str**| Attachment name or index | 
 **folder** | **str**| Path to folder in storage | [optional] 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="get_calendar_list"></a>
# **get_calendar_list**
> get_calendar_list(self, get_calendar_list_request)

Get iCalendar files list in folder on storage

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

<a name="get_calendar_list_async"></a>
# **get_calendar_list_async**
> get_calendar_list_async(self, get_calendar_list_request)

Get iCalendar files list in folder on storage

Performs operation asynchronously.

### Return type

[**ListResponseOfHierarchicalObjectResponse**](ListResponseOfHierarchicalObjectResponse.md)

### Request Parameters
```python
__init__(self, 
    folder, 
    items_per_page, 
    page_number, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| Path to folder in storage | 
 **items_per_page** | **int**| Count of items on page | 
 **page_number** | **int**| Page number | 
 **storage** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="update_calendar_properties"></a>
# **update_calendar_properties**
> update_calendar_properties(self, update_calendar_properties_request)

Update calendar file properties

### Return type

void (empty response body)

<a name="update_calendar_properties_async"></a>
# **update_calendar_properties_async**
> update_calendar_properties_async(self, update_calendar_properties_request)

Update calendar file properties

Performs operation asynchronously.

### Return type

void (empty response body)

### Request Parameters
```python
__init__(self, 
    name, 
    request)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| iCalendar file name in storage | 
 **request** | [**HierarchicalObjectRequest**](HierarchicalObjectRequest.md)| Calendar properties update request | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

