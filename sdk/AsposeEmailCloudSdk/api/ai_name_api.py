
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_name_api.py">
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


class AiNameApi(ApiBase):
    """
    Aspose.Email Cloud API. AiNameApi operations.

    """

    def __init__(self, api_client):
        super(ApiBase, self).__init__(api_client)
            
    def complete(self, request: AiNameCompleteRequest) -> AiNameWeightedVariants:
        """The call proposes k most probable names for given starting characters.             


        :param request AiNameCompleteRequest object with parameters
        :return: AiNameWeightedVariants
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `complete`")

        collection_formats = {}
        path = '/email/AiName/complete'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameWeightedVariants')
            
    def expand(self, request: AiNameExpandRequest) -> AiNameWeightedVariants:
        """Expands a person&#39;s name into a list of possible alternatives using options for expanding instructions.             


        :param request AiNameExpandRequest object with parameters
        :return: AiNameWeightedVariants
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `expand`")

        collection_formats = {}
        path = '/email/AiName/expand'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameWeightedVariants')
            
    def expand_parsed(self, request: AiNameParsedRequest) -> AiNameWeightedVariants:
        """Expands a person&#39;s parsed name into a list of possible alternatives using options for expanding instructions.             

        :param request AiNameParsedRequest Parsed name with options.
        :return: AiNameWeightedVariants
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `expand_parsed`")

        collection_formats = {}
        path = '/email/AiName/expand-parsed'

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

        return self._make_request(http_request_object, 'PUT', 'AiNameWeightedVariants')
            
    def format(self, request: AiNameFormatRequest) -> AiNameFormatted:
        """Formats a person&#39;s name in correct case and name order using options for formatting instructions.             


        :param request AiNameFormatRequest object with parameters
        :return: AiNameFormatted
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `format`")

        collection_formats = {}
        path = '/email/AiName/format'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameFormatted')
            
    def format_parsed(self, request: AiNameParsedRequest) -> AiNameFormatted:
        """Formats a person&#39;s parsed name in correct case and name order using options for formatting instructions.             

        :param request AiNameParsedRequest Parsed name with options.
        :return: AiNameFormatted
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `format_parsed`")

        collection_formats = {}
        path = '/email/AiName/format-parsed'

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

        return self._make_request(http_request_object, 'PUT', 'AiNameFormatted')
            
    def genderize(self, request: AiNameGenderizeRequest) -> AiNameGenderHypothesisList:
        """Detect person&#39;s gender from name string.             


        :param request AiNameGenderizeRequest object with parameters
        :return: AiNameGenderHypothesisList
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `genderize`")

        collection_formats = {}
        path = '/email/AiName/genderize'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameGenderHypothesisList')
            
    def genderize_parsed(self, request: AiNameParsedRequest) -> AiNameGenderHypothesisList:
        """Detect person&#39;s gender from parsed name.             

        :param request AiNameParsedRequest Gender detection request data.
        :return: AiNameGenderHypothesisList
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `genderize_parsed`")

        collection_formats = {}
        path = '/email/AiName/genderize-parsed'

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

        return self._make_request(http_request_object, 'PUT', 'AiNameGenderHypothesisList')
            
    def match(self, request: AiNameMatchRequest) -> AiNameMatchResult:
        """Compare people&#39;s names. Uses options for comparing instructions.             


        :param request AiNameMatchRequest object with parameters
        :return: AiNameMatchResult
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `match`")
        # verify the required parameter 'other_name' is set
        if request.other_name is None:
            raise ValueError("Missing the required parameter `other_name` when calling `match`")

        collection_formats = {}
        path = '/email/AiName/match'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.other_name is not None:
            query_params.append((self._lowercase_first_letter('otherName'), request.other_name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameMatchResult')
            
    def match_parsed(self, request: AiNameParsedMatchRequest) -> AiNameMatchResult:
        """Compare people&#39;s parsed names and attributes. Uses options for comparing instructions.             

        :param request AiNameParsedMatchRequest Parsed names to match.
        :return: AiNameMatchResult
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `match_parsed`")

        collection_formats = {}
        path = '/email/AiName/match-parsed'

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

        return self._make_request(http_request_object, 'PUT', 'AiNameMatchResult')
            
    def parse(self, request: AiNameParseRequest) -> AiNameComponentList:
        """Parse name to components.             


        :param request AiNameParseRequest object with parameters
        :return: AiNameComponentList
        """
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `parse`")

        collection_formats = {}
        path = '/email/AiName/parse'

        query_params = []
        if request.name is not None:
            query_params.append((self._lowercase_first_letter('name'), request.name))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameComponentList')
            
    def parse_email_address(self, request: AiNameParseEmailAddressRequest) -> AiNameExtractedList:
        """Parse person&#39;s name out of an email address.             


        :param request AiNameParseEmailAddressRequest object with parameters
        :return: AiNameExtractedList
        """
        # verify the required parameter 'email_address' is set
        if request.email_address is None:
            raise ValueError("Missing the required parameter `email_address` when calling `parse_email_address`")

        collection_formats = {}
        path = '/email/AiName/parse-email-address'

        query_params = []
        if request.email_address is not None:
            query_params.append((self._lowercase_first_letter('emailAddress'), request.email_address))
        if request.language is not None:
            query_params.append((self._lowercase_first_letter('language'), request.language))
        if request.location is not None:
            query_params.append((self._lowercase_first_letter('location'), request.location))
        if request.encoding is not None:
            query_params.append((self._lowercase_first_letter('encoding'), request.encoding))
        if request.script is not None:
            query_params.append((self._lowercase_first_letter('script'), request.script))
        if request.style is not None:
            query_params.append((self._lowercase_first_letter('style'), request.style))

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

        return self._make_request(http_request_object, 'GET', 'AiNameExtractedList')