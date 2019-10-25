#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="SetMessageReadFlagAccountBaseRequest.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

from AsposeEmailCloudSdk.models.account_base_request import AccountBaseRequest
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class SetMessageReadFlagAccountBaseRequest(AccountBaseRequest):
    """Set message is read request
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'message_id': 'str',
        'is_read': 'bool'
    }

    attribute_map = {
        'message_id': 'MessageId',
        'is_read': 'IsRead'
    }

    def __init__(self, message_id=None, is_read=None):
        """SetMessageReadFlagAccountBaseRequest - a model defined in Swagger"""

        self._message_id = None
        self._is_read = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if is_read is not None:
            self.is_read = is_read

    @property
    def message_id(self):
        """Gets the message_id of this SetMessageReadFlagAccountBaseRequest.

        Message identifier

        :return: The message_id of this SetMessageReadFlagAccountBaseRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this SetMessageReadFlagAccountBaseRequest.

        Message identifier

        :param message_id: The message_id of this SetMessageReadFlagAccountBaseRequest.
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")
        if message_id is not None and len(message_id) < 1:
            raise ValueError("Invalid value for `message_id`, length must be greater than or equal to `1`")
        self._message_id = message_id

    @property
    def is_read(self):
        """Gets the is_read of this SetMessageReadFlagAccountBaseRequest.

        Specifies that message should be marked read or unread

        :return: The is_read of this SetMessageReadFlagAccountBaseRequest.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this SetMessageReadFlagAccountBaseRequest.

        Specifies that message should be marked read or unread

        :param is_read: The is_read of this SetMessageReadFlagAccountBaseRequest.
        :type: bool
        """
        if is_read is None:
            raise ValueError("Invalid value for `is_read`, must not be `None`")
        self._is_read = is_read

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
        if not isinstance(other, SetMessageReadFlagAccountBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
