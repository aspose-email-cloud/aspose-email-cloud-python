#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="add_contact_attachment_request.py">
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
##for __init__.py:from AsposeEmailCloudSdk.models.requests.add_contact_attachment_request import AddContactAttachmentRequest

from AsposeEmailCloudSdk.models.requests.base_request import BaseRequest
from AsposeEmailCloudSdk.models.requests.http_request import HttpRequest


class AddContactAttachmentRequest(BaseRequest):
    """
    Request model for add_contact_attachment operation.
    Initializes a new instance.

    :param format Contact document format
    :param name Contact document file name
    :param attachment Attachment name
    :param request Add attachment request
    """

    def __init__(self, format, name, attachment, request):
        BaseRequest.__init__(self)
        self.format = format
        self.name = name
        self.attachment = attachment
        self.request = request

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
            raise ValueError("Missing the required parameter `format` when calling `add_contact_attachment`")
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `add_contact_attachment`")
        # verify the required parameter 'attachment' is set
        if self.attachment is None:
            raise ValueError("Missing the required parameter `attachment` when calling `add_contact_attachment`")
        # verify the required parameter 'request' is set
        if self.request is None:
            raise ValueError("Missing the required parameter `request` when calling `add_contact_attachment`")

        collection_formats = {}
        path = '/email/Contact/{format}/{name}/attachments/{attachment}'
        path_params = {}
        if self.format is not None:
            path_params[self._lowercase_first_letter('format')] = self.format
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name
        if self.attachment is not None:
            path_params[self._lowercase_first_letter('attachment')] = self.attachment

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