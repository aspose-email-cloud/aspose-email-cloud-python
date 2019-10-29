#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="IndexedHierarchicalObject.py">
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

from AsposeEmailCloudSdk.models.base_object import BaseObject


class IndexedHierarchicalObject(BaseObject):
    """Indexed hierarchical property
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'index': 'int',
        'internal_properties': 'list[BaseObject]'
    }

    attribute_map = {
        'index': 'index',
        'internal_properties': 'internalProperties'
    }

    def __init__(self, index=None, internal_properties=None):
        """IndexedHierarchicalObject - a model defined in Swagger"""

        self._index = None
        self._internal_properties = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if internal_properties is not None:
            self.internal_properties = internal_properties

    @property
    def index(self):
        """Gets the index of this IndexedHierarchicalObject.

        Index of property in list

        :return: The index of this IndexedHierarchicalObject.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IndexedHierarchicalObject.

        Index of property in list

        :param index: The index of this IndexedHierarchicalObject.
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")
        self._index = index

    @property
    def internal_properties(self):
        """Gets the internal_properties of this IndexedHierarchicalObject.

        List of internal properties

        :return: The internal_properties of this IndexedHierarchicalObject.
        :rtype: list[BaseObject]
        """
        return self._internal_properties

    @internal_properties.setter
    def internal_properties(self, internal_properties):
        """Sets the internal_properties of this IndexedHierarchicalObject.

        List of internal properties

        :param internal_properties: The internal_properties of this IndexedHierarchicalObject.
        :type: list[BaseObject]
        """
        self._internal_properties = internal_properties

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
        if not isinstance(other, IndexedHierarchicalObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
