#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="disposable_email_api.py">
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


class DisposableEmailApi(ApiBase):
    """
    Aspose.Email Cloud API. DisposableEmailApi operations.

    """

    def __init__(self, api_client):
        super(DisposableEmailApi, self).__init__(api_client)

    def is_disposable(self, request: DisposableEmailIsDisposableRequest) -> ValueTOfBoolean:
        """Check email address is disposable             


        :param request: DisposableEmailIsDisposableRequest object with parameters
        :type request: DisposableEmailIsDisposableRequest
        :return: ValueTOfBoolean
        """
        # verify the required parameter 'address' is set
        if request.address is None:
            raise ValueError("Missing the required parameter `address` when calling `is_disposable`")

        collection_formats = {}
        path = '/email/disposable/is-disposable'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('address') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.address if request.address is not None else '')
        else:
            if request.address is not None:
                query_params.append((self._lowercase_first_letter('address'), request.address))

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'ValueTOfBoolean')

