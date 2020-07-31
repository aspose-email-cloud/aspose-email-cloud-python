
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="contact_api.py">
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


class ContactApi(ApiBase):
    """
    Aspose.Email Cloud API. ContactApi operations.

    """

    def __init__(self, api_client):
        super(ApiBase, self).__init__(api_client)
            
    def as_file(self, request: ContactAsFileRequest) -> str:
        """Converts contact model to specified format and returns as file             

        :param request ContactAsFileRequest Contact model and format to convert
        :return: str
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `as_file`")

        collection_formats = {}
        path = '/email/Contact/as-file'

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
            
    def as_mapi(self, contact_dto: ContactDto) -> MapiContactDto:
        """Converts ContactDto to MapiContactDto.             

        :param contact_dto ContactDto Contact model to convert
        :return: MapiContactDto
        """
        # verify the required parameter 'contact_dto' is set
        if contact_dto is None:
            raise ValueError("Missing the required parameter `contact_dto` when calling `as_mapi`")

        collection_formats = {}
        path = '/email/Contact/as-mapi'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = contact_dto
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'MapiContactDto')
            
    def convert(self, request: ContactConvertRequest) -> str:
        """Converts contact document to specified format and returns as file             


        :param request ContactConvertRequest object with parameters
        :return: str
        """
        # verify the required parameter 'to_format' is set
        if request.to_format is None:
            raise ValueError("Missing the required parameter `to_format` when calling `convert`")
        # verify the required parameter 'from_format' is set
        if request.from_format is None:
            raise ValueError("Missing the required parameter `from_format` when calling `convert`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `convert`")

        collection_formats = {}
        path = '/email/Contact/convert'

        query_params = []
        if request.to_format is not None:
            query_params.append((self._lowercase_first_letter('toFormat'), request.to_format))
        if request.from_format is not None:
            query_params.append((self._lowercase_first_letter('fromFormat'), request.from_format))

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'file')
            
    def from_file(self, request: ContactFromFileRequest) -> ContactDto:
        """Converts contact document to a model representation             


        :param request ContactFromFileRequest object with parameters
        :return: ContactDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `from_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `from_file`")

        collection_formats = {}
        path = '/email/Contact/from-file'

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

        return self._make_request(http_request_object, 'PUT', 'ContactDto')
            
    def get(self, request: ContactGetRequest) -> ContactDto:
        """Get contact document from storage.             


        :param request ContactGetRequest object with parameters
        :return: ContactDto
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get`")
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get`")

        collection_formats = {}
        path = '/email/Contact'

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

        return self._make_request(http_request_object, 'GET', 'ContactDto')
            
    def get_as_file(self, request: ContactGetAsFileRequest) -> str:
        """Converts contact document from storage to specified format and returns as file             


        :param request ContactGetAsFileRequest object with parameters
        :return: str
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get_as_file`")
        # verify the required parameter 'to_format' is set
        if request.to_format is None:
            raise ValueError("Missing the required parameter `to_format` when calling `get_as_file`")
        # verify the required parameter 'from_format' is set
        if request.from_format is None:
            raise ValueError("Missing the required parameter `from_format` when calling `get_as_file`")

        collection_formats = {}
        path = '/email/Contact/as-file'

        query_params = []
        if request.file_name is not None:
            query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        if request.to_format is not None:
            query_params.append((self._lowercase_first_letter('toFormat'), request.to_format))
        if request.from_format is not None:
            query_params.append((self._lowercase_first_letter('fromFormat'), request.from_format))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))

        form_params = []
        local_var_files = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'file')
            
    def get_list(self, request: ContactGetListRequest) -> ContactStorageList:
        """Get contact list from storage folder.             


        :param request ContactGetListRequest object with parameters
        :return: ContactStorageList
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_list`")

        collection_formats = {}
        path = '/email/Contact/list'

        query_params = []
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.items_per_page is not None:
            query_params.append((self._lowercase_first_letter('itemsPerPage'), request.items_per_page))
        if request.page_number is not None:
            query_params.append((self._lowercase_first_letter('pageNumber'), request.page_number))

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

        return self._make_request(http_request_object, 'GET', 'ContactStorageList')
            
    def save(self, request: ContactSaveRequest):
        """Save contact to storage.             

        :param request ContactSaveRequest Create/Update contact request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save`")

        collection_formats = {}
        path = '/email/Contact'

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
