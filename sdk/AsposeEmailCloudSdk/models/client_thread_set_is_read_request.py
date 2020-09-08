#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ClientThreadSetIsReadRequest.py">
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

from AsposeEmailCloudSdk.models.client_thread_base_request import ClientThreadBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class ClientThreadSetIsReadRequest(ClientThreadBaseRequest):
    """Mark thread messages as read or unread request.             
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
        'thread_id': 'str',
        'is_read': 'bool',
        'folder': 'str'
    }

    attribute_map = {
        'account_location': 'accountLocation',
        'thread_id': 'threadId',
        'is_read': 'isRead',
        'folder': 'folder'
    }

    def __init__(self, account_location: StorageFileLocation = None, thread_id: str = None, is_read: bool = None, folder: str = None):
        """
        Mark thread messages as read or unread request.             
        :param account_location: Email client account configuration location on storage.             
        :type account_location: StorageFileLocation
        :param thread_id: Thread identifier.             
        :type thread_id: str
        :param is_read: Message is read flag.             
        :type is_read: bool
        :param folder: Folder on email server, where thread is stored.             
        :type folder: str
        """
        super(ClientThreadSetIsReadRequest, self).__init__()

        self._is_read = None
        self._folder = None

        if account_location is not None:
            self.account_location = account_location
        if thread_id is not None:
            self.thread_id = thread_id
        if is_read is not None:
            self.is_read = is_read
        if folder is not None:
            self.folder = folder


    @property
    def is_read(self) -> bool:
        """
        Message is read flag.             

        :return: The is_read of this ClientThreadSetIsReadRequest.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read: bool):
        """
        Message is read flag.             

        :param is_read: The is_read of this ClientThreadSetIsReadRequest.
        :type: bool
        """
        if is_read is None:
            raise ValueError("Invalid value for `is_read`, must not be `None`")
        self._is_read = is_read

    @property
    def folder(self) -> str:
        """
        Folder on email server, where thread is stored.             

        :return: The folder of this ClientThreadSetIsReadRequest.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder: str):
        """
        Folder on email server, where thread is stored.             

        :param folder: The folder of this ClientThreadSetIsReadRequest.
        :type: str
        """
        self._folder = folder

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
        if not isinstance(other, ClientThreadSetIsReadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
