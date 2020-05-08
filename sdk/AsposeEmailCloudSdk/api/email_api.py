#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="email_api.py">
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

import six

from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.configuration import Configuration
from AsposeEmailCloudSdk.rest import ApiException
from AsposeEmailCloudSdk.models import *
from AsposeEmailCloudSdk.models import requests
import multiprocessing


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

    def add_calendar_attachment(self, request: requests.AddCalendarAttachmentRequest) :
        """Adds an attachment to iCalendar file             


        :param request AddCalendarAttachmentRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_calendar_attachment_async(self, request: requests.AddCalendarAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Adds an attachment to iCalendar file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AddCalendarAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def add_contact_attachment(self, request: requests.AddContactAttachmentRequest) :
        """Add attachment to contact document             


        :param request AddContactAttachmentRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_contact_attachment_async(self, request: requests.AddContactAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Add attachment to contact document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AddContactAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def add_email_attachment(self, request: requests.AddEmailAttachmentRequest)  -> EmailDocumentResponse:
        """Adds an attachment to Email document             


        :param request AddEmailAttachmentRequest object with parameters
        :return: EmailDocumentResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'EmailDocumentResponse')

    def add_email_attachment_async(self, request: requests.AddEmailAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Adds an attachment to Email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AddEmailAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocumentResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'EmailDocumentResponse')

    def add_mapi_attachment(self, request: requests.AddMapiAttachmentRequest) :
        """Add attachment to document             


        :param request AddMapiAttachmentRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_mapi_attachment_async(self, request: requests.AddMapiAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Add attachment to document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AddMapiAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def ai_bcr_ocr(self, request: requests.AiBcrOcrRequest)  -> ListResponseOfAiBcrOcrData:
        """Ocr images             


        :param request AiBcrOcrRequest object with parameters
        :return: ListResponseOfAiBcrOcrData
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_async(self, request: requests.AiBcrOcrRequest) -> multiprocessing.pool.AsyncResult:
        """Ocr images             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrOcrRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiBcrOcrData)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_storage(self, request: requests.AiBcrOcrStorageRequest)  -> ListResponseOfAiBcrOcrData:
        """Ocr images from storage             


        :param request AiBcrOcrStorageRequest object with parameters
        :return: ListResponseOfAiBcrOcrData
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_ocr_storage_async(self, request: requests.AiBcrOcrStorageRequest) -> multiprocessing.pool.AsyncResult:
        """Ocr images from storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrOcrStorageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiBcrOcrData)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiBcrOcrData')

    def ai_bcr_parse(self, request: requests.AiBcrParseRequest)  -> ListResponseOfHierarchicalObject:
        """Parse images to vCard properties             


        :param request AiBcrParseRequest object with parameters
        :return: ListResponseOfHierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_async(self, request: requests.AiBcrParseRequest) -> multiprocessing.pool.AsyncResult:
        """Parse images to vCard properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrParseRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfHierarchicalObject')

    def ai_bcr_parse_model(self, request: requests.AiBcrParseModelRequest)  -> ListResponseOfContactDto:
        """Parse images to vCard document models             


        :param request AiBcrParseModelRequest object with parameters
        :return: ListResponseOfContactDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfContactDto')

    def ai_bcr_parse_model_async(self, request: requests.AiBcrParseModelRequest) -> multiprocessing.pool.AsyncResult:
        """Parse images to vCard document models             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrParseModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfContactDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfContactDto')

    def ai_bcr_parse_ocr_data_model(self, request: requests.AiBcrParseOcrDataModelRequest)  -> ListResponseOfContactDto:
        """Parse OCR data to vCard document models             


        :param request AiBcrParseOcrDataModelRequest object with parameters
        :return: ListResponseOfContactDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfContactDto')

    def ai_bcr_parse_ocr_data_model_async(self, request: requests.AiBcrParseOcrDataModelRequest) -> multiprocessing.pool.AsyncResult:
        """Parse OCR data to vCard document models             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrParseOcrDataModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfContactDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfContactDto')

    def ai_bcr_parse_storage(self, request: requests.AiBcrParseStorageRequest)  -> ListResponseOfStorageFileLocation:
        """Parse images from storage to vCard files             


        :param request AiBcrParseStorageRequest object with parameters
        :return: ListResponseOfStorageFileLocation
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_bcr_parse_storage_async(self, request: requests.AiBcrParseStorageRequest) -> multiprocessing.pool.AsyncResult:
        """Parse images from storage to vCard files             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiBcrParseStorageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfStorageFileLocation)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfStorageFileLocation')

    def ai_name_complete(self, request: requests.AiNameCompleteRequest)  -> AiNameWeightedVariants:
        """The call proposes k most probable names for given starting characters             


        :param request AiNameCompleteRequest object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_complete_async(self, request: requests.AiNameCompleteRequest) -> multiprocessing.pool.AsyncResult:
        """The call proposes k most probable names for given starting characters             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameCompleteRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand(self, request: requests.AiNameExpandRequest)  -> AiNameWeightedVariants:
        """Expands a person&#39;s name into a list of possible alternatives using options for expanding instructions             


        :param request AiNameExpandRequest object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand_async(self, request: requests.AiNameExpandRequest) -> multiprocessing.pool.AsyncResult:
        """Expands a person&#39;s name into a list of possible alternatives using options for expanding instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameExpandRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameWeightedVariants')

    def ai_name_expand_parsed(self, request: requests.AiNameExpandParsedRequest)  -> AiNameWeightedVariants:
        """Expands a person&#39;s parsed name into a list of possible alternatives using options for expanding instructions             


        :param request AiNameExpandParsedRequest object with parameters
        :return: AiNameWeightedVariants
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameWeightedVariants')

    def ai_name_expand_parsed_async(self, request: requests.AiNameExpandParsedRequest) -> multiprocessing.pool.AsyncResult:
        """Expands a person&#39;s parsed name into a list of possible alternatives using options for expanding instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameExpandParsedRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameWeightedVariants)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameWeightedVariants')

    def ai_name_format(self, request: requests.AiNameFormatRequest)  -> AiNameFormatted:
        """Formats a person&#39;s name in correct case and name order using options for formatting instructions             


        :param request AiNameFormatRequest object with parameters
        :return: AiNameFormatted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameFormatted')

    def ai_name_format_async(self, request: requests.AiNameFormatRequest) -> multiprocessing.pool.AsyncResult:
        """Formats a person&#39;s name in correct case and name order using options for formatting instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameFormatRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameFormatted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameFormatted')

    def ai_name_format_parsed(self, request: requests.AiNameFormatParsedRequest)  -> AiNameFormatted:
        """Formats a person&#39;s parsed name in correct case and name order using options for formatting instructions             


        :param request AiNameFormatParsedRequest object with parameters
        :return: AiNameFormatted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameFormatted')

    def ai_name_format_parsed_async(self, request: requests.AiNameFormatParsedRequest) -> multiprocessing.pool.AsyncResult:
        """Formats a person&#39;s parsed name in correct case and name order using options for formatting instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameFormatParsedRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameFormatted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameFormatted')

    def ai_name_genderize(self, request: requests.AiNameGenderizeRequest)  -> ListResponseOfAiNameGenderHypothesis:
        """Detect person&#39;s gender from name string             


        :param request AiNameGenderizeRequest object with parameters
        :return: ListResponseOfAiNameGenderHypothesis
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_async(self, request: requests.AiNameGenderizeRequest) -> multiprocessing.pool.AsyncResult:
        """Detect person&#39;s gender from name string             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameGenderizeRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameGenderHypothesis)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_parsed(self, request: requests.AiNameGenderizeParsedRequest)  -> ListResponseOfAiNameGenderHypothesis:
        """Detect person&#39;s gender from parsed name             


        :param request AiNameGenderizeParsedRequest object with parameters
        :return: ListResponseOfAiNameGenderHypothesis
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_genderize_parsed_async(self, request: requests.AiNameGenderizeParsedRequest) -> multiprocessing.pool.AsyncResult:
        """Detect person&#39;s gender from parsed name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameGenderizeParsedRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameGenderHypothesis)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ListResponseOfAiNameGenderHypothesis')

    def ai_name_match(self, request: requests.AiNameMatchRequest)  -> AiNameMatchResult:
        """Compare people&#39;s names. Uses options for comparing instructions             


        :param request AiNameMatchRequest object with parameters
        :return: AiNameMatchResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AiNameMatchResult')

    def ai_name_match_async(self, request: requests.AiNameMatchRequest) -> multiprocessing.pool.AsyncResult:
        """Compare people&#39;s names. Uses options for comparing instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameMatchRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameMatchResult)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AiNameMatchResult')

    def ai_name_match_parsed(self, request: requests.AiNameMatchParsedRequest)  -> AiNameMatchResult:
        """Compare people&#39;s parsed names and attributes. Uses options for comparing instructions             


        :param request AiNameMatchParsedRequest object with parameters
        :return: AiNameMatchResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'AiNameMatchResult')

    def ai_name_match_parsed_async(self, request: requests.AiNameMatchParsedRequest) -> multiprocessing.pool.AsyncResult:
        """Compare people&#39;s parsed names and attributes. Uses options for comparing instructions             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameMatchParsedRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AiNameMatchResult)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'AiNameMatchResult')

    def ai_name_parse(self, request: requests.AiNameParseRequest)  -> ListResponseOfAiNameComponent:
        """Parse name to components             


        :param request AiNameParseRequest object with parameters
        :return: ListResponseOfAiNameComponent
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameComponent')

    def ai_name_parse_async(self, request: requests.AiNameParseRequest) -> multiprocessing.pool.AsyncResult:
        """Parse name to components             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameParseRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameComponent)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameComponent')

    def ai_name_parse_email_address(self, request: requests.AiNameParseEmailAddressRequest)  -> ListResponseOfAiNameExtracted:
        """Parse person&#39;s name out of an email address             


        :param request AiNameParseEmailAddressRequest object with parameters
        :return: ListResponseOfAiNameExtracted
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfAiNameExtracted')

    def ai_name_parse_email_address_async(self, request: requests.AiNameParseEmailAddressRequest) -> multiprocessing.pool.AsyncResult:
        """Parse person&#39;s name out of an email address             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AiNameParseEmailAddressRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfAiNameExtracted)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfAiNameExtracted')

    def append_email_message(self, request: requests.AppendEmailMessageRequest)  -> EmailPropertyResponse:
        """Adds an email from *.eml file to specified folder in email account             


        :param request AppendEmailMessageRequest object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailPropertyResponse')

    def append_email_message_async(self, request: requests.AppendEmailMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Adds an email from *.eml file to specified folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AppendEmailMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailPropertyResponse')

    def append_email_model_message(self, request: requests.AppendEmailModelMessageRequest)  -> ValueResponse:
        """Adds an email from model to specified folder in email account             


        :param request AppendEmailModelMessageRequest object with parameters
        :return: ValueResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'ValueResponse')

    def append_email_model_message_async(self, request: requests.AppendEmailModelMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Adds an email from model to specified folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AppendEmailModelMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ValueResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'ValueResponse')

    def append_mime_message(self, request: requests.AppendMimeMessageRequest)  -> ValueResponse:
        """Adds an email from MIME to specified folder in email account             


        :param request AppendMimeMessageRequest object with parameters
        :return: ValueResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'ValueResponse')

    def append_mime_message_async(self, request: requests.AppendMimeMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Adds an email from MIME to specified folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request AppendMimeMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ValueResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'ValueResponse')

    def convert_calendar_model_to_alternate(self, request: requests.ConvertCalendarModelToAlternateRequest)  -> AlternateView:
        """Convert iCalendar to AlternateView             


        :param request ConvertCalendarModelToAlternateRequest object with parameters
        :return: AlternateView
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'AlternateView')

    def convert_calendar_model_to_alternate_async(self, request: requests.ConvertCalendarModelToAlternateRequest) -> multiprocessing.pool.AsyncResult:
        """Convert iCalendar to AlternateView             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ConvertCalendarModelToAlternateRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AlternateView)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'AlternateView')

    def convert_email(self, request: requests.ConvertEmailRequest)  -> str:
        """Converts email document to specified format and returns as file             


        :param request ConvertEmailRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'file')

    def convert_email_async(self, request: requests.ConvertEmailRequest) -> multiprocessing.pool.AsyncResult:
        """Converts email document to specified format and returns as file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ConvertEmailRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'file')

    def copy_file(self, request: requests.CopyFileRequest) :
        """Copy file


        :param request CopyFileRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_file_async(self, request: requests.CopyFileRequest) -> multiprocessing.pool.AsyncResult:
        """Copy file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CopyFileRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def copy_folder(self, request: requests.CopyFolderRequest) :
        """Copy folder


        :param request CopyFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_folder_async(self, request: requests.CopyFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Copy folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CopyFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_calendar(self, request: requests.CreateCalendarRequest) :
        """Create calendar file             


        :param request CreateCalendarRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_calendar_async(self, request: requests.CreateCalendarRequest) -> multiprocessing.pool.AsyncResult:
        """Create calendar file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateCalendarRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_contact(self, request: requests.CreateContactRequest) :
        """Create contact document             


        :param request CreateContactRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_contact_async(self, request: requests.CreateContactRequest) -> multiprocessing.pool.AsyncResult:
        """Create contact document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateContactRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_email(self, request: requests.CreateEmailRequest)  -> EmailDocumentResponse:
        """Create an email document             


        :param request CreateEmailRequest object with parameters
        :return: EmailDocumentResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailDocumentResponse')

    def create_email_async(self, request: requests.CreateEmailRequest) -> multiprocessing.pool.AsyncResult:
        """Create an email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateEmailRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocumentResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailDocumentResponse')

    def create_email_folder(self, request: requests.CreateEmailFolderRequest) :
        """Create new folder in email account             


        :param request CreateEmailFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_email_folder_async(self, request: requests.CreateEmailFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Create new folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateEmailFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_folder(self, request: requests.CreateFolderRequest) :
        """Create the folder


        :param request CreateFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_folder_async(self, request: requests.CreateFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Create the folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_mapi(self, request: requests.CreateMapiRequest) :
        """Create new document             


        :param request CreateMapiRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_mapi_async(self, request: requests.CreateMapiRequest) -> multiprocessing.pool.AsyncResult:
        """Create new document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request CreateMapiRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def delete_calendar_property(self, request: requests.DeleteCalendarPropertyRequest) :
        """Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             


        :param request DeleteCalendarPropertyRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_calendar_property_async(self, request: requests.DeleteCalendarPropertyRequest) -> multiprocessing.pool.AsyncResult:
        """Deletes indexed property by index and name. To delete Reminder attachment, use path ReminderAttachment/{ReminderIndex}/{AttachmentIndex}             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteCalendarPropertyRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_contact_property(self, request: requests.DeleteContactPropertyRequest) :
        """Delete property from indexed property list             


        :param request DeleteContactPropertyRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_contact_property_async(self, request: requests.DeleteContactPropertyRequest) -> multiprocessing.pool.AsyncResult:
        """Delete property from indexed property list             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteContactPropertyRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_folder(self, request: requests.DeleteEmailFolderRequest) :
        """Delete a folder in email account             


        :param request DeleteEmailFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_folder_async(self, request: requests.DeleteEmailFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Delete a folder in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteEmailFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_message(self, request: requests.DeleteEmailMessageRequest) :
        """Delete message from email account by id             


        :param request DeleteEmailMessageRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_message_async(self, request: requests.DeleteEmailMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Delete message from email account by id             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteEmailMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_thread(self, request: requests.DeleteEmailThreadRequest) :
        """Delete thread by id. All messages from thread will also be deleted             


        :param request DeleteEmailThreadRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_thread_async(self, request: requests.DeleteEmailThreadRequest) -> multiprocessing.pool.AsyncResult:
        """Delete thread by id. All messages from thread will also be deleted             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteEmailThreadRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_file(self, request: requests.DeleteFileRequest) :
        """Delete file


        :param request DeleteFileRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_file_async(self, request: requests.DeleteFileRequest) -> multiprocessing.pool.AsyncResult:
        """Delete file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteFileRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_folder(self, request: requests.DeleteFolderRequest) :
        """Delete folder


        :param request DeleteFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_folder_async(self, request: requests.DeleteFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Delete folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_mapi_attachment(self, request: requests.DeleteMapiAttachmentRequest) :
        """Remove attachment from document             


        :param request DeleteMapiAttachmentRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_attachment_async(self, request: requests.DeleteMapiAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Remove attachment from document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteMapiAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_mapi_properties(self, request: requests.DeleteMapiPropertiesRequest) :
        """Delete document properties             


        :param request DeleteMapiPropertiesRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_properties_async(self, request: requests.DeleteMapiPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Delete document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DeleteMapiPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def discover_email_config(self, request: requests.DiscoverEmailConfigRequest)  -> EmailAccountConfigList:
        """Discover email accounts by email address. Does not validate discovered accounts.             


        :param request DiscoverEmailConfigRequest object with parameters
        :return: EmailAccountConfigList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailAccountConfigList')

    def discover_email_config_async(self, request: requests.DiscoverEmailConfigRequest) -> multiprocessing.pool.AsyncResult:
        """Discover email accounts by email address. Does not validate discovered accounts.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DiscoverEmailConfigRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailAccountConfigList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailAccountConfigList')

    def discover_email_config_oauth(self, request: requests.DiscoverEmailConfigOauthRequest)  -> EmailAccountConfigList:
        """Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             


        :param request DiscoverEmailConfigOauthRequest object with parameters
        :return: EmailAccountConfigList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'EmailAccountConfigList')

    def discover_email_config_oauth_async(self, request: requests.DiscoverEmailConfigOauthRequest) -> multiprocessing.pool.AsyncResult:
        """Discover email accounts by email address. Validates discovered accounts using OAuth 2.0.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DiscoverEmailConfigOauthRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailAccountConfigList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'EmailAccountConfigList')

    def discover_email_config_password(self, request: requests.DiscoverEmailConfigPasswordRequest)  -> EmailAccountConfigList:
        """Discover email accounts by email address. Validates discovered accounts using login and password.             


        :param request DiscoverEmailConfigPasswordRequest object with parameters
        :return: EmailAccountConfigList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'EmailAccountConfigList')

    def discover_email_config_password_async(self, request: requests.DiscoverEmailConfigPasswordRequest) -> multiprocessing.pool.AsyncResult:
        """Discover email accounts by email address. Validates discovered accounts using login and password.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DiscoverEmailConfigPasswordRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailAccountConfigList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'EmailAccountConfigList')

    def download_file(self, request: requests.DownloadFileRequest)  -> str:
        """Download file


        :param request DownloadFileRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def download_file_async(self, request: requests.DownloadFileRequest) -> multiprocessing.pool.AsyncResult:
        """Download file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request DownloadFileRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def fetch_email_message(self, request: requests.FetchEmailMessageRequest)  -> MimeResponse:
        """Fetch message mime from email account             


        :param request FetchEmailMessageRequest object with parameters
        :return: MimeResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'MimeResponse')

    def fetch_email_message_async(self, request: requests.FetchEmailMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Fetch message mime from email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request FetchEmailMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns MimeResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'MimeResponse')

    def fetch_email_model(self, request: requests.FetchEmailModelRequest)  -> EmailDto:
        """Fetch message model from email account             


        :param request FetchEmailModelRequest object with parameters
        :return: EmailDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailDto')

    def fetch_email_model_async(self, request: requests.FetchEmailModelRequest) -> multiprocessing.pool.AsyncResult:
        """Fetch message model from email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request FetchEmailModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailDto')

    def fetch_email_thread_messages(self, request: requests.FetchEmailThreadMessagesRequest)  -> ListResponseOfEmailDto:
        """Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             


        :param request FetchEmailThreadMessagesRequest object with parameters
        :return: ListResponseOfEmailDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfEmailDto')

    def fetch_email_thread_messages_async(self, request: requests.FetchEmailThreadMessagesRequest) -> multiprocessing.pool.AsyncResult:
        """Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request FetchEmailThreadMessagesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfEmailDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfEmailDto')

    def get_calendar(self, request: requests.GetCalendarRequest)  -> HierarchicalObject:
        """Get calendar file properties             


        :param request GetCalendarRequest object with parameters
        :return: HierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObject')

    def get_calendar_async(self, request: requests.GetCalendarRequest) -> multiprocessing.pool.AsyncResult:
        """Get calendar file properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObject')

    def get_calendar_attachment(self, request: requests.GetCalendarAttachmentRequest)  -> str:
        """Get iCalendar document attachment by name             


        :param request GetCalendarAttachmentRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_calendar_attachment_async(self, request: requests.GetCalendarAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Get iCalendar document attachment by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_calendar_list(self, request: requests.GetCalendarListRequest)  -> ListResponseOfHierarchicalObjectResponse:
        """Get iCalendar files list in folder on storage             


        :param request GetCalendarListRequest object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_calendar_list_async(self, request: requests.GetCalendarListRequest) -> multiprocessing.pool.AsyncResult:
        """Get iCalendar files list in folder on storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_calendar_model(self, request: requests.GetCalendarModelRequest)  -> CalendarDto:
        """Get calendar file             


        :param request GetCalendarModelRequest object with parameters
        :return: CalendarDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'CalendarDto')

    def get_calendar_model_async(self, request: requests.GetCalendarModelRequest) -> multiprocessing.pool.AsyncResult:
        """Get calendar file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns CalendarDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'CalendarDto')

    def get_calendar_model_as_alternate(self, request: requests.GetCalendarModelAsAlternateRequest)  -> AlternateView:
        """Get iCalendar from storage as AlternateView             


        :param request GetCalendarModelAsAlternateRequest object with parameters
        :return: AlternateView
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'AlternateView')

    def get_calendar_model_as_alternate_async(self, request: requests.GetCalendarModelAsAlternateRequest) -> multiprocessing.pool.AsyncResult:
        """Get iCalendar from storage as AlternateView             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarModelAsAlternateRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns AlternateView)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'AlternateView')

    def get_calendar_model_list(self, request: requests.GetCalendarModelListRequest)  -> CalendarDtoList:
        """Get iCalendar list from storage folder             


        :param request GetCalendarModelListRequest object with parameters
        :return: CalendarDtoList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'CalendarDtoList')

    def get_calendar_model_list_async(self, request: requests.GetCalendarModelListRequest) -> multiprocessing.pool.AsyncResult:
        """Get iCalendar list from storage folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetCalendarModelListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns CalendarDtoList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'CalendarDtoList')

    def get_contact_attachment(self, request: requests.GetContactAttachmentRequest)  -> str:
        """Get attachment file by name             


        :param request GetContactAttachmentRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_contact_attachment_async(self, request: requests.GetContactAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Get attachment file by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetContactAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_contact_list(self, request: requests.GetContactListRequest)  -> ListResponseOfHierarchicalObjectResponse:
        """Get contact list from storage folder             


        :param request GetContactListRequest object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_contact_list_async(self, request: requests.GetContactListRequest) -> multiprocessing.pool.AsyncResult:
        """Get contact list from storage folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetContactListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_contact_model(self, request: requests.GetContactModelRequest)  -> ContactDto:
        """Get contact document.             


        :param request GetContactModelRequest object with parameters
        :return: ContactDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ContactDto')

    def get_contact_model_async(self, request: requests.GetContactModelRequest) -> multiprocessing.pool.AsyncResult:
        """Get contact document.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetContactModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ContactDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ContactDto')

    def get_contact_model_list(self, request: requests.GetContactModelListRequest)  -> ContactDtoList:
        """Get contact list from storage folder.             


        :param request GetContactModelListRequest object with parameters
        :return: ContactDtoList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ContactDtoList')

    def get_contact_model_list_async(self, request: requests.GetContactModelListRequest) -> multiprocessing.pool.AsyncResult:
        """Get contact list from storage folder.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetContactModelListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ContactDtoList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ContactDtoList')

    def get_contact_properties(self, request: requests.GetContactPropertiesRequest)  -> HierarchicalObject:
        """Get contact document properties             


        :param request GetContactPropertiesRequest object with parameters
        :return: HierarchicalObject
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObject')

    def get_contact_properties_async(self, request: requests.GetContactPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Get contact document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetContactPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObject)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObject')

    def get_disc_usage(self, request: requests.GetDiscUsageRequest)  -> DiscUsage:
        """Get disc usage


        :param request GetDiscUsageRequest object with parameters
        :return: DiscUsage
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'DiscUsage')

    def get_disc_usage_async(self, request: requests.GetDiscUsageRequest) -> multiprocessing.pool.AsyncResult:
        """Get disc usage
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetDiscUsageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns DiscUsage)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'DiscUsage')

    def get_email(self, request: requests.GetEmailRequest)  -> EmailDocument:
        """Get email document             


        :param request GetEmailRequest object with parameters
        :return: EmailDocument
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailDocument')

    def get_email_async(self, request: requests.GetEmailRequest) -> multiprocessing.pool.AsyncResult:
        """Get email document             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDocument)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailDocument')

    def get_email_as_file(self, request: requests.GetEmailAsFileRequest)  -> str:
        """Converts email document from storage to specified format and returns as file             


        :param request GetEmailAsFileRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_email_as_file_async(self, request: requests.GetEmailAsFileRequest) -> multiprocessing.pool.AsyncResult:
        """Converts email document from storage to specified format and returns as file             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailAsFileRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_email_attachment(self, request: requests.GetEmailAttachmentRequest)  -> str:
        """Get email attachment by name             


        :param request GetEmailAttachmentRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_email_attachment_async(self, request: requests.GetEmailAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Get email attachment by name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_email_client_account(self, request: requests.GetEmailClientAccountRequest)  -> EmailClientAccount:
        """Get email client account from storage             


        :param request GetEmailClientAccountRequest object with parameters
        :return: EmailClientAccount
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailClientAccount')

    def get_email_client_account_async(self, request: requests.GetEmailClientAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Get email client account from storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailClientAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailClientAccount)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailClientAccount')

    def get_email_client_multi_account(self, request: requests.GetEmailClientMultiAccountRequest)  -> EmailClientMultiAccount:
        """Get email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             


        :param request GetEmailClientMultiAccountRequest object with parameters
        :return: EmailClientMultiAccount
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailClientMultiAccount')

    def get_email_client_multi_account_async(self, request: requests.GetEmailClientMultiAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Get email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailClientMultiAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailClientMultiAccount)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailClientMultiAccount')

    def get_email_model(self, request: requests.GetEmailModelRequest)  -> EmailDto:
        """Get email document.             


        :param request GetEmailModelRequest object with parameters
        :return: EmailDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailDto')

    def get_email_model_async(self, request: requests.GetEmailModelRequest) -> multiprocessing.pool.AsyncResult:
        """Get email document.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailDto')

    def get_email_model_list(self, request: requests.GetEmailModelListRequest)  -> EmailDtoList:
        """Get email list from storage folder.             


        :param request GetEmailModelListRequest object with parameters
        :return: EmailDtoList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailDtoList')

    def get_email_model_list_async(self, request: requests.GetEmailModelListRequest) -> multiprocessing.pool.AsyncResult:
        """Get email list from storage folder.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailModelListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailDtoList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailDtoList')

    def get_email_property(self, request: requests.GetEmailPropertyRequest)  -> EmailPropertyResponse:
        """Get an email document property by its name             


        :param request GetEmailPropertyRequest object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailPropertyResponse')

    def get_email_property_async(self, request: requests.GetEmailPropertyRequest) -> multiprocessing.pool.AsyncResult:
        """Get an email document property by its name             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetEmailPropertyRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailPropertyResponse')

    def get_file_versions(self, request: requests.GetFileVersionsRequest)  -> FileVersions:
        """Get file versions


        :param request GetFileVersionsRequest object with parameters
        :return: FileVersions
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FileVersions')

    def get_file_versions_async(self, request: requests.GetFileVersionsRequest) -> multiprocessing.pool.AsyncResult:
        """Get file versions
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetFileVersionsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns FileVersions)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FileVersions')

    def get_files_list(self, request: requests.GetFilesListRequest)  -> FilesList:
        """Get all files and folders within a folder


        :param request GetFilesListRequest object with parameters
        :return: FilesList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FilesList')

    def get_files_list_async(self, request: requests.GetFilesListRequest) -> multiprocessing.pool.AsyncResult:
        """Get all files and folders within a folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetFilesListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns FilesList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FilesList')

    def get_mapi_attachment(self, request: requests.GetMapiAttachmentRequest)  -> str:
        """Get document attachment as file stream             


        :param request GetMapiAttachmentRequest object with parameters
        :return: str
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_mapi_attachment_async(self, request: requests.GetMapiAttachmentRequest) -> multiprocessing.pool.AsyncResult:
        """Get document attachment as file stream             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetMapiAttachmentRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns file)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_mapi_attachments(self, request: requests.GetMapiAttachmentsRequest)  -> ListResponseOfString:
        """Get document attachment list             


        :param request GetMapiAttachmentsRequest object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_attachments_async(self, request: requests.GetMapiAttachmentsRequest) -> multiprocessing.pool.AsyncResult:
        """Get document attachment list             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetMapiAttachmentsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfString)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_list(self, request: requests.GetMapiListRequest)  -> ListResponseOfHierarchicalObjectResponse:
        """Get document list from storage folder             


        :param request GetMapiListRequest object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_list_async(self, request: requests.GetMapiListRequest) -> multiprocessing.pool.AsyncResult:
        """Get document list from storage folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetMapiListRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfHierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_properties(self, request: requests.GetMapiPropertiesRequest)  -> HierarchicalObjectResponse:
        """Get document properties             


        :param request GetMapiPropertiesRequest object with parameters
        :return: HierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObjectResponse')

    def get_mapi_properties_async(self, request: requests.GetMapiPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Get document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request GetMapiPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns HierarchicalObjectResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObjectResponse')

    def is_email_address_disposable(self, request: requests.IsEmailAddressDisposableRequest)  -> ValueTOfBoolean:
        """Check email address is disposable             


        :param request IsEmailAddressDisposableRequest object with parameters
        :return: ValueTOfBoolean
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ValueTOfBoolean')

    def is_email_address_disposable_async(self, request: requests.IsEmailAddressDisposableRequest) -> multiprocessing.pool.AsyncResult:
        """Check email address is disposable             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request IsEmailAddressDisposableRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ValueTOfBoolean)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ValueTOfBoolean')

    def list_email_folders(self, request: requests.ListEmailFoldersRequest)  -> ListResponseOfMailServerFolder:
        """Get folders list in email account             


        :param request ListEmailFoldersRequest object with parameters
        :return: ListResponseOfMailServerFolder
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfMailServerFolder')

    def list_email_folders_async(self, request: requests.ListEmailFoldersRequest) -> multiprocessing.pool.AsyncResult:
        """Get folders list in email account             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ListEmailFoldersRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfMailServerFolder)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfMailServerFolder')

    def list_email_messages(self, request: requests.ListEmailMessagesRequest)  -> ListResponseOfString:
        """Get messages from folder, filtered by query             

        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request ListEmailMessagesRequest object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfString')

    def list_email_messages_async(self, request: requests.ListEmailMessagesRequest) -> multiprocessing.pool.AsyncResult:
        """Get messages from folder, filtered by query             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult
        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request ListEmailMessagesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfString)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfString')

    def list_email_models(self, request: requests.ListEmailModelsRequest)  -> ListResponseOfEmailDto:
        """Get messages from folder, filtered by query             

        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request ListEmailModelsRequest object with parameters
        :return: ListResponseOfEmailDto
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfEmailDto')

    def list_email_models_async(self, request: requests.ListEmailModelsRequest) -> multiprocessing.pool.AsyncResult:
        """Get messages from folder, filtered by query             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult
        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request ListEmailModelsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ListResponseOfEmailDto)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfEmailDto')

    def list_email_threads(self, request: requests.ListEmailThreadsRequest)  -> EmailThreadList:
        """Get message threads from folder. All messages are partly fetched (without email body and other fields)             


        :param request ListEmailThreadsRequest object with parameters
        :return: EmailThreadList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'EmailThreadList')

    def list_email_threads_async(self, request: requests.ListEmailThreadsRequest) -> multiprocessing.pool.AsyncResult:
        """Get message threads from folder. All messages are partly fetched (without email body and other fields)             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ListEmailThreadsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailThreadList)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'EmailThreadList')

    def move_email_message(self, request: requests.MoveEmailMessageRequest) :
        """Move message to another folder             


        :param request MoveEmailMessageRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_email_message_async(self, request: requests.MoveEmailMessageRequest) -> multiprocessing.pool.AsyncResult:
        """Move message to another folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request MoveEmailMessageRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def move_email_thread(self, request: requests.MoveEmailThreadRequest) :
        """Move thread to another folder             


        :param request MoveEmailThreadRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_email_thread_async(self, request: requests.MoveEmailThreadRequest) -> multiprocessing.pool.AsyncResult:
        """Move thread to another folder             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request MoveEmailThreadRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def move_file(self, request: requests.MoveFileRequest) :
        """Move file


        :param request MoveFileRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_file_async(self, request: requests.MoveFileRequest) -> multiprocessing.pool.AsyncResult:
        """Move file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request MoveFileRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def move_folder(self, request: requests.MoveFolderRequest) :
        """Move folder


        :param request MoveFolderRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_folder_async(self, request: requests.MoveFolderRequest) -> multiprocessing.pool.AsyncResult:
        """Move folder
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request MoveFolderRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def object_exists(self, request: requests.ObjectExistsRequest)  -> ObjectExist:
        """Check if file or folder exists


        :param request ObjectExistsRequest object with parameters
        :return: ObjectExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ObjectExist')

    def object_exists_async(self, request: requests.ObjectExistsRequest) -> multiprocessing.pool.AsyncResult:
        """Check if file or folder exists
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request ObjectExistsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns ObjectExist)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ObjectExist')

    def save_calendar_model(self, request: requests.SaveCalendarModelRequest) :
        """Save iCalendar             


        :param request SaveCalendarModelRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def save_calendar_model_async(self, request: requests.SaveCalendarModelRequest) -> multiprocessing.pool.AsyncResult:
        """Save iCalendar             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveCalendarModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def save_contact_model(self, request: requests.SaveContactModelRequest) :
        """Save contact.             


        :param request SaveContactModelRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def save_contact_model_async(self, request: requests.SaveContactModelRequest) -> multiprocessing.pool.AsyncResult:
        """Save contact.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveContactModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def save_email_client_account(self, request: requests.SaveEmailClientAccountRequest) :
        """Create email client account file (*.account) with any of supported credentials             


        :param request SaveEmailClientAccountRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def save_email_client_account_async(self, request: requests.SaveEmailClientAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Create email client account file (*.account) with any of supported credentials             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveEmailClientAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def save_email_client_multi_account(self, request: requests.SaveEmailClientMultiAccountRequest) :
        """Create email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             


        :param request SaveEmailClientMultiAccountRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def save_email_client_multi_account_async(self, request: requests.SaveEmailClientMultiAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Create email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveEmailClientMultiAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def save_email_model(self, request: requests.SaveEmailModelRequest) :
        """Save email document.             


        :param request SaveEmailModelRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def save_email_model_async(self, request: requests.SaveEmailModelRequest) -> multiprocessing.pool.AsyncResult:
        """Save email document.             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveEmailModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def save_mail_account(self, request: requests.SaveMailAccountRequest) :
        """Create email account file (*.account) with login/password authentication             


        :param request SaveMailAccountRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_account_async(self, request: requests.SaveMailAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Create email account file (*.account) with login/password authentication             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveMailAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def save_mail_o_auth_account(self, request: requests.SaveMailOAuthAccountRequest) :
        """Create email account file (*.account) with OAuth             


        :param request SaveMailOAuthAccountRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_o_auth_account_async(self, request: requests.SaveMailOAuthAccountRequest) -> multiprocessing.pool.AsyncResult:
        """Create email account file (*.account) with OAuth             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SaveMailOAuthAccountRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email(self, request: requests.SendEmailRequest) :
        """Send an email from *.eml file located on storage             


        :param request SendEmailRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_async(self, request: requests.SendEmailRequest) -> multiprocessing.pool.AsyncResult:
        """Send an email from *.eml file located on storage             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SendEmailRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email_mime(self, request: requests.SendEmailMimeRequest) :
        """Send an email specified by MIME in request             


        :param request SendEmailMimeRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_mime_async(self, request: requests.SendEmailMimeRequest) -> multiprocessing.pool.AsyncResult:
        """Send an email specified by MIME in request             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SendEmailMimeRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email_model(self, request: requests.SendEmailModelRequest) :
        """Send an email specified by model in request             


        :param request SendEmailModelRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_model_async(self, request: requests.SendEmailModelRequest) -> multiprocessing.pool.AsyncResult:
        """Send an email specified by model in request             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SendEmailModelRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def set_email_property(self, request: requests.SetEmailPropertyRequest)  -> EmailPropertyResponse:
        """Set email document property value             


        :param request SetEmailPropertyRequest object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailPropertyResponse')

    def set_email_property_async(self, request: requests.SetEmailPropertyRequest) -> multiprocessing.pool.AsyncResult:
        """Set email document property value             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SetEmailPropertyRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns EmailPropertyResponse)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailPropertyResponse')

    def set_email_read_flag(self, request: requests.SetEmailReadFlagRequest) :
        """Sets \&quot;Message is read\&quot; flag             


        :param request SetEmailReadFlagRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def set_email_read_flag_async(self, request: requests.SetEmailReadFlagRequest) -> multiprocessing.pool.AsyncResult:
        """Sets \&quot;Message is read\&quot; flag             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SetEmailReadFlagRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def set_email_thread_read_flag(self, request: requests.SetEmailThreadReadFlagRequest) :
        """Mark all messages in thread as read or unread             


        :param request SetEmailThreadReadFlagRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def set_email_thread_read_flag_async(self, request: requests.SetEmailThreadReadFlagRequest) -> multiprocessing.pool.AsyncResult:
        """Mark all messages in thread as read or unread             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request SetEmailThreadReadFlagRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def storage_exists(self, request: requests.StorageExistsRequest)  -> StorageExist:
        """Check if storage exists


        :param request StorageExistsRequest object with parameters
        :return: StorageExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'StorageExist')

    def storage_exists_async(self, request: requests.StorageExistsRequest) -> multiprocessing.pool.AsyncResult:
        """Check if storage exists
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request StorageExistsRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns StorageExist)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'StorageExist')

    def update_calendar_properties(self, request: requests.UpdateCalendarPropertiesRequest) :
        """Update calendar file properties             


        :param request UpdateCalendarPropertiesRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_calendar_properties_async(self, request: requests.UpdateCalendarPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Update calendar file properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request UpdateCalendarPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def update_contact_properties(self, request: requests.UpdateContactPropertiesRequest) :
        """Update contact document properties             


        :param request UpdateContactPropertiesRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_contact_properties_async(self, request: requests.UpdateContactPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Update contact document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request UpdateContactPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def update_mapi_properties(self, request: requests.UpdateMapiPropertiesRequest) :
        """Update document properties             


        :param request UpdateMapiPropertiesRequest object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_mapi_properties_async(self, request: requests.UpdateMapiPropertiesRequest) -> multiprocessing.pool.AsyncResult:
        """Update document properties             
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request UpdateMapiPropertiesRequest object with parameters
        :return: multiprocessing.pool.AsyncResult (AsyncResult.get() returns None)
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def upload_file(self, request: requests.UploadFileRequest)  -> FilesUploadResult:
        """Upload file


        :param request UploadFileRequest object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'FilesUploadResult')

    def upload_file_async(self, request: requests.UploadFileRequest) -> multiprocessing.pool.AsyncResult:
        """Upload file
        Performs operation asynchronously. Returns multiprocessing.pool.AsyncResult

        :param request UploadFileRequest object with parameters
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
                                        files={}, _return_http_data_only=True,
                                        host=config.get_auth_url())
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

