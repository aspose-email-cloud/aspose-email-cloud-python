#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameParsedRq.py">
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

from AsposeEmailCloudSdk.models.ai_name_component import AiNameComponent
from AsposeEmailCloudSdk.models.ai_name_cultural_context import AiNameCulturalContext


class AiNameParsedRq(object):
    """Parsed name request model             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cultural_context': 'AiNameCulturalContext',
        'format': 'str',
        'parsed_name': 'list[AiNameComponent]'
    }

    attribute_map = {
        'cultural_context': 'culturalContext',
        'format': 'format',
        'parsed_name': 'parsedName'
    }

    discriminator_value_class_map = {
        'AiNameParsedMatchRq': 'AiNameParsedMatchRq'
    }

    def __init__(self, cultural_context=None, format=None, parsed_name=None):
        """AiNameParsedRq - a model defined in Swagger"""

        self._cultural_context = None
        self._format = None
        self._parsed_name = None
        self.discriminator = 'Type'

        if cultural_context is not None:
            self.cultural_context = cultural_context
        if format is not None:
            self.format = format
        if parsed_name is not None:
            self.parsed_name = parsed_name

    @property
    def cultural_context(self):
        """Gets the cultural_context of this AiNameParsedRq.

        AiName parser cultural context             

        :return: The cultural_context of this AiNameParsedRq.
        :rtype: AiNameCulturalContext
        """
        return self._cultural_context

    @cultural_context.setter
    def cultural_context(self, cultural_context):
        """Sets the cultural_context of this AiNameParsedRq.

        AiName parser cultural context             

        :param cultural_context: The cultural_context of this AiNameParsedRq.
        :type: AiNameCulturalContext
        """
        self._cultural_context = cultural_context

    @property
    def format(self):
        """Gets the format of this AiNameParsedRq.

        Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (= '%t%F%m%N%L%p')     /format/FN+LN/ (= '%F%L')     /format/title+FN+LN/ (= '%t%F%L')     /format/FN+MN+LN/ (= '%F%M%N%L')     /format/title+FN+MN+LN/ (= '%t%F%M%N%L')     /format/FN+MI+LN/ (= '%F%m%N%L')     /format/title+FN+MI+LN/ (= '%t%F%m%N%L')     /format/LN/ (= '%L')     /format/title+LN/ (= '%t%L')     /format/LN+FN+MN/ (= '%L,%F%M%N')     /format/LN+title+FN+MN/ (= '%L,%t%F%M%N')     /format/LN+FN+MI/ (= '%L,%F%m%N')     /format/LN+title+FN+MI/ (= '%L,%t%F%m%N')  Custom format string - custom combination of characters and the next term placeholders:      '%t' - Title (prefix)     '%F' - First name     '%f' - First initial     '%M' - Middle name(s)     '%m' - Middle initial(s)     '%N' - Nickname     '%L' - Last name     '%l' - Last initial     '%p' - Postfix  If no value for format option was provided, its default value is '%t%F%m%N%L%p'             

        :return: The format of this AiNameParsedRq.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AiNameParsedRq.

        Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (= '%t%F%m%N%L%p')     /format/FN+LN/ (= '%F%L')     /format/title+FN+LN/ (= '%t%F%L')     /format/FN+MN+LN/ (= '%F%M%N%L')     /format/title+FN+MN+LN/ (= '%t%F%M%N%L')     /format/FN+MI+LN/ (= '%F%m%N%L')     /format/title+FN+MI+LN/ (= '%t%F%m%N%L')     /format/LN/ (= '%L')     /format/title+LN/ (= '%t%L')     /format/LN+FN+MN/ (= '%L,%F%M%N')     /format/LN+title+FN+MN/ (= '%L,%t%F%M%N')     /format/LN+FN+MI/ (= '%L,%F%m%N')     /format/LN+title+FN+MI/ (= '%L,%t%F%m%N')  Custom format string - custom combination of characters and the next term placeholders:      '%t' - Title (prefix)     '%F' - First name     '%f' - First initial     '%M' - Middle name(s)     '%m' - Middle initial(s)     '%N' - Nickname     '%L' - Last name     '%l' - Last initial     '%p' - Postfix  If no value for format option was provided, its default value is '%t%F%m%N%L%p'             

        :param format: The format of this AiNameParsedRq.
        :type: str
        """
        self._format = format

    @property
    def parsed_name(self):
        """Gets the parsed_name of this AiNameParsedRq.

        Parsed name             

        :return: The parsed_name of this AiNameParsedRq.
        :rtype: list[AiNameComponent]
        """
        return self._parsed_name

    @parsed_name.setter
    def parsed_name(self, parsed_name):
        """Sets the parsed_name of this AiNameParsedRq.

        Parsed name             

        :param parsed_name: The parsed_name of this AiNameParsedRq.
        :type: list[AiNameComponent]
        """
        if parsed_name is None:
            raise ValueError("Invalid value for `parsed_name`, must not be `None`")
        self._parsed_name = parsed_name

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, AiNameParsedRq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other