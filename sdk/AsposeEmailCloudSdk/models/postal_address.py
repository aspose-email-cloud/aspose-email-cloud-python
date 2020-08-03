#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PostalAddress.py">
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

from AsposeEmailCloudSdk.models.enum_with_custom_of_postal_address_category import EnumWithCustomOfPostalAddressCategory


class PostalAddress(object):
    """A postal address             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'category': 'EnumWithCustomOfPostalAddressCategory',
        'city': 'str',
        'country': 'str',
        'country_code': 'str',
        'is_mailing_address': 'bool',
        'postal_code': 'str',
        'post_office_box': 'str',
        'preferred': 'bool',
        'state_or_province': 'str',
        'street': 'str'
    }

    attribute_map = {
        'address': 'address',
        'category': 'category',
        'city': 'city',
        'country': 'country',
        'country_code': 'countryCode',
        'is_mailing_address': 'isMailingAddress',
        'postal_code': 'postalCode',
        'post_office_box': 'postOfficeBox',
        'preferred': 'preferred',
        'state_or_province': 'stateOrProvince',
        'street': 'street'
    }

    def __init__(self, address: str = None, category: EnumWithCustomOfPostalAddressCategory = None, city: str = None, country: str = None, country_code: str = None, is_mailing_address: bool = None, postal_code: str = None, post_office_box: str = None, preferred: bool = None, state_or_province: str = None, street: str = None):
        """
        A postal address             
        :param address: Address.             
        :type address: str
        :param category: Address category.             
        :type category: EnumWithCustomOfPostalAddressCategory
        :param city: Address's city.             
        :type city: str
        :param country: Address's country.             
        :type country: str
        :param country_code: Country code.             
        :type country_code: str
        :param is_mailing_address: Defines whether address may be used for mailing.             
        :type is_mailing_address: bool
        :param postal_code: Postal code.             
        :type postal_code: str
        :param post_office_box: Post Office box.             
        :type post_office_box: str
        :param preferred: Defines whether postal address is preferred.             
        :type preferred: bool
        :param state_or_province: Address's region.             
        :type state_or_province: str
        :param street: Address's street.             
        :type street: str
        """

        self._address = None
        self._category = None
        self._city = None
        self._country = None
        self._country_code = None
        self._is_mailing_address = None
        self._postal_code = None
        self._post_office_box = None
        self._preferred = None
        self._state_or_province = None
        self._street = None

        if address is not None:
            self.address = address
        if category is not None:
            self.category = category
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if is_mailing_address is not None:
            self.is_mailing_address = is_mailing_address
        if postal_code is not None:
            self.postal_code = postal_code
        if post_office_box is not None:
            self.post_office_box = post_office_box
        if preferred is not None:
            self.preferred = preferred
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if street is not None:
            self.street = street


    @property
    def address(self) -> str:
        """
        Address.             

        :return: The address of this PostalAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Address.             

        :param address: The address of this PostalAddress.
        :type: str
        """
        self._address = address

    @property
    def category(self) -> EnumWithCustomOfPostalAddressCategory:
        """
        Address category.             

        :return: The category of this PostalAddress.
        :rtype: EnumWithCustomOfPostalAddressCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfPostalAddressCategory):
        """
        Address category.             

        :param category: The category of this PostalAddress.
        :type: EnumWithCustomOfPostalAddressCategory
        """
        self._category = category

    @property
    def city(self) -> str:
        """
        Address's city.             

        :return: The city of this PostalAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """
        Address's city.             

        :param city: The city of this PostalAddress.
        :type: str
        """
        self._city = city

    @property
    def country(self) -> str:
        """
        Address's country.             

        :return: The country of this PostalAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """
        Address's country.             

        :param country: The country of this PostalAddress.
        :type: str
        """
        self._country = country

    @property
    def country_code(self) -> str:
        """
        Country code.             

        :return: The country_code of this PostalAddress.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """
        Country code.             

        :param country_code: The country_code of this PostalAddress.
        :type: str
        """
        self._country_code = country_code

    @property
    def is_mailing_address(self) -> bool:
        """
        Defines whether address may be used for mailing.             

        :return: The is_mailing_address of this PostalAddress.
        :rtype: bool
        """
        return self._is_mailing_address

    @is_mailing_address.setter
    def is_mailing_address(self, is_mailing_address: bool):
        """
        Defines whether address may be used for mailing.             

        :param is_mailing_address: The is_mailing_address of this PostalAddress.
        :type: bool
        """
        if is_mailing_address is None:
            raise ValueError("Invalid value for `is_mailing_address`, must not be `None`")
        self._is_mailing_address = is_mailing_address

    @property
    def postal_code(self) -> str:
        """
        Postal code.             

        :return: The postal_code of this PostalAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """
        Postal code.             

        :param postal_code: The postal_code of this PostalAddress.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def post_office_box(self) -> str:
        """
        Post Office box.             

        :return: The post_office_box of this PostalAddress.
        :rtype: str
        """
        return self._post_office_box

    @post_office_box.setter
    def post_office_box(self, post_office_box: str):
        """
        Post Office box.             

        :param post_office_box: The post_office_box of this PostalAddress.
        :type: str
        """
        self._post_office_box = post_office_box

    @property
    def preferred(self) -> bool:
        """
        Defines whether postal address is preferred.             

        :return: The preferred of this PostalAddress.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """
        Defines whether postal address is preferred.             

        :param preferred: The preferred of this PostalAddress.
        :type: bool
        """
        if preferred is None:
            raise ValueError("Invalid value for `preferred`, must not be `None`")
        self._preferred = preferred

    @property
    def state_or_province(self) -> str:
        """
        Address's region.             

        :return: The state_or_province of this PostalAddress.
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province: str):
        """
        Address's region.             

        :param state_or_province: The state_or_province of this PostalAddress.
        :type: str
        """
        self._state_or_province = state_or_province

    @property
    def street(self) -> str:
        """
        Address's street.             

        :return: The street of this PostalAddress.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """
        Address's street.             

        :param street: The street of this PostalAddress.
        :type: str
        """
        self._street = street

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
        if not isinstance(other, PostalAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
