# AsposeEmailCloudSdk.models.CalendarDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**list[Attachment]**](Attachment.md) | Document attachments. | [optional] 
**attendees** | [**list[MailAddress]**](MailAddress.md) | Event attendees. | 
**description** | **str** | Description. | [optional] 
**end_date** | **datetime** | End date. | 
**end_time_zone** | **str** | End time zone. | [optional] 
**flags** | **list[str]** | Appointment flags. Items: Enumerates iCalendar flags. Enum, available values: None, AllDayEvent | [optional] 
**is_description_html** | **bool** | Indicates if description is in HTML format. | 
**location** | **str** | Location. | 
**method** | **str** | Defines the iCalendar object method type associated with the calendar document. Enum, available values: None, Publish, Request, Reply, Add, Cancel, Refresh, Counter, DeclineCounter | 
**microsoft_busy_status** | **str** | Specifies the BUSY status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof | 
**microsoft_intended_status** | **str** | Specifies the INTENDED status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof | 
**optional_attendees** | [**list[MailAddress]**](MailAddress.md) | Optional attendees.              | [optional] 
**organizer** | [**MailAddress**](MailAddress.md) | Event organizer.              | 
**recurrence_string** | **str** | Deprecated, use &#39;Recurrence&#39; property. String representation of recurrence pattern (See iCalendar RFC, \&quot;Recurrence rule\&quot; section). For example:               For daily recurrence:         \&quot;FREQ&#x3D;DAILY;COUNT&#x3D;10;WKST&#x3D;MO\&quot;                   For monthly recurrence:         \&quot;BYSETPOS&#x3D;1;BYDAY&#x3D;MO,TU,WE,TH,FR;FREQ&#x3D;MONTHLY;INTERVAL&#x3D;10;WKST&#x3D;MO\&quot;                   For yearly recurrence:         \&quot;BYMONTHDAY&#x3D;30;BYMONTH&#x3D;1;FREQ&#x3D;YEARLY;WKST&#x3D;MO\&quot;                    | [optional] 
**recurrence** | [**RecurrencePatternDto**](RecurrencePatternDto.md) | Recurrence pattern              | [optional] 
**reminders** | [**list[CalendarReminder]**](CalendarReminder.md) | Reminders. | [optional] 
**sequence_id** | **str** | The sequence id. Read only. | [optional] 
**start_date** | **datetime** | Start date. | 
**start_time_zone** | **str** | Start time zone. | [optional] 
**status** | **str** | Defines the overall status or confirmation for the calendar document. Enum, available values: NotDefined, Cancelled, Tentative, Confirmed | 
**summary** | **str** | Summary. | [optional] 
**transparency** | **str** | Specifies whether or not this appointment is intended to be visible in availability searches. Enum, available values: NotDefined, Transparent, Opaque | 



[[Back to Model list]](Models.md) [[Back to README]](README.md)


