#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ContentType.py">
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

from AsposeEmailCloudSdk.models.content_type_parameter import ContentTypeParameter


class ContentType(object):
    """Represents a Content-Type header.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'boundary': 'str',
        'char_set': 'str',
        'media_type': 'str',
        'name': 'str',
        'parameters': 'list[ContentTypeParameter]'
    }

    attribute_map = {
        'boundary': 'boundary',
        'char_set': 'charSet',
        'media_type': 'mediaType',
        'name': 'name',
        'parameters': 'parameters'
    }

    def __init__(self, boundary: str = None, char_set: str = None, media_type: str = None, name: str = None, parameters: List[ContentTypeParameter] = None):
        """
        Represents a Content-Type header.             
        :param boundary: The boundary parameter included in the Content-Type header.             
        :type boundary: str
        :param char_set: CharSet parameter.             
        :type char_set: str
        :param media_type: The internet media type.             
        :type media_type: str
        :param name: Name parameter.             
        :type name: str
        :param parameters: Full list of parameters             
        :type parameters: List[ContentTypeParameter]
        """

        self._boundary = None
        self._char_set = None
        self._media_type = None
        self._name = None
        self._parameters = None

        if boundary is not None:
            self.boundary = boundary
        if char_set is not None:
            self.char_set = char_set
        if media_type is not None:
            self.media_type = media_type
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters


    @property
    def boundary(self) -> str:
        """
        The boundary parameter included in the Content-Type header.             

        :return: The boundary of this ContentType.
        :rtype: str
        """
        return self._boundary

    @boundary.setter
    def boundary(self, boundary: str):
        """
        The boundary parameter included in the Content-Type header.             

        :param boundary: The boundary of this ContentType.
        :type: str
        """
        self._boundary = boundary

    @property
    def char_set(self) -> str:
        """
        CharSet parameter.             

        :return: The char_set of this ContentType.
        :rtype: str
        """
        return self._char_set

    @char_set.setter
    def char_set(self, char_set: str):
        """
        CharSet parameter.             

        :param char_set: The char_set of this ContentType.
        :type: str
        """
        self._char_set = char_set

    @property
    def media_type(self) -> str:
        """
        The internet media type.             

        :return: The media_type of this ContentType.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str):
        """
        The internet media type.             

        :param media_type: The media_type of this ContentType.
        :type: str
        """
        self._media_type = media_type

    @property
    def name(self) -> str:
        """
        Name parameter.             

        :return: The name of this ContentType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Name parameter.             

        :param name: The name of this ContentType.
        :type: str
        """
        self._name = name

    @property
    def parameters(self) -> List[ContentTypeParameter]:
        """
        Full list of parameters             

        :return: The parameters of this ContentType.
        :rtype: list[ContentTypeParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[ContentTypeParameter]):
        """
        Full list of parameters             

        :param parameters: The parameters of this ContentType.
        :type: list[ContentTypeParameter]
        """
        self._parameters = parameters

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
        if not isinstance(other, ContentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
