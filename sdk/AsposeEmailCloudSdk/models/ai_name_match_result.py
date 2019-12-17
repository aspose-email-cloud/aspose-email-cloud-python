#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameMatchResult.py">
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

from AsposeEmailCloudSdk.models.ai_name_mismatch import AiNameMismatch


class AiNameMatchResult(object):
    """Two names match result             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'similarity': 'float',
        'mismatches': 'list[AiNameMismatch]'
    }

    attribute_map = {
        'similarity': 'similarity',
        'mismatches': 'mismatches'
    }

    def __init__(self, similarity=None, mismatches=None):
        """AiNameMatchResult - a model defined in Swagger"""

        self._similarity = None
        self._mismatches = None
        self.discriminator = None

        if similarity is not None:
            self.similarity = similarity
        if mismatches is not None:
            self.mismatches = mismatches

    @property
    def similarity(self):
        """Gets the similarity of this AiNameMatchResult.

        Similarity score             

        :return: The similarity of this AiNameMatchResult.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this AiNameMatchResult.

        Similarity score             

        :param similarity: The similarity of this AiNameMatchResult.
        :type: float
        """
        if similarity is None:
            raise ValueError("Invalid value for `similarity`, must not be `None`")
        self._similarity = similarity

    @property
    def mismatches(self):
        """Gets the mismatches of this AiNameMatchResult.

        Detailed description of mismatches             

        :return: The mismatches of this AiNameMatchResult.
        :rtype: list[AiNameMismatch]
        """
        return self._mismatches

    @mismatches.setter
    def mismatches(self, mismatches):
        """Sets the mismatches of this AiNameMatchResult.

        Detailed description of mismatches             

        :param mismatches: The mismatches of this AiNameMatchResult.
        :type: list[AiNameMismatch]
        """
        self._mismatches = mismatches

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
        if not isinstance(other, AiNameMatchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other