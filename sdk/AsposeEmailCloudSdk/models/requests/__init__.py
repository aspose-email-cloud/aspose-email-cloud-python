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
