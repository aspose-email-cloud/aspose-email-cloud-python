#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="BaseObject.py">
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


class BaseObject(object):
    """Base property object
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'PrimitiveObject': 'PrimitiveObject',
        'IndexedHierarchicalObject': 'IndexedHierarchicalObject',
        'HierarchicalObject': 'HierarchicalObject',
        'IndexedPrimitiveObject': 'IndexedPrimitiveObject'
    }

    def __init__(self, name=None, type=None):
        """BaseObject - a model defined in Swagger"""

        self._name = None
        self._type = self.__class__.__name__
        self.discriminator = 'Type'

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this BaseObject.

        Gets or sets the name of an object.

        :return: The name of this BaseObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseObject.

        Gets or sets the name of an object.

        :param name: The name of this BaseObject.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this BaseObject.

        Property type. Used for deserialization purposes

        :return: The type of this BaseObject.
        :rtype: str
        """
        return self.__class__.__name__

    @type.setter
    def type(self, type):
        """Sets the type of this BaseObject.

        Property type. Used for deserialization purposes

        :param type: The type of this BaseObject.
        :type: str
        """
        self._type = self.__class__.__name__

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
        if not isinstance(other, BaseObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
