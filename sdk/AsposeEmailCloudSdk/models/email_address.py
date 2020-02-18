#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailAddress.py">
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
        'address': 'str'
    }

    attribute_map = {
        'category': 'category',
        'display_name': 'displayName',
        'preferred': 'preferred',
        'routing_type': 'routingType',
        'address': 'address'
    }

    def __init__(self, category: EnumWithCustomOfEmailAddressCategory = None, display_name: str = None, preferred: bool = None, routing_type: str = None, address: str = None):
        """
        Email address.             
        :param category (EnumWithCustomOfEmailAddressCategory) Address category.             
        :param display_name (str) Display name.             
        :param preferred (bool) Defines whether email address is preferred.             
        :param routing_type (str) A routing type for an email.             
        :param address (str) Email address.             
        """

        self._category = None
        self._display_name = None
        self._preferred = None
        self._routing_type = None
        self._address = None
        self.discriminator = None

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

    @property
    def category(self) -> EnumWithCustomOfEmailAddressCategory:
        """Gets the category of this EmailAddress.

        Address category.             

        :return: The category of this EmailAddress.
        :rtype: EnumWithCustomOfEmailAddressCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfEmailAddressCategory):
        """Sets the category of this EmailAddress.

        Address category.             

        :param category: The category of this EmailAddress.
        :type: EnumWithCustomOfEmailAddressCategory
        """
        self._category = category

    @property
    def display_name(self) -> str:
        """Gets the display_name of this EmailAddress.

        Display name.             

        :return: The display_name of this EmailAddress.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this EmailAddress.

        Display name.             

        :param display_name: The display_name of this EmailAddress.
        :type: str
        """
        self._display_name = display_name

    @property
    def preferred(self) -> bool:
        """Gets the preferred of this EmailAddress.

        Defines whether email address is preferred.             

        :return: The preferred of this EmailAddress.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """Sets the preferred of this EmailAddress.

        Defines whether email address is preferred.             

        :param preferred: The preferred of this EmailAddress.
        :type: bool
        """
        if preferred is None:
            raise ValueError("Invalid value for `preferred`, must not be `None`")
        self._preferred = preferred

    @property
    def routing_type(self) -> str:
        """Gets the routing_type of this EmailAddress.

        A routing type for an email.             

        :return: The routing_type of this EmailAddress.
        :rtype: str
        """
        return self._routing_type

    @routing_type.setter
    def routing_type(self, routing_type: str):
        """Sets the routing_type of this EmailAddress.

        A routing type for an email.             

        :param routing_type: The routing_type of this EmailAddress.
        :type: str
        """
        self._routing_type = routing_type

    @property
    def address(self) -> str:
        """Gets the address of this EmailAddress.

        Email address.             

        :return: The address of this EmailAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this EmailAddress.

        Email address.             

        :param address: The address of this EmailAddress.
        :type: str
        """
        self._address = address

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
