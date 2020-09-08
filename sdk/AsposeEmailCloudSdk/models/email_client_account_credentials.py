#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailClientAccountCredentials.py">
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


class EmailClientAccountCredentials(object):
    """Represents email client account credentials             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'login': 'str',
        'discriminator': 'str'
    }

    attribute_map = {
        'login': 'login',
        'discriminator': 'discriminator'
    }

    def __init__(self, login: str = None):
        """
        Represents email client account credentials             
        :param login: Email client account login             
        :type login: str
        """

        self._login = None

        if login is not None:
            self.login = login


    @property
    def login(self) -> str:
        """
        Email client account login             

        :return: The login of this EmailClientAccountCredentials.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """
        Email client account login             

        :param login: The login of this EmailClientAccountCredentials.
        :type: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")
        if login is not None and len(login) < 1:
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `1`")
        self._login = login

    @property
    def discriminator(self) -> str:
        """
        Gets the discriminator of this EmailClientAccountCredentials.

        :return: The discriminator of this EmailClientAccountCredentials.
        :rtype: str
        """
        return self.__class__.__name__

    @discriminator.setter
    def discriminator(self, discriminator: str):
        """
        Sets the discriminator of this EmailClientAccountCredentials.

        :param discriminator: The discriminator of this EmailClientAccountCredentials.
        :type: str
        """
        pass    # setter is ignored for discriminator property

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
        if not isinstance(other, EmailClientAccountCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
