#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="__init__.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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
from AsposeEmailCloudSdk.models.base_object import BaseObject
from AsposeEmailCloudSdk.models.create_email_request import CreateEmailRequest
from AsposeEmailCloudSdk.models.disc_usage import DiscUsage
from AsposeEmailCloudSdk.models.email_account_request import EmailAccountRequest
from AsposeEmailCloudSdk.models.email_document import EmailDocument
from AsposeEmailCloudSdk.models.email_document_response import EmailDocumentResponse
from AsposeEmailCloudSdk.models.email_properties import EmailProperties
from AsposeEmailCloudSdk.models.email_property import EmailProperty
from AsposeEmailCloudSdk.models.email_property_response import EmailPropertyResponse
from AsposeEmailCloudSdk.models.error import Error
from AsposeEmailCloudSdk.models.error_details import ErrorDetails
from AsposeEmailCloudSdk.models.file_versions import FileVersions
from AsposeEmailCloudSdk.models.files_list import FilesList
from AsposeEmailCloudSdk.models.files_upload_result import FilesUploadResult
from AsposeEmailCloudSdk.models.hierarchical_object_request import HierarchicalObjectRequest
from AsposeEmailCloudSdk.models.hierarchical_object_response import HierarchicalObjectResponse
from AsposeEmailCloudSdk.models.link import Link
from AsposeEmailCloudSdk.models.list_response_of_ai_bcr_ocr_data import ListResponseOfAiBcrOcrData
from AsposeEmailCloudSdk.models.list_response_of_ai_name_component import ListResponseOfAiNameComponent
from AsposeEmailCloudSdk.models.list_response_of_ai_name_extracted import ListResponseOfAiNameExtracted
from AsposeEmailCloudSdk.models.list_response_of_ai_name_gender_hypothesis import ListResponseOfAiNameGenderHypothesis
from AsposeEmailCloudSdk.models.list_response_of_hierarchical_object import ListResponseOfHierarchicalObject
from AsposeEmailCloudSdk.models.list_response_of_hierarchical_object_response import ListResponseOfHierarchicalObjectResponse
from AsposeEmailCloudSdk.models.list_response_of_mail_server_folder import ListResponseOfMailServerFolder
from AsposeEmailCloudSdk.models.list_response_of_storage_file_location import ListResponseOfStorageFileLocation
from AsposeEmailCloudSdk.models.list_response_of_string import ListResponseOfString
from AsposeEmailCloudSdk.models.mail_server_folder import MailServerFolder
from AsposeEmailCloudSdk.models.mime_response import MimeResponse
from AsposeEmailCloudSdk.models.object_exist import ObjectExist
from AsposeEmailCloudSdk.models.set_email_property_request import SetEmailPropertyRequest
from AsposeEmailCloudSdk.models.storage_exist import StorageExist
from AsposeEmailCloudSdk.models.storage_file import StorageFile
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation
from AsposeEmailCloudSdk.models.value_response import ValueResponse
from AsposeEmailCloudSdk.models.ai_bcr_base64_image import AiBcrBase64Image
from AsposeEmailCloudSdk.models.ai_bcr_base64_rq import AiBcrBase64Rq
from AsposeEmailCloudSdk.models.ai_bcr_image_storage_file import AiBcrImageStorageFile
from AsposeEmailCloudSdk.models.ai_bcr_storage_image_rq import AiBcrStorageImageRq
from AsposeEmailCloudSdk.models.ai_name_parsed_match_rq import AiNameParsedMatchRq
from AsposeEmailCloudSdk.models.append_email_account_base_request import AppendEmailAccountBaseRequest
from AsposeEmailCloudSdk.models.create_folder_base_request import CreateFolderBaseRequest
from AsposeEmailCloudSdk.models.delete_folder_base_request import DeleteFolderBaseRequest
from AsposeEmailCloudSdk.models.delete_message_base_request import DeleteMessageBaseRequest
from AsposeEmailCloudSdk.models.file_version import FileVersion
from AsposeEmailCloudSdk.models.hierarchical_object import HierarchicalObject
from AsposeEmailCloudSdk.models.indexed_hierarchical_object import IndexedHierarchicalObject
from AsposeEmailCloudSdk.models.indexed_primitive_object import IndexedPrimitiveObject
from AsposeEmailCloudSdk.models.primitive_object import PrimitiveObject
from AsposeEmailCloudSdk.models.save_email_account_request import SaveEmailAccountRequest
from AsposeEmailCloudSdk.models.save_o_auth_email_account_request import SaveOAuthEmailAccountRequest
from AsposeEmailCloudSdk.models.send_email_base_request import SendEmailBaseRequest
from AsposeEmailCloudSdk.models.send_email_mime_base_request import SendEmailMimeBaseRequest
from AsposeEmailCloudSdk.models.set_message_read_flag_account_base_request import SetMessageReadFlagAccountBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation
from AsposeEmailCloudSdk.models.ai_bcr_parse_storage_rq import AiBcrParseStorageRq
from AsposeEmailCloudSdk.models.append_email_base_request import AppendEmailBaseRequest
from AsposeEmailCloudSdk.models.append_email_mime_base_request import AppendEmailMimeBaseRequest

