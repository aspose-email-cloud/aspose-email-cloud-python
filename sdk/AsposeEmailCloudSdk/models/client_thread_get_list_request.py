
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_thread_get_list_request.py">
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

from AsposeEmailCloudSdk.models import *


class ClientThreadGetListRequest(object):
    """
    Request model for client_thread_get_list operation.
    Initializes a new instance.

    :param folder (str) A folder in email account.             
    :param account (str) Email account
    :param storage (str) Storage name where account file located
    :param account_storage_folder (str) Folder in storage where account file located
    :param update_folder_cache (bool) This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account             
    :param messages_cache_limit (int) Limit messages cache size if CacheFile is used. Ignored in accounts without limits support             
    """

    def __init__(self, folder: str, account: str, storage: str = None, account_storage_folder: str = None, update_folder_cache: bool = None, messages_cache_limit: int = None):
        """
        Request model for client_thread_get_list operation.
        Initializes a new instance.

        :param folder (str) A folder in email account.             
        :param account (str) Email account
        :param storage (str) Storage name where account file located
        :param account_storage_folder (str) Folder in storage where account file located
        :param update_folder_cache (bool) This parameter is only used in accounts with CacheFile. If true - get new messages and update threads cache for given folder. If false, get only threads from cache without any calls to an email account             
        :param messages_cache_limit (int) Limit messages cache size if CacheFile is used. Ignored in accounts without limits support             
        """

        self.folder = folder
        self.account = account
        self.storage = storage
        self.account_storage_folder = account_storage_folder
        self.update_folder_cache = update_folder_cache
        self.messages_cache_limit = messages_cache_limit