#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="copy_folder_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.copy_folder_request import CopyFolderRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class CopyFolderRequest(BaseRequest):
    """
    Request model for copy_folder operation.
    Initializes a new instance.

    :param src_path (str) Source folder path e.g. '/src'
    :param dest_path (str) Destination folder path e.g. '/dst'
    :param src_storage_name (str) Source storage name
    :param dest_storage_name (str) Destination storage name
    """

    def __init__(self, src_path: str, dest_path: str, src_storage_name: str = None, dest_storage_name: str = None):
        """
        Request model for copy_folder operation.
        Initializes a new instance.

        :param src_path (str) Source folder path e.g. '/src'
        :param dest_path (str) Destination folder path e.g. '/dst'
        :param src_storage_name (str) Source storage name
        :param dest_storage_name (str) Destination storage name
        """

        BaseRequest.__init__(self)
        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_folder`")
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_folder`")

        collection_formats = {}
        path = '/email/storage/folder/copy/{srcPath}'
        path_params = {}
        if self.src_path is not None:
            path_params[self._lowercase_first_letter('srcPath')] = self.src_path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('destPath') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.dest_path if self.dest_path is not None else '')
        else:
            if self.dest_path is not None:
                query_params.append((self._lowercase_first_letter('destPath'), self.dest_path))
        path_parameter = '{' + self._lowercase_first_letter('srcStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.src_storage_name if self.src_storage_name is not None else '')
        else:
            if self.src_storage_name is not None:
                query_params.append((self._lowercase_first_letter('srcStorageName'), self.src_storage_name))
        path_parameter = '{' + self._lowercase_first_letter('destStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.dest_storage_name if self.dest_storage_name is not None else '')
        else:
            if self.dest_storage_name is not None:
                query_params.append((self._lowercase_first_letter('destStorageName'), self.dest_storage_name))

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
