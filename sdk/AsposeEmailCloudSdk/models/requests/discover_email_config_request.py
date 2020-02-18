#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="discover_email_config_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.discover_email_config_request import DiscoverEmailConfigRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class DiscoverEmailConfigRequest(BaseRequest):
    """
    Request model for discover_email_config operation.
    Initializes a new instance.

    :param address (str) Email address
    :param fast_processing (bool) Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned             
    """

    def __init__(self, address: str, fast_processing: bool = None):
        """
        Request model for discover_email_config operation.
        Initializes a new instance.

        :param address (str) Email address
        :param fast_processing (bool) Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned             
        """

        BaseRequest.__init__(self)
        self.address = address
        self.fast_processing = fast_processing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'address' is set
        if self.address is None:
            raise ValueError("Missing the required parameter `address` when calling `discover_email_config`")

        collection_formats = {}
        path = '/email/config/discover'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('address') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.address if self.address is not None else '')
        else:
            if self.address is not None:
                query_params.append((self._lowercase_first_letter('address'), self.address))
        path_parameter = '{' + self._lowercase_first_letter('fastProcessing') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.fast_processing if self.fast_processing is not None else '')
        else:
            if self.fast_processing is not None:
                query_params.append((self._lowercase_first_letter('fastProcessing'), self.fast_processing))

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
