#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="DiscUsage.py">
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


class DiscUsage(object):
    """Class for disc space information.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'used_size': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'used_size': 'usedSize',
        'total_size': 'totalSize'
    }

    def __init__(self, used_size: int = None, total_size: int = None):
        """
        Class for disc space information.
        :param used_size: Application used disc space.
        :type used_size: int
        :param total_size: Total disc space.
        :type total_size: int
        """

        self._used_size = None
        self._total_size = None

        if used_size is not None:
            self.used_size = used_size
        if total_size is not None:
            self.total_size = total_size

    @property
    def used_size(self) -> int:
        """Gets the used_size of this DiscUsage.

        Application used disc space.

        :return: The used_size of this DiscUsage.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size: int):
        """Sets the used_size of this DiscUsage.

        Application used disc space.

        :param used_size: The used_size of this DiscUsage.
        :type: int
        """
        if used_size is None:
            raise ValueError("Invalid value for `used_size`, must not be `None`")
        self._used_size = used_size

    @property
    def total_size(self) -> int:
        """Gets the total_size of this DiscUsage.

        Total disc space.

        :return: The total_size of this DiscUsage.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size: int):
        """Sets the total_size of this DiscUsage.

        Total disc space.

        :param total_size: The total_size of this DiscUsage.
        :type: int
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")
        self._total_size = total_size

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
        if not isinstance(other, DiscUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
