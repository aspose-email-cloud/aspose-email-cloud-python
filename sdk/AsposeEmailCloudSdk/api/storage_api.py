#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="storage_api.py">
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


class StorageApi(ApiBase):
    """
    Aspose.Email Cloud API. StorageApi operations.

    """

    def __init__(self, api_client):
        super(StorageApi, self).__init__(api_client)

    def get_disc_usage(self, request: GetDiscUsageRequest) -> DiscUsage:
        """Get disc usage


        :param request: GetDiscUsageRequest object with parameters
        :type request: GetDiscUsageRequest
        :return: DiscUsage
        """

        collection_formats = {}
        path = '/email/storage/disc'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('storageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), request.storage_name))

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

        return self._make_request(http_request_object, 'GET', 'DiscUsage')

    def get_file_versions(self, request: GetFileVersionsRequest) -> FileVersions:
        """Get file versions


        :param request: GetFileVersionsRequest object with parameters
        :type request: GetFileVersionsRequest
        :return: FileVersions
        """
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")

        collection_formats = {}
        path = '/email/storage/version/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self._lowercase_first_letter('path')] = request.path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('storageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), request.storage_name))

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

        return self._make_request(http_request_object, 'GET', 'FileVersions')

    def object_exists(self, request: ObjectExistsRequest) -> ObjectExist:
        """Check if file or folder exists


        :param request: ObjectExistsRequest object with parameters
        :type request: ObjectExistsRequest
        :return: ObjectExist
        """
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")

        collection_formats = {}
        path = '/email/storage/exist/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self._lowercase_first_letter('path')] = request.path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('storageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), request.storage_name))
        path_parameter = '{' + self._lowercase_first_letter('versionId') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self._lowercase_first_letter('versionId'), request.version_id))

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

        return self._make_request(http_request_object, 'GET', 'ObjectExist')

    def exists(self, request: StorageExistsRequest) -> StorageExist:
        """Check if storage exists


        :param request: StorageExistsRequest object with parameters
        :type request: StorageExistsRequest
        :return: StorageExist
        """
        # verify the required parameter 'storage_name' is set
        if request.storage_name is None:
            raise ValueError("Missing the required parameter `storage_name` when calling `exists`")

        collection_formats = {}
        path = '/email/storage/{storageName}/exist'
        path_params = {}
        if request.storage_name is not None:
            path_params[self._lowercase_first_letter('storageName')] = request.storage_name

        query_params = []

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

        return self._make_request(http_request_object, 'GET', 'StorageExist')

