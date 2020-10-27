#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_bcr_api.py">
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


class AiBcrApi(ApiBase):
    """
    Aspose.Email Cloud API. AiBcrApi operations.

    """

    def __init__(self, api_client):
        super(AiBcrApi, self).__init__(api_client)

    def parse(self, request: AiBcrParseRequest) -> ContactList:
        """Parse images to vCard document models             


        :param request: AiBcrParseRequest object with parameters
        :type request: AiBcrParseRequest
        :return: ContactList
        """
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `parse`")

        collection_formats = {}
        path = '/email/AiBcr/parse'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('countries') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.countries if request.countries is not None else '')
        else:
            if request.countries is not None:
                query_params.append((self._lowercase_first_letter('countries'), request.countries))
        path_parameter = '{' + self._lowercase_first_letter('languages') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.languages if request.languages is not None else '')
        else:
            if request.languages is not None:
                query_params.append((self._lowercase_first_letter('languages'), request.languages))
        path_parameter = '{' + self._lowercase_first_letter('isSingle') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.is_single if request.is_single is not None else '')
        else:
            if request.is_single is not None:
                query_params.append((self._lowercase_first_letter('isSingle'), request.is_single))

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

        return self._make_request(http_request_object, 'PUT', 'ContactList')

    def parse_storage(self, request: AiBcrParseStorageRequest) -> StorageFileLocationList:
        """Parse images from storage to vCard files             

        :param request: Request with images located on storage
        :type request: AiBcrParseStorageRequest
        :return: StorageFileLocationList
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `parse_storage`")

        collection_formats = {}
        path = '/email/AiBcr/parse-storage'

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

        return self._make_request(http_request_object, 'PUT', 'StorageFileLocationList')

