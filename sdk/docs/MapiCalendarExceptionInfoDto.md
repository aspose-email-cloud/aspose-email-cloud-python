# AsposeEmailCloudSdk.models.MapiCalendarExceptionInfoDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**list[MapiAttachmentDto]**](MapiAttachmentDto.md) | Attachments in the recurrence exception.              | [optional] 
**body** | **str** | Body.              | [optional] 
**busy_status** | **str** | Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice | 
**end_date_time** | **datetime** | End date.              | 
**has_attachment** | **bool** | Value of this field specifies whether the Exception Embedded Message object contains attachments.              | 
**location** | **str** | Location.              | [optional] 
**meeting_type** | **str** | Enumerates the appointment state Enum, available values: Meeting, Received, Canceled | 
**original_start_date** | **datetime** | Original start date.              | 
**override_flags** | **list[str]** | Override flags.              Items: Specifies what data in the MapiCalendarOverride structure has a value different from the recurring series. Enum, available values: Subject, MeetingType, ReminderDelta, Reminder, Location, BusyStatus, Attachment, Subtype, AppointmentColor, ExceptionalBody | [optional] 
**reminder_delta** | **int** | Reminder delta.              | 
**reminder_set** | **bool** | Value for the PidLidReminderSet property.              | 
**start_date_time** | **datetime** | Start date.              | 
**subject** | **str** | Subject.              | [optional] 
**sub_type** | **int** | SubType.              | 



[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


