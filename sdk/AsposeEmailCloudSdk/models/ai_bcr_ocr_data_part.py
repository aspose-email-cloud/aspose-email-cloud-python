#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiBcrOcrDataPart.py">
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


class AiBcrOcrDataPart(object):
    """Recognized text block             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float',
        'text': 'str',
        'details': 'dict(str, str)'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height',
        'text': 'text',
        'details': 'details'
    }

    def __init__(self, x: float = None, y: float = None, width: float = None, height: float = None, text: str = None, details: Dict[str, str] = None):
        """
        Recognized text block             
        :param x (float) X position of text block             
        :param y (float) Y position of text block             
        :param width (float) Width of text block             
        :param height (float) Height of text block             
        :param text (str) Recognized text             
        :param details (Dict[str, str]) Additional recognition result details             
        """

        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._text = None
        self._details = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if text is not None:
            self.text = text
        if details is not None:
            self.details = details

    @property
    def x(self) -> float:
        """Gets the x of this AiBcrOcrDataPart.

        X position of text block             

        :return: The x of this AiBcrOcrDataPart.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x: float):
        """Sets the x of this AiBcrOcrDataPart.

        X position of text block             

        :param x: The x of this AiBcrOcrDataPart.
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")
        self._x = x

    @property
    def y(self) -> float:
        """Gets the y of this AiBcrOcrDataPart.

        Y position of text block             

        :return: The y of this AiBcrOcrDataPart.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y: float):
        """Sets the y of this AiBcrOcrDataPart.

        Y position of text block             

        :param y: The y of this AiBcrOcrDataPart.
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")
        self._y = y

    @property
    def width(self) -> float:
        """Gets the width of this AiBcrOcrDataPart.

        Width of text block             

        :return: The width of this AiBcrOcrDataPart.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width: float):
        """Sets the width of this AiBcrOcrDataPart.

        Width of text block             

        :param width: The width of this AiBcrOcrDataPart.
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def height(self) -> float:
        """Gets the height of this AiBcrOcrDataPart.

        Height of text block             

        :return: The height of this AiBcrOcrDataPart.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height: float):
        """Sets the height of this AiBcrOcrDataPart.

        Height of text block             

        :param height: The height of this AiBcrOcrDataPart.
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

    @property
    def text(self) -> str:
        """Gets the text of this AiBcrOcrDataPart.

        Recognized text             

        :return: The text of this AiBcrOcrDataPart.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this AiBcrOcrDataPart.

        Recognized text             

        :param text: The text of this AiBcrOcrDataPart.
        :type: str
        """
        self._text = text

    @property
    def details(self) -> Dict[str, str]:
        """Gets the details of this AiBcrOcrDataPart.

        Additional recognition result details             

        :return: The details of this AiBcrOcrDataPart.
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details: Dict[str, str]):
        """Sets the details of this AiBcrOcrDataPart.

        Additional recognition result details             

        :param details: The details of this AiBcrOcrDataPart.
        :type: dict(str, str)
        """
        self._details = details

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
        if not isinstance(other, AiBcrOcrDataPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
