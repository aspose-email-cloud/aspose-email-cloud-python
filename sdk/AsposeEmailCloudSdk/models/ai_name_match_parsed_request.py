#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameMatchParsedRequest.py">
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

from AsposeEmailCloudSdk.models.ai_name_component import AiNameComponent
from AsposeEmailCloudSdk.models.ai_name_cultural_context import AiNameCulturalContext
from AsposeEmailCloudSdk.models.ai_name_parsed_request import AiNameParsedRequest


class AiNameMatchParsedRequest(AiNameParsedRequest):
    """Two parsed names to match request             
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
        'parsed_name': 'list[AiNameComponent]',
        'other_parsed_name': 'list[AiNameComponent]'
    }

    attribute_map = {
        'cultural_context': 'culturalContext',
        'format': 'format',
        'parsed_name': 'parsedName',
        'other_parsed_name': 'otherParsedName'
    }

    def __init__(self, cultural_context: AiNameCulturalContext = None, format: str = None, parsed_name: List[AiNameComponent] = None, other_parsed_name: List[AiNameComponent] = None):
        """
        Two parsed names to match request             
        :param cultural_context: AiName parser cultural context             
        :type cultural_context: AiNameCulturalContext
        :param format: Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (= '%t%F%m%N%L%p')     /format/FN+LN/ (= '%F%L')     /format/title+FN+LN/ (= '%t%F%L')     /format/FN+MN+LN/ (= '%F%M%N%L')     /format/title+FN+MN+LN/ (= '%t%F%M%N%L')     /format/FN+MI+LN/ (= '%F%m%N%L')     /format/title+FN+MI+LN/ (= '%t%F%m%N%L')     /format/LN/ (= '%L')     /format/title+LN/ (= '%t%L')     /format/LN+FN+MN/ (= '%L,%F%M%N')     /format/LN+title+FN+MN/ (= '%L,%t%F%M%N')     /format/LN+FN+MI/ (= '%L,%F%m%N')     /format/LN+title+FN+MI/ (= '%L,%t%F%m%N')  Custom format string - custom combination of characters and the next term placeholders:      '%t' - Title (prefix)     '%F' - First name     '%f' - First initial     '%M' - Middle name(s)     '%m' - Middle initial(s)     '%N' - Nickname     '%L' - Last name     '%l' - Last initial     '%p' - Postfix  If no value for format option was provided, its default value is '%t%F%m%N%L%p'             
        :type format: str
        :param parsed_name: Parsed name             
        :type parsed_name: List[AiNameComponent]
        :param other_parsed_name: Other parsed name to match             
        :type other_parsed_name: List[AiNameComponent]
        """
        super(AiNameMatchParsedRequest, self).__init__()

        self._other_parsed_name = None

        if cultural_context is not None:
            self.cultural_context = cultural_context
        if format is not None:
            self.format = format
        if parsed_name is not None:
            self.parsed_name = parsed_name
        if other_parsed_name is not None:
            self.other_parsed_name = other_parsed_name


    @property
    def other_parsed_name(self) -> List[AiNameComponent]:
        """
        Other parsed name to match             

        :return: The other_parsed_name of this AiNameMatchParsedRequest.
        :rtype: list[AiNameComponent]
        """
        return self._other_parsed_name

    @other_parsed_name.setter
    def other_parsed_name(self, other_parsed_name: List[AiNameComponent]):
        """
        Other parsed name to match             

        :param other_parsed_name: The other_parsed_name of this AiNameMatchParsedRequest.
        :type: list[AiNameComponent]
        """
        if other_parsed_name is None:
            raise ValueError("Invalid value for `other_parsed_name`, must not be `None`")
        self._other_parsed_name = other_parsed_name

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
        if not isinstance(other, AiNameMatchParsedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
