#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_name_parse_email_address_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.ai_name_parse_email_address_request import AiNameParseEmailAddressRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class AiNameParseEmailAddressRequest(BaseRequest):
    """
    Request model for ai_name_parse_email_address operation.
    Initializes a new instance.

    :param email_address (str) Email address to parse (required)
    :param language (str) An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)
    :param location (str) A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France
    :param encoding (str) A character encoding name
    :param script (str) A writing system code; starts with the ISO-15924 script name
    :param style (str) Name writing style. Enum, available values: Formal, Informal, Legal, Academic
    """

    def __init__(self, email_address: str, language: str = None, location: str = None, encoding: str = None, script: str = None, style: str = None):
        BaseRequest.__init__(self)
        self.email_address = email_address
        self.language = language
        self.location = location
        self.encoding = encoding
        self.script = script
        self.style = style

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'email_address' is set
        if self.email_address is None:
            raise ValueError("Missing the required parameter `email_address` when calling `ai_name_parse_email_address`")

        collection_formats = {}
        path = '/email/AiName/parse-email-address'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('emailAddress') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.email_address if self.email_address is not None else '')
        else:
            if self.email_address is not None:
                query_params.append((self._lowercase_first_letter('emailAddress'), self.email_address))
        path_parameter = '{' + self._lowercase_first_letter('language') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.language if self.language is not None else '')
        else:
            if self.language is not None:
                query_params.append((self._lowercase_first_letter('language'), self.language))
        path_parameter = '{' + self._lowercase_first_letter('location') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.location if self.location is not None else '')
        else:
            if self.location is not None:
                query_params.append((self._lowercase_first_letter('location'), self.location))
        path_parameter = '{' + self._lowercase_first_letter('encoding') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.encoding if self.encoding is not None else '')
        else:
            if self.encoding is not None:
                query_params.append((self._lowercase_first_letter('encoding'), self.encoding))
        path_parameter = '{' + self._lowercase_first_letter('script') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.script if self.script is not None else '')
        else:
            if self.script is not None:
                query_params.append((self._lowercase_first_letter('script'), self.script))
        path_parameter = '{' + self._lowercase_first_letter('style') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.style if self.style is not None else '')
        else:
            if self.style is not None:
                query_params.append((self._lowercase_first_letter('style'), self.style))

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
