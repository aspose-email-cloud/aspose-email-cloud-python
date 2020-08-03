#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactEventPropertySetDto.py">
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


class MapiContactEventPropertySetDto(object):
    """Specify events associated with a contact.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'birthday': 'datetime',
        'wedding_anniversary': 'datetime'
    }

    attribute_map = {
        'birthday': 'birthday',
        'wedding_anniversary': 'weddingAnniversary'
    }

    def __init__(self, birthday: datetime = None, wedding_anniversary: datetime = None):
        """
        Specify events associated with a contact.             
        :param birthday: Specifies the birthday of the contact.
        :type birthday: datetime
        :param wedding_anniversary: Specifies the wedding anniversary of the contact.             
        :type wedding_anniversary: datetime
        """

        self._birthday = None
        self._wedding_anniversary = None

        if birthday is not None:
            self.birthday = birthday
        if wedding_anniversary is not None:
            self.wedding_anniversary = wedding_anniversary


    @property
    def birthday(self) -> datetime:
        """
        Specifies the birthday of the contact.

        :return: The birthday of this MapiContactEventPropertySetDto.
        :rtype: datetime
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: datetime):
        """
        Specifies the birthday of the contact.

        :param birthday: The birthday of this MapiContactEventPropertySetDto.
        :type: datetime
        """
        if birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")
        self._birthday = birthday

    @property
    def wedding_anniversary(self) -> datetime:
        """
        Specifies the wedding anniversary of the contact.             

        :return: The wedding_anniversary of this MapiContactEventPropertySetDto.
        :rtype: datetime
        """
        return self._wedding_anniversary

    @wedding_anniversary.setter
    def wedding_anniversary(self, wedding_anniversary: datetime):
        """
        Specifies the wedding anniversary of the contact.             

        :param wedding_anniversary: The wedding_anniversary of this MapiContactEventPropertySetDto.
        :type: datetime
        """
        if wedding_anniversary is None:
            raise ValueError("Invalid value for `wedding_anniversary`, must not be `None`")
        self._wedding_anniversary = wedding_anniversary

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
        if not isinstance(other, MapiContactEventPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
