#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="email_api.py">
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

import six

from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.configuration import Configuration
from AsposeEmailCloudSdk.rest import ApiException


class EmailApi(object):
    """
    Aspose.Email Cloud API

    """

    def __init__(self, app_key=None, app_sid=None, base_url=None,
                 api_version=None, debug=False):
        """
        Initializes a new instance of the EmailApi class.

        :param app_key: The app key.
        :param app_sid: The app sid.
        :param base_url: The base URL.
        :param api_version: API version.
        :param debug: If debug mode is enabled. False by default.
        :param on_premise:
            True for on-premise solution with metered license usage.
            False for Aspose Cloud-hosted solution usage, default.
        """
        configuration = Configuration(app_key=app_key,
                                      app_sid=app_sid,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug)
        self.api_client = ApiClient(configuration)

    def add_calendar_attachment(self, request):
        """Adds an attachment to iCalendar file             


        :param request add_calendar_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_calendar_attachment_async(self, request):
        """Adds an attachment to iCalendar file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request add_calendar_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def add_contact_attachment(self, request):
        """Add attachment to contact document             


        :param request add_contact_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_contact_attachment_async(self, request):
        """Add attachment to contact document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request add_contact_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def add_email_attachment(self, request):
        """Adds an attachment to Email document             


        :param request add_email_attachment_request object with parameters
        :return: EmailDocumentResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'EmailDocumentResponse')

    def add_email_attachment_async(self, request):
        """Adds an attachment to Email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request add_email_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocumentResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'EmailDocumentResponse')

    def add_mapi_attachment(self, request):
        """Add attachment to document             


        :param request add_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_mapi_attachment_async(self, request):
        """Add attachment to document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request add_mapi_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def ai_bcr_ocr(self, request):
        """Ocr images             


        :param request ai_bcr_ocr_request object with parameters
        :return: ListResponseOfAiBcrOcrData
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_async(self, request):
        """Ocr images             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_ocr_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiBcrOcrData)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_storage(self, request):
        """Ocr images from storage             


        :param request ai_bcr_ocr_storage_request object with parameters
        :return: ListResponseOfAiBcrOcrData
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_storage_async(self, request):
        """Ocr images from storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_ocr_storage_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiBcrOcrData)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_parse(self, request):
        """Parse images to vCard properties             


        :param request ai_bcr_parse_request object with parameters
        :return: ListResponseOfHierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_async(self, request):
        """Parse images to vCard properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_parse_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_ocr_data(self, request):
        """Parse OCR data to vCard properties             


        :param request ai_bcr_parse_ocr_data_request object with parameters
        :return: ListResponseOfHierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_ocr_data_async(self, request):
        """Parse OCR data to vCard properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_parse_ocr_data_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_ocr_data_storage(self, request):
        """Parse vCards from OCR data and save them to Storage             


        :param request ai_bcr_parse_ocr_data_storage_request object with parameters
        :return: ListResponseOfStorageFileLocation
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_bcr_parse_ocr_data_storage_async(self, request):
        """Parse vCards from OCR data and save them to Storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_parse_ocr_data_storage_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfStorageFileLocation)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_bcr_parse_storage(self, request):
        """Parse images from storage to vCard files             


        :param request ai_bcr_parse_storage_request object with parameters
        :return: ListResponseOfStorageFileLocation
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_bcr_parse_storage_async(self, request):
        """Parse images from storage to vCard files             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_bcr_parse_storage_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfStorageFileLocation)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_name_complete(self, request):
        """The call proposes k most probable names for given starting characters             


        :param request ai_name_complete_request object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_complete_async(self, request):
        """The call proposes k most probable names for given starting characters             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_complete_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand(self, request):
        """Expands a person&#39;s name into a list of possible alternatives using options for expanding instructions             


        :param request ai_name_expand_request object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand_async(self, request):
        """Expands a person&#39;s name into a list of possible alternatives using options for expanding instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_expand_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand_parsed(self, request):
        """Expands a person&#39;s parsed name into a list of possible alternatives using options for expanding instructions             


        :param request ai_name_expand_parsed_request object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameWeightedVariants')

    def ai_name_expand_parsed_async(self, request):
        """Expands a person&#39;s parsed name into a list of possible alternatives using options for expanding instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_expand_parsed_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameWeightedVariants')

    def ai_name_format(self, request):
        """Formats a person&#39;s name in correct case and name order using options for formatting instructions             


        :param request ai_name_format_request object with parameters
        :return: AiNameFormatted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameFormatted')

    def ai_name_format_async(self, request):
        """Formats a person&#39;s name in correct case and name order using options for formatting instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_format_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameFormatted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameFormatted')

    def ai_name_format_parsed(self, request):
        """Formats a person&#39;s parsed name in correct case and name order using options for formatting instructions             


        :param request ai_name_format_parsed_request object with parameters
        :return: AiNameFormatted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameFormatted')

    def ai_name_format_parsed_async(self, request):
        """Formats a person&#39;s parsed name in correct case and name order using options for formatting instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_format_parsed_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameFormatted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameFormatted')

    def ai_name_genderize(self, request):
        """Detect person&#39;s gender from name string             


        :param request ai_name_genderize_request object with parameters
        :return: ListResponseOfAiNameGenderHypothesis
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_async(self, request):
        """Detect person&#39;s gender from name string             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_genderize_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameGenderHypothesis)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_parsed(self, request):
        """Detect person&#39;s gender from parsed name             


        :param request ai_name_genderize_parsed_request object with parameters
        :return: ListResponseOfAiNameGenderHypothesis
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_parsed_async(self, request):
        """Detect person&#39;s gender from parsed name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_genderize_parsed_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameGenderHypothesis)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_match(self, request):
        """Compare people&#39;s names. Uses options for comparing instructions             


        :param request ai_name_match_request object with parameters
        :return: AiNameMatchResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameMatchResult')

    def ai_name_match_async(self, request):
        """Compare people&#39;s names. Uses options for comparing instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_match_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameMatchResult)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameMatchResult')

    def ai_name_match_parsed(self, request):
        """Compare people&#39;s parsed names and attributes. Uses options for comparing instructions             


        :param request ai_name_match_parsed_request object with parameters
        :return: AiNameMatchResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameMatchResult')

    def ai_name_match_parsed_async(self, request):
        """Compare people&#39;s parsed names and attributes. Uses options for comparing instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_match_parsed_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameMatchResult)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameMatchResult')

    def ai_name_parse(self, request):
        """Parse name to components             


        :param request ai_name_parse_request object with parameters
        :return: ListResponseOfAiNameComponent
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameComponent')

    def ai_name_parse_async(self, request):
        """Parse name to components             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_parse_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameComponent)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameComponent')

    def ai_name_parse_email_address(self, request):
        """Parse person&#39;s name out of an email address             


        :param request ai_name_parse_email_address_request object with parameters
        :return: ListResponseOfAiNameExtracted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameExtracted')

    def ai_name_parse_email_address_async(self, request):
        """Parse person&#39;s name out of an email address             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ai_name_parse_email_address_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameExtracted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameExtracted')

    def append_email_message(self, request):
        """Adds an email from *.eml file to specified folder in email account             


        :param request append_email_message_request object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailPropertyResponse')

    def append_email_message_async(self, request):
        """Adds an email from *.eml file to specified folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request append_email_message_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailPropertyResponse')

    def append_mime_message(self, request):
        """Adds an email from MIME to specified folder in email account             


        :param request append_mime_message_request object with parameters
        :return: ValueResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'ValueResponse')

    def append_mime_message_async(self, request):
        """Adds an email from MIME to specified folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request append_mime_message_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ValueResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'ValueResponse')

    def copy_file(self, request):
        """Copy file


        :param request copy_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_file_async(self, request):
        """Copy file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request copy_file_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def copy_folder(self, request):
        """Copy folder


        :param request copy_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_folder_async(self, request):
        """Copy folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request copy_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_calendar(self, request):
        """Create calendar file             


        :param request create_calendar_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_calendar_async(self, request):
        """Create calendar file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_calendar_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_contact(self, request):
        """Create contact document             


        :param request create_contact_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_contact_async(self, request):
        """Create contact document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_contact_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_email(self, request):
        """Create an email document             


        :param request create_email_request object with parameters
        :return: EmailDocumentResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailDocumentResponse')

    def create_email_async(self, request):
        """Create an email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_email_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocumentResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailDocumentResponse')

    def create_email_folder(self, request):
        """Create new folder in email account             


        :param request create_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_email_folder_async(self, request):
        """Create new folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_email_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_folder(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_folder_async(self, request):
        """Create the folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_mapi(self, request):
        """Create new document             


        :param request create_mapi_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_mapi_async(self, request):
        """Create new document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request create_mapi_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def delete_calendar_property(self, request):
        """Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             


        :param request delete_calendar_property_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_calendar_property_async(self, request):
        """Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_calendar_property_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_contact_property(self, request):
        """Delete property from indexed property list             


        :param request delete_contact_property_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_contact_property_async(self, request):
        """Delete property from indexed property list             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_contact_property_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_folder(self, request):
        """Delete a folder in email account             


        :param request delete_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_folder_async(self, request):
        """Delete a folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_email_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_message(self, request):
        """Delete message from email account by id             


        :param request delete_email_message_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_message_async(self, request):
        """Delete message from email account by id             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_email_message_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_file(self, request):
        """Delete file


        :param request delete_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_file_async(self, request):
        """Delete file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_file_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_folder(self, request):
        """Delete folder


        :param request delete_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_folder_async(self, request):
        """Delete folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_mapi_attachment(self, request):
        """Remove attachment from document             


        :param request delete_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_attachment_async(self, request):
        """Remove attachment from document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_mapi_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_mapi_properties(self, request):
        """Delete document properties             


        :param request delete_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_properties_async(self, request):
        """Delete document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request delete_mapi_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def download_file(self, request):
        """Download file


        :param request download_file_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def download_file_async(self, request):
        """Download file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request download_file_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def fetch_email_message(self, request):
        """Fetch message mime from email account             


        :param request fetch_email_message_request object with parameters
        :return: MimeResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'MimeResponse')

    def fetch_email_message_async(self, request):
        """Fetch message mime from email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request fetch_email_message_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns MimeResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'MimeResponse')

    def get_calendar(self, request):
        """Get calendar file properties             


        :param request get_calendar_request object with parameters
        :return: HierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObject')

    def get_calendar_async(self, request):
        """Get calendar file properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_calendar_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObject')

    def get_calendar_attachment(self, request):
        """Get iCalendar document attachment by name             


        :param request get_calendar_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_calendar_attachment_async(self, request):
        """Get iCalendar document attachment by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_calendar_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_calendar_list(self, request):
        """Get iCalendar files list in folder on storage             


        :param request get_calendar_list_request object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_calendar_list_async(self, request):
        """Get iCalendar files list in folder on storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_calendar_list_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_contact_attachment(self, request):
        """Get attachment file by name             


        :param request get_contact_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_contact_attachment_async(self, request):
        """Get attachment file by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_contact_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_contact_list(self, request):
        """Get contact list from storage folder             


        :param request get_contact_list_request object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_contact_list_async(self, request):
        """Get contact list from storage folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_contact_list_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_contact_properties(self, request):
        """Get contact document properties             


        :param request get_contact_properties_request object with parameters
        :return: HierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObject')

    def get_contact_properties_async(self, request):
        """Get contact document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_contact_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObject')

    def get_disc_usage(self, request):
        """Get disc usage


        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'DiscUsage')

    def get_disc_usage_async(self, request):
        """Get disc usage
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_disc_usage_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns DiscUsage)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'DiscUsage')

    def get_email(self, request):
        """Get email document             


        :param request get_email_request object with parameters
        :return: EmailDocument
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailDocument')

    def get_email_async(self, request):
        """Get email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_email_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocument)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailDocument')

    def get_email_attachment(self, request):
        """Get email attachment by name             


        :param request get_email_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_email_attachment_async(self, request):
        """Get email attachment by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_email_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_email_property(self, request):
        """Get an email document property by its name             


        :param request get_email_property_request object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailPropertyResponse')

    def get_email_property_async(self, request):
        """Get an email document property by its name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_email_property_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailPropertyResponse')

    def get_file_versions(self, request):
        """Get file versions


        :param request get_file_versions_request object with parameters
        :return: FileVersions
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FileVersions')

    def get_file_versions_async(self, request):
        """Get file versions
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_file_versions_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns FileVersions)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FileVersions')

    def get_files_list(self, request):
        """Get all files and folders within a folder


        :param request get_files_list_request object with parameters
        :return: FilesList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FilesList')

    def get_files_list_async(self, request):
        """Get all files and folders within a folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_files_list_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns FilesList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FilesList')

    def get_mapi_attachment(self, request):
        """Get document attachment as file stream             


        :param request get_mapi_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_mapi_attachment_async(self, request):
        """Get document attachment as file stream             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_mapi_attachment_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_mapi_attachments(self, request):
        """Get document attachment list             


        :param request get_mapi_attachments_request object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_attachments_async(self, request):
        """Get document attachment list             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_mapi_attachments_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfString)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_list(self, request):
        """Get document list from storage folder             


        :param request get_mapi_list_request object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_list_async(self, request):
        """Get document list from storage folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_mapi_list_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_properties(self, request):
        """Get document properties             


        :param request get_mapi_properties_request object with parameters
        :return: HierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObjectResponse')

    def get_mapi_properties_async(self, request):
        """Get document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request get_mapi_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObjectResponse')

    def list_email_folders(self, request):
        """Get folders list in email account             


        :param request list_email_folders_request object with parameters
        :return: ListResponseOfMailServerFolder
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfMailServerFolder')

    def list_email_folders_async(self, request):
        """Get folders list in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request list_email_folders_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfMailServerFolder)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfMailServerFolder')

    def list_email_messages(self, request):
        """Get messages from folder, filtered by query             

        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request list_email_messages_request object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfString')

    def list_email_messages_async(self, request):
        """Get messages from folder, filtered by query             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult
        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request list_email_messages_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfString)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfString')

    def move_file(self, request):
        """Move file


        :param request move_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_file_async(self, request):
        """Move file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request move_file_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def move_folder(self, request):
        """Move folder


        :param request move_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_folder_async(self, request):
        """Move folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request move_folder_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def object_exists(self, request):
        """Check if file or folder exists


        :param request object_exists_request object with parameters
        :return: ObjectExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ObjectExist')

    def object_exists_async(self, request):
        """Check if file or folder exists
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request object_exists_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ObjectExist)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ObjectExist')

    def save_mail_account(self, request):
        """Create email account file (*.account) with login/password authentication             


        :param request save_mail_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_account_async(self, request):
        """Create email account file (*.account) with login/password authentication             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request save_mail_account_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def save_mail_o_auth_account(self, request):
        """Create email account file (*.account) with OAuth             


        :param request save_mail_o_auth_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_o_auth_account_async(self, request):
        """Create email account file (*.account) with OAuth             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request save_mail_o_auth_account_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email(self, request):
        """Send an email from *.eml file located on storage             


        :param request send_email_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_async(self, request):
        """Send an email from *.eml file located on storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request send_email_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email_mime(self, request):
        """Send an email specified by MIME in request             


        :param request send_email_mime_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_mime_async(self, request):
        """Send an email specified by MIME in request             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request send_email_mime_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def set_email_property(self, request):
        """Set email document property value             


        :param request set_email_property_request object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailPropertyResponse')

    def set_email_property_async(self, request):
        """Set email document property value             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request set_email_property_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailPropertyResponse')

    def set_email_read_flag(self, request):
        """Sets \&quot;Message is read\&quot; flag             


        :param request set_email_read_flag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def set_email_read_flag_async(self, request):
        """Sets \&quot;Message is read\&quot; flag             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request set_email_read_flag_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def storage_exists(self, request):
        """Check if storage exists


        :param request storage_exists_request object with parameters
        :return: StorageExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'StorageExist')

    def storage_exists_async(self, request):
        """Check if storage exists
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request storage_exists_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns StorageExist)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'StorageExist')

    def update_calendar_properties(self, request):
        """Update calendar file properties             


        :param request update_calendar_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_calendar_properties_async(self, request):
        """Update calendar file properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request update_calendar_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def update_contact_properties(self, request):
        """Update contact document properties             


        :param request update_contact_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_contact_properties_async(self, request):
        """Update contact document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request update_contact_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def update_mapi_properties(self, request):
        """Update document properties             


        :param request update_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_mapi_properties_async(self, request):
        """Update document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request update_mapi_properties_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def upload_file(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'FilesUploadResult')

    def upload_file_async(self, request):
        """Upload file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request upload_file_request object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns FilesUploadResult)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'FilesUploadResult')

    def __make_request(self, http_request, method, return_type):
        def call_api():
            return self.api_client.call_api(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api()
            raise

    def __make_request_async(self, http_request, method, return_type):
        def call_api_async():
            return self.api_client.call_api_async(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api_async()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

