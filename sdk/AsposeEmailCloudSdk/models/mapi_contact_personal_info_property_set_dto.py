#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactPersonalInfoPropertySetDto.py">
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


class MapiContactPersonalInfoPropertySetDto(object):
    """Specify other additional contact information.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'spouse_name': 'str',
        'personal_home_page': 'str',
        'language': 'str',
        'notes': 'str',
        'hobbies': 'str',
        'location': 'str',
        'instant_messaging_address': 'str',
        'organizational_id_number': 'str',
        'customer_id': 'str',
        'government_id_number': 'str',
        'free_busy_location': 'str',
        'account': 'str',
        'html': 'str',
        'business_home_page': 'str',
        'ftp_site': 'str',
        'computer_network_name': 'str',
        'gender': 'str',
        'referred_by_name': 'str',
        'children': 'list[str]'
    }

    attribute_map = {
        'spouse_name': 'spouseName',
        'personal_home_page': 'personalHomePage',
        'language': 'language',
        'notes': 'notes',
        'hobbies': 'hobbies',
        'location': 'location',
        'instant_messaging_address': 'instantMessagingAddress',
        'organizational_id_number': 'organizationalIdNumber',
        'customer_id': 'customerId',
        'government_id_number': 'governmentIdNumber',
        'free_busy_location': 'freeBusyLocation',
        'account': 'account',
        'html': 'html',
        'business_home_page': 'businessHomePage',
        'ftp_site': 'ftpSite',
        'computer_network_name': 'computerNetworkName',
        'gender': 'gender',
        'referred_by_name': 'referredByName',
        'children': 'children'
    }

    def __init__(self, spouse_name: str = None, personal_home_page: str = None, language: str = None, notes: str = None, hobbies: str = None, location: str = None, instant_messaging_address: str = None, organizational_id_number: str = None, customer_id: str = None, government_id_number: str = None, free_busy_location: str = None, account: str = None, html: str = None, business_home_page: str = None, ftp_site: str = None, computer_network_name: str = None, gender: str = None, referred_by_name: str = None, children: List[str] = None):
        """
        Specify other additional contact information.             
        :param spouse_name: Specifies the name of the contact's spouse/partner             
        :type spouse_name: str
        :param personal_home_page: Specifies the contact's personal web page URL             
        :type personal_home_page: str
        :param language: Specifies the language that the contact uses             
        :type language: str
        :param notes: Specifies the additional notes             
        :type notes: str
        :param hobbies: Specifies the hobbies of the contact             
        :type hobbies: str
        :param location: Specifies the location of the contact             
        :type location: str
        :param instant_messaging_address: Specifies the contact's instant messaging address             
        :type instant_messaging_address: str
        :param organizational_id_number: Specifies an organizational ID number for the contact             
        :type organizational_id_number: str
        :param customer_id: Specifies the contact's customer ID number             
        :type customer_id: str
        :param government_id_number: Specifies the contact's government ID number             
        :type government_id_number: str
        :param free_busy_location: Specifies a URL path from which a client can retrieve free/busy information for the contact as an iCal file             
        :type free_busy_location: str
        :param account: Specifies the account name of the contact             
        :type account: str
        :param html: Specifies the contact's business web page URL             
        :type html: str
        :param business_home_page: Specifies the contact's business web page URL             
        :type business_home_page: str
        :param ftp_site: Specifies the contact's File Transfer Protocol (FTP) URL             
        :type ftp_site: str
        :param computer_network_name: Specifies the name of the network to which the contact's computer is connected             
        :type computer_network_name: str
        :param gender: Gender of the contact Enum, available values: Unspecified, Female, Male
        :type gender: str
        :param referred_by_name: Specifies the name of the person who referred this contact to the user             
        :type referred_by_name: str
        :param children: Contains a list of names of children.             
        :type children: List[str]
        """

        self._spouse_name = None
        self._personal_home_page = None
        self._language = None
        self._notes = None
        self._hobbies = None
        self._location = None
        self._instant_messaging_address = None
        self._organizational_id_number = None
        self._customer_id = None
        self._government_id_number = None
        self._free_busy_location = None
        self._account = None
        self._html = None
        self._business_home_page = None
        self._ftp_site = None
        self._computer_network_name = None
        self._gender = None
        self._referred_by_name = None
        self._children = None

        if spouse_name is not None:
            self.spouse_name = spouse_name
        if personal_home_page is not None:
            self.personal_home_page = personal_home_page
        if language is not None:
            self.language = language
        if notes is not None:
            self.notes = notes
        if hobbies is not None:
            self.hobbies = hobbies
        if location is not None:
            self.location = location
        if instant_messaging_address is not None:
            self.instant_messaging_address = instant_messaging_address
        if organizational_id_number is not None:
            self.organizational_id_number = organizational_id_number
        if customer_id is not None:
            self.customer_id = customer_id
        if government_id_number is not None:
            self.government_id_number = government_id_number
        if free_busy_location is not None:
            self.free_busy_location = free_busy_location
        if account is not None:
            self.account = account
        if html is not None:
            self.html = html
        if business_home_page is not None:
            self.business_home_page = business_home_page
        if ftp_site is not None:
            self.ftp_site = ftp_site
        if computer_network_name is not None:
            self.computer_network_name = computer_network_name
        if gender is not None:
            self.gender = gender
        if referred_by_name is not None:
            self.referred_by_name = referred_by_name
        if children is not None:
            self.children = children


    @property
    def spouse_name(self) -> str:
        """
        Specifies the name of the contact's spouse/partner             

        :return: The spouse_name of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._spouse_name

    @spouse_name.setter
    def spouse_name(self, spouse_name: str):
        """
        Specifies the name of the contact's spouse/partner             

        :param spouse_name: The spouse_name of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._spouse_name = spouse_name

    @property
    def personal_home_page(self) -> str:
        """
        Specifies the contact's personal web page URL             

        :return: The personal_home_page of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._personal_home_page

    @personal_home_page.setter
    def personal_home_page(self, personal_home_page: str):
        """
        Specifies the contact's personal web page URL             

        :param personal_home_page: The personal_home_page of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._personal_home_page = personal_home_page

    @property
    def language(self) -> str:
        """
        Specifies the language that the contact uses             

        :return: The language of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """
        Specifies the language that the contact uses             

        :param language: The language of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._language = language

    @property
    def notes(self) -> str:
        """
        Specifies the additional notes             

        :return: The notes of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """
        Specifies the additional notes             

        :param notes: The notes of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._notes = notes

    @property
    def hobbies(self) -> str:
        """
        Specifies the hobbies of the contact             

        :return: The hobbies of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._hobbies

    @hobbies.setter
    def hobbies(self, hobbies: str):
        """
        Specifies the hobbies of the contact             

        :param hobbies: The hobbies of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._hobbies = hobbies

    @property
    def location(self) -> str:
        """
        Specifies the location of the contact             

        :return: The location of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Specifies the location of the contact             

        :param location: The location of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._location = location

    @property
    def instant_messaging_address(self) -> str:
        """
        Specifies the contact's instant messaging address             

        :return: The instant_messaging_address of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._instant_messaging_address

    @instant_messaging_address.setter
    def instant_messaging_address(self, instant_messaging_address: str):
        """
        Specifies the contact's instant messaging address             

        :param instant_messaging_address: The instant_messaging_address of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._instant_messaging_address = instant_messaging_address

    @property
    def organizational_id_number(self) -> str:
        """
        Specifies an organizational ID number for the contact             

        :return: The organizational_id_number of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._organizational_id_number

    @organizational_id_number.setter
    def organizational_id_number(self, organizational_id_number: str):
        """
        Specifies an organizational ID number for the contact             

        :param organizational_id_number: The organizational_id_number of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._organizational_id_number = organizational_id_number

    @property
    def customer_id(self) -> str:
        """
        Specifies the contact's customer ID number             

        :return: The customer_id of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """
        Specifies the contact's customer ID number             

        :param customer_id: The customer_id of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def government_id_number(self) -> str:
        """
        Specifies the contact's government ID number             

        :return: The government_id_number of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._government_id_number

    @government_id_number.setter
    def government_id_number(self, government_id_number: str):
        """
        Specifies the contact's government ID number             

        :param government_id_number: The government_id_number of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._government_id_number = government_id_number

    @property
    def free_busy_location(self) -> str:
        """
        Specifies a URL path from which a client can retrieve free/busy information for the contact as an iCal file             

        :return: The free_busy_location of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._free_busy_location

    @free_busy_location.setter
    def free_busy_location(self, free_busy_location: str):
        """
        Specifies a URL path from which a client can retrieve free/busy information for the contact as an iCal file             

        :param free_busy_location: The free_busy_location of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._free_busy_location = free_busy_location

    @property
    def account(self) -> str:
        """
        Specifies the account name of the contact             

        :return: The account of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account: str):
        """
        Specifies the account name of the contact             

        :param account: The account of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._account = account

    @property
    def html(self) -> str:
        """
        Specifies the contact's business web page URL             

        :return: The html of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html: str):
        """
        Specifies the contact's business web page URL             

        :param html: The html of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._html = html

    @property
    def business_home_page(self) -> str:
        """
        Specifies the contact's business web page URL             

        :return: The business_home_page of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._business_home_page

    @business_home_page.setter
    def business_home_page(self, business_home_page: str):
        """
        Specifies the contact's business web page URL             

        :param business_home_page: The business_home_page of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._business_home_page = business_home_page

    @property
    def ftp_site(self) -> str:
        """
        Specifies the contact's File Transfer Protocol (FTP) URL             

        :return: The ftp_site of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._ftp_site

    @ftp_site.setter
    def ftp_site(self, ftp_site: str):
        """
        Specifies the contact's File Transfer Protocol (FTP) URL             

        :param ftp_site: The ftp_site of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._ftp_site = ftp_site

    @property
    def computer_network_name(self) -> str:
        """
        Specifies the name of the network to which the contact's computer is connected             

        :return: The computer_network_name of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._computer_network_name

    @computer_network_name.setter
    def computer_network_name(self, computer_network_name: str):
        """
        Specifies the name of the network to which the contact's computer is connected             

        :param computer_network_name: The computer_network_name of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._computer_network_name = computer_network_name

    @property
    def gender(self) -> str:
        """
        Gender of the contact Enum, available values: Unspecified, Female, Male

        :return: The gender of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """
        Gender of the contact Enum, available values: Unspecified, Female, Male

        :param gender: The gender of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        if gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")
        self._gender = gender

    @property
    def referred_by_name(self) -> str:
        """
        Specifies the name of the person who referred this contact to the user             

        :return: The referred_by_name of this MapiContactPersonalInfoPropertySetDto.
        :rtype: str
        """
        return self._referred_by_name

    @referred_by_name.setter
    def referred_by_name(self, referred_by_name: str):
        """
        Specifies the name of the person who referred this contact to the user             

        :param referred_by_name: The referred_by_name of this MapiContactPersonalInfoPropertySetDto.
        :type: str
        """
        self._referred_by_name = referred_by_name

    @property
    def children(self) -> List[str]:
        """
        Contains a list of names of children.             

        :return: The children of this MapiContactPersonalInfoPropertySetDto.
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children: List[str]):
        """
        Contains a list of names of children.             

        :param children: The children of this MapiContactPersonalInfoPropertySetDto.
        :type: list[str]
        """
        self._children = children

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
        if not isinstance(other, MapiContactPersonalInfoPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
