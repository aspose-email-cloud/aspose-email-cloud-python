#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="LinkedResource.py">
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

from AsposeEmailCloudSdk.models.attachment_base import AttachmentBase
from AsposeEmailCloudSdk.models.content_type import ContentType


class LinkedResource(AttachmentBase):
    """Represents an embedded resource in a message.             
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
        'headers': 'dict(str, str)',
        'content_link': 'str'
    }

    attribute_map = {
        'base64_data': 'base64Data',
        'content_id': 'contentId',
        'content_type': 'contentType',
        'headers': 'headers',
        'content_link': 'contentLink'
    }

    def __init__(self, base64_data: str = None, content_id: str = None, content_type: ContentType = None, headers: Dict[str, str] = None, content_link: str = None):
        """
        Represents an embedded resource in a message.             
        :param base64_data: Attachment file content as Base64 string.             
        :type base64_data: str
        :param content_id: Attachment content id             
        :type content_id: str
        :param content_type: Content type             
        :type content_type: ContentType
        :param headers: Attachment headers.             
        :type headers: Dict[str, str]
        :param content_link: URI that the resource must match.             
        :type content_link: str
        """
        super(LinkedResource, self).__init__()

        self._content_link = None

        if base64_data is not None:
            self.base64_data = base64_data
        if content_id is not None:
            self.content_id = content_id
        if content_type is not None:
            self.content_type = content_type
        if headers is not None:
            self.headers = headers
        if content_link is not None:
            self.content_link = content_link


    @property
    def content_link(self) -> str:
        """
        URI that the resource must match.             

        :return: The content_link of this LinkedResource.
        :rtype: str
        """
        return self._content_link

    @content_link.setter
    def content_link(self, content_link: str):
        """
        URI that the resource must match.             

        :param content_link: The content_link of this LinkedResource.
        :type: str
        """
        self._content_link = content_link

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
        if not isinstance(other, LinkedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
