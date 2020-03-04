#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="StorageModelRqOfCalendarDto.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

from AsposeEmailCloudSdk.models.calendar_dto import CalendarDto
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class StorageModelRqOfCalendarDto(object):
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
        'value': 'CalendarDto',
        'storage_folder': 'StorageFolderLocation'
    }

    attribute_map = {
        'value': 'value',
        'storage_folder': 'storageFolder'
    }

    def __init__(self, value: CalendarDto = None, storage_folder: StorageFolderLocation = None):
        """
        
        :param value (CalendarDto) 
        :param storage_folder (StorageFolderLocation) 
        """

        self._value = None
        self._storage_folder = None

        if value is not None:
            self.value = value
        if storage_folder is not None:
            self.storage_folder = storage_folder

    @property
    def value(self) -> CalendarDto:
        """Gets the value of this StorageModelRqOfCalendarDto.


        :return: The value of this StorageModelRqOfCalendarDto.
        :rtype: CalendarDto
        """
        return self._value

    @value.setter
    def value(self, value: CalendarDto):
        """Sets the value of this StorageModelRqOfCalendarDto.


        :param value: The value of this StorageModelRqOfCalendarDto.
        :type: CalendarDto
        """
        self._value = value

    @property
    def storage_folder(self) -> StorageFolderLocation:
        """Gets the storage_folder of this StorageModelRqOfCalendarDto.


        :return: The storage_folder of this StorageModelRqOfCalendarDto.
        :rtype: StorageFolderLocation
        """
        return self._storage_folder

    @storage_folder.setter
    def storage_folder(self, storage_folder: StorageFolderLocation):
        """Sets the storage_folder of this StorageModelRqOfCalendarDto.


        :param storage_folder: The storage_folder of this StorageModelRqOfCalendarDto.
        :type: StorageFolderLocation
        """
        self._storage_folder = storage_folder

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
        if not isinstance(other, StorageModelRqOfCalendarDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
