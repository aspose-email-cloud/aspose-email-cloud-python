# AsposeEmailCloudSdk.MapiCalendarApi (EmailCloud.mapi.calendar)

MAPI calendar operations.

<a name="as_calendar_dto"></a>
## as_calendar_dto

Description: Converts MAPI calendar model to CalendarDto model.             

Returns: CalendarDto model.

Method call example:
```python
result = api.mapi.calendar.as_calendar_dto(mapi_calendar_dto)
```

### Parameter: mapi_calendar_dto

Description: MAPI calendar model to convert.

See parameter model documentation at [MapiCalendarDto](MapiCalendarDto.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
mapi_calendar_dto = models.MapiCalendarDto(
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

### Result

Description: CalendarDto model.

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
mapi_calendar_dto = models.MapiCalendarDto(
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

// Call method:
result = api.mapi.calendar.as_calendar_dto(mapi_calendar_dto)

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
<a name="as_file"></a>
## as_file

Description: Converts MAPI calendar model to specified format and returns as file.             

Returns: File stream in specified format.

Method call example:
```python
result = api.mapi.calendar.as_file(request)
```

### Parameter: request

Description: MAPI calendar model to convert.

See parameter model documentation at [MapiCalendarAsFileRequest](MapiCalendarAsFileRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiCalendarAsFileRequest(
    format='Msg',
    value=models.MapiCalendarDto(
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
        subject='Some summary'))
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
request = models.MapiCalendarAsFileRequest(
    format='Msg',
    value=models.MapiCalendarDto(
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
        subject='Some summary'))

// Call method:
result = api.mapi.calendar.as_file(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)
<a name="from_file"></a>
## from_file

Description: Converts calendar file to a MAPI model representation.             

Returns: MAPI model.

Method call example:
```python
result = api.mapi.calendar.from_file(request)
```

### Parameter: request

Description: from_file method request.

See parameter model documentation at [MapiCalendarFromFileRequest](MapiCalendarFromFileRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiCalendarFromFileRequest(
    file='/path/to/calendar.msg')
```

</details>

### Result

Description: MAPI model.

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
request = models.MapiCalendarFromFileRequest(
    file='/path/to/calendar.msg')

// Call method:
result = api.mapi.calendar.from_file(request)

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
<a name="get"></a>
## get

Description: Get MAPI calendar document.             

Returns: MAPI Calendar model.

Method call example:
```python
result = api.mapi.calendar.get(request)
```

### Parameter: request

Description: get method request.

See parameter model documentation at [MapiCalendarGetRequest](MapiCalendarGetRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiCalendarGetRequest(
    file_name='calendar.msg',
    folder='calendar/location/on/storage',
    storage='First Storage')
```

</details>

### Result

Description: MAPI Calendar model.

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
request = models.MapiCalendarGetRequest(
    file_name='calendar.msg',
    folder='calendar/location/on/storage',
    storage='First Storage')

// Call method:
result = api.mapi.calendar.get(request)

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
<a name="save"></a>
## save

Description: Save MAPI Calendar to storage.             

Method call example:
```python
api.mapi.calendar.save(request)
```

### Parameter: request

Description: Calendar create/update request.

See parameter model documentation at [MapiCalendarSaveRequest](MapiCalendarSaveRequest.md)

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.MapiCalendarSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='calendar.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiCalendarDto(
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
        subject='Some summary'))
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
request = models.MapiCalendarSaveRequest(
    format='Msg',
    storage_file=models.StorageFileLocation(
        file_name='calendar.msg',
        storage='First Storage',
        folder_path='file/location/folder/on/storage'),
    value=models.MapiCalendarDto(
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
        subject='Some summary'))

// Call method:
api.mapi.calendar.save(request)
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

