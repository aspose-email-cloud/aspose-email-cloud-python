#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameFormatted.py">
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


class AiNameFormatted(object):
    """Formatted name             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'name': 'name',
        'comments': 'comments'
    }

    def __init__(self, name: str = None, comments: str = None):
        """
        Formatted name             
        :param name: Formatted name value             
        :param comments: Usually empty; can contain extra message describing some issue occurred during the formatting             
        :type AiNameFormatted: 
        """

        self._name = None
        self._comments = None

        if name is not None:
            self.name = name
        if comments is not None:
            self.comments = comments

    @property
    def name(self) -> str:
        """Gets the name of this AiNameFormatted.

        Formatted name value             

        :return: The name of this AiNameFormatted.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AiNameFormatted.

        Formatted name value             

        :param name: The name of this AiNameFormatted.
        :type: str
        """
        self._name = name

    @property
    def comments(self) -> str:
        """Gets the comments of this AiNameFormatted.

        Usually empty; can contain extra message describing some issue occurred during the formatting             

        :return: The comments of this AiNameFormatted.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments: str):
        """Sets the comments of this AiNameFormatted.

        Usually empty; can contain extra message describing some issue occurred during the formatting             

        :param comments: The comments of this AiNameFormatted.
        :type: str
        """
        self._comments = comments

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
        if not isinstance(other, AiNameFormatted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
