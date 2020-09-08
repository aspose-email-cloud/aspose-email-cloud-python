#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="InstantMessengerAddress.py">
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

from AsposeEmailCloudSdk.models.enum_with_custom_of_instant_messenger_category import EnumWithCustomOfInstantMessengerCategory


class InstantMessengerAddress(object):
    """Instant messenger address.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'EnumWithCustomOfInstantMessengerCategory',
        'address': 'str',
        'preferred': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'address': 'address',
        'preferred': 'preferred'
    }

    def __init__(self, category: EnumWithCustomOfInstantMessengerCategory = None, address: str = None, preferred: bool = None):
        """
        Instant messenger address.             
        :param category: Address category.             
        :type category: EnumWithCustomOfInstantMessengerCategory
        :param address: Address.             
        :type address: str
        :param preferred: Determines whether this address is preferred.             
        :type preferred: bool
        """

        self._category = None
        self._address = None
        self._preferred = None

        if category is not None:
            self.category = category
        if address is not None:
            self.address = address
        if preferred is not None:
            self.preferred = preferred


    @property
    def category(self) -> EnumWithCustomOfInstantMessengerCategory:
        """
        Address category.             

        :return: The category of this InstantMessengerAddress.
        :rtype: EnumWithCustomOfInstantMessengerCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfInstantMessengerCategory):
        """
        Address category.             

        :param category: The category of this InstantMessengerAddress.
        :type: EnumWithCustomOfInstantMessengerCategory
        """
        self._category = category

    @property
    def address(self) -> str:
        """
        Address.             

        :return: The address of this InstantMessengerAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Address.             

        :param address: The address of this InstantMessengerAddress.
        :type: str
        """
        self._address = address

    @property
    def preferred(self) -> bool:
        """
        Determines whether this address is preferred.             

        :return: The preferred of this InstantMessengerAddress.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """
        Determines whether this address is preferred.             

        :param preferred: The preferred of this InstantMessengerAddress.
        :type: bool
        """
        if preferred is None:
            raise ValueError("Invalid value for `preferred`, must not be `None`")
        self._preferred = preferred

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
        if not isinstance(other, InstantMessengerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
