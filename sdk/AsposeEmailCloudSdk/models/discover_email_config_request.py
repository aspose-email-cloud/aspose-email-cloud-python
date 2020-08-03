#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="DiscoverEmailConfigRequest.py">
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


class DiscoverEmailConfigRequest(object):
    """Discover email configuration request.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'fast_processing': 'bool',
        'login': 'str'
    }

    attribute_map = {
        'address': 'address',
        'fast_processing': 'fastProcessing',
        'login': 'login'
    }

    def __init__(self, address: str = None, fast_processing: bool = None, login: str = None):
        """
        Discover email configuration request.             
        :param address: Email address to discover.             
        :type address: str
        :param fast_processing: Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.             
        :type fast_processing: bool
        :param login: Email account login. If not specified, address used as a login.             
        :type login: str
        """

        self._address = None
        self._fast_processing = None
        self._login = None

        if address is not None:
            self.address = address
        if fast_processing is not None:
            self.fast_processing = fast_processing
        if login is not None:
            self.login = login


    @property
    def address(self) -> str:
        """
        Email address to discover.             

        :return: The address of this DiscoverEmailConfigRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """
        Email address to discover.             

        :param address: The address of this DiscoverEmailConfigRequest.
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")
        if address is not None and len(address) < 1:
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `1`")
        self._address = address

    @property
    def fast_processing(self) -> bool:
        """
        Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.             

        :return: The fast_processing of this DiscoverEmailConfigRequest.
        :rtype: bool
        """
        return self._fast_processing

    @fast_processing.setter
    def fast_processing(self, fast_processing: bool):
        """
        Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.             

        :param fast_processing: The fast_processing of this DiscoverEmailConfigRequest.
        :type: bool
        """
        if fast_processing is None:
            raise ValueError("Invalid value for `fast_processing`, must not be `None`")
        self._fast_processing = fast_processing

    @property
    def login(self) -> str:
        """
        Email account login. If not specified, address used as a login.             

        :return: The login of this DiscoverEmailConfigRequest.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """
        Email account login. If not specified, address used as a login.             

        :param login: The login of this DiscoverEmailConfigRequest.
        :type: str
        """
        self._login = login

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
        if not isinstance(other, DiscoverEmailConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
