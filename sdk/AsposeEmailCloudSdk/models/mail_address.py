#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MailAddress.py">
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


class MailAddress(object):
    """Represents the address of a message.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_name': 'str',
        'address': 'str',
        'participation_status': 'str',
        'original_address_string': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'address': 'address',
        'participation_status': 'participationStatus',
        'original_address_string': 'originalAddressString'
    }

    def __init__(self, display_name: str = None, address: str = None, participation_status: str = None, original_address_string: str = None):
        """
        Represents the address of a message.
        :param display_name: Display name             
        :type display_name: str
        :param address: Address             
        :type address: str
        :param participation_status: Identifies the participation status for the calendar user. Enum, available values: NeedsAction, Accepted, Declined, Tentative, Delegated
        :type participation_status: str
        :param original_address_string: The original e-mail address string             
        :type original_address_string: str
        """

        self._display_name = None
        self._address = None
        self._participation_status = None
        self._original_address_string = None

        if display_name is not None:
            self.display_name = display_name
        if address is not None:
            self.address = address
        if participation_status is not None:
            self.participation_status = participation_status
        if original_address_string is not None:
            self.original_address_string = original_address_string


    @property
    def display_name(self) -> str:
        """
        Display name             

        :return: The display_name of this MailAddress.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        Display name             

        :param display_name: The display_name of this MailAddress.
        :type: str
        """
        self._display_name = display_name

    @property
    def address(self) -> str:
        """
        Address             

        :return: The address of this MailAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Address             

        :param address: The address of this MailAddress.
        :type: str
        """
        self._address = address

    @property
    def participation_status(self) -> str:
        """
        Identifies the participation status for the calendar user. Enum, available values: NeedsAction, Accepted, Declined, Tentative, Delegated

        :return: The participation_status of this MailAddress.
        :rtype: str
        """
        return self._participation_status

    @participation_status.setter
    def participation_status(self, participation_status: str):
        """
        Identifies the participation status for the calendar user. Enum, available values: NeedsAction, Accepted, Declined, Tentative, Delegated

        :param participation_status: The participation_status of this MailAddress.
        :type: str
        """
        if participation_status is None:
            raise ValueError("Invalid value for `participation_status`, must not be `None`")
        self._participation_status = participation_status

    @property
    def original_address_string(self) -> str:
        """
        The original e-mail address string             

        :return: The original_address_string of this MailAddress.
        :rtype: str
        """
        return self._original_address_string

    @original_address_string.setter
    def original_address_string(self, original_address_string: str):
        """
        The original e-mail address string             

        :param original_address_string: The original_address_string of this MailAddress.
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
        if not isinstance(other, MailAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
