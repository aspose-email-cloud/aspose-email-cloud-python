#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="convert_contact_model_to_file_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.convert_contact_model_to_file_request import ConvertContactModelToFileRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class ConvertContactModelToFileRequest(BaseRequest):
    """
    Request model for convert_contact_model_to_file operation.
    Initializes a new instance.

    :param destination_format (str) File format Enum, available values: VCard, WebDav, Msg
    :param contact_dto (ContactDto) Contact model to convert
    """

    def __init__(self, destination_format: str, contact_dto: ContactDto):
        """
        Request model for convert_contact_model_to_file operation.
        Initializes a new instance.

        :param destination_format (str) File format Enum, available values: VCard, WebDav, Msg
        :param contact_dto (ContactDto) Contact model to convert
        """

        BaseRequest.__init__(self)
        self.destination_format = destination_format
        self.contact_dto = contact_dto

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'destination_format' is set
        if self.destination_format is None:
            raise ValueError("Missing the required parameter `destination_format` when calling `convert_contact_model_to_file`")
        # verify the required parameter 'contact_dto' is set
        if self.contact_dto is None:
            raise ValueError("Missing the required parameter `contact_dto` when calling `convert_contact_model_to_file`")

        collection_formats = {}
        path = '/email/ContactModel/model-as-file/{destinationFormat}'
        path_params = {}
        if self.destination_format is not None:
            path_params[self._lowercase_first_letter('destinationFormat')] = self.destination_format

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.contact_dto is not None:
            body_params = self.contact_dto

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
