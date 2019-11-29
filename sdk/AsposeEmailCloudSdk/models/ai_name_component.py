#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameComponent.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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


class AiNameComponent(object):
    """Parsed name component             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'str',
        'category': 'object',
        'score': 'float',
        'position': 'int'
    }

    attribute_map = {
        'value': 'value',
        'category': 'category',
        'score': 'score',
        'position': 'position'
    }

    def __init__(self, value=None, category=None, score=None, position=None):
        """AiNameComponent - a model defined in Swagger"""

        self._value = None
        self._category = None
        self._score = None
        self._position = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if category is not None:
            self.category = category
        if score is not None:
            self.score = score
        if position is not None:
            self.position = position

    @property
    def value(self):
        """Gets the value of this AiNameComponent.

        Component value             

        :return: The value of this AiNameComponent.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AiNameComponent.

        Component value             

        :param value: The value of this AiNameComponent.
        :type: str
        """
        self._value = value

    @property
    def category(self):
        """Gets the category of this AiNameComponent.

        Component category             

        :return: The category of this AiNameComponent.
        :rtype: object
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AiNameComponent.

        Component category             

        :param category: The category of this AiNameComponent.
        :type: object
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")
        self._category = category

    @property
    def score(self):
        """Gets the score of this AiNameComponent.

        Score from 0.0 to 1.0             

        :return: The score of this AiNameComponent.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this AiNameComponent.

        Score from 0.0 to 1.0             

        :param score: The score of this AiNameComponent.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")
        self._score = score

    @property
    def position(self):
        """Gets the position of this AiNameComponent.

        Component position from 0             

        :return: The position of this AiNameComponent.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this AiNameComponent.

        Component position from 0             

        :param position: The position of this AiNameComponent.
        :type: int
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")
        self._position = position

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
        if not isinstance(other, AiNameComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
