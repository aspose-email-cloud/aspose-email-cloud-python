#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MailMessageBase64.py">
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

from AsposeEmailCloudSdk.models.mail_message_base import MailMessageBase


class MailMessageBase64(MailMessageBase):
    """Email message represented as file, encoded to Base64 format.             
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
        'value_base64': 'str',
        'format': 'str'
    }

    attribute_map = {
        'discriminator': 'discriminator',
        'value_base64': 'valueBase64',
        'format': 'format'
    }

    def __init__(self, value_base64: str = None, format: str = None):
        """
        Email message represented as file, encoded to Base64 format.             
        :param value_base64: Email message file data encoded to Base64 string.             
        :type value_base64: str
        :param format: Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft
        :type format: str
        """
        super(MailMessageBase64, self).__init__()

        self._value_base64 = None
        self._format = None
        if value_base64 is not None:
            self.value_base64 = value_base64
        if format is not None:
            self.format = format


    @property
    def value_base64(self) -> str:
        """
        Email message file data encoded to Base64 string.             

        :return: The value_base64 of this MailMessageBase64.
        :rtype: str
        """
        return self._value_base64

    @value_base64.setter
    def value_base64(self, value_base64: str):
        """
        Email message file data encoded to Base64 string.             

        :param value_base64: The value_base64 of this MailMessageBase64.
        :type: str
        """
        if value_base64 is None:
            raise ValueError("Invalid value for `value_base64`, must not be `None`")
        if value_base64 is not None and len(value_base64) < 1:
            raise ValueError("Invalid value for `value_base64`, length must be greater than or equal to `1`")
        self._value_base64 = value_base64

    @property
    def format(self) -> str:
        """
        Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft

        :return: The format of this MailMessageBase64.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str):
        """
        Email document format. Enum, available values: Eml, Msg, MsgUnicode, Mhtml, Html, Tnef, Oft

        :param format: The format of this MailMessageBase64.
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")
        self._format = format

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
        if not isinstance(other, MailMessageBase64):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
