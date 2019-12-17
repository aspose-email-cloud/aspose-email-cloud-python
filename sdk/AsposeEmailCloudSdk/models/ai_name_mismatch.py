#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiNameMismatch.py">
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


class AiNameMismatch(object):
    """Names mismatch detailed description             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'str',
        'similarity': 'float',
        'explanation': 'str'
    }

    attribute_map = {
        'category': 'category',
        'similarity': 'similarity',
        'explanation': 'explanation'
    }

    def __init__(self, category=None, similarity=None, explanation=None):
        """AiNameMismatch - a model defined in Swagger"""

        self._category = None
        self._similarity = None
        self._explanation = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if similarity is not None:
            self.similarity = similarity
        if explanation is not None:
            self.explanation = explanation

    @property
    def category(self):
        """Gets the category of this AiNameMismatch.

        Mismatch type. Enum, available values: Unknown, FirstName, MiddleName, MiddleLastName, MiddleNickname, Gender, Context

        :return: The category of this AiNameMismatch.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AiNameMismatch.

        Mismatch type. Enum, available values: Unknown, FirstName, MiddleName, MiddleLastName, MiddleNickname, Gender, Context

        :param category: The category of this AiNameMismatch.
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")
        self._category = category

    @property
    def similarity(self):
        """Gets the similarity of this AiNameMismatch.

        Similarity score             

        :return: The similarity of this AiNameMismatch.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this AiNameMismatch.

        Similarity score             

        :param similarity: The similarity of this AiNameMismatch.
        :type: float
        """
        if similarity is None:
            raise ValueError("Invalid value for `similarity`, must not be `None`")
        self._similarity = similarity

    @property
    def explanation(self):
        """Gets the explanation of this AiNameMismatch.

        Explanation or mismatch subtype             

        :return: The explanation of this AiNameMismatch.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this AiNameMismatch.

        Explanation or mismatch subtype             

        :param explanation: The explanation of this AiNameMismatch.
        :type: str
        """
        self._explanation = explanation

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
        if not isinstance(other, AiNameMismatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other