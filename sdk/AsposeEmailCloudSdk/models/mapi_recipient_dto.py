#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiRecipientDto.py">
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


class MapiRecipientDto(object):
    """Represents the recipient information in the Microsoft Outlook Message.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email_address': 'str',
        'address_type': 'str',
        'display_name': 'str',
        'recipient_type': 'str'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'address_type': 'addressType',
        'display_name': 'displayName',
        'recipient_type': 'recipientType'
    }

    def __init__(self, email_address: str = None, address_type: str = None, display_name: str = None, recipient_type: str = None):
        """
        Represents the recipient information in the Microsoft Outlook Message.             
        :param email_address: Email address of the message recipient or sender.             
        :type email_address: str
        :param address_type: Type of the address of the message recipient or sender.             
        :type address_type: str
        :param display_name: Display name of the message recipient or sender.             
        :type display_name: str
        :param recipient_type: Represent the PR_RECIPIENT_TYPE property which contains the recipient type for a message recipient. Enum, available values: Unknown, MapiBcc, MapiCc, MapiP1, MapiSubmitted, MapiTo
        :type recipient_type: str
        """

        self._email_address = None
        self._address_type = None
        self._display_name = None
        self._recipient_type = None

        if email_address is not None:
            self.email_address = email_address
        if address_type is not None:
            self.address_type = address_type
        if display_name is not None:
            self.display_name = display_name
        if recipient_type is not None:
            self.recipient_type = recipient_type


    @property
    def email_address(self) -> str:
        """
        Email address of the message recipient or sender.             

        :return: The email_address of this MapiRecipientDto.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str):
        """
        Email address of the message recipient or sender.             

        :param email_address: The email_address of this MapiRecipientDto.
        :type: str
        """
        self._email_address = email_address

    @property
    def address_type(self) -> str:
        """
        Type of the address of the message recipient or sender.             

        :return: The address_type of this MapiRecipientDto.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type: str):
        """
        Type of the address of the message recipient or sender.             

        :param address_type: The address_type of this MapiRecipientDto.
        :type: str
        """
        self._address_type = address_type

    @property
    def display_name(self) -> str:
        """
        Display name of the message recipient or sender.             

        :return: The display_name of this MapiRecipientDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        Display name of the message recipient or sender.             

        :param display_name: The display_name of this MapiRecipientDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def recipient_type(self) -> str:
        """
        Represent the PR_RECIPIENT_TYPE property which contains the recipient type for a message recipient. Enum, available values: Unknown, MapiBcc, MapiCc, MapiP1, MapiSubmitted, MapiTo

        :return: The recipient_type of this MapiRecipientDto.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type: str):
        """
        Represent the PR_RECIPIENT_TYPE property which contains the recipient type for a message recipient. Enum, available values: Unknown, MapiBcc, MapiCc, MapiP1, MapiSubmitted, MapiTo

        :param recipient_type: The recipient_type of this MapiRecipientDto.
        :type: str
        """
        if recipient_type is None:
            raise ValueError("Invalid value for `recipient_type`, must not be `None`")
        self._recipient_type = recipient_type

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
        if not isinstance(other, MapiRecipientDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
