#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactPhysicalAddressPropertySetDto.py">
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

from AsposeEmailCloudSdk.models.mapi_contact_physical_address_dto import MapiContactPhysicalAddressDto


class MapiContactPhysicalAddressPropertySetDto(object):
    """Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'work_address': 'MapiContactPhysicalAddressDto',
        'home_address': 'MapiContactPhysicalAddressDto',
        'other_address': 'MapiContactPhysicalAddressDto'
    }

    attribute_map = {
        'work_address': 'workAddress',
        'home_address': 'homeAddress',
        'other_address': 'otherAddress'
    }

    def __init__(self, work_address: MapiContactPhysicalAddressDto = None, home_address: MapiContactPhysicalAddressDto = None, other_address: MapiContactPhysicalAddressDto = None):
        """
        Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address             
        :param work_address: Specifies the address of the contact's work             
        :type work_address: MapiContactPhysicalAddressDto
        :param home_address: Specifies the address of the contact's home             
        :type home_address: MapiContactPhysicalAddressDto
        :param other_address: Specifies the other contact's address             
        :type other_address: MapiContactPhysicalAddressDto
        """

        self._work_address = None
        self._home_address = None
        self._other_address = None

        if work_address is not None:
            self.work_address = work_address
        if home_address is not None:
            self.home_address = home_address
        if other_address is not None:
            self.other_address = other_address


    @property
    def work_address(self) -> MapiContactPhysicalAddressDto:
        """
        Specifies the address of the contact's work             

        :return: The work_address of this MapiContactPhysicalAddressPropertySetDto.
        :rtype: MapiContactPhysicalAddressDto
        """
        return self._work_address

    @work_address.setter
    def work_address(self, work_address: MapiContactPhysicalAddressDto):
        """
        Specifies the address of the contact's work             

        :param work_address: The work_address of this MapiContactPhysicalAddressPropertySetDto.
        :type: MapiContactPhysicalAddressDto
        """
        self._work_address = work_address

    @property
    def home_address(self) -> MapiContactPhysicalAddressDto:
        """
        Specifies the address of the contact's home             

        :return: The home_address of this MapiContactPhysicalAddressPropertySetDto.
        :rtype: MapiContactPhysicalAddressDto
        """
        return self._home_address

    @home_address.setter
    def home_address(self, home_address: MapiContactPhysicalAddressDto):
        """
        Specifies the address of the contact's home             

        :param home_address: The home_address of this MapiContactPhysicalAddressPropertySetDto.
        :type: MapiContactPhysicalAddressDto
        """
        self._home_address = home_address

    @property
    def other_address(self) -> MapiContactPhysicalAddressDto:
        """
        Specifies the other contact's address             

        :return: The other_address of this MapiContactPhysicalAddressPropertySetDto.
        :rtype: MapiContactPhysicalAddressDto
        """
        return self._other_address

    @other_address.setter
    def other_address(self, other_address: MapiContactPhysicalAddressDto):
        """
        Specifies the other contact's address             

        :param other_address: The other_address of this MapiContactPhysicalAddressPropertySetDto.
        :type: MapiContactPhysicalAddressDto
        """
        self._other_address = other_address

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
        if not isinstance(other, MapiContactPhysicalAddressPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
