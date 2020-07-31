
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_message_list_request.py">
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


class ClientMessageListRequest(object):
    """
    Request model for client_message_list operation.
    Initializes a new instance.

    :param folder (str) A folder in email account
    :param account (str) Email account
    :param query_string (str) A MailQuery search string
    :param storage (str) Storage name where account file located
    :param account_storage_folder (str) Folder in storage where account file located
    :param recursive (bool) Specifies that should message be searched in subfolders recursively
    :param type (str) MailMessageBase type. Using this property you can get messages in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64
    :param format (str) Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
    """

    def __init__(self, folder: str, account: str, query_string: str = None, storage: str = None, account_storage_folder: str = None, recursive: bool = None, type: str = None, format: str = None):
        """
        Request model for client_message_list operation.
        Initializes a new instance.

        :param folder (str) A folder in email account
        :param account (str) Email account
        :param query_string (str) A MailQuery search string
        :param storage (str) Storage name where account file located
        :param account_storage_folder (str) Folder in storage where account file located
        :param recursive (bool) Specifies that should message be searched in subfolders recursively
        :param type (str) MailMessageBase type. Using this property you can get messages in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64
        :param format (str) Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
        """

        self.folder = folder
        self.account = account
        self.query_string = query_string
        self.storage = storage
        self.account_storage_folder = account_storage_folder
        self.recursive = recursive
        self.type = type
        self.format = format