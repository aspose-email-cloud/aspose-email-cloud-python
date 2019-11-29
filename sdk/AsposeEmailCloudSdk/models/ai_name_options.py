#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameOptions.py">
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


class AiNameOptions(object):
    """AiName parser options             
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

    def __init__(self, language=None, location=None, script=None, encoding=None, style=None):
        """AiNameOptions - a model defined in Swagger"""

        self._language = None
        self._location = None
        self._script = None
        self._encoding = None
        self._style = None
        self.discriminator = None

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
    def language(self):
        """Gets the language of this AiNameOptions.

        An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             

        :return: The language of this AiNameOptions.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AiNameOptions.

        An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian)             

        :param language: The language of this AiNameOptions.
        :type: str
        """
        self._language = language

    @property
    def location(self):
        """Gets the location of this AiNameOptions.

        A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             

        :return: The location of this AiNameOptions.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AiNameOptions.

        A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France             

        :param location: The location of this AiNameOptions.
        :type: str
        """
        self._location = location

    @property
    def script(self):
        """Gets the script of this AiNameOptions.

        A writing system code; starts with the ISO-15924 script name             

        :return: The script of this AiNameOptions.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this AiNameOptions.

        A writing system code; starts with the ISO-15924 script name             

        :param script: The script of this AiNameOptions.
        :type: str
        """
        self._script = script

    @property
    def encoding(self):
        """Gets the encoding of this AiNameOptions.

        A character encoding name             

        :return: The encoding of this AiNameOptions.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this AiNameOptions.

        A character encoding name             

        :param encoding: The encoding of this AiNameOptions.
        :type: str
        """
        self._encoding = encoding

    @property
    def style(self):
        """Gets the style of this AiNameOptions.

        Name writing style. Allowed values are: \"Formal\", \"Informal\", \"Legal\", \"Academic\"             

        :return: The style of this AiNameOptions.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this AiNameOptions.

        Name writing style. Allowed values are: \"Formal\", \"Informal\", \"Legal\", \"Academic\"             

        :param style: The style of this AiNameOptions.
        :type: str
        """
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
        if not isinstance(other, AiNameOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
