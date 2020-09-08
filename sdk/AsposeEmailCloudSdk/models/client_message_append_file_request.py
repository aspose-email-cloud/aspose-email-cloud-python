#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_message_append_file_request.py">
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


class ClientMessageAppendFileRequest(object):
    """
    Request model for client_message_append_file operation.
    Initializes a new instance.

    :param account: Email account.
    :type account: str
    :param file: Message file to append.
    :type file: str
    :param storage: Storage name where account file located.
    :type storage: str
    :param account_storage_folder: Folder in storage where account file located.
    :type account_storage_folder: str
    :param format: Email file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft
    :type format: str
    :param folder: Path to folder on email server to append message to.
    :type folder: str
    :param mark_as_sent: Determines that appended message should be market as sent or not.
    :type mark_as_sent: bool
    """

    def __init__(self, account: str, file: str, storage: str = None, account_storage_folder: str = None, format: str = None, folder: str = None, mark_as_sent: bool = None):
        """
        Request model for client_message_append_file operation.
        Initializes a new instance.

        :param account: Email account.
        :type account: str
        :param file: Message file to append.
        :type file: str
        :param storage: Storage name where account file located.
        :type storage: str
        :param account_storage_folder: Folder in storage where account file located.
        :type account_storage_folder: str
        :param format: Email file format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft
        :type format: str
        :param folder: Path to folder on email server to append message to.
        :type folder: str
        :param mark_as_sent: Determines that appended message should be market as sent or not.
        :type mark_as_sent: bool
        """

        self.account = account
        self.file = file
        self.storage = storage
        self.account_storage_folder = account_storage_folder
        self.format = format
        self.folder = folder
        self.mark_as_sent = mark_as_sent
