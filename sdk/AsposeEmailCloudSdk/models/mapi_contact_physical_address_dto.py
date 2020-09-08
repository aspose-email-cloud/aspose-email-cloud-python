#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactPhysicalAddressDto.py">
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


class MapiContactPhysicalAddressDto(object):
    """Refers to the group of properties that define physical address for a contact.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_mailing_address': 'bool',
        'street': 'str',
        'city': 'str',
        'state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str',
        'country_code': 'str',
        'address': 'str',
        'post_office_box': 'str'
    }

    attribute_map = {
        'is_mailing_address': 'isMailingAddress',
        'street': 'street',
        'city': 'city',
        'state_or_province': 'stateOrProvince',
        'postal_code': 'postalCode',
        'country': 'country',
        'country_code': 'countryCode',
        'address': 'address',
        'post_office_box': 'postOfficeBox'
    }

    def __init__(self, is_mailing_address: bool = None, street: str = None, city: str = None, state_or_province: str = None, postal_code: str = None, country: str = None, country_code: str = None, address: str = None, post_office_box: str = None):
        """
        Refers to the group of properties that define physical address for a contact.             
        :param is_mailing_address: Gets or sets a value indicating whether this address is mailing address             
        :type is_mailing_address: bool
        :param street: Specifies the street portion of the contact's address             
        :type street: str
        :param city: Specifies the city or locality portion of the contact's address             
        :type city: str
        :param state_or_province: Specifies the state or province portion of the contact's address             
        :type state_or_province: str
        :param postal_code: Specifies the postal code (ZIP code) portion of the contact's address             
        :type postal_code: str
        :param country: Specifies the country or region portion of the contact's address             
        :type country: str
        :param country_code: Specifies the country code portion of the contact's address             
        :type country_code: str
        :param address: Specifies the complete address of the contact's address             
        :type address: str
        :param post_office_box: Gets or sets the post office box             
        :type post_office_box: str
        """

        self._is_mailing_address = None
        self._street = None
        self._city = None
        self._state_or_province = None
        self._postal_code = None
        self._country = None
        self._country_code = None
        self._address = None
        self._post_office_box = None

        if is_mailing_address is not None:
            self.is_mailing_address = is_mailing_address
        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if address is not None:
            self.address = address
        if post_office_box is not None:
            self.post_office_box = post_office_box


    @property
    def is_mailing_address(self) -> bool:
        """
        Gets or sets a value indicating whether this address is mailing address             

        :return: The is_mailing_address of this MapiContactPhysicalAddressDto.
        :rtype: bool
        """
        return self._is_mailing_address

    @is_mailing_address.setter
    def is_mailing_address(self, is_mailing_address: bool):
        """
        Gets or sets a value indicating whether this address is mailing address             

        :param is_mailing_address: The is_mailing_address of this MapiContactPhysicalAddressDto.
        :type: bool
        """
        if is_mailing_address is None:
            raise ValueError("Invalid value for `is_mailing_address`, must not be `None`")
        self._is_mailing_address = is_mailing_address

    @property
    def street(self) -> str:
        """
        Specifies the street portion of the contact's address             

        :return: The street of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """
        Specifies the street portion of the contact's address             

        :param street: The street of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._street = street

    @property
    def city(self) -> str:
        """
        Specifies the city or locality portion of the contact's address             

        :return: The city of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """
        Specifies the city or locality portion of the contact's address             

        :param city: The city of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._city = city

    @property
    def state_or_province(self) -> str:
        """
        Specifies the state or province portion of the contact's address             

        :return: The state_or_province of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province: str):
        """
        Specifies the state or province portion of the contact's address             

        :param state_or_province: The state_or_province of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._state_or_province = state_or_province

    @property
    def postal_code(self) -> str:
        """
        Specifies the postal code (ZIP code) portion of the contact's address             

        :return: The postal_code of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """
        Specifies the postal code (ZIP code) portion of the contact's address             

        :param postal_code: The postal_code of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def country(self) -> str:
        """
        Specifies the country or region portion of the contact's address             

        :return: The country of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """
        Specifies the country or region portion of the contact's address             

        :param country: The country of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._country = country

    @property
    def country_code(self) -> str:
        """
        Specifies the country code portion of the contact's address             

        :return: The country_code of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """
        Specifies the country code portion of the contact's address             

        :param country_code: The country_code of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._country_code = country_code

    @property
    def address(self) -> str:
        """
        Specifies the complete address of the contact's address             

        :return: The address of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Specifies the complete address of the contact's address             

        :param address: The address of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._address = address

    @property
    def post_office_box(self) -> str:
        """
        Gets or sets the post office box             

        :return: The post_office_box of this MapiContactPhysicalAddressDto.
        :rtype: str
        """
        return self._post_office_box

    @post_office_box.setter
    def post_office_box(self, post_office_box: str):
        """
        Gets or sets the post office box             

        :param post_office_box: The post_office_box of this MapiContactPhysicalAddressDto.
        :type: str
        """
        self._post_office_box = post_office_box

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
        if not isinstance(other, MapiContactPhysicalAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
