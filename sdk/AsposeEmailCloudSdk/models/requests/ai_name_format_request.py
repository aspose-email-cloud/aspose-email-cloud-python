#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_name_format_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.ai_name_format_request import AiNameFormatRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest
from AsposeEmailCloudSdk.models import *


class AiNameFormatRequest(BaseRequest):
    """
    Request model for ai_name_format operation.
    Initializes a new instance.

    :param name (str) A name to format (required)
    :param language (str) An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             
    :param location (str) A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             
    :param encoding (str) A character encoding name
    :param script (str) A writing system code; starts with the ISO-15924 script name
    :param format (str) Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (= '%t%F%m%N%L%p')     /format/FN+LN/ (= '%F%L')     /format/title+FN+LN/ (= '%t%F%L')     /format/FN+MN+LN/ (= '%F%M%N%L')     /format/title+FN+MN+LN/ (= '%t%F%M%N%L')     /format/FN+MI+LN/ (= '%F%m%N%L')     /format/title+FN+MI+LN/ (= '%t%F%m%N%L')     /format/LN/ (= '%L')     /format/title+LN/ (= '%t%L')     /format/LN+FN+MN/ (= '%L,%F%M%N')     /format/LN+title+FN+MN/ (= '%L,%t%F%M%N')     /format/LN+FN+MI/ (= '%L,%F%m%N')     /format/LN+title+FN+MI/ (= '%L,%t%F%m%N')  Custom format string - custom combination of characters and the next term placeholders:      '%t' - Title (prefix)     '%F' - First name     '%f' - First initial     '%M' - Middle name(s)     '%m' - Middle initial(s)     '%N' - Nickname     '%L' - Last name     '%l' - Last initial     '%p' - Postfix  If no value for format option was provided, its default value is '%t%F%m%N%L%p'             
    :param style (str) Name writing style. Enum, available values: Formal, Informal, Legal, Academic
    """

    def __init__(self, name: str, language: str = None, location: str = None, encoding: str = None, script: str = None, format: str = None, style: str = None):
        """
        Request model for ai_name_format operation.
        Initializes a new instance.

        :param name (str) A name to format (required)
        :param language (str) An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             
        :param location (str) A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             
        :param encoding (str) A character encoding name
        :param script (str) A writing system code; starts with the ISO-15924 script name
        :param format (str) Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (= '%t%F%m%N%L%p')     /format/FN+LN/ (= '%F%L')     /format/title+FN+LN/ (= '%t%F%L')     /format/FN+MN+LN/ (= '%F%M%N%L')     /format/title+FN+MN+LN/ (= '%t%F%M%N%L')     /format/FN+MI+LN/ (= '%F%m%N%L')     /format/title+FN+MI+LN/ (= '%t%F%m%N%L')     /format/LN/ (= '%L')     /format/title+LN/ (= '%t%L')     /format/LN+FN+MN/ (= '%L,%F%M%N')     /format/LN+title+FN+MN/ (= '%L,%t%F%M%N')     /format/LN+FN+MI/ (= '%L,%F%m%N')     /format/LN+title+FN+MI/ (= '%L,%t%F%m%N')  Custom format string - custom combination of characters and the next term placeholders:      '%t' - Title (prefix)     '%F' - First name     '%f' - First initial     '%M' - Middle name(s)     '%m' - Middle initial(s)     '%N' - Nickname     '%L' - Last name     '%l' - Last initial     '%p' - Postfix  If no value for format option was provided, its default value is '%t%F%m%N%L%p'             
        :param style (str) Name writing style. Enum, available values: Formal, Informal, Legal, Academic
        """

        BaseRequest.__init__(self)
        self.name = name
        self.language = language
        self.location = location
        self.encoding = encoding
        self.script = script
        self.format = format
        self.style = style

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Email API configuration
        :type: AsposeEmailCloudSdk.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `ai_name_format`")

        collection_formats = {}
        path = '/email/AiName/format'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('name') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.name if self.name is not None else '')
        else:
            if self.name is not None:
                query_params.append((self._lowercase_first_letter('name'), self.name))
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
        path_parameter = '{' + self._lowercase_first_letter('format') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, self.format if self.format is not None else '')
        else:
            if self.format is not None:
                query_params.append((self._lowercase_first_letter('format'), self.format))
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
