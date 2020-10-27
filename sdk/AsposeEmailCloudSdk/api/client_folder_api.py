#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_folder_api.py">
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


class ClientFolderApi(ApiBase):
    """
    Aspose.Email Cloud API. ClientFolderApi operations.

    """

    def __init__(self, api_client):
        super(ClientFolderApi, self).__init__(api_client)

    def create(self, request: ClientFolderCreateRequest):
        """Create new folder in email account             

        :param request: Create folder request
        :type request: ClientFolderCreateRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `create`")

        collection_formats = {}
        path = '/email/client/folder'

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

    def delete(self, request: ClientFolderDeleteRequest):
        """Delete a folder in email account             

        :param request: Delete folder request
        :type request: ClientFolderDeleteRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `delete`")

        collection_formats = {}
        path = '/email/client/folder'

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

        return self._make_request(http_request_object, 'DELETE', None)

    def get_list(self, request: ClientFolderGetListRequest) -> MailServerFolderList:
        """Get folders list in email account             


        :param request: ClientFolderGetListRequest object with parameters
        :type request: ClientFolderGetListRequest
        :return: MailServerFolderList
        """
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `get_list`")

        collection_formats = {}
        path = '/email/client/folder/list'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('account') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account if request.account is not None else '')
        else:
            if request.account is not None:
                query_params.append((self._lowercase_first_letter('account'), request.account))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))
        path_parameter = '{' + self._lowercase_first_letter('accountStorageFolder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account_storage_folder if request.account_storage_folder is not None else '')
        else:
            if request.account_storage_folder is not None:
                query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        path_parameter = '{' + self._lowercase_first_letter('parentFolder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.parent_folder if request.parent_folder is not None else '')
        else:
            if request.parent_folder is not None:
                query_params.append((self._lowercase_first_letter('parentFolder'), request.parent_folder))

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

        return self._make_request(http_request_object, 'GET', 'MailServerFolderList')

