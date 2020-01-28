#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="list_email_models_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.list_email_models_request import ListEmailModelsRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class ListEmailModelsRequest(BaseRequest):
    """
    Request model for list_email_models operation.
    Initializes a new instance.

    :param folder (str) A folder in email account
    :param query_string (str) A MailQuery search string
    :param first_account (str) Email account
    :param second_account (str) Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)             
    :param storage (str) Storage name where account file(s) located
    :param storage_folder (str) Folder in storage where account file(s) located
    :param recursive (bool) Specifies that should message be searched in subfolders recursively
    """

    def __init__(self, folder: str, query_string: str, first_account: str, second_account: str = None, storage: str = None, storage_folder: str = None, recursive: bool = None):
        BaseRequest.__init__(self)
        self.folder = folder
        self.query_string = query_string
        self.first_account = first_account
        self.second_account = second_account
        self.storage = storage
        self.storage_folder = storage_folder
        self.recursive = recursive

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'folder' is set
        if self.folder is None:
            raise ValueError("Missing the required parameter `folder` when calling `list_email_models`")
        # verify the required parameter 'query_string' is set
        if self.query_string is None:
            raise ValueError("Missing the required parameter `query_string` when calling `list_email_models`")
        # verify the required parameter 'first_account' is set
        if self.first_account is None:
            raise ValueError("Missing the required parameter `first_account` when calling `list_email_models`")

        collection_formats = {}
        path = '/email/client/ListMessagesModel'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        path_parameter = '{' + self._lowercase_first_letter('queryString') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.query_string if self.query_string is not None else '')
        else:
            if self.query_string is not None:
                query_params.append((self._lowercase_first_letter('queryString'), self.query_string))
        path_parameter = '{' + self._lowercase_first_letter('firstAccount') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.first_account if self.first_account is not None else '')
        else:
            if self.first_account is not None:
                query_params.append((self._lowercase_first_letter('firstAccount'), self.first_account))
        path_parameter = '{' + self._lowercase_first_letter('secondAccount') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.second_account if self.second_account is not None else '')
        else:
            if self.second_account is not None:
                query_params.append((self._lowercase_first_letter('secondAccount'), self.second_account))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))
        path_parameter = '{' + self._lowercase_first_letter('storageFolder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.storage_folder if self.storage_folder is not None else '')
        else:
            if self.storage_folder is not None:
                query_params.append((self._lowercase_first_letter('storageFolder'), self.storage_folder))
        path_parameter = '{' + self._lowercase_first_letter('recursive') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.recursive if self.recursive is not None else '')
        else:
            if self.recursive is not None:
                query_params.append((self._lowercase_first_letter('recursive'), self.recursive))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
