#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiPidPropertyDescriptor.py">
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


class MapiPidPropertyDescriptor(MapiPropertyDescriptor):
    """Mapi pid property descriptor base class             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'discriminator': 'str',
        'canonical_name': 'str',
        'data_type': 'str',
        'multiple_values_data_type': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'discriminator': 'discriminator',
        'canonical_name': 'canonicalName',
        'data_type': 'dataType',
        'multiple_values_data_type': 'multipleValuesDataType',
        'name': 'name'
    }

    def __init__(self, canonical_name: str = None, data_type: str = None, multiple_values_data_type: bool = None, name: str = None):
        """
        Mapi pid property descriptor base class             
        :param canonical_name: The name used to refer to the property in the documentation. The prefix of the canonical name identifies the basic characteristics of a property to the implementer. The canonical naming structure uses three categories that are denoted by the following prefixes to the canonical property name: * PidLid prefix: Properties identified by an unsigned 32-bit quantity along with a property set. * PidName prefix: Properties identified by a string name along with a property set. * PidTag prefix: Properties identified by an unsigned 16-bit quantity.             
        :type canonical_name: str
        :param data_type: [MS-OXCDATA]: Data Structures. Enum, available values: Unspecified, Null, Integer16, Integer32, Floating32, Floating64, Currency, FloatingTime, ErrorCode, Boolean, Integer64, String, String8, Time, Guid, ServerId, Restriction, RuleAction, Binary, MultipleInteger16, MultipleInteger32, MultipleFloating32, MultipleFloating64, MultipleCurrency, MultipleFloatingTime, MultipleBoolean, MultipleInteger64, MultipleString, MultipleString8, MultipleTime, MultipleGuid, MultipleBinary, Object
        :type data_type: str
        :param multiple_values_data_type: Indicates if data type contains of multiple values             
        :type multiple_values_data_type: bool
        :param name: A string that identifies the property             
        :type name: str
        """
        super(MapiPidPropertyDescriptor, self).__init__()

        self._canonical_name = None
        self._data_type = None
        self._multiple_values_data_type = None
        self._name = None
        if canonical_name is not None:
            self.canonical_name = canonical_name
        if data_type is not None:
            self.data_type = data_type
        if multiple_values_data_type is not None:
            self.multiple_values_data_type = multiple_values_data_type
        if name is not None:
            self.name = name


    @property
    def canonical_name(self) -> str:
        """
        The name used to refer to the property in the documentation. The prefix of the canonical name identifies the basic characteristics of a property to the implementer. The canonical naming structure uses three categories that are denoted by the following prefixes to the canonical property name: * PidLid prefix: Properties identified by an unsigned 32-bit quantity along with a property set. * PidName prefix: Properties identified by a string name along with a property set. * PidTag prefix: Properties identified by an unsigned 16-bit quantity.             

        :return: The canonical_name of this MapiPidPropertyDescriptor.
        :rtype: str
        """
        return self._canonical_name

    @canonical_name.setter
    def canonical_name(self, canonical_name: str):
        """
        The name used to refer to the property in the documentation. The prefix of the canonical name identifies the basic characteristics of a property to the implementer. The canonical naming structure uses three categories that are denoted by the following prefixes to the canonical property name: * PidLid prefix: Properties identified by an unsigned 32-bit quantity along with a property set. * PidName prefix: Properties identified by a string name along with a property set. * PidTag prefix: Properties identified by an unsigned 16-bit quantity.             

        :param canonical_name: The canonical_name of this MapiPidPropertyDescriptor.
        :type: str
        """
        self._canonical_name = canonical_name

    @property
    def data_type(self) -> str:
        """
        [MS-OXCDATA]: Data Structures. Enum, available values: Unspecified, Null, Integer16, Integer32, Floating32, Floating64, Currency, FloatingTime, ErrorCode, Boolean, Integer64, String, String8, Time, Guid, ServerId, Restriction, RuleAction, Binary, MultipleInteger16, MultipleInteger32, MultipleFloating32, MultipleFloating64, MultipleCurrency, MultipleFloatingTime, MultipleBoolean, MultipleInteger64, MultipleString, MultipleString8, MultipleTime, MultipleGuid, MultipleBinary, Object

        :return: The data_type of this MapiPidPropertyDescriptor.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type: str):
        """
        [MS-OXCDATA]: Data Structures. Enum, available values: Unspecified, Null, Integer16, Integer32, Floating32, Floating64, Currency, FloatingTime, ErrorCode, Boolean, Integer64, String, String8, Time, Guid, ServerId, Restriction, RuleAction, Binary, MultipleInteger16, MultipleInteger32, MultipleFloating32, MultipleFloating64, MultipleCurrency, MultipleFloatingTime, MultipleBoolean, MultipleInteger64, MultipleString, MultipleString8, MultipleTime, MultipleGuid, MultipleBinary, Object

        :param data_type: The data_type of this MapiPidPropertyDescriptor.
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")
        self._data_type = data_type

    @property
    def multiple_values_data_type(self) -> bool:
        """
        Indicates if data type contains of multiple values             

        :return: The multiple_values_data_type of this MapiPidPropertyDescriptor.
        :rtype: bool
        """
        return self._multiple_values_data_type

    @multiple_values_data_type.setter
    def multiple_values_data_type(self, multiple_values_data_type: bool):
        """
        Indicates if data type contains of multiple values             

        :param multiple_values_data_type: The multiple_values_data_type of this MapiPidPropertyDescriptor.
        :type: bool
        """
        if multiple_values_data_type is None:
            raise ValueError("Invalid value for `multiple_values_data_type`, must not be `None`")
        self._multiple_values_data_type = multiple_values_data_type

    @property
    def name(self) -> str:
        """
        A string that identifies the property             

        :return: The name of this MapiPidPropertyDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        A string that identifies the property             

        :param name: The name of this MapiPidPropertyDescriptor.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, MapiPidPropertyDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
