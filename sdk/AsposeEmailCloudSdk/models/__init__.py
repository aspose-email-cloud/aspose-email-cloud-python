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

# import models into model package
from AsposeEmailCloudSdk.models.account_base_request import AccountBaseRequest
from AsposeEmailCloudSdk.models.add_attachment_request import AddAttachmentRequest
from AsposeEmailCloudSdk.models.ai_bcr_image import AiBcrImage
from AsposeEmailCloudSdk.models.ai_bcr_ocr_data import AiBcrOcrData
from AsposeEmailCloudSdk.models.ai_bcr_ocr_data_part import AiBcrOcrDataPart
from AsposeEmailCloudSdk.models.ai_bcr_options import AiBcrOptions
from AsposeEmailCloudSdk.models.ai_bcr_rq import AiBcrRq
from AsposeEmailCloudSdk.models.ai_name_component import AiNameComponent
from AsposeEmailCloudSdk.models.ai_name_cultural_context import AiNameCulturalContext
from AsposeEmailCloudSdk.models.ai_name_extracted import AiNameExtracted
from AsposeEmailCloudSdk.models.ai_name_extracted_component import AiNameExtractedComponent
from AsposeEmailCloudSdk.models.ai_name_formatted import AiNameFormatted
from AsposeEmailCloudSdk.models.ai_name_gender_hypothesis import AiNameGenderHypothesis
from AsposeEmailCloudSdk.models.ai_name_match_result import AiNameMatchResult
from AsposeEmailCloudSdk.models.ai_name_mismatch import AiNameMismatch
from AsposeEmailCloudSdk.models.ai_name_parsed_rq import AiNameParsedRq
from AsposeEmailCloudSdk.models.ai_name_weighted import AiNameWeighted
from AsposeEmailCloudSdk.models.ai_name_weighted_variants import AiNameWeightedVariants
from AsposeEmailCloudSdk.models.associated_person import AssociatedPerson
from AsposeEmailCloudSdk.models.attachment_base import AttachmentBase
from AsposeEmailCloudSdk.models.base_object import BaseObject
from AsposeEmailCloudSdk.models.calendar_dto import CalendarDto
from AsposeEmailCloudSdk.models.calendar_dto_alternate_rq import CalendarDtoAlternateRq
from AsposeEmailCloudSdk.models.calendar_reminder import CalendarReminder
from AsposeEmailCloudSdk.models.contact_dto import ContactDto
from AsposeEmailCloudSdk.models.contact_photo import ContactPhoto
from AsposeEmailCloudSdk.models.content_type import ContentType
from AsposeEmailCloudSdk.models.content_type_parameter import ContentTypeParameter
from AsposeEmailCloudSdk.models.create_email_request import CreateEmailRequest
from AsposeEmailCloudSdk.models.customer_event import CustomerEvent
from AsposeEmailCloudSdk.models.disc_usage import DiscUsage
from AsposeEmailCloudSdk.models.discover_email_config_rq import DiscoverEmailConfigRq
from AsposeEmailCloudSdk.models.email_account_config import EmailAccountConfig
from AsposeEmailCloudSdk.models.email_account_request import EmailAccountRequest
from AsposeEmailCloudSdk.models.email_address import EmailAddress
from AsposeEmailCloudSdk.models.email_client_account import EmailClientAccount
from AsposeEmailCloudSdk.models.email_client_account_credentials import EmailClientAccountCredentials
from AsposeEmailCloudSdk.models.email_client_multi_account import EmailClientMultiAccount
from AsposeEmailCloudSdk.models.email_document import EmailDocument
from AsposeEmailCloudSdk.models.email_document_response import EmailDocumentResponse
from AsposeEmailCloudSdk.models.email_dto import EmailDto
from AsposeEmailCloudSdk.models.email_properties import EmailProperties
from AsposeEmailCloudSdk.models.email_property import EmailProperty
from AsposeEmailCloudSdk.models.email_property_response import EmailPropertyResponse
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
from AsposeEmailCloudSdk.models.hierarchical_object_request import HierarchicalObjectRequest
from AsposeEmailCloudSdk.models.hierarchical_object_response import HierarchicalObjectResponse
from AsposeEmailCloudSdk.models.instant_messenger_address import InstantMessengerAddress
from AsposeEmailCloudSdk.models.link import Link
from AsposeEmailCloudSdk.models.list_response_of_ai_bcr_ocr_data import ListResponseOfAiBcrOcrData
from AsposeEmailCloudSdk.models.list_response_of_ai_name_component import ListResponseOfAiNameComponent
from AsposeEmailCloudSdk.models.list_response_of_ai_name_extracted import ListResponseOfAiNameExtracted
from AsposeEmailCloudSdk.models.list_response_of_ai_name_gender_hypothesis import ListResponseOfAiNameGenderHypothesis
from AsposeEmailCloudSdk.models.list_response_of_contact_dto import ListResponseOfContactDto
from AsposeEmailCloudSdk.models.list_response_of_email_account_config import ListResponseOfEmailAccountConfig
from AsposeEmailCloudSdk.models.list_response_of_email_dto import ListResponseOfEmailDto
from AsposeEmailCloudSdk.models.list_response_of_email_thread import ListResponseOfEmailThread
from AsposeEmailCloudSdk.models.list_response_of_hierarchical_object import ListResponseOfHierarchicalObject
from AsposeEmailCloudSdk.models.list_response_of_hierarchical_object_response import ListResponseOfHierarchicalObjectResponse
from AsposeEmailCloudSdk.models.list_response_of_mail_server_folder import ListResponseOfMailServerFolder
from AsposeEmailCloudSdk.models.list_response_of_storage_file_location import ListResponseOfStorageFileLocation
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_calendar_dto import ListResponseOfStorageModelOfCalendarDto
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_contact_dto import ListResponseOfStorageModelOfContactDto
from AsposeEmailCloudSdk.models.list_response_of_storage_model_of_email_dto import ListResponseOfStorageModelOfEmailDto
from AsposeEmailCloudSdk.models.list_response_of_string import ListResponseOfString
from AsposeEmailCloudSdk.models.mail_address import MailAddress
from AsposeEmailCloudSdk.models.mail_server_folder import MailServerFolder
from AsposeEmailCloudSdk.models.mapi_attachment_dto import MapiAttachmentDto
from AsposeEmailCloudSdk.models.mapi_calendar_attendees_dto import MapiCalendarAttendeesDto
from AsposeEmailCloudSdk.models.mapi_calendar_event_recurrence_dto import MapiCalendarEventRecurrenceDto
from AsposeEmailCloudSdk.models.mapi_calendar_exception_info_dto import MapiCalendarExceptionInfoDto
from AsposeEmailCloudSdk.models.mapi_calendar_recurrence_pattern_dto import MapiCalendarRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_dto import MapiCalendarTimeZoneDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_info_dto import MapiCalendarTimeZoneInfoDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_rule_dto import MapiCalendarTimeZoneRuleDto
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
from AsposeEmailCloudSdk.models.mapi_message_item_base_dto import MapiMessageItemBaseDto
from AsposeEmailCloudSdk.models.mapi_property_descriptor import MapiPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto
from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto
from AsposeEmailCloudSdk.models.mime_response import MimeResponse
from AsposeEmailCloudSdk.models.name_value_pair import NameValuePair
from AsposeEmailCloudSdk.models.object_exist import ObjectExist
from AsposeEmailCloudSdk.models.phone_number import PhoneNumber
from AsposeEmailCloudSdk.models.postal_address import PostalAddress
from AsposeEmailCloudSdk.models.recurrence_pattern_dto import RecurrencePatternDto
from AsposeEmailCloudSdk.models.reminder_attendee import ReminderAttendee
from AsposeEmailCloudSdk.models.reminder_trigger import ReminderTrigger
from AsposeEmailCloudSdk.models.set_email_property_request import SetEmailPropertyRequest
from AsposeEmailCloudSdk.models.storage_exist import StorageExist
from AsposeEmailCloudSdk.models.storage_file import StorageFile
from AsposeEmailCloudSdk.models.storage_file_rq_of_email_client_account import StorageFileRqOfEmailClientAccount
from AsposeEmailCloudSdk.models.storage_file_rq_of_email_client_multi_account import StorageFileRqOfEmailClientMultiAccount
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation
from AsposeEmailCloudSdk.models.storage_model_of_calendar_dto import StorageModelOfCalendarDto
from AsposeEmailCloudSdk.models.storage_model_of_contact_dto import StorageModelOfContactDto
from AsposeEmailCloudSdk.models.storage_model_of_email_dto import StorageModelOfEmailDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_calendar_dto import StorageModelRqOfCalendarDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_contact_dto import StorageModelRqOfContactDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_email_dto import StorageModelRqOfEmailDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_mapi_calendar_dto import StorageModelRqOfMapiCalendarDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_mapi_contact_dto import StorageModelRqOfMapiContactDto
from AsposeEmailCloudSdk.models.storage_model_rq_of_mapi_message_dto import StorageModelRqOfMapiMessageDto
from AsposeEmailCloudSdk.models.url import Url
from AsposeEmailCloudSdk.models.value_response import ValueResponse
from AsposeEmailCloudSdk.models.value_t_of_boolean import ValueTOfBoolean
from AsposeEmailCloudSdk.models.ai_bcr_base64_image import AiBcrBase64Image
from AsposeEmailCloudSdk.models.ai_bcr_base64_rq import AiBcrBase64Rq
from AsposeEmailCloudSdk.models.ai_bcr_image_storage_file import AiBcrImageStorageFile
from AsposeEmailCloudSdk.models.ai_bcr_parse_ocr_data_rq import AiBcrParseOcrDataRq
from AsposeEmailCloudSdk.models.ai_bcr_storage_image_rq import AiBcrStorageImageRq
from AsposeEmailCloudSdk.models.ai_name_parsed_match_rq import AiNameParsedMatchRq
from AsposeEmailCloudSdk.models.alternate_view import AlternateView
from AsposeEmailCloudSdk.models.append_email_account_base_request import AppendEmailAccountBaseRequest
from AsposeEmailCloudSdk.models.attachment import Attachment
from AsposeEmailCloudSdk.models.calendar_dto_list import CalendarDtoList
from AsposeEmailCloudSdk.models.contact_dto_list import ContactDtoList
from AsposeEmailCloudSdk.models.create_folder_base_request import CreateFolderBaseRequest
from AsposeEmailCloudSdk.models.daily_recurrence_pattern_dto import DailyRecurrencePatternDto
from AsposeEmailCloudSdk.models.delete_email_thread_account_rq import DeleteEmailThreadAccountRq
from AsposeEmailCloudSdk.models.delete_folder_base_request import DeleteFolderBaseRequest
from AsposeEmailCloudSdk.models.delete_message_base_request import DeleteMessageBaseRequest
from AsposeEmailCloudSdk.models.discover_email_config_oauth import DiscoverEmailConfigOauth
from AsposeEmailCloudSdk.models.discover_email_config_password import DiscoverEmailConfigPassword
from AsposeEmailCloudSdk.models.email_account_config_list import EmailAccountConfigList
from AsposeEmailCloudSdk.models.email_client_account_oauth_credentials import EmailClientAccountOauthCredentials
from AsposeEmailCloudSdk.models.email_client_account_password_credentials import EmailClientAccountPasswordCredentials
from AsposeEmailCloudSdk.models.email_dto_list import EmailDtoList
from AsposeEmailCloudSdk.models.email_thread_list import EmailThreadList
from AsposeEmailCloudSdk.models.email_thread_read_flag_rq import EmailThreadReadFlagRq
from AsposeEmailCloudSdk.models.file_version import FileVersion
from AsposeEmailCloudSdk.models.hierarchical_object import HierarchicalObject
from AsposeEmailCloudSdk.models.indexed_hierarchical_object import IndexedHierarchicalObject
from AsposeEmailCloudSdk.models.indexed_primitive_object import IndexedPrimitiveObject
from AsposeEmailCloudSdk.models.linked_resource import LinkedResource
from AsposeEmailCloudSdk.models.mapi_binary_property_dto import MapiBinaryPropertyDto
from AsposeEmailCloudSdk.models.mapi_boolean_property_dto import MapiBooleanPropertyDto
from AsposeEmailCloudSdk.models.mapi_calendar_daily_recurrence_pattern_dto import MapiCalendarDailyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_dto import MapiCalendarDto
from AsposeEmailCloudSdk.models.mapi_calendar_weekly_recurrence_pattern_dto import MapiCalendarWeeklyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_yearly_and_monthly_recurrence_pattern_dto import MapiCalendarYearlyAndMonthlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_contact_dto import MapiContactDto
from AsposeEmailCloudSdk.models.mapi_contact_photo_dto import MapiContactPhotoDto
from AsposeEmailCloudSdk.models.mapi_date_time_property_dto import MapiDateTimePropertyDto
from AsposeEmailCloudSdk.models.mapi_file_as_property_dto import MapiFileAsPropertyDto
from AsposeEmailCloudSdk.models.mapi_importance_property_dto import MapiImportancePropertyDto
from AsposeEmailCloudSdk.models.mapi_int_property_dto import MapiIntPropertyDto
from AsposeEmailCloudSdk.models.mapi_known_property_descriptor import MapiKnownPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_legacy_free_busy_property_dto import MapiLegacyFreeBusyPropertyDto
from AsposeEmailCloudSdk.models.mapi_message_dto import MapiMessageDto
from AsposeEmailCloudSdk.models.mapi_multi_int_property_dto import MapiMultiIntPropertyDto
from AsposeEmailCloudSdk.models.mapi_multi_string_property_dto import MapiMultiStringPropertyDto
from AsposeEmailCloudSdk.models.mapi_physical_address_index_property_dto import MapiPhysicalAddressIndexPropertyDto
from AsposeEmailCloudSdk.models.mapi_pid_property_descriptor import MapiPidPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_response_type_property_dto import MapiResponseTypePropertyDto
from AsposeEmailCloudSdk.models.mapi_string_property_dto import MapiStringPropertyDto
from AsposeEmailCloudSdk.models.monthly_recurrence_pattern_dto import MonthlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.move_email_message_rq import MoveEmailMessageRq
from AsposeEmailCloudSdk.models.move_email_thread_rq import MoveEmailThreadRq
from AsposeEmailCloudSdk.models.primitive_object import PrimitiveObject
from AsposeEmailCloudSdk.models.save_email_account_request import SaveEmailAccountRequest
from AsposeEmailCloudSdk.models.save_o_auth_email_account_request import SaveOAuthEmailAccountRequest
from AsposeEmailCloudSdk.models.send_email_base_request import SendEmailBaseRequest
from AsposeEmailCloudSdk.models.send_email_mime_base_request import SendEmailMimeBaseRequest
from AsposeEmailCloudSdk.models.send_email_model_rq import SendEmailModelRq
from AsposeEmailCloudSdk.models.set_message_read_flag_account_base_request import SetMessageReadFlagAccountBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation
from AsposeEmailCloudSdk.models.task_regenerating_pattern_dto import TaskRegeneratingPatternDto
from AsposeEmailCloudSdk.models.weekly_recurrence_pattern_dto import WeeklyRecurrencePatternDto
from AsposeEmailCloudSdk.models.yearly_recurrence_pattern_dto import YearlyRecurrencePatternDto
from AsposeEmailCloudSdk.models.ai_bcr_parse_storage_rq import AiBcrParseStorageRq
from AsposeEmailCloudSdk.models.append_email_base_request import AppendEmailBaseRequest
from AsposeEmailCloudSdk.models.append_email_mime_base_request import AppendEmailMimeBaseRequest
from AsposeEmailCloudSdk.models.append_email_model_rq import AppendEmailModelRq
from AsposeEmailCloudSdk.models.mapi_pid_lid_property_descriptor import MapiPidLidPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_pid_name_property_descriptor import MapiPidNamePropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_pid_tag_property_descriptor import MapiPidTagPropertyDescriptor

