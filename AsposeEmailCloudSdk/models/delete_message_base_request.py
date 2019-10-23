#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="DeleteMessageBaseRequest.py">
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
from AsposeEmailCloudSdk.models.storage_folder import StorageFolder


class DeleteMessageBaseRequest(AccountBaseRequest):
    """Delete message request
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
        'delete_permanently': 'bool'
    }

    attribute_map = {
        'message_id': 'MessageId',
        'delete_permanently': 'DeletePermanently'
    }

    def __init__(self, message_id=None, delete_permanently=None):
        """DeleteMessageBaseRequest - a model defined in Swagger"""

        self._message_id = None
        self._delete_permanently = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if delete_permanently is not None:
            self.delete_permanently = delete_permanently

    @property
    def message_id(self):
        """Gets the message_id of this DeleteMessageBaseRequest.

        Message identifier

        :return: The message_id of this DeleteMessageBaseRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this DeleteMessageBaseRequest.

        Message identifier

        :param message_id: The message_id of this DeleteMessageBaseRequest.
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")
        if message_id is not None and len(message_id) < 1:
            raise ValueError("Invalid value for `message_id`, length must be greater than or equal to `1`")
        self._message_id = message_id

    @property
    def delete_permanently(self):
        """Gets the delete_permanently of this DeleteMessageBaseRequest.

        Specifies that message should be deleted permanently

        :return: The delete_permanently of this DeleteMessageBaseRequest.
        :rtype: bool
        """
        return self._delete_permanently

    @delete_permanently.setter
    def delete_permanently(self, delete_permanently):
        """Sets the delete_permanently of this DeleteMessageBaseRequest.

        Specifies that message should be deleted permanently

        :param delete_permanently: The delete_permanently of this DeleteMessageBaseRequest.
        :type: bool
        """
        if delete_permanently is None:
            raise ValueError("Invalid value for `delete_permanently`, must not be `None`")
        self._delete_permanently = delete_permanently

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
        if not isinstance(other, DeleteMessageBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
