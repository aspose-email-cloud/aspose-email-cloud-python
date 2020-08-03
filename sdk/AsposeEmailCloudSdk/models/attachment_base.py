#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AttachmentBase.py">
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

from AsposeEmailCloudSdk.models.content_type import ContentType


class AttachmentBase(object):
    """AttachmentBase class             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base64_data': 'str',
        'content_id': 'str',
        'content_type': 'ContentType',
        'headers': 'dict(str, str)'
    }

    attribute_map = {
        'base64_data': 'base64Data',
        'content_id': 'contentId',
        'content_type': 'contentType',
        'headers': 'headers'
    }

    def __init__(self, base64_data: str = None, content_id: str = None, content_type: ContentType = None, headers: Dict[str, str] = None):
        """
        AttachmentBase class             
        :param base64_data: Attachment file content as Base64 string.             
        :type base64_data: str
        :param content_id: Attachment content id             
        :type content_id: str
        :param content_type: Content type             
        :type content_type: ContentType
        :param headers: Attachment headers.             
        :type headers: Dict[str, str]
        """

        self._base64_data = None
        self._content_id = None
        self._content_type = None
        self._headers = None

        if base64_data is not None:
            self.base64_data = base64_data
        if content_id is not None:
            self.content_id = content_id
        if content_type is not None:
            self.content_type = content_type
        if headers is not None:
            self.headers = headers


    @property
    def base64_data(self) -> str:
        """
        Attachment file content as Base64 string.             

        :return: The base64_data of this AttachmentBase.
        :rtype: str
        """
        return self._base64_data

    @base64_data.setter
    def base64_data(self, base64_data: str):
        """
        Attachment file content as Base64 string.             

        :param base64_data: The base64_data of this AttachmentBase.
        :type: str
        """
        self._base64_data = base64_data

    @property
    def content_id(self) -> str:
        """
        Attachment content id             

        :return: The content_id of this AttachmentBase.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id: str):
        """
        Attachment content id             

        :param content_id: The content_id of this AttachmentBase.
        :type: str
        """
        self._content_id = content_id

    @property
    def content_type(self) -> ContentType:
        """
        Content type             

        :return: The content_type of this AttachmentBase.
        :rtype: ContentType
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: ContentType):
        """
        Content type             

        :param content_type: The content_type of this AttachmentBase.
        :type: ContentType
        """
        self._content_type = content_type

    @property
    def headers(self) -> Dict[str, str]:
        """
        Attachment headers.             

        :return: The headers of this AttachmentBase.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, str]):
        """
        Attachment headers.             

        :param headers: The headers of this AttachmentBase.
        :type: dict(str, str)
        """
        self._headers = headers

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
        if not isinstance(other, AttachmentBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
