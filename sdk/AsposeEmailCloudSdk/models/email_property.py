#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailProperty.py">
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

from AsposeEmailCloudSdk.models.link import Link


class EmailProperty(object):
    """Email property.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'Link',
        'name': 'str',
        'value': 'object'
    }

    attribute_map = {
        'link': 'link',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, link: Link = None, name: str = None, value: object = None):
        """EmailProperty - a model defined in Swagger"""

        self._link = None
        self._name = None
        self._value = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def link(self) -> Link:
        """Gets the link of this EmailProperty.

        Link to property             

        :return: The link of this EmailProperty.
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link: Link):
        """Sets the link of this EmailProperty.

        Link to property             

        :param link: The link of this EmailProperty.
        :type: Link
        """
        self._link = link

    @property
    def name(self) -> str:
        """Gets the name of this EmailProperty.

        Property name             

        :return: The name of this EmailProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this EmailProperty.

        Property name             

        :param name: The name of this EmailProperty.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")
        self._name = name

    @property
    def value(self) -> object:
        """Gets the value of this EmailProperty.

        Property value             

        :return: The value of this EmailProperty.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value: object):
        """Sets the value of this EmailProperty.

        Property value             

        :param value: The value of this EmailProperty.
        :type: object
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
        if not isinstance(other, EmailProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
