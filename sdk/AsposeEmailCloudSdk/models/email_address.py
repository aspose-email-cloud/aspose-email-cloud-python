#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailAddress.py">
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

from AsposeEmailCloudSdk.models.enum_with_custom_of_email_address_category import EnumWithCustomOfEmailAddressCategory


class EmailAddress(object):
    """Email address.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'EnumWithCustomOfEmailAddressCategory',
        'display_name': 'str',
        'preferred': 'bool',
        'routing_type': 'str',
        'address': 'str',
        'original_address_string': 'str'
    }

    attribute_map = {
        'category': 'category',
        'display_name': 'displayName',
        'preferred': 'preferred',
        'routing_type': 'routingType',
        'address': 'address',
        'original_address_string': 'originalAddressString'
    }

    def __init__(self, category: EnumWithCustomOfEmailAddressCategory = None, display_name: str = None, preferred: bool = None, routing_type: str = None, address: str = None, original_address_string: str = None):
        """
        Email address.             
        :param category: Address category.             
        :type category: EnumWithCustomOfEmailAddressCategory
        :param display_name: Display name.             
        :type display_name: str
        :param preferred: Defines whether email address is preferred.             
        :type preferred: bool
        :param routing_type: A routing type for an email.             
        :type routing_type: str
        :param address: Email address.             
        :type address: str
        :param original_address_string: The original e-mail address string             
        :type original_address_string: str
        """

        self._category = None
        self._display_name = None
        self._preferred = None
        self._routing_type = None
        self._address = None
        self._original_address_string = None

        if category is not None:
            self.category = category
        if display_name is not None:
            self.display_name = display_name
        if preferred is not None:
            self.preferred = preferred
        if routing_type is not None:
            self.routing_type = routing_type
        if address is not None:
            self.address = address
        if original_address_string is not None:
            self.original_address_string = original_address_string


    @property
    def category(self) -> EnumWithCustomOfEmailAddressCategory:
        """
        Address category.             

        :return: The category of this EmailAddress.
        :rtype: EnumWithCustomOfEmailAddressCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfEmailAddressCategory):
        """
        Address category.             

        :param category: The category of this EmailAddress.
        :type: EnumWithCustomOfEmailAddressCategory
        """
        self._category = category

    @property
    def display_name(self) -> str:
        """
        Display name.             

        :return: The display_name of this EmailAddress.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        Display name.             

        :param display_name: The display_name of this EmailAddress.
        :type: str
        """
        self._display_name = display_name

    @property
    def preferred(self) -> bool:
        """
        Defines whether email address is preferred.             

        :return: The preferred of this EmailAddress.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """
        Defines whether email address is preferred.             

        :param preferred: The preferred of this EmailAddress.
        :type: bool
        """
        if preferred is None:
            raise ValueError("Invalid value for `preferred`, must not be `None`")
        self._preferred = preferred

    @property
    def routing_type(self) -> str:
        """
        A routing type for an email.             

        :return: The routing_type of this EmailAddress.
        :rtype: str
        """
        return self._routing_type

    @routing_type.setter
    def routing_type(self, routing_type: str):
        """
        A routing type for an email.             

        :param routing_type: The routing_type of this EmailAddress.
        :type: str
        """
        self._routing_type = routing_type

    @property
    def address(self) -> str:
        """
        Email address.             

        :return: The address of this EmailAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Email address.             

        :param address: The address of this EmailAddress.
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")
        if address is not None and len(address) < 1:
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `1`")
        self._address = address

    @property
    def original_address_string(self) -> str:
        """
        The original e-mail address string             

        :return: The original_address_string of this EmailAddress.
        :rtype: str
        """
        return self._original_address_string

    @original_address_string.setter
    def original_address_string(self, original_address_string: str):
        """
        The original e-mail address string             

        :param original_address_string: The original_address_string of this EmailAddress.
        :type: str
        """
        self._original_address_string = original_address_string

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
        if not isinstance(other, EmailAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
