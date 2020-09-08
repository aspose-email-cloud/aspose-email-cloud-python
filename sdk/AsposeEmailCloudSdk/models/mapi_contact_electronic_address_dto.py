#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactElectronicAddressDto.py">
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


class MapiContactElectronicAddressDto(object):
    """Refers to the group of properties that define the e-mail address or fax address for a contact.             
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
        'display_name': 'str',
        'email_address': 'str',
        'fax_number': 'str',
        'is_empty': 'bool',
        'original_display_name': 'str'
    }

    attribute_map = {
        'address_type': 'addressType',
        'display_name': 'displayName',
        'email_address': 'emailAddress',
        'fax_number': 'faxNumber',
        'is_empty': 'isEmpty',
        'original_display_name': 'originalDisplayName'
    }

    def __init__(self, address_type: str = None, display_name: str = None, email_address: str = None, fax_number: str = None, is_empty: bool = None, original_display_name: str = None):
        """
        Refers to the group of properties that define the e-mail address or fax address for a contact.             
        :param address_type: Address type of an electronic address
        :type address_type: str
        :param display_name: User-readable display name for the e-mail address
        :type display_name: str
        :param email_address: E-mail address of the contact
        :type email_address: str
        :param fax_number: Telephone number of the mail user's primary fax machine
        :type fax_number: str
        :param is_empty: Shows if MapiContactElectronicAddress is empty
        :type is_empty: bool
        :param original_display_name: SMTP e-mail address that corresponds to the e-mail address for the Contact object.
        :type original_display_name: str
        """

        self._address_type = None
        self._display_name = None
        self._email_address = None
        self._fax_number = None
        self._is_empty = None
        self._original_display_name = None

        if address_type is not None:
            self.address_type = address_type
        if display_name is not None:
            self.display_name = display_name
        if email_address is not None:
            self.email_address = email_address
        if fax_number is not None:
            self.fax_number = fax_number
        if is_empty is not None:
            self.is_empty = is_empty
        if original_display_name is not None:
            self.original_display_name = original_display_name


    @property
    def address_type(self) -> str:
        """
        Address type of an electronic address

        :return: The address_type of this MapiContactElectronicAddressDto.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type: str):
        """
        Address type of an electronic address

        :param address_type: The address_type of this MapiContactElectronicAddressDto.
        :type: str
        """
        self._address_type = address_type

    @property
    def display_name(self) -> str:
        """
        User-readable display name for the e-mail address

        :return: The display_name of this MapiContactElectronicAddressDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        User-readable display name for the e-mail address

        :param display_name: The display_name of this MapiContactElectronicAddressDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def email_address(self) -> str:
        """
        E-mail address of the contact

        :return: The email_address of this MapiContactElectronicAddressDto.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str):
        """
        E-mail address of the contact

        :param email_address: The email_address of this MapiContactElectronicAddressDto.
        :type: str
        """
        self._email_address = email_address

    @property
    def fax_number(self) -> str:
        """
        Telephone number of the mail user's primary fax machine

        :return: The fax_number of this MapiContactElectronicAddressDto.
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number: str):
        """
        Telephone number of the mail user's primary fax machine

        :param fax_number: The fax_number of this MapiContactElectronicAddressDto.
        :type: str
        """
        self._fax_number = fax_number

    @property
    def is_empty(self) -> bool:
        """
        Shows if MapiContactElectronicAddress is empty

        :return: The is_empty of this MapiContactElectronicAddressDto.
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty: bool):
        """
        Shows if MapiContactElectronicAddress is empty

        :param is_empty: The is_empty of this MapiContactElectronicAddressDto.
        :type: bool
        """
        if is_empty is None:
            raise ValueError("Invalid value for `is_empty`, must not be `None`")
        self._is_empty = is_empty

    @property
    def original_display_name(self) -> str:
        """
        SMTP e-mail address that corresponds to the e-mail address for the Contact object.

        :return: The original_display_name of this MapiContactElectronicAddressDto.
        :rtype: str
        """
        return self._original_display_name

    @original_display_name.setter
    def original_display_name(self, original_display_name: str):
        """
        SMTP e-mail address that corresponds to the e-mail address for the Contact object.

        :param original_display_name: The original_display_name of this MapiContactElectronicAddressDto.
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
        if not isinstance(other, MapiContactElectronicAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