from AsposeEmailCloudSdk.models.requests.add_calendar_attachment_request import AddCalendarAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_contact_attachment_request import AddContactAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_email_attachment_request import AddEmailAttachmentRequest
from AsposeEmailCloudSdk.models.requests.add_mapi_attachment_request import AddMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_ocr_request import AiBcrOcrRequest
from AsposeEmailCloudSdk.models.requests.ai_bcr_ocr_storage_request import AiBcrOcrStorageRequest
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
from AsposeEmailCloudSdk.models.requests.append_mime_message_request import AppendMimeMessageRequest
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
from AsposeEmailCloudSdk.models.requests.delete_file_request import DeleteFileRequest
from AsposeEmailCloudSdk.models.requests.delete_folder_request import DeleteFolderRequest
from AsposeEmailCloudSdk.models.requests.delete_mapi_attachment_request import DeleteMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.delete_mapi_properties_request import DeleteMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.download_file_request import DownloadFileRequest
from AsposeEmailCloudSdk.models.requests.fetch_email_message_request import FetchEmailMessageRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_attachment_request import GetCalendarAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_list_request import GetCalendarListRequest
from AsposeEmailCloudSdk.models.requests.get_calendar_request import GetCalendarRequest
from AsposeEmailCloudSdk.models.requests.get_contact_attachment_request import GetContactAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_contact_list_request import GetContactListRequest
from AsposeEmailCloudSdk.models.requests.get_contact_properties_request import GetContactPropertiesRequest
from AsposeEmailCloudSdk.models.requests.get_disc_usage_request import GetDiscUsageRequest
from AsposeEmailCloudSdk.models.requests.get_email_attachment_request import GetEmailAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_email_property_request import GetEmailPropertyRequest
from AsposeEmailCloudSdk.models.requests.get_email_request import GetEmailRequest
from AsposeEmailCloudSdk.models.requests.get_files_list_request import GetFilesListRequest
from AsposeEmailCloudSdk.models.requests.get_file_versions_request import GetFileVersionsRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_attachments_request import GetMapiAttachmentsRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_attachment_request import GetMapiAttachmentRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_list_request import GetMapiListRequest
from AsposeEmailCloudSdk.models.requests.get_mapi_properties_request import GetMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.list_email_folders_request import ListEmailFoldersRequest
from AsposeEmailCloudSdk.models.requests.list_email_messages_request import ListEmailMessagesRequest
from AsposeEmailCloudSdk.models.requests.move_file_request import MoveFileRequest
from AsposeEmailCloudSdk.models.requests.move_folder_request import MoveFolderRequest
from AsposeEmailCloudSdk.models.requests.object_exists_request import ObjectExistsRequest
from AsposeEmailCloudSdk.models.requests.save_mail_account_request import SaveMailAccountRequest
from AsposeEmailCloudSdk.models.requests.save_mail_o_auth_account_request import SaveMailOAuthAccountRequest
from AsposeEmailCloudSdk.models.requests.send_email_mime_request import SendEmailMimeRequest
from AsposeEmailCloudSdk.models.requests.send_email_request import SendEmailRequest
from AsposeEmailCloudSdk.models.requests.set_email_property_request import SetEmailPropertyRequest
from AsposeEmailCloudSdk.models.requests.set_email_read_flag_request import SetEmailReadFlagRequest
from AsposeEmailCloudSdk.models.requests.storage_exists_request import StorageExistsRequest
from AsposeEmailCloudSdk.models.requests.update_calendar_properties_request import UpdateCalendarPropertiesRequest
from AsposeEmailCloudSdk.models.requests.update_contact_properties_request import UpdateContactPropertiesRequest
from AsposeEmailCloudSdk.models.requests.update_mapi_properties_request import UpdateMapiPropertiesRequest
from AsposeEmailCloudSdk.models.requests.upload_file_request import UploadFileRequest
