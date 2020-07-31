
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="mapi_message_api.py">
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

from AsposeEmailCloudSdk.api.api_base import ApiBase
from AsposeEmailCloudSdk.models import *


class MapiMessageApi(ApiBase):
    """
    Aspose.Email Cloud API. MapiMessageApi operations.

    """

    def __init__(self, api_client):
        super(ApiBase, self).__init__(api_client)
            
    def as_email_dto(self, mapi_message: MapiMessageDto) -> EmailDto:
        """Converts MAPI message model to EmailDto model             

        :param mapi_message MapiMessageDto MAPI message model to convert
        :return: EmailDto
        """
        # verify the required parameter 'mapi_message' is set
        if mapi_message is None:
            raise ValueError("Missing the required parameter `mapi_message` when calling `as_email_dto`")

        collection_formats = {}
        path = '/email/MapiMessage/as-email-dto'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = mapi_message
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'EmailDto')
            
    def as_file(self, request: MapiMessageAsFileRequest) -> str:
        """Converts MAPI message model to specified format and returns as file.             

        :param request MapiMessageAsFileRequest MAPI message model to convert.
        :return: str
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `as_file`")

        collection_formats = {}
        path = '/email/MapiMessage/as-file'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'file')
            
    def from_file(self, request: MapiMessageFromFileRequest) -> MapiMessageDto:
        """Converts email file to a MAPI model representation             


        :param request MapiMessageFromFileRequest object with parameters
        :return: MapiMessageDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `from_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `from_file`")

        collection_formats = {}
        path = '/email/MapiMessage/from-file'

        query_params = []
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'MapiMessageDto')
            
    def get(self, request: MapiMessageGetRequest) -> MapiMessageDto:
        """Get MAPI message document.             


        :param request MapiMessageGetRequest object with parameters
        :return: MapiMessageDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get`")
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get`")

        collection_formats = {}
        path = '/email/MapiMessage'

        query_params = []
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))
        if request.file_name is not None:
            query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))

        form_params = []
        local_var_files = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'MapiMessageDto')
            
    def save(self, request: MapiMessageSaveRequest):
        """Save MAPI message to storage.             

        :param request MapiMessageSaveRequest Message create/update request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save`")

        collection_formats = {}
        path = '/email/MapiMessage'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', None)
