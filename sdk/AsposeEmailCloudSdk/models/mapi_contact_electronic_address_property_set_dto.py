#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactElectronicAddressPropertySetDto.py">
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

from AsposeEmailCloudSdk.models.mapi_contact_electronic_address_dto import MapiContactElectronicAddressDto


class MapiContactElectronicAddressPropertySetDto(object):
    """Specify properties for up to three different e-mail addresses (Email1, Email2, and Email3) and three different fax addresses (Primary Fax, Business Fax, and Home Fax)             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_fax': 'MapiContactElectronicAddressDto',
        'default_email_address': 'MapiContactElectronicAddressDto',
        'email1': 'MapiContactElectronicAddressDto',
        'email2': 'MapiContactElectronicAddressDto',
        'email3': 'MapiContactElectronicAddressDto',
        'home_fax': 'MapiContactElectronicAddressDto',
        'is_empty': 'bool',
        'primary_fax': 'MapiContactElectronicAddressDto',
        'use_autocomplete': 'bool'
    }

    attribute_map = {
        'business_fax': 'businessFax',
        'default_email_address': 'defaultEmailAddress',
        'email1': 'email1',
        'email2': 'email2',
        'email3': 'email3',
        'home_fax': 'homeFax',
        'is_empty': 'isEmpty',
        'primary_fax': 'primaryFax',
        'use_autocomplete': 'useAutocomplete'
    }

    def __init__(self, business_fax: MapiContactElectronicAddressDto = None, default_email_address: MapiContactElectronicAddressDto = None, email1: MapiContactElectronicAddressDto = None, email2: MapiContactElectronicAddressDto = None, email3: MapiContactElectronicAddressDto = None, home_fax: MapiContactElectronicAddressDto = None, is_empty: bool = None, primary_fax: MapiContactElectronicAddressDto = None, use_autocomplete: bool = None):
        """
        Specify properties for up to three different e-mail addresses (Email1, Email2, and Email3) and three different fax addresses (Primary Fax, Business Fax, and Home Fax)             
        :param business_fax: Refers to the group of properties that define the business fax address for a contact.
        :type business_fax: MapiContactElectronicAddressDto
        :param default_email_address: Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             
        :type default_email_address: MapiContactElectronicAddressDto
        :param email1: Refers to the group of properties that define the first e-mail address for a contact.             
        :type email1: MapiContactElectronicAddressDto
        :param email2: Refers to the group of properties that define the second e-mail address for a contact.             
        :type email2: MapiContactElectronicAddressDto
        :param email3: Refers to the group of properties that define the third e-mail address for a contact.             
        :type email3: MapiContactElectronicAddressDto
        :param home_fax: Refers to the group of properties that define the home fax address for a contact.             
        :type home_fax: MapiContactElectronicAddressDto
        :param is_empty: Shows if MapiContactElectronicAddressPropertySetDto is empty
        :type is_empty: bool
        :param primary_fax: Refers to the group of properties that define the primary fax address for a contact.             
        :type primary_fax: MapiContactElectronicAddressDto
        :param use_autocomplete: Indicates that one electronic address is completed automatically in case if user does not set any electronic address             
        :type use_autocomplete: bool
        """

        self._business_fax = None
        self._default_email_address = None
        self._email1 = None
        self._email2 = None
        self._email3 = None
        self._home_fax = None
        self._is_empty = None
        self._primary_fax = None
        self._use_autocomplete = None

        if business_fax is not None:
            self.business_fax = business_fax
        if default_email_address is not None:
            self.default_email_address = default_email_address
        if email1 is not None:
            self.email1 = email1
        if email2 is not None:
            self.email2 = email2
        if email3 is not None:
            self.email3 = email3
        if home_fax is not None:
            self.home_fax = home_fax
        if is_empty is not None:
            self.is_empty = is_empty
        if primary_fax is not None:
            self.primary_fax = primary_fax
        if use_autocomplete is not None:
            self.use_autocomplete = use_autocomplete


    @property
    def business_fax(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the business fax address for a contact.

        :return: The business_fax of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._business_fax

    @business_fax.setter
    def business_fax(self, business_fax: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the business fax address for a contact.

        :param business_fax: The business_fax of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._business_fax = business_fax

    @property
    def default_email_address(self) -> MapiContactElectronicAddressDto:
        """
        Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             

        :return: The default_email_address of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._default_email_address

    @default_email_address.setter
    def default_email_address(self, default_email_address: MapiContactElectronicAddressDto):
        """
        Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             

        :param default_email_address: The default_email_address of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._default_email_address = default_email_address

    @property
    def email1(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the first e-mail address for a contact.             

        :return: The email1 of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._email1

    @email1.setter
    def email1(self, email1: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the first e-mail address for a contact.             

        :param email1: The email1 of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._email1 = email1

    @property
    def email2(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the second e-mail address for a contact.             

        :return: The email2 of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._email2

    @email2.setter
    def email2(self, email2: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the second e-mail address for a contact.             

        :param email2: The email2 of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._email2 = email2

    @property
    def email3(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the third e-mail address for a contact.             

        :return: The email3 of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._email3

    @email3.setter
    def email3(self, email3: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the third e-mail address for a contact.             

        :param email3: The email3 of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._email3 = email3

    @property
    def home_fax(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the home fax address for a contact.             

        :return: The home_fax of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._home_fax

    @home_fax.setter
    def home_fax(self, home_fax: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the home fax address for a contact.             

        :param home_fax: The home_fax of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._home_fax = home_fax

    @property
    def is_empty(self) -> bool:
        """
        Shows if MapiContactElectronicAddressPropertySetDto is empty

        :return: The is_empty of this MapiContactElectronicAddressPropertySetDto.
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty: bool):
        """
        Shows if MapiContactElectronicAddressPropertySetDto is empty

        :param is_empty: The is_empty of this MapiContactElectronicAddressPropertySetDto.
        :type: bool
        """
        if is_empty is None:
            raise ValueError("Invalid value for `is_empty`, must not be `None`")
        self._is_empty = is_empty

    @property
    def primary_fax(self) -> MapiContactElectronicAddressDto:
        """
        Refers to the group of properties that define the primary fax address for a contact.             

        :return: The primary_fax of this MapiContactElectronicAddressPropertySetDto.
        :rtype: MapiContactElectronicAddressDto
        """
        return self._primary_fax

    @primary_fax.setter
    def primary_fax(self, primary_fax: MapiContactElectronicAddressDto):
        """
        Refers to the group of properties that define the primary fax address for a contact.             

        :param primary_fax: The primary_fax of this MapiContactElectronicAddressPropertySetDto.
        :type: MapiContactElectronicAddressDto
        """
        self._primary_fax = primary_fax

    @property
    def use_autocomplete(self) -> bool:
        """
        Indicates that one electronic address is completed automatically in case if user does not set any electronic address             

        :return: The use_autocomplete of this MapiContactElectronicAddressPropertySetDto.
        :rtype: bool
        """
        return self._use_autocomplete

    @use_autocomplete.setter
    def use_autocomplete(self, use_autocomplete: bool):
        """
        Indicates that one electronic address is completed automatically in case if user does not set any electronic address             

        :param use_autocomplete: The use_autocomplete of this MapiContactElectronicAddressPropertySetDto.
        :type: bool
        """
        if use_autocomplete is None:
            raise ValueError("Invalid value for `use_autocomplete`, must not be `None`")
        self._use_autocomplete = use_autocomplete

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
        if not isinstance(other, MapiContactElectronicAddressPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
