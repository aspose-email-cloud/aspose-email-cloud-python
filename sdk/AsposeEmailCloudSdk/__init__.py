#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="__init__.py">
#    Copyright (c) 2018-2020 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

from __future__ import absolute_import

# import apis into sdk package
from AsposeEmailCloudSdk.api.ai_bcr_api import AiBcrApi
from AsposeEmailCloudSdk.api.ai_name_api import AiNameApi
from AsposeEmailCloudSdk.api.calendar_api import CalendarApi
from AsposeEmailCloudSdk.api.client_account_api import ClientAccountApi
from AsposeEmailCloudSdk.api.client_folder_api import ClientFolderApi
from AsposeEmailCloudSdk.api.client_message_api import ClientMessageApi
from AsposeEmailCloudSdk.api.client_thread_api import ClientThreadApi
from AsposeEmailCloudSdk.api.contact_api import ContactApi
from AsposeEmailCloudSdk.api.disposable_email_api import DisposableEmailApi
from AsposeEmailCloudSdk.api.email_api import EmailApi
from AsposeEmailCloudSdk.api.email_config_api import EmailConfigApi
from AsposeEmailCloudSdk.api.file_api import FileApi
from AsposeEmailCloudSdk.api.folder_api import FolderApi
from AsposeEmailCloudSdk.api.mapi_calendar_api import MapiCalendarApi
from AsposeEmailCloudSdk.api.mapi_contact_api import MapiContactApi
from AsposeEmailCloudSdk.api.mapi_message_api import MapiMessageApi
from AsposeEmailCloudSdk.api.storage_api import StorageApi
# import ApiClient
from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.configuration import Configuration
# import models into sdk package
from AsposeEmailCloudSdk.models.ai_bcr_image import AiBcrImage
from AsposeEmailCloudSdk.models.ai_bcr_options import AiBcrOptions
from AsposeEmailCloudSdk.models.ai_bcr_parse_storage_request import AiBcrParseStorageRequest
from AsposeEmailCloudSdk.models.ai_name_component import AiNameComponent
from AsposeEmailCloudSdk.models.ai_name_cultural_context import AiNameCulturalContext
from AsposeEmailCloudSdk.models.ai_name_extracted import AiNameExtracted
from AsposeEmailCloudSdk.models.ai_name_extracted_component import AiNameExtractedComponent
from AsposeEmailCloudSdk.models.ai_name_formatted import AiNameFormatted
from AsposeEmailCloudSdk.models.ai_name_gender_hypothesis import AiNameGenderHypothesis
from AsposeEmailCloudSdk.models.ai_name_match_result import AiNameMatchResult
from AsposeEmailCloudSdk.models.ai_name_mismatch import AiNameMismatch
from AsposeEmailCloudSdk.models.ai_name_parsed_request import AiNameParsedRequest
from AsposeEmailCloudSdk.models.ai_name_weighted import AiNameWeighted
from AsposeEmailCloudSdk.models.ai_name_weighted_variants import AiNameWeightedVariants
from AsposeEmailCloudSdk.models.associated_person import AssociatedPerson
from AsposeEmailCloudSdk.models.attachment_base import AttachmentBase
from AsposeEmailCloudSdk.models.calendar_as_alternate_request import CalendarAsAlternateRequest
from AsposeEmailCloudSdk.models.calendar_as_file_request import CalendarAsFileRequest
from AsposeEmailCloudSdk.models.calendar_dto import CalendarDto
from AsposeEmailCloudSdk.models.calendar_reminder import CalendarReminder
from AsposeEmailCloudSdk.models.client_account_base_request import ClientAccountBaseRequest
from AsposeEmailCloudSdk.models.contact_as_file_request import ContactAsFileRequest
from AsposeEmailCloudSdk.models.contact_dto import ContactDto
from AsposeEmailCloudSdk.models.contact_photo import ContactPhoto
from AsposeEmailCloudSdk.models.content_type import ContentType
from AsposeEmailCloudSdk.models.content_type_parameter import ContentTypeParameter
from AsposeEmailCloudSdk.models.customer_event import CustomerEvent
from AsposeEmailCloudSdk.models.disc_usage import DiscUsage
from AsposeEmailCloudSdk.models.discover_email_config_request import DiscoverEmailConfigRequest
from AsposeEmailCloudSdk.models.email_account_config import EmailAccountConfig
from AsposeEmailCloudSdk.models.email_address import EmailAddress
from AsposeEmailCloudSdk.models.email_as_file_request import EmailAsFileRequest
from AsposeEmailCloudSdk.models.email_client_account import EmailClientAccount
from AsposeEmailCloudSdk.models.email_client_account_credentials import EmailClientAccountCredentials
from AsposeEmailCloudSdk.models.email_client_multi_account import EmailClientMultiAccount
from AsposeEmailCloudSdk.models.email_dto import EmailDto
from AsposeEmailCloudSdk.models.email_thread import EmailThread
from AsposeEmailCloudSdk.models.enum_with_custom_of_associated_person_category import EnumWithCustomOfAssociatedPersonCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_email_address_category import EnumWithCustomOfEmailAddressCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_event_category import EnumWithCustomOfEventCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_instant_messenger_category import EnumWithCustomOfInstantMessengerCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_phone_number_category import EnumWithCustomOfPhoneNumberCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_postal_address_category import EnumWithCustomOfPostalAddressCategory
from AsposeEmailCloudSdk.models.enum_with_custom_of_url_category import EnumWithCustomOfUrlCategory
from AsposeEmailCloudSdk.models.error import Error
from AsposeEmailCloudSdk.models.error_details import ErrorDetails
from AsposeEmailCloudSdk.models.file_versions import FileVersions
from AsposeEmailCloudSdk.models.files_list import FilesList
from AsposeEmailCloudSdk.models.files_upload_result import FilesUploadResult
from AsposeEmailCloudSdk.models.instant_messenger_address import InstantMessengerAddress
from AsposeEmailCloudSdk.models.list_response_of_ai_name_component import ListResponseOfAiNameComponent
from AsposeEmailCloudSdk.models.list_response_of_ai_name_extracted import ListResponseOfAiNameExtracted
from AsposeEmailCloudSdk.models.list_response_of_ai_name_gender_hypothesis import ListResponseOfAiNameGenderHypothesis
from AsposeEmailCloudSdk.models.list_response_of_contact_dto import ListResponseOfContactDto
from AsposeEmailCloudSdk.models.list_response_of_email_account_config import ListResponseOfEmailAccountConfig
from AsposeEmailCloudSdk.models.list_response_of_email_dto import ListResponseOfEmailDto
from AsposeEmailCloudSdk.models.list_response_of_email_thread import ListResponseOfEmailThread
from AsposeEmailCloudSdk.models.list_response_of_mail_message_base import ListResponseOfMailMessageBase
from AsposeEmailCloudSdk.models.list_response_of_mail_server_folder import ListResponseOfMailServerFolder
from AsposeEmailCloudSdk.models.list_response_of_storage_file_location import ListResponseOfStorageFileLocation
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_calendar_dto import ListResponseOfStorageModelOfCalendarDto
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_contact_dto import ListResponseOfStorageModelOfContactDto
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_email_dto import ListResponseOfStorageModelOfEmailDto
from AsposeEmailCloudSdk.models.mail_address import MailAddress
from AsposeEmailCloudSdk.models.mail_message_base import MailMessageBase
from AsposeEmailCloudSdk.models.mail_server_folder import MailServerFolder
from AsposeEmailCloudSdk.models.mapi_attachment_dto import MapiAttachmentDto
from AsposeEmailCloudSdk.models.mapi_calendar_as_file_request import MapiCalendarAsFileRequest
from AsposeEmailCloudSdk.models.mapi_calendar_attendees_dto import MapiCalendarAttendeesDto
from AsposeEmailCloudSdk.models.mapi_calendar_event_recurrence_dto import MapiCalendarEventRecurrenceDto
from AsposeEmailCloudSdk.models.mapi_calendar_exception_info_dto import MapiCalendarExceptionInfoDto
from AsposeEmailCloudSdk.models.mapi_calendar_recurrence_pattern_dto import MapiCalendarRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_dto import MapiCalendarTimeZoneDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_info_dto import MapiCalendarTimeZoneInfoDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_rule_dto import MapiCalendarTimeZoneRuleDto
from AsposeEmailCloudSdk.models.mapi_contact_as_file_request import MapiContactAsFileRequest
from AsposeEmailCloudSdk.models.mapi_contact_electronic_address_dto import MapiContactElectronicAddressDto
from AsposeEmailCloudSdk.models.mapi_contact_electronic_address_property_set_dto import MapiContactElectronicAddressPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_event_property_set_dto import MapiContactEventPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_name_property_set_dto import MapiContactNamePropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_other_property_set_dto import MapiContactOtherPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_personal_info_property_set_dto import MapiContactPersonalInfoPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_physical_address_dto import MapiContactPhysicalAddressDto
from AsposeEmailCloudSdk.models.mapi_contact_physical_address_property_set_dto import MapiContactPhysicalAddressPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_professional_property_set_dto import MapiContactProfessionalPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_telephone_property_set_dto import MapiContactTelephonePropertySetDto
from AsposeEmailCloudSdk.models.mapi_electronic_address_dto import MapiElectronicAddressDto
from AsposeEmailCloudSdk.models.mapi_message_as_file_request import MapiMessageAsFileRequest
from AsposeEmailCloudSdk.models.mapi_message_item_base_dto import MapiMessageItemBaseDto
from AsposeEmailCloudSdk.models.mapi_property_descriptor import MapiPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto
from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto
from AsposeEmailCloudSdk.models.name_value_pair import NameValuePair
from AsposeEmailCloudSdk.models.object_exist import ObjectExist
from AsposeEmailCloudSdk.models.phone_number import PhoneNumber
from AsposeEmailCloudSdk.models.postal_address import PostalAddress
from AsposeEmailCloudSdk.models.recurrence_pattern_dto import RecurrencePatternDto
from AsposeEmailCloudSdk.models.reminder_attendee import ReminderAttendee
from AsposeEmailCloudSdk.models.reminder_trigger import ReminderTrigger
from AsposeEmailCloudSdk.models.storage_exist import StorageExist
from AsposeEmailCloudSdk.models.storage_file import StorageFile
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation
from AsposeEmailCloudSdk.models.storage_model_of_calendar_dto import StorageModelOfCalendarDto
from AsposeEmailCloudSdk.models.storage_model_of_contact_dto import StorageModelOfContactDto
from AsposeEmailCloudSdk.models.storage_model_of_email_client_account import StorageModelOfEmailClientAccount
from AsposeEmailCloudSdk.models.storage_model_of_email_client_multi_account import StorageModelOfEmailClientMultiAccount
from AsposeEmailCloudSdk.models.storage_model_of_email_dto import StorageModelOfEmailDto
from AsposeEmailCloudSdk.models.storage_model_of_mapi_calendar_dto import StorageModelOfMapiCalendarDto
from AsposeEmailCloudSdk.models.storage_model_of_mapi_contact_dto import StorageModelOfMapiContactDto
from AsposeEmailCloudSdk.models.storage_model_of_mapi_message_dto import StorageModelOfMapiMessageDto
from AsposeEmailCloudSdk.models.url import Url
from AsposeEmailCloudSdk.models.value_t_of_boolean import ValueTOfBoolean
from AsposeEmailCloudSdk.models.value_t_of_string import ValueTOfString
from AsposeEmailCloudSdk.models.ai_bcr_image_storage_file import AiBcrImageStorageFile
from AsposeEmailCloudSdk.models.ai_name_component_list import AiNameComponentList
from AsposeEmailCloudSdk.models.ai_name_extracted_list import AiNameExtractedList
from AsposeEmailCloudSdk.models.ai_name_gender_hypothesis_list import AiNameGenderHypothesisList
from AsposeEmailCloudSdk.models.ai_name_parsed_match_request import AiNameParsedMatchRequest
from AsposeEmailCloudSdk.models.alternate_view import AlternateView
from AsposeEmailCloudSdk.models.attachment import Attachment
from AsposeEmailCloudSdk.models.calendar_save_request import CalendarSaveRequest
from AsposeEmailCloudSdk.models.calendar_storage_list import CalendarStorageList
from AsposeEmailCloudSdk.models.client_folder_create_request import ClientFolderCreateRequest
from AsposeEmailCloudSdk.models.client_folder_delete_request import ClientFolderDeleteRequest
from AsposeEmailCloudSdk.models.client_message_append_request import ClientMessageAppendRequest
from AsposeEmailCloudSdk.models.client_message_base_request import ClientMessageBaseRequest
from AsposeEmailCloudSdk.models.client_message_send_request import ClientMessageSendRequest
from AsposeEmailCloudSdk.models.client_thread_base_request import ClientThreadBaseRequest
from AsposeEmailCloudSdk.models.contact_list import ContactList
from AsposeEmailCloudSdk.models.contact_save_request import ContactSaveRequest
from AsposeEmailCloudSdk.models.contact_storage_list import ContactStorageList
from AsposeEmailCloudSdk.models.daily_recurrence_pattern_dto import DailyRecurrencePatternDto
from AsposeEmailCloudSdk.models.discover_email_config_oauth import DiscoverEmailConfigOauth
from AsposeEmailCloudSdk.models.discover_email_config_password import DiscoverEmailConfigPassword
from AsposeEmailCloudSdk.models.email_account_config_list import EmailAccountConfigList
from AsposeEmailCloudSdk.models.email_client_account_oauth_credentials import EmailClientAccountOauthCredentials
from AsposeEmailCloudSdk.models.email_client_account_password_credentials import EmailClientAccountPasswordCredentials
from AsposeEmailCloudSdk.models.email_client_account_save_request import EmailClientAccountSaveRequest
from AsposeEmailCloudSdk.models.email_client_multi_account_save_request import EmailClientMultiAccountSaveRequest
from AsposeEmailCloudSdk.models.email_list import EmailList
from AsposeEmailCloudSdk.models.email_save_request import EmailSaveRequest
from AsposeEmailCloudSdk.models.email_storage_list import EmailStorageList
from AsposeEmailCloudSdk.models.email_thread_list import EmailThreadList
from AsposeEmailCloudSdk.models.file_version import FileVersion
from AsposeEmailCloudSdk.models.linked_resource import LinkedResource
from AsposeEmailCloudSdk.models.mail_message_base64 import MailMessageBase64
from AsposeEmailCloudSdk.models.mail_message_base_list import MailMessageBaseList
from AsposeEmailCloudSdk.models.mail_message_dto import MailMessageDto
from AsposeEmailCloudSdk.models.mail_message_mapi import MailMessageMapi
from AsposeEmailCloudSdk.models.mail_server_folder_list import MailServerFolderList
from AsposeEmailCloudSdk.models.mapi_binary_property_dto import MapiBinaryPropertyDto
from AsposeEmailCloudSdk.models.mapi_boolean_property_dto import MapiBooleanPropertyDto
from AsposeEmailCloudSdk.models.mapi_calendar_daily_recurrence_pattern_dto import MapiCalendarDailyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_dto import MapiCalendarDto
from AsposeEmailCloudSdk.models.mapi_calendar_save_request import MapiCalendarSaveRequest
from AsposeEmailCloudSdk.models.mapi_calendar_weekly_recurrence_pattern_dto import MapiCalendarWeeklyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_yearly_and_monthly_recurrence_pattern_dto import MapiCalendarYearlyAndMonthlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_contact_dto import MapiContactDto
from AsposeEmailCloudSdk.models.mapi_contact_photo_dto import MapiContactPhotoDto
from AsposeEmailCloudSdk.models.mapi_contact_save_request import MapiContactSaveRequest
from AsposeEmailCloudSdk.models.mapi_date_time_property_dto import MapiDateTimePropertyDto
from AsposeEmailCloudSdk.models.mapi_file_as_property_dto import MapiFileAsPropertyDto
from AsposeEmailCloudSdk.models.mapi_importance_property_dto import MapiImportancePropertyDto
from AsposeEmailCloudSdk.models.mapi_int_property_dto import MapiIntPropertyDto
from AsposeEmailCloudSdk.models.mapi_known_property_descriptor import MapiKnownPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_legacy_free_busy_property_dto import MapiLegacyFreeBusyPropertyDto
from AsposeEmailCloudSdk.models.mapi_message_dto import MapiMessageDto
from AsposeEmailCloudSdk.models.mapi_message_save_request import MapiMessageSaveRequest
from AsposeEmailCloudSdk.models.mapi_multi_int_property_dto import MapiMultiIntPropertyDto
from AsposeEmailCloudSdk.models.mapi_multi_string_property_dto import MapiMultiStringPropertyDto
from AsposeEmailCloudSdk.models.mapi_physical_address_index_property_dto import MapiPhysicalAddressIndexPropertyDto
from AsposeEmailCloudSdk.models.mapi_pid_property_descriptor import MapiPidPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_response_type_property_dto import MapiResponseTypePropertyDto
from AsposeEmailCloudSdk.models.mapi_string_property_dto import MapiStringPropertyDto
from AsposeEmailCloudSdk.models.monthly_recurrence_pattern_dto import MonthlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation
from AsposeEmailCloudSdk.models.storage_file_location_list import StorageFileLocationList
from AsposeEmailCloudSdk.models.task_regenerating_pattern_dto import TaskRegeneratingPatternDto
from AsposeEmailCloudSdk.models.weekly_recurrence_pattern_dto import WeeklyRecurrencePatternDto
from AsposeEmailCloudSdk.models.yearly_recurrence_pattern_dto import YearlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.client_message_delete_request import ClientMessageDeleteRequest
from AsposeEmailCloudSdk.models.client_message_move_request import ClientMessageMoveRequest
from AsposeEmailCloudSdk.models.client_message_set_is_read_request import ClientMessageSetIsReadRequest
from AsposeEmailCloudSdk.models.client_thread_delete_request import ClientThreadDeleteRequest
from AsposeEmailCloudSdk.models.client_thread_move_request import ClientThreadMoveRequest
from AsposeEmailCloudSdk.models.client_thread_set_is_read_request import ClientThreadSetIsReadRequest
from AsposeEmailCloudSdk.models.mapi_pid_lid_property_descriptor import MapiPidLidPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_pid_name_property_descriptor import MapiPidNamePropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_pid_tag_property_descriptor import MapiPidTagPropertyDescriptor
from AsposeEmailCloudSdk.models.ai_bcr_parse_request import AiBcrParseRequest
from AsposeEmailCloudSdk.models.ai_name_complete_request import AiNameCompleteRequest
from AsposeEmailCloudSdk.models.ai_name_expand_request import AiNameExpandRequest
from AsposeEmailCloudSdk.models.ai_name_format_request import AiNameFormatRequest
from AsposeEmailCloudSdk.models.ai_name_genderize_request import AiNameGenderizeRequest
from AsposeEmailCloudSdk.models.ai_name_match_request import AiNameMatchRequest
from AsposeEmailCloudSdk.models.ai_name_parse_request import AiNameParseRequest
from AsposeEmailCloudSdk.models.ai_name_parse_email_address_request import AiNameParseEmailAddressRequest
from AsposeEmailCloudSdk.models.calendar_convert_request import CalendarConvertRequest
from AsposeEmailCloudSdk.models.calendar_from_file_request import CalendarFromFileRequest
from AsposeEmailCloudSdk.models.calendar_get_request import CalendarGetRequest
from AsposeEmailCloudSdk.models.calendar_get_as_alternate_request import CalendarGetAsAlternateRequest
from AsposeEmailCloudSdk.models.calendar_get_as_file_request import CalendarGetAsFileRequest
from AsposeEmailCloudSdk.models.calendar_get_list_request import CalendarGetListRequest
from AsposeEmailCloudSdk.models.client_account_get_request import ClientAccountGetRequest
from AsposeEmailCloudSdk.models.client_account_get_multi_request import ClientAccountGetMultiRequest
from AsposeEmailCloudSdk.models.client_folder_get_list_request import ClientFolderGetListRequest
from AsposeEmailCloudSdk.models.client_message_append_file_request import ClientMessageAppendFileRequest
from AsposeEmailCloudSdk.models.client_message_fetch_request import ClientMessageFetchRequest
from AsposeEmailCloudSdk.models.client_message_fetch_file_request import ClientMessageFetchFileRequest
from AsposeEmailCloudSdk.models.client_message_list_request import ClientMessageListRequest
from AsposeEmailCloudSdk.models.client_message_send_file_request import ClientMessageSendFileRequest
from AsposeEmailCloudSdk.models.client_thread_get_list_request import ClientThreadGetListRequest
from AsposeEmailCloudSdk.models.client_thread_get_messages_request import ClientThreadGetMessagesRequest
from AsposeEmailCloudSdk.models.contact_convert_request import ContactConvertRequest
from AsposeEmailCloudSdk.models.contact_from_file_request import ContactFromFileRequest
from AsposeEmailCloudSdk.models.contact_get_request import ContactGetRequest
from AsposeEmailCloudSdk.models.contact_get_as_file_request import ContactGetAsFileRequest
from AsposeEmailCloudSdk.models.contact_get_list_request import ContactGetListRequest
from AsposeEmailCloudSdk.models.disposable_email_is_disposable_request import DisposableEmailIsDisposableRequest
from AsposeEmailCloudSdk.models.email_convert_request import EmailConvertRequest
from AsposeEmailCloudSdk.models.email_from_file_request import EmailFromFileRequest
from AsposeEmailCloudSdk.models.email_get_request import EmailGetRequest
from AsposeEmailCloudSdk.models.email_get_as_file_request import EmailGetAsFileRequest
from AsposeEmailCloudSdk.models.email_get_list_request import EmailGetListRequest
from AsposeEmailCloudSdk.models.email_config_discover_request import EmailConfigDiscoverRequest
from AsposeEmailCloudSdk.models.copy_file_request import CopyFileRequest
from AsposeEmailCloudSdk.models.delete_file_request import DeleteFileRequest
from AsposeEmailCloudSdk.models.download_file_request import DownloadFileRequest
from AsposeEmailCloudSdk.models.move_file_request import MoveFileRequest
from AsposeEmailCloudSdk.models.upload_file_request import UploadFileRequest
from AsposeEmailCloudSdk.models.copy_folder_request import CopyFolderRequest
from AsposeEmailCloudSdk.models.create_folder_request import CreateFolderRequest
from AsposeEmailCloudSdk.models.delete_folder_request import DeleteFolderRequest
from AsposeEmailCloudSdk.models.get_files_list_request import GetFilesListRequest
from AsposeEmailCloudSdk.models.move_folder_request import MoveFolderRequest
from AsposeEmailCloudSdk.models.mapi_calendar_from_file_request import MapiCalendarFromFileRequest
from AsposeEmailCloudSdk.models.mapi_calendar_get_request import MapiCalendarGetRequest
from AsposeEmailCloudSdk.models.mapi_contact_from_file_request import MapiContactFromFileRequest
from AsposeEmailCloudSdk.models.mapi_contact_get_request import MapiContactGetRequest
from AsposeEmailCloudSdk.models.mapi_message_from_file_request import MapiMessageFromFileRequest
from AsposeEmailCloudSdk.models.mapi_message_get_request import MapiMessageGetRequest
from AsposeEmailCloudSdk.models.get_disc_usage_request import GetDiscUsageRequest
from AsposeEmailCloudSdk.models.get_file_versions_request import GetFileVersionsRequest
from AsposeEmailCloudSdk.models.object_exists_request import ObjectExistsRequest
from AsposeEmailCloudSdk.models.storage_exists_request import StorageExistsRequest

# EmailCloud imports
from AsposeEmailCloudSdk.api.email_cloud import EmailCloud

from AsposeEmailCloudSdk.api.mapi_group import MapiGroup

from AsposeEmailCloudSdk.api.client_group import ClientGroup

from AsposeEmailCloudSdk.api.ai_group import AiGroup

from AsposeEmailCloudSdk.api.cloud_storage_group import CloudStorageGroup