from AsposeEmailCloudSdk.models.requests.add_calendar_attachment_request import AddCalendarAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_contact_attachment_request import AddContactAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_email_attachment_request import AddEmailAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_mapi_attachment_request import AddMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_ocr_request import AiBcrOcrRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_ocr_storage_request import AiBcrOcrStorageRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_parse_model_request import AiBcrParseModelRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_parse_ocr_data_model_request import AiBcrParseOcrDataModelRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_parse_request import AiBcrParseRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_parse_storage_request import AiBcrParseStorageRequest
from AsposeEmailCloudSdk.models.requests.ai_name_complete_request import AiNameCompleteRequest
from AsposeEmailCloudSdk.models.requests.ai_name_expand_parsed_request import AiNameExpandParsedRequest
from AsposeEmailCloudSdk.models.requests.ai_name_expand_request import AiNameExpandRequest
from AsposeEmailCloudSdk.models.requests.ai_name_format_parsed_request import AiNameFormatParsedRequest
from AsposeEmailCloudSdk.models.requests.ai_name_format_request import AiNameFormatRequest
from AsposeEmailCloudSdk.models.requests.ai_name_genderize_parsed_request import AiNameGenderizeParsedRequest
from AsposeEmailCloudSdk.models.requests.ai_name_genderize_request import AiNameGenderizeRequest
from AsposeEmailCloudSdk.models.requests.ai_name_match_parsed_request import AiNameMatchParsedRequest
from AsposeEmailCloudSdk.models.requests.ai_name_match_request import AiNameMatchRequest
from AsposeEmailCloudSdk.models.requests.ai_name_parse_email_address_request import AiNameParseEmailAddressRequest
from AsposeEmailCloudSdk.models.requests.ai_name_parse_request import AiNameParseRequest
from AsposeEmailCloudSdk.models.requests.append_email_message_request import AppendEmailMessageRequest
from AsposeEmailCloudSdk.models.requests.append_email_model_message_request import AppendEmailModelMessageRequest
from AsposeEmailCloudSdk.models.requests.append_mime_message_request import AppendMimeMessageRequest
from AsposeEmailCloudSdk.models.requests.convert_calendar_model_to_alternate_request import ConvertCalendarModelToAlternateRequest
from AsposeEmailCloudSdk.models.requests.convert_calendar_model_to_file_request import ConvertCalendarModelToFileRequest
from AsposeEmailCloudSdk.models.requests.convert_calendar_model_to_mapi_model_request import ConvertCalendarModelToMapiModelRequest
from AsposeEmailCloudSdk.models.requests.convert_calendar_request import ConvertCalendarRequest
from AsposeEmailCloudSdk.models.requests.convert_contact_model_to_file_request import ConvertContactModelToFileRequest
from AsposeEmailCloudSdk.models.requests.convert_contact_model_to_mapi_model_request import ConvertContactModelToMapiModelRequest
from AsposeEmailCloudSdk.models.requests.convert_contact_request import ConvertContactRequest
from AsposeEmailCloudSdk.models.requests.convert_email_model_to_file_request import ConvertEmailModelToFileRequest
from AsposeEmailCloudSdk.models.requests.convert_email_model_to_mapi_model_request import ConvertEmailModelToMapiModelRequest
from AsposeEmailCloudSdk.models.requests.convert_email_request import ConvertEmailRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_calendar_model_to_calendar_model_request import ConvertMapiCalendarModelToCalendarModelRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_calendar_model_to_file_request import ConvertMapiCalendarModelToFileRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_contact_model_to_contact_model_request import ConvertMapiContactModelToContactModelRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_contact_model_to_file_request import ConvertMapiContactModelToFileRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_message_model_to_email_model_request import ConvertMapiMessageModelToEmailModelRequest
from AsposeEmailCloudSdk.models.requests.convert_mapi_message_model_to_file_request import ConvertMapiMessageModelToFileRequest
from AsposeEmailCloudSdk.models.requests.copy_file_request import CopyFileRequest
from AsposeEmailCloudSdk.models.requests.copy_folder_request import CopyFolderRequest
from AsposeEmailCloudSdk.models.requests.create_calendar_request import CreateCalendarRequest
from AsposeEmailCloudSdk.models.requests.create_contact_request import CreateContactRequest
from AsposeEmailCloudSdk.models.requests.create_email_folder_request import CreateEmailFolderRequest
from AsposeEmailCloudSdk.models.requests.create_email_request import CreateEmailRequest
from AsposeEmailCloudSdk.models.requests.create_folder_request import CreateFolderRequest
from AsposeEmailCloudSdk.models.requests.create_mapi_request import CreateMapiRequest
from AsposeEmailCloudSdk.models.requests.delete_calendar_property_request import DeleteCalendarPropertyRequest
from AsposeEmailCloudSdk.models.requests.delete_contact_property_request import DeleteContactPropertyRequest
from AsposeEmailCloudSdk.models.requests.delete_email_folder_request import DeleteEmailFolderRequest
from AsposeEmailCloudSdk.models.requests.delete_email_message_request import DeleteEmailMessageRequest
from AsposeEmailCloudSdk.models.requests.delete_email_thread_request import DeleteEmailThreadRequest
from AsposeEmailCloudSdk.models.requests.delete_file_request import DeleteFileRequest
from AsposeEmailCloudSdk.models.requests.delete_folder_request import DeleteFolderRequest
from AsposeEmailCloudSdk.models.requests.delete_mapi_attachment_request import DeleteMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.delete_mapi_properties_request import DeleteMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.discover_email_config_oauth_request import DiscoverEmailConfigOauthRequest
from AsposeEmailCloudSdk.models.requests.discover_email_config_password_request import DiscoverEmailConfigPasswordRequest
from AsposeEmailCloudSdk.models.requests.discover_email_config_request import DiscoverEmailConfigRequest
from AsposeEmailCloudSdk.models.requests.download_file_request import DownloadFileRequest
from AsposeEmailCloudSdk.models.requests.fetch_email_message_request import FetchEmailMessageRequest
from AsposeEmailCloudSdk.models.requests.fetch_email_model_request import FetchEmailModelRequest
from AsposeEmailCloudSdk.models.requests.fetch_email_thread_messages_request import FetchEmailThreadMessagesRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_as_file_request import GetCalendarAsFileRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_attachment_request import GetCalendarAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_file_as_mapi_model_request import GetCalendarFileAsMapiModelRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_file_as_model_request import GetCalendarFileAsModelRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_list_request import GetCalendarListRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_model_as_alternate_request import GetCalendarModelAsAlternateRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_model_list_request import GetCalendarModelListRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_model_request import GetCalendarModelRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_request import GetCalendarRequest
from AsposeEmailCloudSdk.models.requests.get_contact_as_file_request import GetContactAsFileRequest
from AsposeEmailCloudSdk.models.requests.get_contact_attachment_request import GetContactAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_contact_file_as_mapi_model_request import GetContactFileAsMapiModelRequest
from AsposeEmailCloudSdk.models.requests.get_contact_file_as_model_request import GetContactFileAsModelRequest
from AsposeEmailCloudSdk.models.requests.get_contact_list_request import GetContactListRequest
from AsposeEmailCloudSdk.models.requests.get_contact_model_list_request import GetContactModelListRequest
from AsposeEmailCloudSdk.models.requests.get_contact_model_request import GetContactModelRequest
from AsposeEmailCloudSdk.models.requests.get_contact_properties_request import GetContactPropertiesRequest
from AsposeEmailCloudSdk.models.requests.get_disc_usage_request import GetDiscUsageRequest
from AsposeEmailCloudSdk.models.requests.get_email_as_file_request import GetEmailAsFileRequest
from AsposeEmailCloudSdk.models.requests.get_email_attachment_request import GetEmailAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_email_client_account_request import GetEmailClientAccountRequest
from AsposeEmailCloudSdk.models.requests.get_email_client_multi_account_request import GetEmailClientMultiAccountRequest
from AsposeEmailCloudSdk.models.requests.get_email_file_as_mapi_model_request import GetEmailFileAsMapiModelRequest
from AsposeEmailCloudSdk.models.requests.get_email_file_as_model_request import GetEmailFileAsModelRequest
from AsposeEmailCloudSdk.models.requests.get_email_model_list_request import GetEmailModelListRequest
from AsposeEmailCloudSdk.models.requests.get_email_model_request import GetEmailModelRequest
from AsposeEmailCloudSdk.models.requests.get_email_property_request import GetEmailPropertyRequest
from AsposeEmailCloudSdk.models.requests.get_email_request import GetEmailRequest
from AsposeEmailCloudSdk.models.requests.get_files_list_request import GetFilesListRequest
from AsposeEmailCloudSdk.models.requests.get_file_versions_request import GetFileVersionsRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_attachments_request import GetMapiAttachmentsRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_attachment_request import GetMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_calendar_model_request import GetMapiCalendarModelRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_contact_model_request import GetMapiContactModelRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_list_request import GetMapiListRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_message_model_request import GetMapiMessageModelRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_properties_request import GetMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.is_email_address_disposable_request import IsEmailAddressDisposableRequest
from AsposeEmailCloudSdk.models.requests.list_email_folders_request import ListEmailFoldersRequest
from AsposeEmailCloudSdk.models.requests.list_email_messages_request import ListEmailMessagesRequest
from AsposeEmailCloudSdk.models.requests.list_email_models_request import ListEmailModelsRequest
from AsposeEmailCloudSdk.models.requests.list_email_threads_request import ListEmailThreadsRequest
from AsposeEmailCloudSdk.models.requests.move_email_message_request import MoveEmailMessageRequest
from AsposeEmailCloudSdk.models.requests.move_email_thread_request import MoveEmailThreadRequest
from AsposeEmailCloudSdk.models.requests.move_file_request import MoveFileRequest
from AsposeEmailCloudSdk.models.requests.move_folder_request import MoveFolderRequest
from AsposeEmailCloudSdk.models.requests.object_exists_request import ObjectExistsRequest
from AsposeEmailCloudSdk.models.requests.save_calendar_model_request import SaveCalendarModelRequest
from AsposeEmailCloudSdk.models.requests.save_contact_model_request import SaveContactModelRequest
from AsposeEmailCloudSdk.models.requests.save_email_client_account_request import SaveEmailClientAccountRequest
from AsposeEmailCloudSdk.models.requests.save_email_client_multi_account_request import SaveEmailClientMultiAccountRequest
from AsposeEmailCloudSdk.models.requests.save_email_model_request import SaveEmailModelRequest
from AsposeEmailCloudSdk.models.requests.save_mail_account_request import SaveMailAccountRequest
from AsposeEmailCloudSdk.models.requests.save_mail_o_auth_account_request import SaveMailOAuthAccountRequest
from AsposeEmailCloudSdk.models.requests.save_mapi_calendar_model_request import SaveMapiCalendarModelRequest
from AsposeEmailCloudSdk.models.requests.save_mapi_contact_model_request import SaveMapiContactModelRequest
from AsposeEmailCloudSdk.models.requests.save_mapi_message_model_request import SaveMapiMessageModelRequest
from AsposeEmailCloudSdk.models.requests.send_email_mime_request import SendEmailMimeRequest
from AsposeEmailCloudSdk.models.requests.send_email_model_request import SendEmailModelRequest
from AsposeEmailCloudSdk.models.requests.send_email_request import SendEmailRequest
from AsposeEmailCloudSdk.models.requests.set_email_property_request import SetEmailPropertyRequest
from AsposeEmailCloudSdk.models.requests.set_email_read_flag_request import SetEmailReadFlagRequest
from AsposeEmailCloudSdk.models.requests.set_email_thread_read_flag_request import SetEmailThreadReadFlagRequest
from AsposeEmailCloudSdk.models.requests.storage_exists_request import StorageExistsRequest
from AsposeEmailCloudSdk.models.requests.update_calendar_properties_request import UpdateCalendarPropertiesRequest
from AsposeEmailCloudSdk.models.requests.update_contact_properties_request import UpdateContactPropertiesRequest
from AsposeEmailCloudSdk.models.requests.update_mapi_properties_request import UpdateMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.upload_file_request import UploadFileRequest
