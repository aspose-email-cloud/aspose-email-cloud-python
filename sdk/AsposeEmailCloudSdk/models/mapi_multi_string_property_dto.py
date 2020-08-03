#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiMultiStringPropertyDto.py">
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

from AsposeEmailCloudSdk.models.mapi_property_descriptor import MapiPropertyDescriptor
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto


class MapiMultiStringPropertyDto(MapiPropertyDto):
    """Mapi property with Multiple String values             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'descriptor': 'MapiPropertyDescriptor',
        'discriminator': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'descriptor': 'descriptor',
        'discriminator': 'discriminator',
        'values': 'values'
    }

    def __init__(self, descriptor: MapiPropertyDescriptor = None, discriminator: str = None, values: List[str] = None):
        """
        Mapi property with Multiple String values             
        :param descriptor: Property descriptor             
        :type descriptor: MapiPropertyDescriptor
        :param discriminator: 
        :type discriminator: str
        :param values: Property values             
        :type values: List[str]
        """
        super(MapiMultiStringPropertyDto, self).__init__()

        self._values = None

        if descriptor is not None:
            self.descriptor = descriptor
        if discriminator is not None:
            self.discriminator = discriminator
        if values is not None:
            self.values = values

    @property
    def values(self) -> List[str]:
        """Gets the values of this MapiMultiStringPropertyDto.

        Property values             

        :return: The values of this MapiMultiStringPropertyDto.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]):
        """Sets the values of this MapiMultiStringPropertyDto.

        Property values             

        :param values: The values of this MapiMultiStringPropertyDto.
        :type: list[str]
        """
        self._values = values

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
        if not isinstance(other, MapiMultiStringPropertyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
