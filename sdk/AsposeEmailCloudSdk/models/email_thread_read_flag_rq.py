#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailThreadReadFlagRq.py">
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


class EmailThreadReadFlagRq(AccountBaseRequest):
    """Request to mark all messages in thread as read or unread             
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
        'is_read': 'bool',
        'folder_id': 'str'
    }

    attribute_map = {
        'first_account': 'firstAccount',
        'second_account': 'secondAccount',
        'storage_folder': 'storageFolder',
        'is_read': 'isRead',
        'folder_id': 'folderId'
    }

    def __init__(self, first_account: str = None, second_account: str = None, storage_folder: StorageFolderLocation = None, is_read: bool = None, folder_id: str = None):
        """
        Request to mark all messages in thread as read or unread             
        :param first_account (str) First account storage file name             
        :param second_account (str) Additional email account (for example, FirstAccount could be IMAP, and second one could be SMTP)             
        :param storage_folder (StorageFolderLocation) Storage folder location of account files             
        :param is_read (bool) Read flag to set. \"true\" by default             
        :param folder_id (str) Specifies account folder to get thread from (required for some account types, such as EWS). Use folder Id from ListEmailFolders (MailServerFolder.Id). For IMAP folder Id is always same as folder name.             
        """
        super(EmailThreadReadFlagRq, self).__init__()

        self._is_read = None
        self._folder_id = None

        if first_account is not None:
            self.first_account = first_account
        if second_account is not None:
            self.second_account = second_account
        if storage_folder is not None:
            self.storage_folder = storage_folder
        if is_read is not None:
            self.is_read = is_read
        if folder_id is not None:
            self.folder_id = folder_id

    @property
    def is_read(self) -> bool:
        """Gets the is_read of this EmailThreadReadFlagRq.

        Read flag to set. \"true\" by default             

        :return: The is_read of this EmailThreadReadFlagRq.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read: bool):
        """Sets the is_read of this EmailThreadReadFlagRq.

        Read flag to set. \"true\" by default             

        :param is_read: The is_read of this EmailThreadReadFlagRq.
        :type: bool
        """
        if is_read is None:
            raise ValueError("Invalid value for `is_read`, must not be `None`")
        self._is_read = is_read

    @property
    def folder_id(self) -> str:
        """Gets the folder_id of this EmailThreadReadFlagRq.

        Specifies account folder to get thread from (required for some account types, such as EWS). Use folder Id from ListEmailFolders (MailServerFolder.Id). For IMAP folder Id is always same as folder name.             

        :return: The folder_id of this EmailThreadReadFlagRq.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id: str):
        """Sets the folder_id of this EmailThreadReadFlagRq.

        Specifies account folder to get thread from (required for some account types, such as EWS). Use folder Id from ListEmailFolders (MailServerFolder.Id). For IMAP folder Id is always same as folder name.             

        :param folder_id: The folder_id of this EmailThreadReadFlagRq.
        :type: str
        """
        self._folder_id = folder_id

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
        if not isinstance(other, EmailThreadReadFlagRq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
