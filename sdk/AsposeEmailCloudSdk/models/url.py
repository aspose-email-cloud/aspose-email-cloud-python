#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="Url.py">
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

from AsposeEmailCloudSdk.models.enum_with_custom_of_url_category import EnumWithCustomOfUrlCategory


class Url(object):
    """Url and its category.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'EnumWithCustomOfUrlCategory',
        'preferred': 'bool',
        'href': 'str'
    }

    attribute_map = {
        'category': 'category',
        'preferred': 'preferred',
        'href': 'href'
    }

    def __init__(self, category: EnumWithCustomOfUrlCategory = None, preferred: bool = None, href: str = None):
        """
        Url and its category.             
        :param category: Url category.             
        :type category: EnumWithCustomOfUrlCategory
        :param preferred: Defines whether url is preferred.             
        :type preferred: bool
        :param href: URL.             
        :type href: str
        """

        self._category = None
        self._preferred = None
        self._href = None

        if category is not None:
            self.category = category
        if preferred is not None:
            self.preferred = preferred
        if href is not None:
            self.href = href


    @property
    def category(self) -> EnumWithCustomOfUrlCategory:
        """
        Url category.             

        :return: The category of this Url.
        :rtype: EnumWithCustomOfUrlCategory
        """
        return self._category

    @category.setter
    def category(self, category: EnumWithCustomOfUrlCategory):
        """
        Url category.             

        :param category: The category of this Url.
        :type: EnumWithCustomOfUrlCategory
        """
        self._category = category

    @property
    def preferred(self) -> bool:
        """
        Defines whether url is preferred.             

        :return: The preferred of this Url.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred: bool):
        """
        Defines whether url is preferred.             

        :param preferred: The preferred of this Url.
        :type: bool
        """
        if preferred is None:
            raise ValueError("Invalid value for `preferred`, must not be `None`")
        self._preferred = preferred

    @property
    def href(self) -> str:
        """
        URL.             

        :return: The href of this Url.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """
        URL.             

        :param href: The href of this Url.
        :type: str
        """
        self._href = href

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
        if not isinstance(other, Url):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
