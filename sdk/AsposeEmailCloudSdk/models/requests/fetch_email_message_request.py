#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="fetch_email_message_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.fetch_email_message_request import FetchEmailMessageRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest


class FetchEmailMessageRequest(BaseRequest):
    """
    Request model for fetch_email_message operation.
    Initializes a new instance.

    :param message_id (str) Message identifier
    :param first_account (str) Email account
    :param second_account (str) Additional email account (should be specified for POP/IMAP accounts and should be SMTP account)             
    :param storage (str) Storage name where account file(s) located
    :param storage_folder (str) Folder in storage where account file(s) located
    """

    def __init__(self, message_id, first_account, second_account=None, storage=None, storage_folder=None):
        BaseRequest.__init__(self)
        self.message_id = message_id
        self.first_account = first_account
        self.second_account = second_account
        self.storage = storage
        self.storage_folder = storage_folder

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'message_id' is set
        if self.message_id is None:
            raise ValueError("Missing the required parameter `message_id` when calling `fetch_email_message`")
        # verify the required parameter 'first_account' is set
        if self.first_account is None:
            raise ValueError("Missing the required parameter `first_account` when calling `fetch_email_message`")

        collection_formats = {}
        path = '/email/client/Fetch'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('messageId') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.message_id if self.message_id is not None else '')
        else:
            if self.message_id is not None:
                query_params.append((self._lowercase_first_letter('messageId'), self.message_id))
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
