#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiAttachmentDto.py">
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


class MapiAttachmentDto(object):
    """Mapi attachment             
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
        'data_base64': 'str'
    }

    attribute_map = {
        'name': 'name',
        'data_base64': 'dataBase64'
    }

    def __init__(self, name: str = None, data_base64: str = None):
        """
        Mapi attachment             
        :param name: Attachment's name             
        :type name: str
        :param data_base64: Attachment data represented as Base64 string.             
        :type data_base64: str
        """

        self._name = None
        self._data_base64 = None

        if name is not None:
            self.name = name
        if data_base64 is not None:
            self.data_base64 = data_base64


    @property
    def name(self) -> str:
        """
        Attachment's name             

        :return: The name of this MapiAttachmentDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Attachment's name             

        :param name: The name of this MapiAttachmentDto.
        :type: str
        """
        self._name = name

    @property
    def data_base64(self) -> str:
        """
        Attachment data represented as Base64 string.             

        :return: The data_base64 of this MapiAttachmentDto.
        :rtype: str
        """
        return self._data_base64

    @data_base64.setter
    def data_base64(self, data_base64: str):
        """
        Attachment data represented as Base64 string.             

        :param data_base64: The data_base64 of this MapiAttachmentDto.
        :type: str
        """
        self._data_base64 = data_base64

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
        if not isinstance(other, MapiAttachmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
