#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ClientMessageAppendRequest.py">
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

import pprint
import re
import six
from typing import List, Set, Dict, Tuple, Optional
from datetime import datetime

from AsposeEmailCloudSdk.models.client_account_base_request import ClientAccountBaseRequest
from AsposeEmailCloudSdk.models.mail_message_base import MailMessageBase
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class ClientMessageAppendRequest(ClientAccountBaseRequest):
    """Email client append message request.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_location': 'StorageFileLocation',
        'folder': 'str',
        'message': 'MailMessageBase',
        'mark_as_sent': 'bool'
    }

    attribute_map = {
        'account_location': 'accountLocation',
        'folder': 'folder',
        'message': 'message',
        'mark_as_sent': 'markAsSent'
    }

    def __init__(self, account_location: StorageFileLocation = None, folder: str = None, message: MailMessageBase = None, mark_as_sent: bool = None):
        """
        Email client append message request.             
        :param account_location: Email client account configuration location on storage.             
        :type account_location: StorageFileLocation
        :param folder: Path to folder on email server to append message to.             
        :type folder: str
        :param message: Message to append.             
        :type message: MailMessageBase
        :param mark_as_sent: Determines that appended message should be market as sent or not.             
        :type mark_as_sent: bool
        """
        super(ClientMessageAppendRequest, self).__init__()

        self._folder = None
        self._message = None
        self._mark_as_sent = None

        if account_location is not None:
            self.account_location = account_location
        if folder is not None:
            self.folder = folder
        if message is not None:
            self.message = message
        if mark_as_sent is not None:
            self.mark_as_sent = mark_as_sent


    @property
    def folder(self) -> str:
        """
        Path to folder on email server to append message to.             

        :return: The folder of this ClientMessageAppendRequest.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder: str):
        """
        Path to folder on email server to append message to.             

        :param folder: The folder of this ClientMessageAppendRequest.
        :type: str
        """
        self._folder = folder

    @property
    def message(self) -> MailMessageBase:
        """
        Message to append.             

        :return: The message of this ClientMessageAppendRequest.
        :rtype: MailMessageBase
        """
        return self._message

    @message.setter
    def message(self, message: MailMessageBase):
        """
        Message to append.             

        :param message: The message of this ClientMessageAppendRequest.
        :type: MailMessageBase
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")
        self._message = message

    @property
    def mark_as_sent(self) -> bool:
        """
        Determines that appended message should be market as sent or not.             

        :return: The mark_as_sent of this ClientMessageAppendRequest.
        :rtype: bool
        """
        return self._mark_as_sent

    @mark_as_sent.setter
    def mark_as_sent(self, mark_as_sent: bool):
        """
        Determines that appended message should be market as sent or not.             

        :param mark_as_sent: The mark_as_sent of this ClientMessageAppendRequest.
        :type: bool
        """
        if mark_as_sent is None:
            raise ValueError("Invalid value for `mark_as_sent`, must not be `None`")
        self._mark_as_sent = mark_as_sent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientMessageAppendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
