
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_account_api.py">
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


class ClientAccountApi(ApiBase):
    """
    Aspose.Email Cloud API. ClientAccountApi operations.

    """

    def __init__(self, api_client):
        super(ApiBase, self).__init__(api_client)
            
    def get(self, request: ClientAccountGetRequest) -> EmailClientAccount:
        """Get email client account from storage.             


        :param request ClientAccountGetRequest object with parameters
        :return: EmailClientAccount
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get`")

        collection_formats = {}
        path = '/email/client/account'

        query_params = []
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

        return self._make_request(http_request_object, 'GET', 'EmailClientAccount')
            
    def get_multi(self, request: ClientAccountGetMultiRequest) -> EmailClientMultiAccount:
        """Get email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             


        :param request ClientAccountGetMultiRequest object with parameters
        :return: EmailClientMultiAccount
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get_multi`")

        collection_formats = {}
        path = '/email/client/account/multi'

        query_params = []
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

        return self._make_request(http_request_object, 'GET', 'EmailClientMultiAccount')
            
    def save(self, request: EmailClientAccountSaveRequest):
        """Create/update email client account file (*.account) with credentials             

        :param request EmailClientAccountSaveRequest Email account information
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save`")

        collection_formats = {}
        path = '/email/client/account'

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
            
    def save_multi(self, request: EmailClientMultiAccountSaveRequest):
        """Create email client multi account file (*.multi.account). Will respond error if file extension is not \&quot;.multi.account\&quot;.             

        :param request EmailClientMultiAccountSaveRequest Email accounts information.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save_multi`")

        collection_formats = {}
        path = '/email/client/account/multi'

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