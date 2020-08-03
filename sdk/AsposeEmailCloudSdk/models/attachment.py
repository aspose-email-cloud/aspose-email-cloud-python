#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="Attachment.py">
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


class Attachment(AttachmentBase):
    """Document attachment.             
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
        'content_disposition': 'str',
        'is_embedded_message': 'bool',
        'name': 'str',
        'name_encoding': 'str',
        'preferred_text_encoding': 'str'
    }

    attribute_map = {
        'base64_data': 'base64Data',
        'content_id': 'contentId',
        'content_type': 'contentType',
        'headers': 'headers',
        'content_disposition': 'contentDisposition',
        'is_embedded_message': 'isEmbeddedMessage',
        'name': 'name',
        'name_encoding': 'nameEncoding',
        'preferred_text_encoding': 'preferredTextEncoding'
    }

    def __init__(self, base64_data: str = None, content_id: str = None, content_type: ContentType = None, headers: Dict[str, str] = None, content_disposition: str = None, is_embedded_message: bool = None, name: str = None, name_encoding: str = None, preferred_text_encoding: str = None):
        """
        Document attachment.             
        :param base64_data: Attachment file content as Base64 string.             
        :type base64_data: str
        :param content_id: Attachment content id             
        :type content_id: str
        :param content_type: Content type             
        :type content_type: ContentType
        :param headers: Attachment headers.             
        :type headers: Dict[str, str]
        :param content_disposition: Content-Disposition header. Read only.             
        :type content_disposition: str
        :param is_embedded_message: Determines if attachment is an embedded message. Read only.             
        :type is_embedded_message: bool
        :param name: Attachment name.             
        :type name: str
        :param name_encoding: Encoding of attachment name.             
        :type name_encoding: str
        :param preferred_text_encoding: Preferred text encoding.             
        :type preferred_text_encoding: str
        """
        super(Attachment, self).__init__()

        self._content_disposition = None
        self._is_embedded_message = None
        self._name = None
        self._name_encoding = None
        self._preferred_text_encoding = None

        if base64_data is not None:
            self.base64_data = base64_data
        if content_id is not None:
            self.content_id = content_id
        if content_type is not None:
            self.content_type = content_type
        if headers is not None:
            self.headers = headers
        if content_disposition is not None:
            self.content_disposition = content_disposition
        if is_embedded_message is not None:
            self.is_embedded_message = is_embedded_message
        if name is not None:
            self.name = name
        if name_encoding is not None:
            self.name_encoding = name_encoding
        if preferred_text_encoding is not None:
            self.preferred_text_encoding = preferred_text_encoding


    @property
    def content_disposition(self) -> str:
        """
        Content-Disposition header. Read only.             

        :return: The content_disposition of this Attachment.
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition: str):
        """
        Content-Disposition header. Read only.             

        :param content_disposition: The content_disposition of this Attachment.
        :type: str
        """
        self._content_disposition = content_disposition

    @property
    def is_embedded_message(self) -> bool:
        """
        Determines if attachment is an embedded message. Read only.             

        :return: The is_embedded_message of this Attachment.
        :rtype: bool
        """
        return self._is_embedded_message

    @is_embedded_message.setter
    def is_embedded_message(self, is_embedded_message: bool):
        """
        Determines if attachment is an embedded message. Read only.             

        :param is_embedded_message: The is_embedded_message of this Attachment.
        :type: bool
        """
        if is_embedded_message is None:
            raise ValueError("Invalid value for `is_embedded_message`, must not be `None`")
        self._is_embedded_message = is_embedded_message

    @property
    def name(self) -> str:
        """
        Attachment name.             

        :return: The name of this Attachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Attachment name.             

        :param name: The name of this Attachment.
        :type: str
        """
        self._name = name

    @property
    def name_encoding(self) -> str:
        """
        Encoding of attachment name.             

        :return: The name_encoding of this Attachment.
        :rtype: str
        """
        return self._name_encoding

    @name_encoding.setter
    def name_encoding(self, name_encoding: str):
        """
        Encoding of attachment name.             

        :param name_encoding: The name_encoding of this Attachment.
        :type: str
        """
        self._name_encoding = name_encoding

    @property
    def preferred_text_encoding(self) -> str:
        """
        Preferred text encoding.             

        :return: The preferred_text_encoding of this Attachment.
        :rtype: str
        """
        return self._preferred_text_encoding

    @preferred_text_encoding.setter
    def preferred_text_encoding(self, preferred_text_encoding: str):
        """
        Preferred text encoding.             

        :param preferred_text_encoding: The preferred_text_encoding of this Attachment.
        :type: str
        """
        self._preferred_text_encoding = preferred_text_encoding

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
        if not isinstance(other, Attachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
