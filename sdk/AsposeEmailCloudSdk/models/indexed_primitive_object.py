#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="IndexedPrimitiveObject.py">
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

from AsposeEmailCloudSdk.models.base_object import BaseObject


class IndexedPrimitiveObject(BaseObject):
    """Simple indexed property             
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
        'type': 'str',
        'index': 'int',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'index': 'index',
        'value': 'value'
    }

    def __init__(self, name: str = None, type: str = None, index: int = None, value: str = None):
        """
        Simple indexed property             
        :param name (str) Gets or sets the name of an object.             
        :param type (str) Property type. Used for deserialization purposes             
        :param index (int) Index of property in list             
        :param value (str) Gets or sets the name of a property.             
        """
        super(IndexedPrimitiveObject, self).__init__()

        self._index = None
        self._value = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if index is not None:
            self.index = index
        if value is not None:
            self.value = value

    @property
    def index(self) -> int:
        """Gets the index of this IndexedPrimitiveObject.

        Index of property in list             

        :return: The index of this IndexedPrimitiveObject.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this IndexedPrimitiveObject.

        Index of property in list             

        :param index: The index of this IndexedPrimitiveObject.
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")
        self._index = index

    @property
    def value(self) -> str:
        """Gets the value of this IndexedPrimitiveObject.

        Gets or sets the name of a property.             

        :return: The value of this IndexedPrimitiveObject.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this IndexedPrimitiveObject.

        Gets or sets the name of a property.             

        :param value: The value of this IndexedPrimitiveObject.
        :type: str
        """
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
        if not isinstance(other, IndexedPrimitiveObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
