
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_message_fetch_request.py">
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


class ClientMessageFetchRequest(object):
    """
    Request model for client_message_fetch operation.
    Initializes a new instance.

    :param message_id (str) Message identifier
    :param account (str) Email account
    :param folder (str) Account folder to fetch from (should be specified for some protocols such as IMAP)             
    :param storage (str) Storage name where account file located.
    :param account_storage_folder (str) Folder in storage where account file located.
    :param type (str) MailMessageBase type. Using this property you can fetch message in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64
    :param format (str) Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
    """

    def __init__(self, message_id: str, account: str, folder: str = None, storage: str = None, account_storage_folder: str = None, type: str = None, format: str = None):
        """
        Request model for client_message_fetch operation.
        Initializes a new instance.

        :param message_id (str) Message identifier
        :param account (str) Email account
        :param folder (str) Account folder to fetch from (should be specified for some protocols such as IMAP)             
        :param storage (str) Storage name where account file located.
        :param account_storage_folder (str) Folder in storage where account file located.
        :param type (str) MailMessageBase type. Using this property you can fetch message in different formats (as EmailDto, MapiMessageDto or a file represented as Base64 string).              Enum, available values: Dto, Mapi, Base64
        :param format (str) Base64 data format. Used only if type is set to Base64. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef
        """

        self.message_id = message_id
        self.account = account
        self.folder = folder
        self.storage = storage
        self.account_storage_folder = account_storage_folder
        self.type = type
        self.format = format
