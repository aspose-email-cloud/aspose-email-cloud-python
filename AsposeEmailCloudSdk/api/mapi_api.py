#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="mapi_api.py">
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

from __future__ import absolute_import

import six

from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.configuration import Configuration
from AsposeEmailCloudSdk.rest import ApiException


class MapiApi(object):
    """
    Aspose.Email Cloud API

    """

    def __init__(self, app_key=None, app_sid=None, base_url=None,
                 api_version=None, debug=False):
        """
        Initializes a new instance of the MapiApi class.

        :param app_key: The app key.
        :param app_sid: The app sid.
        :param base_url: The base URL.
        :param api_version: API version.
        :param debug: If debug mode is enabled. False by default.
        :param on_premise:
            True for on-premise solution with metered license usage.
            False for Aspose Cloud-hosted solution usage, default.
        """
        configuration = Configuration(app_key=app_key,
                                      app_sid=app_sid,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug)
        self.api_client = ApiClient(configuration)

    def add_mapi_attachment(self, request):
        """Add attachment to document


        :param request add_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def add_mapi_attachment_async(self, request):
        """Add attachment to document


        :param request add_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_mapi(self, request):
        """Create new document


        :param request create_mapi_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_mapi_async(self, request):
        """Create new document


        :param request create_mapi_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def delete_mapi_attachment(self, request):
        """Remove attachment from document


        :param request delete_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_attachment_async(self, request):
        """Remove attachment from document


        :param request delete_mapi_attachment_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_mapi_properties(self, request):
        """Delete document properties


        :param request delete_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_mapi_properties_async(self, request):
        """Delete document properties


        :param request delete_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def get_mapi_attachment(self, request):
        """Get document attachment as file stream


        :param request get_mapi_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_mapi_attachment_async(self, request):
        """Get document attachment as file stream


        :param request get_mapi_attachment_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_mapi_attachments(self, request):
        """Get document attachment list


        :param request get_mapi_attachments_request object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_attachments_async(self, request):
        """Get document attachment list


        :param request get_mapi_attachments_request object with parameters
        :return: ListResponseOfString
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfString')

    def get_mapi_list(self, request):
        """Get document list from storage folder


        :param request get_mapi_list_request object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_list_async(self, request):
        """Get document list from storage folder


        :param request get_mapi_list_request object with parameters
        :return: ListResponseOfHierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListResponseOfHierarchicalObjectResponse')

    def get_mapi_properties(self, request):
        """Get document properties


        :param request get_mapi_properties_request object with parameters
        :return: HierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'HierarchicalObjectResponse')

    def get_mapi_properties_async(self, request):
        """Get document properties


        :param request get_mapi_properties_request object with parameters
        :return: HierarchicalObjectResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'HierarchicalObjectResponse')

    def update_mapi_properties(self, request):
        """Update document properties


        :param request update_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_mapi_properties_async(self, request):
        """Update document properties


        :param request update_mapi_properties_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def __make_request(self, http_request, method, return_type):
        def call_api():
            return self.api_client.call_api(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api()
            raise

    def __make_request_async(self, http_request, method, return_type):
        def call_api_async():
            self.api_client.call_api_async(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api_async()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

