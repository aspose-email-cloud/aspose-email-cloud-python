#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MoveEmailMessageRq.py">
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

from AsposeEmailCloudSdk.models.account_base_request import AccountBaseRequest
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class MoveEmailMessageRq(AccountBaseRequest):
    """Move email message request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_account': 'str',
        'second_account': 'str',
        'storage_folder': 'StorageFolderLocation',
        'message_id': 'str',
        'source_folder': 'str',
        'destination_folder': 'str'
    }

    attribute_map = {
        'first_account': 'firstAccount',
        'second_account': 'secondAccount',
        'storage_folder': 'storageFolder',
        'message_id': 'messageId',
        'source_folder': 'sourceFolder',
        'destination_folder': 'destinationFolder'
    }

    def __init__(self, first_account: str = None, second_account: str = None, storage_folder: StorageFolderLocation = None, message_id: str = None, source_folder: str = None, destination_folder: str = None):
        """
        Move email message request             
        :param first_account (str) First account storage file name             
        :param second_account (str) Additional email account (for example, FirstAccount could be IMAP, and second one could be SMTP)             
        :param storage_folder (StorageFolderLocation) Storage folder location of account files             
        :param message_id (str) Message identifier             
        :param source_folder (str) Message source folder. Account root folder by default             
        :param destination_folder (str) Folder in email account to move message to             
        """
        super(MoveEmailMessageRq, self).__init__()

        self._message_id = None
        self._source_folder = None
        self._destination_folder = None

        if first_account is not None:
            self.first_account = first_account
        if second_account is not None:
            self.second_account = second_account
        if storage_folder is not None:
            self.storage_folder = storage_folder
        if message_id is not None:
            self.message_id = message_id
        if source_folder is not None:
            self.source_folder = source_folder
        if destination_folder is not None:
            self.destination_folder = destination_folder

    @property
    def message_id(self) -> str:
        """Gets the message_id of this MoveEmailMessageRq.

        Message identifier             

        :return: The message_id of this MoveEmailMessageRq.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: str):
        """Sets the message_id of this MoveEmailMessageRq.

        Message identifier             

        :param message_id: The message_id of this MoveEmailMessageRq.
        :type: str
        """
        self._message_id = message_id

    @property
    def source_folder(self) -> str:
        """Gets the source_folder of this MoveEmailMessageRq.

        Message source folder. Account root folder by default             

        :return: The source_folder of this MoveEmailMessageRq.
        :rtype: str
        """
        return self._source_folder

    @source_folder.setter
    def source_folder(self, source_folder: str):
        """Sets the source_folder of this MoveEmailMessageRq.

        Message source folder. Account root folder by default             

        :param source_folder: The source_folder of this MoveEmailMessageRq.
        :type: str
        """
        self._source_folder = source_folder

    @property
    def destination_folder(self) -> str:
        """Gets the destination_folder of this MoveEmailMessageRq.

        Folder in email account to move message to             

        :return: The destination_folder of this MoveEmailMessageRq.
        :rtype: str
        """
        return self._destination_folder

    @destination_folder.setter
    def destination_folder(self, destination_folder: str):
        """Sets the destination_folder of this MoveEmailMessageRq.

        Folder in email account to move message to             

        :param destination_folder: The destination_folder of this MoveEmailMessageRq.
        :type: str
        """
        self._destination_folder = destination_folder

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
        if not isinstance(other, MoveEmailMessageRq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
