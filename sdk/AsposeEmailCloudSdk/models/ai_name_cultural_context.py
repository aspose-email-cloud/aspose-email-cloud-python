#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameCulturalContext.py">
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


class AiNameCulturalContext(object):
    """AiName cultural context             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language': 'str',
        'location': 'str',
        'script': 'str',
        'encoding': 'str',
        'style': 'str'
    }

    attribute_map = {
        'language': 'language',
        'location': 'location',
        'script': 'script',
        'encoding': 'encoding',
        'style': 'style'
    }

    def __init__(self, language: str = None, location: str = None, script: str = None, encoding: str = None, style: str = None):
        """
        AiName cultural context             
        :param language: An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             
        :type language: str
        :param location: A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             
        :type location: str
        :param script: A writing system code; starts with the ISO-15924 script name             
        :type script: str
        :param encoding: A character encoding name             
        :type encoding: str
        :param style: Name writing style. Enum, available values: Formal, Informal, Legal, Academic
        :type style: str
        """

        self._language = None
        self._location = None
        self._script = None
        self._encoding = None
        self._style = None

        if language is not None:
            self.language = language
        if location is not None:
            self.location = location
        if script is not None:
            self.script = script
        if encoding is not None:
            self.encoding = encoding
        if style is not None:
            self.style = style


    @property
    def language(self) -> str:
        """
        An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             

        :return: The language of this AiNameCulturalContext.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """
        An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             

        :param language: The language of this AiNameCulturalContext.
        :type: str
        """
        self._language = language

    @property
    def location(self) -> str:
        """
        A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             

        :return: The location of this AiNameCulturalContext.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             

        :param location: The location of this AiNameCulturalContext.
        :type: str
        """
        self._location = location

    @property
    def script(self) -> str:
        """
        A writing system code; starts with the ISO-15924 script name             

        :return: The script of this AiNameCulturalContext.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script: str):
        """
        A writing system code; starts with the ISO-15924 script name             

        :param script: The script of this AiNameCulturalContext.
        :type: str
        """
        self._script = script

    @property
    def encoding(self) -> str:
        """
        A character encoding name             

        :return: The encoding of this AiNameCulturalContext.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding: str):
        """
        A character encoding name             

        :param encoding: The encoding of this AiNameCulturalContext.
        :type: str
        """
        self._encoding = encoding

    @property
    def style(self) -> str:
        """
        Name writing style. Enum, available values: Formal, Informal, Legal, Academic

        :return: The style of this AiNameCulturalContext.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style: str):
        """
        Name writing style. Enum, available values: Formal, Informal, Legal, Academic

        :param style: The style of this AiNameCulturalContext.
        :type: str
        """
        if style is None:
            raise ValueError("Invalid value for `style`, must not be `None`")
        self._style = style

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
        if not isinstance(other, AiNameCulturalContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
