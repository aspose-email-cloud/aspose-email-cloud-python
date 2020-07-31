#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ClientMessageDeleteRequest.py">
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

from AsposeEmailCloudSdk.models.client_message_base_request import ClientMessageBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class ClientMessageDeleteRequest(ClientMessageBaseRequest):
    """Email client delete message request.             
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
        'message_id': 'str',
        'folder': 'str'
    }

    attribute_map = {
        'account_location': 'accountLocation',
        'message_id': 'messageId',
        'folder': 'folder'
    }

    def __init__(self, account_location: StorageFileLocation = None, message_id: str = None, folder: str = None):
        """
        Email client delete message request.             
        :param account_location (StorageFileLocation) Email client account configuration location on storage.             
        :param message_id (str) Message identifier.             
        :param folder (str) Folder to delete message from.             
        """
        super(ClientMessageDeleteRequest, self).__init__()

        self._folder = None

        if account_location is not None:
            self.account_location = account_location
        if message_id is not None:
            self.message_id = message_id
        if folder is not None:
            self.folder = folder

    @property
    def folder(self) -> str:
        """Gets the folder of this ClientMessageDeleteRequest.

        Folder to delete message from.             

        :return: The folder of this ClientMessageDeleteRequest.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder: str):
        """Sets the folder of this ClientMessageDeleteRequest.

        Folder to delete message from.             

        :param folder: The folder of this ClientMessageDeleteRequest.
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
        if not isinstance(other, ClientMessageDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other