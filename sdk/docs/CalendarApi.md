# AsposeEmailCloudSdk.CalendarApi (EmailCloud.calendar)

iCalendar document operations.

<a name="as_alternate"></a>
## as_alternate

Description: Convert iCalendar to AlternateView             

Returns: iCalendar document represented as AlternateView

Method call example:
```python
result = api.calendar.as_alternate(request)
```

### Parameter: request

Description: iCalendar to AlternateView request

See parameter model documentation at [CalendarAsAlternateRequest](CalendarAsAlternateRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarAsAlternateRequest(
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'),
    sequence_id='cf4ffb6c-895d-4e58-bdb4-0a3918e96a43')
```

</details>

### Result

Description: iCalendar document represented as AlternateView

Return type: [**AlternateView**](AlternateView.md)

<details>
    <summary>Result example</summary>

```python
result = models.AlternateView(
    base64_data='<File content represented as Base64 string>',
    content_id='fa7a8948-4af1-432a-b4d9-ee0c28542e75',
    content_type=models.ContentType(
        char_set='utf-8',
        media_type='text/calendar',
        name='meeting.ics',
        parameters=[
            models.ContentTypeParameter(
                name='Method',
                value='REQUEST'),
            models.ContentTypeParameter(
                name='Name',
                value='meeting.ics'),
            models.ContentTypeParameter(
                name='charset',
                value='utf-8')]))
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarAsAlternateRequest(
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'),
    sequence_id='cf4ffb6c-895d-4e58-bdb4-0a3918e96a43')

// Call method:
result = api.calendar.as_alternate(request)

// Result example:
result = models.AlternateView(
    base64_data='<File content represented as Base64 string>',
    content_id='fa7a8948-4af1-432a-b4d9-ee0c28542e75',
    content_type=models.ContentType(
        char_set='utf-8',
        media_type='text/calendar',
        name='meeting.ics',
        parameters=[
            models.ContentTypeParameter(
                name='Method',
                value='REQUEST'),
            models.ContentTypeParameter(
                name='Name',
                value='meeting.ics'),
            models.ContentTypeParameter(
                name='charset',
                value='utf-8')]))
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="as_file"></a>
## as_file

Description: Converts calendar model to specified format and returns as file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.calendar.as_file(request)
```

### Parameter: request

Description: Calendar model and format to convert.

See parameter model documentation at [CalendarAsFileRequest](CalendarAsFileRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarAsFileRequest(
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'))
```

</details>

### Result

Description: File stream in specified format.

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarAsFileRequest(
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'))

// Call method:
result = api.calendar.as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="as_mapi"></a>
## as_mapi

Description: Converts CalendarDto to MapiCalendarDto.             

Returns: MAPI model calendar representation.

Method call example:
```python
result = api.calendar.as_mapi(calendar_dto)
```

### Parameter: calendar_dto

Description: iCalendar model calendar representation.

See parameter model documentation at [CalendarDto](CalendarDto.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
calendar_dto = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')
```

</details>

### Result

Description: MAPI model calendar representation.

Return type: [**MapiCalendarDto**](MapiCalendarDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.MapiCalendarDto(
    attendees=models.MapiCalendarAttendeesDto(
        appointment_recipients=[
            models.MapiRecipientDto(
                email_address='organizer@aspose.com',
                address_type='SMTP',
                display_name='Organizer Name',
                recipient_type='MapiTo'),
            models.MapiRecipientDto(
                email_address='attendee@aspose.com',
                address_type='SMTP',
                display_name='Attendee Name',
                recipient_type='MapiTo')]),
    busy_status='Tentative',
    client_intent=[
        'Manager'],
    end_date=datetime.today(),
    location='Some location',
    recurrence=models.MapiCalendarEventRecurrenceDto(
        recurrence_pattern=models.MapiCalendarDailyRecurrencePatternDto(
            frequency='Daily',
            occurrence_count=10,
            week_start_day='Monday')),
    start_date=datetime.today(),
    organizer=models.MapiElectronicAddressDto(
        email_address='organizer@aspose.com'),
    body='Some description',
    subject='Some summary')
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
calendar_dto = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')

// Call method:
result = api.calendar.as_mapi(calendar_dto)

// Result example:
result = models.MapiCalendarDto(
    attendees=models.MapiCalendarAttendeesDto(
        appointment_recipients=[
            models.MapiRecipientDto(
                email_address='organizer@aspose.com',
                address_type='SMTP',
                display_name='Organizer Name',
                recipient_type='MapiTo'),
            models.MapiRecipientDto(
                email_address='attendee@aspose.com',
                address_type='SMTP',
                display_name='Attendee Name',
                recipient_type='MapiTo')]),
    busy_status='Tentative',
    client_intent=[
        'Manager'],
    end_date=datetime.today(),
    location='Some location',
    recurrence=models.MapiCalendarEventRecurrenceDto(
        recurrence_pattern=models.MapiCalendarDailyRecurrencePatternDto(
            frequency='Daily',
            occurrence_count=10,
            week_start_day='Monday')),
    start_date=datetime.today(),
    organizer=models.MapiElectronicAddressDto(
        email_address='organizer@aspose.com'),
    body='Some description',
    subject='Some summary')
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="convert"></a>
## convert

Description: Converts calendar document to specified format and returns as file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.calendar.convert(request)
```

### Parameter: request

Description: convert method request.

See parameter model documentation at [CalendarConvertRequest](CalendarConvertRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarConvertRequest(
    format='Ics',
    file='/path/to/calendar.msg')
```

</details>

### Result

Description: File stream in specified format.

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarConvertRequest(
    format='Ics',
    file='/path/to/calendar.msg')

// Call method:
result = api.calendar.convert(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="from_file"></a>
## from_file

Description: Converts calendar document to a model representation.             

Returns: iCalendar model.

Method call example:
```python
result = api.calendar.from_file(request)
```

### Parameter: request

Description: from_file method request.

See parameter model documentation at [CalendarFromFileRequest](CalendarFromFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarFromFileRequest(
    file='/path/to/calendar.ics')
```

</details>

### Result

Description: iCalendar model.

Return type: [**CalendarDto**](CalendarDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarFromFileRequest(
    file='/path/to/calendar.ics')

// Call method:
result = api.calendar.from_file(request)

// Result example:
result = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get"></a>
## get

Description: Get calendar file from storage.             

Returns: iCalendar model.

Method call example:
```python
result = api.calendar.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [CalendarGetRequest](CalendarGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarGetRequest(
    file_name='calendar.ics',
    folder='calendar/location/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: iCalendar model.

Return type: [**CalendarDto**](CalendarDto.md)

<details>
    <summary>Result example</summary>

```python
result = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarGetRequest(
    file_name='calendar.ics',
    folder='calendar/location/on/storage',
    storage='First Storage')

// Call method:
result = api.calendar.get(request)

// Result example:
result = models.CalendarDto(
    attendees=[
        models.MailAddress(
            display_name='Attendee Name',
            address='attendee@aspose.com',
            participation_status='Accepted')],
    description='Some description',
    end_date=datetime.today(),
    location='Some location',
    organizer=models.MailAddress(
        display_name='Organizer Name',
        address='organizer@aspose.com'),
    recurrence=models.DailyRecurrencePatternDto(
        interval=-1,
        occurs=10,
        week_start='Monday'),
    start_date=datetime.today(),
    summary='Some summary')
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_as_alternate"></a>
## get_as_alternate

Description: Get iCalendar from storage as AlternateView             

Returns: iCalendar document represented as AlternateView

Method call example:
```python
result = api.calendar.get_as_alternate(request)
```

### Parameter: request

Description: get_as_alternate method request.

See parameter model documentation at [CalendarGetAsAlternateRequest](CalendarGetAsAlternateRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarGetAsAlternateRequest(
    file_name='calendar.ics',
    calendar_action='Create',
    folder='calendar/location/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: iCalendar document represented as AlternateView

Return type: [**AlternateView**](AlternateView.md)

<details>
    <summary>Result example</summary>

```python
result = models.AlternateView(
    base64_data='<File content represented as Base64 string>',
    content_id='fa7a8948-4af1-432a-b4d9-ee0c28542e75',
    content_type=models.ContentType(
        char_set='utf-8',
        media_type='text/calendar',
        name='meeting.ics',
        parameters=[
            models.ContentTypeParameter(
                name='Method',
                value='REQUEST'),
            models.ContentTypeParameter(
                name='Name',
                value='meeting.ics'),
            models.ContentTypeParameter(
                name='charset',
                value='utf-8')]))
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarGetAsAlternateRequest(
    file_name='calendar.ics',
    calendar_action='Create',
    folder='calendar/location/on/storage',
    storage='First Storage')

// Call method:
result = api.calendar.get_as_alternate(request)

// Result example:
result = models.AlternateView(
    base64_data='<File content represented as Base64 string>',
    content_id='fa7a8948-4af1-432a-b4d9-ee0c28542e75',
    content_type=models.ContentType(
        char_set='utf-8',
        media_type='text/calendar',
        name='meeting.ics',
        parameters=[
            models.ContentTypeParameter(
                name='Method',
                value='REQUEST'),
            models.ContentTypeParameter(
                name='Name',
                value='meeting.ics'),
            models.ContentTypeParameter(
                name='charset',
                value='utf-8')]))
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_as_file"></a>
## get_as_file

Description: Converts calendar document from storage to specified format and returns as file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.calendar.get_as_file(request)
```

### Parameter: request

Description: get_as_file method request.

See parameter model documentation at [CalendarGetAsFileRequest](CalendarGetAsFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarGetAsFileRequest(
    file_name='calendar.msg',
    format='Ics',
    storage='First Storage',
    folder='calendar/file/location/on/storage')
```

</details>

### Result

Description: File stream in specified format.

Return type: **Stream**

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarGetAsFileRequest(
    file_name='calendar.msg',
    format='Ics',
    storage='First Storage',
    folder='calendar/file/location/on/storage')

// Call method:
result = api.calendar.get_as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="get_list"></a>
## get_list

Description: Get iCalendar list from storage folder.             

Returns: iCalendar document list.

Method call example:
```python
result = api.calendar.get_list(request)
```

### Parameter: request

Description: get_list method request.

See parameter model documentation at [CalendarGetListRequest](CalendarGetListRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarGetListRequest(
    folder='some/folder/on/storage',
    items_per_page=10,
    page_number=0,
    storage='First Storage')
```

</details>

### Result

Description: iCalendar document list.

Return type: [**CalendarStorageList**](CalendarStorageList.md)

<details>
    <summary>Result example</summary>

```python
result = models.CalendarStorageList(
    value=[
        models.StorageModelOfCalendarDto(
            storage_file=models.StorageFileLocation(
                file_name='calendar.ics',
                storage='First Storage',
                folder_path='file/location/folder/on/storage'),
            value=models.CalendarDto(
                attendees=[
                    models.MailAddress(
                        display_name='Attendee Name',
                        address='attendee@aspose.com',
                        participation_status='Accepted')],
                description='Some description',
                end_date=datetime.today(),
                location='Some location',
                organizer=models.MailAddress(
                    display_name='Organizer Name',
                    address='organizer@aspose.com'),
                recurrence=models.DailyRecurrencePatternDto(
                    interval=-1,
                    occurs=10,
                    week_start='Monday'),
                start_date=datetime.today(),
                summary='Some summary'))])
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarGetListRequest(
    folder='some/folder/on/storage',
    items_per_page=10,
    page_number=0,
    storage='First Storage')

// Call method:
result = api.calendar.get_list(request)

// Result example:
result = models.CalendarStorageList(
    value=[
        models.StorageModelOfCalendarDto(
            storage_file=models.StorageFileLocation(
                file_name='calendar.ics',
                storage='First Storage',
                folder_path='file/location/folder/on/storage'),
            value=models.CalendarDto(
                attendees=[
                    models.MailAddress(
                        display_name='Attendee Name',
                        address='attendee@aspose.com',
                        participation_status='Accepted')],
                description='Some description',
                end_date=datetime.today(),
                location='Some location',
                organizer=models.MailAddress(
                    display_name='Organizer Name',
                    address='organizer@aspose.com'),
                recurrence=models.DailyRecurrencePatternDto(
                    interval=-1,
                    occurs=10,
                    week_start='Monday'),
                start_date=datetime.today(),
                summary='Some summary'))])
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="save"></a>
## save

Description: Save iCalendar             

Method call example:
```python
api.calendar.save(request)
```

### Parameter: request

Description: iCalendar create/update request

See parameter model documentation at [CalendarSaveRequest](CalendarSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.CalendarSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='calendar.ics',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'))
```

</details>

### Result

Return type: void (empty response body)

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.CalendarSaveRequest(
    storage_file=models.StorageFileLocation(
        file_name='calendar.ics',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.CalendarDto(
        attendees=[
            models.MailAddress(
                display_name='Attendee Name',
                address='attendee@aspose.com',
                participation_status='Accepted')],
        description='Some description',
        end_date=datetime.today(),
        location='Some location',
        organizer=models.MailAddress(
            display_name='Organizer Name',
            address='organizer@aspose.com'),
        recurrence=models.DailyRecurrencePatternDto(
            interval=-1,
            occurs=10,
            week_start='Monday'),
        start_date=datetime.today(),
        summary='Some summary'))

// Call method:
api.calendar.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

