#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="StorageModelOfEmailClientAccount.py">
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

from AsposeEmailCloudSdk.models.email_client_account import EmailClientAccount
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class StorageModelOfEmailClientAccount(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_file': 'StorageFileLocation',
        'value': 'EmailClientAccount'
    }

    attribute_map = {
        'storage_file': 'storageFile',
        'value': 'value'
    }

    def __init__(self, storage_file: StorageFileLocation = None, value: EmailClientAccount = None):
        """
        
        :param storage_file: 
        :type storage_file: StorageFileLocation
        :param value: 
        :type value: EmailClientAccount
        """

        self._storage_file = None
        self._value = None

        if storage_file is not None:
            self.storage_file = storage_file
        if value is not None:
            self.value = value


    @property
    def storage_file(self) -> StorageFileLocation:
        """
        Gets the storage_file of this StorageModelOfEmailClientAccount.

        :return: The storage_file of this StorageModelOfEmailClientAccount.
        :rtype: StorageFileLocation
        """
        return self._storage_file

    @storage_file.setter
    def storage_file(self, storage_file: StorageFileLocation):
        """
        Sets the storage_file of this StorageModelOfEmailClientAccount.

        :param storage_file: The storage_file of this StorageModelOfEmailClientAccount.
        :type: StorageFileLocation
        """
        if storage_file is None:
            raise ValueError("Invalid value for `storage_file`, must not be `None`")
        self._storage_file = storage_file

    @property
    def value(self) -> EmailClientAccount:
        """
        Gets the value of this StorageModelOfEmailClientAccount.

        :return: The value of this StorageModelOfEmailClientAccount.
        :rtype: EmailClientAccount
        """
        return self._value

    @value.setter
    def value(self, value: EmailClientAccount):
        """
        Sets the value of this StorageModelOfEmailClientAccount.

        :param value: The value of this StorageModelOfEmailClientAccount.
        :type: EmailClientAccount
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")
        self._value = value

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
        if not isinstance(other, StorageModelOfEmailClientAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
