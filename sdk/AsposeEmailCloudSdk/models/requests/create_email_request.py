#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="create_email_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.create_email_request import CreateEmailRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class CreateEmailRequest(BaseRequest):
    """
    Request model for create_email operation.
    Initializes a new instance.

    :param file_name (str) Email document file name in storage
    :param request (CreateEmailRequest) An email document and optional Storage info to specify where the file should be located
    """

    def __init__(self, file_name: str, request: CreateEmailRequest):
        BaseRequest.__init__(self)
        self.file_name = file_name
        self.request = request

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'file_name' is set
        if self.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `create_email`")
        # verify the required parameter 'request' is set
        if self.request is None:
            raise ValueError("Missing the required parameter `request` when calling `create_email`")

        collection_formats = {}
        path = '/email/{fileName}'
        path_params = {}
        if self.file_name is not None:
            path_params[self._lowercase_first_letter('fileName')] = self.file_name

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.request is not None:
            body_params = self.request

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
