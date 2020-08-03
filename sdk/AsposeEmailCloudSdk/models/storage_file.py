#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="StorageFile.py">
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


class StorageFile(object):
    """File or folder information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'is_folder': 'bool',
        'modified_date': 'datetime',
        'size': 'int',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_folder': 'isFolder',
        'modified_date': 'modifiedDate',
        'size': 'size',
        'path': 'path'
    }

    def __init__(self, name: str = None, is_folder: bool = None, modified_date: datetime = None, size: int = None, path: str = None):
        """
        File or folder information
        :param name: File or folder name.
        :type name: str
        :param is_folder: True if it is a folder.
        :type is_folder: bool
        :param modified_date: File or folder last modified DateTime.
        :type modified_date: datetime
        :param size: File or folder size.
        :type size: int
        :param path: File or folder path.
        :type path: str
        """

        self._name = None
        self._is_folder = None
        self._modified_date = None
        self._size = None
        self._path = None

        if name is not None:
            self.name = name
        if is_folder is not None:
            self.is_folder = is_folder
        if modified_date is not None:
            self.modified_date = modified_date
        if size is not None:
            self.size = size
        if path is not None:
            self.path = path


    @property
    def name(self) -> str:
        """
        File or folder name.

        :return: The name of this StorageFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        File or folder name.

        :param name: The name of this StorageFile.
        :type: str
        """
        self._name = name

    @property
    def is_folder(self) -> bool:
        """
        True if it is a folder.

        :return: The is_folder of this StorageFile.
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder: bool):
        """
        True if it is a folder.

        :param is_folder: The is_folder of this StorageFile.
        :type: bool
        """
        if is_folder is None:
            raise ValueError("Invalid value for `is_folder`, must not be `None`")
        self._is_folder = is_folder

    @property
    def modified_date(self) -> datetime:
        """
        File or folder last modified DateTime.

        :return: The modified_date of this StorageFile.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date: datetime):
        """
        File or folder last modified DateTime.

        :param modified_date: The modified_date of this StorageFile.
        :type: datetime
        """
        self._modified_date = modified_date

    @property
    def size(self) -> int:
        """
        File or folder size.

        :return: The size of this StorageFile.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """
        File or folder size.

        :param size: The size of this StorageFile.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")
        self._size = size

    @property
    def path(self) -> str:
        """
        File or folder path.

        :return: The path of this StorageFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """
        File or folder path.

        :param path: The path of this StorageFile.
        :type: str
        """
        self._path = path

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
        if not isinstance(other, StorageFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
