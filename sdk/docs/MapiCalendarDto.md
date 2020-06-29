# AsposeEmailCloudSdk.models.MapiCalendarDto
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment_counter_proposal** | **bool** | Value indicating whether a Meeting Response object is a counter proposal.              | 
**attendees** | **object** | Attendees              | [optional] 
**busy_status** | **str** | Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice | 
**client_intent** | **list[str]** | Actions the user has taken on this Meeting object.              Items: Enumerates the actions the user can taken on the Meeting object Enum, available values: Manager, Delegate, DeletedWithNoResponse, DeletedExceptionWithNoResponse, RespondedTentative, RespondedAccept, RespondedDecline, ModifiedStartTime, ModifiedEndTime, ModifiedLocation, RespondedExceptionDecline, Canceled, ExceptionCanceled | [optional] 
**end_date** | **datetime** | End date and time of the event. If the date is not set, default value for DateTime is returned.              | 
**end_date_time_zone** | **object** | Time zone information that indicates the time zone of the EndDate property.              | [optional] 
**is_all_day** | **bool** | Value indicating whether the event is an all-day event.              | 
**key_words** | **str** | Categories of the calendar object.              | [optional] 
**location** | **str** | Location of the event.              | [optional] 
**recurrence** | **object** | Recurrence properties.              | [optional] 
**reminder_delta** | **int** | Interval, in minutes, between the time at which the reminder first becomes overdue and the start time of the Calendar object.              | 
**reminder_file_parameter** | **str** | Full path of the sound that a client SHOULD play when the reminder becomes overdue.              | [optional] 
**reminder_set** | **bool** | Value indicating whether a reminder is set on the object.              | 
**sequence** | **int** | Sequence number.              | 
**start_date** | **datetime** | Start date and time of the event. If the date is not set, default value for DateTime is returned.              | 
**start_date_time_zone** | **object** | Time zone information that indicates the time zone of the StartDate property.              | [optional] 
**uid** | **str** | Unique identifier.              | [optional] 
**organizer** | **object** | Organizer              | [optional] 

 Parent class: [MapiMessageItemBaseDto](MapiMessageItemBaseDto.md)

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


