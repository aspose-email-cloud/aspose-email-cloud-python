# AsposeEmailCloudSdk.models.CalendarReminder
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Defines the action to be invoked when an alarm is triggered. Enum, available values: Audio, Display, Email, Procedure, None | 
**attachments** | **list[str]** | Collection of Reminder Attachments. Could be an absolute URI or Base64 string representation of attachment content              | [optional] 
**attendees** | [**list[ReminderAttendee]**](ReminderAttendee.md) | Contains collection of ReminderAttendee objects.              | [optional] 
**description** | **str** | Provides a more complete description of the alarm. | [optional] 
**duration** | **int** | Specifies the delay period in ticks, after which the alarm will repeat.              | [optional] 
**repeat** | **int** | Defines the number of time the alarm should be repeated, after the initial trigger.              | 
**summary** | **str** | Defines a short summary or subject for the alarm. | [optional] 
**trigger** | [**ReminderTrigger**](ReminderTrigger.md) | Specifies when an alarm will trigger. | [optional] 



[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


