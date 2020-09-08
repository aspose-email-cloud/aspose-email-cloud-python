#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactTelephonePropertySetDto.py">
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


class MapiContactTelephonePropertySetDto(object):
    """Specify optional telephone numbers for the contact.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_empty': 'bool',
        'default_telephone_number': 'str',
        'use_autocomplete': 'bool',
        'callback_telephone_number': 'str',
        'business_telephone_number': 'str',
        'home_telephone_number': 'str',
        'primary_telephone_number': 'str',
        'business2_telephone_number': 'str',
        'mobile_telephone_number': 'str',
        'radio_telephone_number': 'str',
        'car_telephone_number': 'str',
        'other_telephone_number': 'str',
        'assistant_telephone_number': 'str',
        'home2_telephone_number': 'str',
        'tty_tdd_phone_number': 'str',
        'company_main_telephone_number': 'str',
        'telex_number': 'str',
        'isdn_number': 'str',
        'pager_telephone_number': 'str'
    }

    attribute_map = {
        'is_empty': 'isEmpty',
        'default_telephone_number': 'defaultTelephoneNumber',
        'use_autocomplete': 'useAutocomplete',
        'callback_telephone_number': 'callbackTelephoneNumber',
        'business_telephone_number': 'businessTelephoneNumber',
        'home_telephone_number': 'homeTelephoneNumber',
        'primary_telephone_number': 'primaryTelephoneNumber',
        'business2_telephone_number': 'business2TelephoneNumber',
        'mobile_telephone_number': 'mobileTelephoneNumber',
        'radio_telephone_number': 'radioTelephoneNumber',
        'car_telephone_number': 'carTelephoneNumber',
        'other_telephone_number': 'otherTelephoneNumber',
        'assistant_telephone_number': 'assistantTelephoneNumber',
        'home2_telephone_number': 'home2TelephoneNumber',
        'tty_tdd_phone_number': 'ttyTddPhoneNumber',
        'company_main_telephone_number': 'companyMainTelephoneNumber',
        'telex_number': 'telexNumber',
        'isdn_number': 'isdnNumber',
        'pager_telephone_number': 'pagerTelephoneNumber'
    }

    def __init__(self, is_empty: bool = None, default_telephone_number: str = None, use_autocomplete: bool = None, callback_telephone_number: str = None, business_telephone_number: str = None, home_telephone_number: str = None, primary_telephone_number: str = None, business2_telephone_number: str = None, mobile_telephone_number: str = None, radio_telephone_number: str = None, car_telephone_number: str = None, other_telephone_number: str = None, assistant_telephone_number: str = None, home2_telephone_number: str = None, tty_tdd_phone_number: str = None, company_main_telephone_number: str = None, telex_number: str = None, isdn_number: str = None, pager_telephone_number: str = None):
        """
        Specify optional telephone numbers for the contact.             
        :param is_empty: Shows if MapiContactTelephonePropertySet is empty             
        :type is_empty: bool
        :param default_telephone_number: Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             
        :type default_telephone_number: str
        :param use_autocomplete: Indicates that one electronic address is completed automatically in case if user does not set any electronic address             
        :type use_autocomplete: bool
        :param callback_telephone_number: Gets or sets the callback telephone number             
        :type callback_telephone_number: str
        :param business_telephone_number: Gets or sets the business telephone number             
        :type business_telephone_number: str
        :param home_telephone_number: Gets or sets the home telephone number             
        :type home_telephone_number: str
        :param primary_telephone_number: Gets or sets the primary telephone number             
        :type primary_telephone_number: str
        :param business2_telephone_number: Gets or sets the second business telephone number             
        :type business2_telephone_number: str
        :param mobile_telephone_number: Gets or sets the mobile telephone number             
        :type mobile_telephone_number: str
        :param radio_telephone_number: Gets or sets the radio telephone number             
        :type radio_telephone_number: str
        :param car_telephone_number: Gets or sets the car telephone number             
        :type car_telephone_number: str
        :param other_telephone_number: Gets or sets an alternate telephone number             
        :type other_telephone_number: str
        :param assistant_telephone_number: Gets or sets the telephone number of the contact's assistant             
        :type assistant_telephone_number: str
        :param home2_telephone_number: Gets or sets a second home telephone number             
        :type home2_telephone_number: str
        :param tty_tdd_phone_number: Gets or sets the telephone number for the contact's text telephone (TTY) or telecommunication device for the deaf (TDD)             
        :type tty_tdd_phone_number: str
        :param company_main_telephone_number: Gets or sets the company phone number             
        :type company_main_telephone_number: str
        :param telex_number: Gets or sets the telex number             
        :type telex_number: str
        :param isdn_number: Gets or sets the integrated services digital network (ISDN) number             
        :type isdn_number: str
        :param pager_telephone_number: Gets or sets a pager telephone number             
        :type pager_telephone_number: str
        """

        self._is_empty = None
        self._default_telephone_number = None
        self._use_autocomplete = None
        self._callback_telephone_number = None
        self._business_telephone_number = None
        self._home_telephone_number = None
        self._primary_telephone_number = None
        self._business2_telephone_number = None
        self._mobile_telephone_number = None
        self._radio_telephone_number = None
        self._car_telephone_number = None
        self._other_telephone_number = None
        self._assistant_telephone_number = None
        self._home2_telephone_number = None
        self._tty_tdd_phone_number = None
        self._company_main_telephone_number = None
        self._telex_number = None
        self._isdn_number = None
        self._pager_telephone_number = None

        if is_empty is not None:
            self.is_empty = is_empty
        if default_telephone_number is not None:
            self.default_telephone_number = default_telephone_number
        if use_autocomplete is not None:
            self.use_autocomplete = use_autocomplete
        if callback_telephone_number is not None:
            self.callback_telephone_number = callback_telephone_number
        if business_telephone_number is not None:
            self.business_telephone_number = business_telephone_number
        if home_telephone_number is not None:
            self.home_telephone_number = home_telephone_number
        if primary_telephone_number is not None:
            self.primary_telephone_number = primary_telephone_number
        if business2_telephone_number is not None:
            self.business2_telephone_number = business2_telephone_number
        if mobile_telephone_number is not None:
            self.mobile_telephone_number = mobile_telephone_number
        if radio_telephone_number is not None:
            self.radio_telephone_number = radio_telephone_number
        if car_telephone_number is not None:
            self.car_telephone_number = car_telephone_number
        if other_telephone_number is not None:
            self.other_telephone_number = other_telephone_number
        if assistant_telephone_number is not None:
            self.assistant_telephone_number = assistant_telephone_number
        if home2_telephone_number is not None:
            self.home2_telephone_number = home2_telephone_number
        if tty_tdd_phone_number is not None:
            self.tty_tdd_phone_number = tty_tdd_phone_number
        if company_main_telephone_number is not None:
            self.company_main_telephone_number = company_main_telephone_number
        if telex_number is not None:
            self.telex_number = telex_number
        if isdn_number is not None:
            self.isdn_number = isdn_number
        if pager_telephone_number is not None:
            self.pager_telephone_number = pager_telephone_number


    @property
    def is_empty(self) -> bool:
        """
        Shows if MapiContactTelephonePropertySet is empty             

        :return: The is_empty of this MapiContactTelephonePropertySetDto.
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty: bool):
        """
        Shows if MapiContactTelephonePropertySet is empty             

        :param is_empty: The is_empty of this MapiContactTelephonePropertySetDto.
        :type: bool
        """
        if is_empty is None:
            raise ValueError("Invalid value for `is_empty`, must not be `None`")
        self._is_empty = is_empty

    @property
    def default_telephone_number(self) -> str:
        """
        Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             

        :return: The default_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._default_telephone_number

    @default_telephone_number.setter
    def default_telephone_number(self, default_telephone_number: str):
        """
        Default value of electronic address Uses when user does not set any electronic address if UseAutocomplete property is set 'true'             

        :param default_telephone_number: The default_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._default_telephone_number = default_telephone_number

    @property
    def use_autocomplete(self) -> bool:
        """
        Indicates that one electronic address is completed automatically in case if user does not set any electronic address             

        :return: The use_autocomplete of this MapiContactTelephonePropertySetDto.
        :rtype: bool
        """
        return self._use_autocomplete

    @use_autocomplete.setter
    def use_autocomplete(self, use_autocomplete: bool):
        """
        Indicates that one electronic address is completed automatically in case if user does not set any electronic address             

        :param use_autocomplete: The use_autocomplete of this MapiContactTelephonePropertySetDto.
        :type: bool
        """
        if use_autocomplete is None:
            raise ValueError("Invalid value for `use_autocomplete`, must not be `None`")
        self._use_autocomplete = use_autocomplete

    @property
    def callback_telephone_number(self) -> str:
        """
        Gets or sets the callback telephone number             

        :return: The callback_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._callback_telephone_number

    @callback_telephone_number.setter
    def callback_telephone_number(self, callback_telephone_number: str):
        """
        Gets or sets the callback telephone number             

        :param callback_telephone_number: The callback_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._callback_telephone_number = callback_telephone_number

    @property
    def business_telephone_number(self) -> str:
        """
        Gets or sets the business telephone number             

        :return: The business_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._business_telephone_number

    @business_telephone_number.setter
    def business_telephone_number(self, business_telephone_number: str):
        """
        Gets or sets the business telephone number             

        :param business_telephone_number: The business_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._business_telephone_number = business_telephone_number

    @property
    def home_telephone_number(self) -> str:
        """
        Gets or sets the home telephone number             

        :return: The home_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._home_telephone_number

    @home_telephone_number.setter
    def home_telephone_number(self, home_telephone_number: str):
        """
        Gets or sets the home telephone number             

        :param home_telephone_number: The home_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._home_telephone_number = home_telephone_number

    @property
    def primary_telephone_number(self) -> str:
        """
        Gets or sets the primary telephone number             

        :return: The primary_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._primary_telephone_number

    @primary_telephone_number.setter
    def primary_telephone_number(self, primary_telephone_number: str):
        """
        Gets or sets the primary telephone number             

        :param primary_telephone_number: The primary_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._primary_telephone_number = primary_telephone_number

    @property
    def business2_telephone_number(self) -> str:
        """
        Gets or sets the second business telephone number             

        :return: The business2_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._business2_telephone_number

    @business2_telephone_number.setter
    def business2_telephone_number(self, business2_telephone_number: str):
        """
        Gets or sets the second business telephone number             

        :param business2_telephone_number: The business2_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._business2_telephone_number = business2_telephone_number

    @property
    def mobile_telephone_number(self) -> str:
        """
        Gets or sets the mobile telephone number             

        :return: The mobile_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._mobile_telephone_number

    @mobile_telephone_number.setter
    def mobile_telephone_number(self, mobile_telephone_number: str):
        """
        Gets or sets the mobile telephone number             

        :param mobile_telephone_number: The mobile_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._mobile_telephone_number = mobile_telephone_number

    @property
    def radio_telephone_number(self) -> str:
        """
        Gets or sets the radio telephone number             

        :return: The radio_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._radio_telephone_number

    @radio_telephone_number.setter
    def radio_telephone_number(self, radio_telephone_number: str):
        """
        Gets or sets the radio telephone number             

        :param radio_telephone_number: The radio_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._radio_telephone_number = radio_telephone_number

    @property
    def car_telephone_number(self) -> str:
        """
        Gets or sets the car telephone number             

        :return: The car_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._car_telephone_number

    @car_telephone_number.setter
    def car_telephone_number(self, car_telephone_number: str):
        """
        Gets or sets the car telephone number             

        :param car_telephone_number: The car_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._car_telephone_number = car_telephone_number

    @property
    def other_telephone_number(self) -> str:
        """
        Gets or sets an alternate telephone number             

        :return: The other_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._other_telephone_number

    @other_telephone_number.setter
    def other_telephone_number(self, other_telephone_number: str):
        """
        Gets or sets an alternate telephone number             

        :param other_telephone_number: The other_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._other_telephone_number = other_telephone_number

    @property
    def assistant_telephone_number(self) -> str:
        """
        Gets or sets the telephone number of the contact's assistant             

        :return: The assistant_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._assistant_telephone_number

    @assistant_telephone_number.setter
    def assistant_telephone_number(self, assistant_telephone_number: str):
        """
        Gets or sets the telephone number of the contact's assistant             

        :param assistant_telephone_number: The assistant_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._assistant_telephone_number = assistant_telephone_number

    @property
    def home2_telephone_number(self) -> str:
        """
        Gets or sets a second home telephone number             

        :return: The home2_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._home2_telephone_number

    @home2_telephone_number.setter
    def home2_telephone_number(self, home2_telephone_number: str):
        """
        Gets or sets a second home telephone number             

        :param home2_telephone_number: The home2_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._home2_telephone_number = home2_telephone_number

    @property
    def tty_tdd_phone_number(self) -> str:
        """
        Gets or sets the telephone number for the contact's text telephone (TTY) or telecommunication device for the deaf (TDD)             

        :return: The tty_tdd_phone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._tty_tdd_phone_number

    @tty_tdd_phone_number.setter
    def tty_tdd_phone_number(self, tty_tdd_phone_number: str):
        """
        Gets or sets the telephone number for the contact's text telephone (TTY) or telecommunication device for the deaf (TDD)             

        :param tty_tdd_phone_number: The tty_tdd_phone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._tty_tdd_phone_number = tty_tdd_phone_number

    @property
    def company_main_telephone_number(self) -> str:
        """
        Gets or sets the company phone number             

        :return: The company_main_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._company_main_telephone_number

    @company_main_telephone_number.setter
    def company_main_telephone_number(self, company_main_telephone_number: str):
        """
        Gets or sets the company phone number             

        :param company_main_telephone_number: The company_main_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._company_main_telephone_number = company_main_telephone_number

    @property
    def telex_number(self) -> str:
        """
        Gets or sets the telex number             

        :return: The telex_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._telex_number

    @telex_number.setter
    def telex_number(self, telex_number: str):
        """
        Gets or sets the telex number             

        :param telex_number: The telex_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._telex_number = telex_number

    @property
    def isdn_number(self) -> str:
        """
        Gets or sets the integrated services digital network (ISDN) number             

        :return: The isdn_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._isdn_number

    @isdn_number.setter
    def isdn_number(self, isdn_number: str):
        """
        Gets or sets the integrated services digital network (ISDN) number             

        :param isdn_number: The isdn_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._isdn_number = isdn_number

    @property
    def pager_telephone_number(self) -> str:
        """
        Gets or sets a pager telephone number             

        :return: The pager_telephone_number of this MapiContactTelephonePropertySetDto.
        :rtype: str
        """
        return self._pager_telephone_number

    @pager_telephone_number.setter
    def pager_telephone_number(self, pager_telephone_number: str):
        """
        Gets or sets a pager telephone number             

        :param pager_telephone_number: The pager_telephone_number of this MapiContactTelephonePropertySetDto.
        :type: str
        """
        self._pager_telephone_number = pager_telephone_number

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
        if not isinstance(other, MapiContactTelephonePropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
