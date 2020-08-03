#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiElectronicAddressDto.py">
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


class MapiElectronicAddressDto(object):
    """Refers to the group of properties that define the e-mail address or fax address.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address_type': 'str',
        'email_address': 'str',
        'display_name': 'str',
        'fax_number': 'str',
        'original_display_name': 'str'
    }

    attribute_map = {
        'address_type': 'addressType',
        'email_address': 'emailAddress',
        'display_name': 'displayName',
        'fax_number': 'faxNumber',
        'original_display_name': 'originalDisplayName'
    }

    def __init__(self, address_type: str = None, email_address: str = None, display_name: str = None, fax_number: str = None, original_display_name: str = None):
        """
        Refers to the group of properties that define the e-mail address or fax address.             
        :param address_type: Address type.             
        :type address_type: str
        :param email_address: Email address.             
        :type email_address: str
        :param display_name: User-readable display name for the e-mail address.             
        :type display_name: str
        :param fax_number: Telephone number of the mail user's primary fax machine.             
        :type fax_number: str
        :param original_display_name: SMTP e-mail address that  corresponds to the e-mail address.             
        :type original_display_name: str
        """

        self._address_type = None
        self._email_address = None
        self._display_name = None
        self._fax_number = None
        self._original_display_name = None

        if address_type is not None:
            self.address_type = address_type
        if email_address is not None:
            self.email_address = email_address
        if display_name is not None:
            self.display_name = display_name
        if fax_number is not None:
            self.fax_number = fax_number
        if original_display_name is not None:
            self.original_display_name = original_display_name


    @property
    def address_type(self) -> str:
        """
        Address type.             

        :return: The address_type of this MapiElectronicAddressDto.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type: str):
        """
        Address type.             

        :param address_type: The address_type of this MapiElectronicAddressDto.
        :type: str
        """
        self._address_type = address_type

    @property
    def email_address(self) -> str:
        """
        Email address.             

        :return: The email_address of this MapiElectronicAddressDto.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str):
        """
        Email address.             

        :param email_address: The email_address of this MapiElectronicAddressDto.
        :type: str
        """
        self._email_address = email_address

    @property
    def display_name(self) -> str:
        """
        User-readable display name for the e-mail address.             

        :return: The display_name of this MapiElectronicAddressDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        User-readable display name for the e-mail address.             

        :param display_name: The display_name of this MapiElectronicAddressDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def fax_number(self) -> str:
        """
        Telephone number of the mail user's primary fax machine.             

        :return: The fax_number of this MapiElectronicAddressDto.
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number: str):
        """
        Telephone number of the mail user's primary fax machine.             

        :param fax_number: The fax_number of this MapiElectronicAddressDto.
        :type: str
        """
        self._fax_number = fax_number

    @property
    def original_display_name(self) -> str:
        """
        SMTP e-mail address that  corresponds to the e-mail address.             

        :return: The original_display_name of this MapiElectronicAddressDto.
        :rtype: str
        """
        return self._original_display_name

    @original_display_name.setter
    def original_display_name(self, original_display_name: str):
        """
        SMTP e-mail address that  corresponds to the e-mail address.             

        :param original_display_name: The original_display_name of this MapiElectronicAddressDto.
        :type: str
        """
        self._original_display_name = original_display_name

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
        if not isinstance(other, MapiElectronicAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
