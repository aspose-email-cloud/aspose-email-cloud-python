#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ObjectExist.py">
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


class ObjectExist(object):
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
        'exists': 'bool',
        'is_folder': 'bool'
    }

    attribute_map = {
        'exists': 'exists',
        'is_folder': 'isFolder'
    }

    def __init__(self, exists: bool = None, is_folder: bool = None):
        """
        
        :param exists (bool) 
        :param is_folder (bool) 
        """

        self._exists = None
        self._is_folder = None

        if exists is not None:
            self.exists = exists
        if is_folder is not None:
            self.is_folder = is_folder

    @property
    def exists(self) -> bool:
        """Gets the exists of this ObjectExist.


        :return: The exists of this ObjectExist.
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists: bool):
        """Sets the exists of this ObjectExist.


        :param exists: The exists of this ObjectExist.
        :type: bool
        """
        if exists is None:
            raise ValueError("Invalid value for `exists`, must not be `None`")
        self._exists = exists

    @property
    def is_folder(self) -> bool:
        """Gets the is_folder of this ObjectExist.


        :return: The is_folder of this ObjectExist.
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder: bool):
        """Sets the is_folder of this ObjectExist.


        :param is_folder: The is_folder of this ObjectExist.
        :type: bool
        """
        if is_folder is None:
            raise ValueError("Invalid value for `is_folder`, must not be `None`")
        self._is_folder = is_folder

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
        if not isinstance(other, ObjectExist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
