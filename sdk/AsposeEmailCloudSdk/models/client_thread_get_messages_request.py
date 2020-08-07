#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_thread_get_messages_request.py">
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


class ClientThreadGetMessagesRequest(object):
    """
    Request model for client_thread_get_messages operation.
    Initializes a new instance.

    :param thread_id: Thread identifier
    :type thread_id: str
    :param account: Email account
    :type account: str
    :param folder: Specifies account folder to get thread from             
    :type folder: str
    :param storage: Storage name where account file located
    :type storage: str
    :param account_storage_folder: Folder in storage where account file located
    :type account_storage_folder: str
    """

    def __init__(self, thread_id: str, account: str, folder: str = None, storage: str = None, account_storage_folder: str = None):
        """
        Request model for client_thread_get_messages operation.
        Initializes a new instance.

        :param thread_id: Thread identifier
        :type thread_id: str
        :param account: Email account
        :type account: str
        :param folder: Specifies account folder to get thread from             
        :type folder: str
        :param storage: Storage name where account file located
        :type storage: str
        :param account_storage_folder: Folder in storage where account file located
        :type account_storage_folder: str
        """

        self.thread_id = thread_id
        self.account = account
        self.folder = folder
        self.storage = storage
        self.account_storage_folder = account_storage_folder

