#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="mapi_contact_api.py">
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


class MapiContactApi(ApiBase):
    """
    Aspose.Email Cloud API. MapiContactApi operations.

    """

    def __init__(self, api_client):
        super(MapiContactApi, self).__init__(api_client)

    def as_contact_dto(self, mapi_contact_dto: MapiContactDto) -> ContactDto:
        """Converts MAPI contact model to ContactDto model.             

        :param mapi_contact_dto: MAPI contact model to convert.
        :type mapi_contact_dto: MapiContactDto
        :return: ContactDto
        """
        # verify the required parameter 'mapi_contact_dto' is set
        if mapi_contact_dto is None:
            raise ValueError("Missing the required parameter `mapi_contact_dto` when calling `as_contact_dto`")

        collection_formats = {}
        path = '/email/MapiContact/as-contact-dto'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = mapi_contact_dto
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'ContactDto')

    def as_file(self, request: MapiContactAsFileRequest) -> str:
        """Converts MAPI contact model to specified format and returns as file.             

        :param request: MAPI contact model to convert.
        :type request: MapiContactAsFileRequest
        :return: str
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `as_file`")

        collection_formats = {}
        path = '/email/MapiContact/as-file'

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

    def from_file(self, request: MapiContactFromFileRequest) -> MapiContactDto:
        """Converts contact file to a MAPI model representation.             


        :param request: MapiContactFromFileRequest object with parameters
        :type request: MapiContactFromFileRequest
        :return: MapiContactDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `from_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `from_file`")

        collection_formats = {}
        path = '/email/MapiContact/from-file'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('format') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.format if request.format is not None else '')
        else:
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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'MapiContactDto')

    def get(self, request: MapiContactGetRequest) -> MapiContactDto:
        """Get MAPI contact document.             


        :param request: MapiContactGetRequest object with parameters
        :type request: MapiContactGetRequest
        :return: MapiContactDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get`")
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get`")

        collection_formats = {}
        path = '/email/MapiContact'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('format') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self._lowercase_first_letter('format'), request.format))
        path_parameter = '{' + self._lowercase_first_letter('fileName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'MapiContactDto')

    def save(self, request: MapiContactSaveRequest):
        """Save MAPI Contact to storage.             

        :param request: Create/Update contact request.
        :type request: MapiContactSaveRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save`")

        collection_formats = {}
        path = '/email/MapiContact'

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

