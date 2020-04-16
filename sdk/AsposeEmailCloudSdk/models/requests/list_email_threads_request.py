#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="list_email_threads_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.list_email_threads_request import ListEmailThreadsRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class ListEmailThreadsRequest(BaseRequest):
    """
    Request model for list_email_threads operation.
    Initializes a new instance.

    :param folder (str) A folder in email account
    :param first_account (str) Email account
    :param second_account (str) Additional email account (for example, firstAccount could be IMAP, and second one could be SMTP)             
    :param storage (str) Storage name where account file(s) located
    :param storage_folder (str) Folder in storage where account file(s) located
    :param update_folder_cache (bool) This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account             
    :param messages_cache_limit (int) Limit messages cache size if CacheFile is used. Ignored in accounts without limits support             
    """

    def __init__(self, folder: str, first_account: str, second_account: str = None, storage: str = None, storage_folder: str = None, update_folder_cache: bool = None, messages_cache_limit: int = None):
        """
        Request model for list_email_threads operation.
        Initializes a new instance.

        :param folder (str) A folder in email account
        :param first_account (str) Email account
        :param second_account (str) Additional email account (for example, firstAccount could be IMAP, and second one could be SMTP)             
        :param storage (str) Storage name where account file(s) located
        :param storage_folder (str) Folder in storage where account file(s) located
        :param update_folder_cache (bool) This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account             
        :param messages_cache_limit (int) Limit messages cache size if CacheFile is used. Ignored in accounts without limits support             
        """

        BaseRequest.__init__(self)
        self.folder = folder
        self.first_account = first_account
        self.second_account = second_account
        self.storage = storage
        self.storage_folder = storage_folder
        self.update_folder_cache = update_folder_cache
        self.messages_cache_limit = messages_cache_limit

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
            raise ValueError("Missing the required parameter `folder` when calling `list_email_threads`")
        # verify the required parameter 'first_account' is set
        if self.first_account is None:
            raise ValueError("Missing the required parameter `first_account` when calling `list_email_threads`")

        collection_formats = {}
        path = '/email/client/threads'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
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
        path_parameter = '{' + self._lowercase_first_letter('updateFolderCache') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.update_folder_cache if self.update_folder_cache is not None else '')
        else:
            if self.update_folder_cache is not None:
                query_params.append((self._lowercase_first_letter('updateFolderCache'), self.update_folder_cache))
        path_parameter = '{' + self._lowercase_first_letter('messagesCacheLimit') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.messages_cache_limit if self.messages_cache_limit is not None else '')
        else:
            if self.messages_cache_limit is not None:
                query_params.append((self._lowercase_first_letter('messagesCacheLimit'), self.messages_cache_limit))

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
