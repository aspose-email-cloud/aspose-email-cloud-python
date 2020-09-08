#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameWeightedVariants.py">
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

from AsposeEmailCloudSdk.models.ai_name_weighted import AiNameWeighted


class AiNameWeightedVariants(object):
    """Name variants             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'names': 'list[AiNameWeighted]',
        'comments': 'str'
    }

    attribute_map = {
        'names': 'names',
        'comments': 'comments'
    }

    def __init__(self, names: List[AiNameWeighted] = None, comments: str = None):
        """
        Name variants             
        :param names: List of name variations             
        :type names: List[AiNameWeighted]
        :param comments: Usually empty; can contain extra message describing some issue occurred during processing             
        :type comments: str
        """

        self._names = None
        self._comments = None

        if names is not None:
            self.names = names
        if comments is not None:
            self.comments = comments


    @property
    def names(self) -> List[AiNameWeighted]:
        """
        List of name variations             

        :return: The names of this AiNameWeightedVariants.
        :rtype: list[AiNameWeighted]
        """
        return self._names

    @names.setter
    def names(self, names: List[AiNameWeighted]):
        """
        List of name variations             

        :param names: The names of this AiNameWeightedVariants.
        :type: list[AiNameWeighted]
        """
        self._names = names

    @property
    def comments(self) -> str:
        """
        Usually empty; can contain extra message describing some issue occurred during processing             

        :return: The comments of this AiNameWeightedVariants.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments: str):
        """
        Usually empty; can contain extra message describing some issue occurred during processing             

        :param comments: The comments of this AiNameWeightedVariants.
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
        if not isinstance(other, AiNameWeightedVariants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
