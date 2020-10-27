#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_thread_api.py">
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


class ClientThreadApi(ApiBase):
    """
    Aspose.Email Cloud API. ClientThreadApi operations.

    """

    def __init__(self, api_client):
        super(ClientThreadApi, self).__init__(api_client)

    def delete(self, request: ClientThreadDeleteRequest):
        """Delete thread by id. All messages from thread will also be deleted.             

        :param request: Delete email thread request.
        :type request: ClientThreadDeleteRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `delete`")

        collection_formats = {}
        path = '/email/client/thread'

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

        return self._make_request(http_request_object, 'DELETE', None)

    def get_list(self, request: ClientThreadGetListRequest) -> EmailThreadList:
        """Get message threads from folder. All messages are partly fetched (without email body and some other fields).             


        :param request: ClientThreadGetListRequest object with parameters
        :type request: ClientThreadGetListRequest
        :return: EmailThreadList
        """
        # verify the required parameter 'folder' is set
        if request.folder is None:
            raise ValueError("Missing the required parameter `folder` when calling `get_list`")
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `get_list`")

        collection_formats = {}
        path = '/email/client/thread/list'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('account') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account if request.account is not None else '')
        else:
            if request.account is not None:
                query_params.append((self._lowercase_first_letter('account'), request.account))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))
        path_parameter = '{' + self._lowercase_first_letter('accountStorageFolder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account_storage_folder if request.account_storage_folder is not None else '')
        else:
            if request.account_storage_folder is not None:
                query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        path_parameter = '{' + self._lowercase_first_letter('updateFolderCache') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.update_folder_cache if request.update_folder_cache is not None else '')
        else:
            if request.update_folder_cache is not None:
                query_params.append((self._lowercase_first_letter('updateFolderCache'), request.update_folder_cache))
        path_parameter = '{' + self._lowercase_first_letter('messagesCacheLimit') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.messages_cache_limit if request.messages_cache_limit is not None else '')
        else:
            if request.messages_cache_limit is not None:
                query_params.append((self._lowercase_first_letter('messagesCacheLimit'), request.messages_cache_limit))

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

        return self._make_request(http_request_object, 'GET', 'EmailThreadList')

    def get_messages(self, request: ClientThreadGetMessagesRequest) -> EmailList:
        """Get messages from thread by id. All messages are fully fetched. For accounts with CacheFile only cached messages will be returned.             


        :param request: ClientThreadGetMessagesRequest object with parameters
        :type request: ClientThreadGetMessagesRequest
        :return: EmailList
        """
        # verify the required parameter 'thread_id' is set
        if request.thread_id is None:
            raise ValueError("Missing the required parameter `thread_id` when calling `get_messages`")
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `get_messages`")

        collection_formats = {}
        path = '/email/client/thread/messages'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('threadId') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.thread_id if request.thread_id is not None else '')
        else:
            if request.thread_id is not None:
                query_params.append((self._lowercase_first_letter('threadId'), request.thread_id))
        path_parameter = '{' + self._lowercase_first_letter('account') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account if request.account is not None else '')
        else:
            if request.account is not None:
                query_params.append((self._lowercase_first_letter('account'), request.account))
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))
        path_parameter = '{' + self._lowercase_first_letter('accountStorageFolder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.account_storage_folder if request.account_storage_folder is not None else '')
        else:
            if request.account_storage_folder is not None:
                query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))

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

        return self._make_request(http_request_object, 'GET', 'EmailList')

    def move(self, request: ClientThreadMoveRequest):
        """Move thread to another folder.             

        :param request: Move thread request.
        :type request: ClientThreadMoveRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `move`")

        collection_formats = {}
        path = '/email/client/thread/move'

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

        return self._make_request(http_request_object, 'PUT', None)

    def set_is_read(self, request: ClientThreadSetIsReadRequest):
        """Mark all messages in thread as read or unread.             

        :param request: Email account specifier and IsRead flag.
        :type request: ClientThreadSetIsReadRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `set_is_read`")

        collection_formats = {}
        path = '/email/client/thread/set-is-read'

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

        return self._make_request(http_request_object, 'PUT', None)

