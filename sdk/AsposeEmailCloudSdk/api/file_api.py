#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="file_api.py">
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


class FileApi(ApiBase):
    """
    Aspose.Email Cloud API. FileApi operations.

    """

    def __init__(self, api_client):
        super(FileApi, self).__init__(api_client)

    def copy_file(self, request: CopyFileRequest):
        """Copy file


        :param request: CopyFileRequest object with parameters
        :type request: CopyFileRequest
        :return: None
        """
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")

        collection_formats = {}
        path = '/email/storage/file/copy/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self._lowercase_first_letter('srcPath')] = request.src_path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('destPath') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self._lowercase_first_letter('destPath'), request.dest_path))
        path_parameter = '{' + self._lowercase_first_letter('srcStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self._lowercase_first_letter('srcStorageName'), request.src_storage_name))
        path_parameter = '{' + self._lowercase_first_letter('destStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self._lowercase_first_letter('destStorageName'), request.dest_storage_name))
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

        return self._make_request(http_request_object, 'PUT', None)

    def delete_file(self, request: DeleteFileRequest):
        """Delete file


        :param request: DeleteFileRequest object with parameters
        :type request: DeleteFileRequest
        :return: None
        """
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_file`")

        collection_formats = {}
        path = '/email/storage/file/{path}'
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

        return self._make_request(http_request_object, 'DELETE', None)

    def download_file(self, request: DownloadFileRequest) -> str:
        """Download file


        :param request: DownloadFileRequest object with parameters
        :type request: DownloadFileRequest
        :return: str
        """
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `download_file`")

        collection_formats = {}
        path = '/email/storage/file/{path}'
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
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'file')

    def move_file(self, request: MoveFileRequest):
        """Move file


        :param request: MoveFileRequest object with parameters
        :type request: MoveFileRequest
        :return: None
        """
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_file`")
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_file`")

        collection_formats = {}
        path = '/email/storage/file/move/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self._lowercase_first_letter('srcPath')] = request.src_path

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('destPath') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self._lowercase_first_letter('destPath'), request.dest_path))
        path_parameter = '{' + self._lowercase_first_letter('srcStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self._lowercase_first_letter('srcStorageName'), request.src_storage_name))
        path_parameter = '{' + self._lowercase_first_letter('destStorageName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self._lowercase_first_letter('destStorageName'), request.dest_storage_name))
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

        return self._make_request(http_request_object, 'PUT', None)

    def upload_file(self, request: UploadFileRequest) -> FilesUploadResult:
        """Upload file


        :param request: UploadFileRequest object with parameters
        :type request: UploadFileRequest
        :return: FilesUploadResult
        """
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `upload_file`")

        collection_formats = {}
        path = '/email/storage/file/{path}'
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
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'FilesUploadResult')

