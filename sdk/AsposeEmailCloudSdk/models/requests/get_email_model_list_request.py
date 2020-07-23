#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="get_email_model_list_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.get_email_model_list_request import GetEmailModelListRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class GetEmailModelListRequest(BaseRequest):
    """
    Request model for get_email_model_list operation.
    Initializes a new instance.

    :param format (str) Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
    :param folder (str) Path to folder in storage.
    :param storage (str) Storage name.
    :param items_per_page (int) Count of items on page.
    :param page_number (int) Page number.
    """

    def __init__(self, format: str, folder: str = None, storage: str = None, items_per_page: int = None, page_number: int = None):
        """
        Request model for get_email_model_list operation.
        Initializes a new instance.

        :param format (str) Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
        :param folder (str) Path to folder in storage.
        :param storage (str) Storage name.
        :param items_per_page (int) Count of items on page.
        :param page_number (int) Page number.
        """

        BaseRequest.__init__(self)
        self.format = format
        self.folder = folder
        self.storage = storage
        self.items_per_page = items_per_page
        self.page_number = page_number

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_email_model_list`")

        collection_formats = {}
        path = '/email/model/{format}'
        path_params = {}
        if self.format is not None:
            path_params[self._lowercase_first_letter('format')] = self.format

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))
        path_parameter = '{' + self._lowercase_first_letter('itemsPerPage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.items_per_page if self.items_per_page is not None else '')
        else:
            if self.items_per_page is not None:
                query_params.append((self._lowercase_first_letter('itemsPerPage'), self.items_per_page))
        path_parameter = '{' + self._lowercase_first_letter('pageNumber') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.page_number if self.page_number is not None else '')
        else:
            if self.page_number is not None:
                query_params.append((self._lowercase_first_letter('pageNumber'), self.page_number))

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
