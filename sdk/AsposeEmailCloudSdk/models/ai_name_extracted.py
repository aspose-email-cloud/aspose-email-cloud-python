#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameExtracted.py">
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

from AsposeEmailCloudSdk.models.ai_name_extracted_component import AiNameExtractedComponent


class AiNameExtracted(object):
    """Extracted name             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'list[AiNameExtractedComponent]',
        'score': 'float'
    }

    attribute_map = {
        'name': 'name',
        'score': 'score'
    }

    def __init__(self, name: List[AiNameExtractedComponent] = None, score: float = None):
        """
        Extracted name             
        :param name: Extracted name components             
        :type name: List[AiNameExtractedComponent]
        :param score: Extracted name score             
        :type score: float
        """

        self._name = None
        self._score = None

        if name is not None:
            self.name = name
        if score is not None:
            self.score = score


    @property
    def name(self) -> List[AiNameExtractedComponent]:
        """
        Extracted name components             

        :return: The name of this AiNameExtracted.
        :rtype: list[AiNameExtractedComponent]
        """
        return self._name

    @name.setter
    def name(self, name: List[AiNameExtractedComponent]):
        """
        Extracted name components             

        :param name: The name of this AiNameExtracted.
        :type: list[AiNameExtractedComponent]
        """
        self._name = name

    @property
    def score(self) -> float:
        """
        Extracted name score             

        :return: The score of this AiNameExtracted.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """
        Extracted name score             

        :param score: The score of this AiNameExtracted.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")
        self._score = score

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
        if not isinstance(other, AiNameExtracted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
