#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PhoneNumber.py">
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

from AsposeEmailCloudSdk.models.enum_with_custom_of_phone_number_category import EnumWithCustomOfPhoneNumberCategory


class PhoneNumber(object):
    """A phone number.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'EnumWithCustomOfPhoneNumberCategory',
        'number': 'str',
        'preferred': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'number': 'number',
        'preferred': 'preferred'
    }

    def __init__(self, category: EnumWithCustomOfPhoneNumberCategory = None, number: str = None, preferred: bool = None):
        """
        A phone number.             
        :param category: Phone number category.             
        :type category: EnumWithCustomOfPhoneNumberCategory
        :param number: Phone number.             
        :type number: str
        :param preferred: Defines whether phone number is preferred.             
        :type preferred: bool
        """

        self._category = None
        self._number = None
        self._preferred = None

        if category is not None:
            self.category = category
        if number is not None:
            self.number = number
        if preferred is not None:
            self.preferred = preferred


    @property
    def category(self) -> EnumWithCustomOfPhoneNumberCategory:
        """
        Phone number category.             

        :return: The category of this PhoneNumber.
        :rtype: EnumWithCustomOfPhoneNumberCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfPhoneNumberCategory):
        """
        Phone number category.             

        :param category: The category of this PhoneNumber.
        :type: EnumWithCustomOfPhoneNumberCategory
        """
        self._category = category

    @property
    def number(self) -> str:
        """
        Phone number.             

        :return: The number of this PhoneNumber.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number: str):
        """
        Phone number.             

        :param number: The number of this PhoneNumber.
        :type: str
        """
        self._number = number

    @property
    def preferred(self) -> bool:
        """
        Defines whether phone number is preferred.             

        :return: The preferred of this PhoneNumber.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """
        Defines whether phone number is preferred.             

        :param preferred: The preferred of this PhoneNumber.
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
        if not isinstance(other, PhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
