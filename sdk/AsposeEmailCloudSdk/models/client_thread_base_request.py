#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ClientThreadBaseRequest.py">
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

from AsposeEmailCloudSdk.models.client_account_base_request import ClientAccountBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class ClientThreadBaseRequest(ClientAccountBaseRequest):
    """Email client thread request.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_location': 'StorageFileLocation',
        'thread_id': 'str'
    }

    attribute_map = {
        'account_location': 'accountLocation',
        'thread_id': 'threadId'
    }

    def __init__(self, account_location: StorageFileLocation = None, thread_id: str = None):
        """
        Email client thread request.             
        :param account_location: Email client account configuration location on storage.             
        :type account_location: StorageFileLocation
        :param thread_id: Thread identifier.             
        :type thread_id: str
        """
        super(ClientThreadBaseRequest, self).__init__()

        self._thread_id = None

        if account_location is not None:
            self.account_location = account_location
        if thread_id is not None:
            self.thread_id = thread_id


    @property
    def thread_id(self) -> str:
        """
        Thread identifier.             

        :return: The thread_id of this ClientThreadBaseRequest.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id: str):
        """
        Thread identifier.             

        :param thread_id: The thread_id of this ClientThreadBaseRequest.
        :type: str
        """
        if thread_id is None:
            raise ValueError("Invalid value for `thread_id`, must not be `None`")
        if thread_id is not None and len(thread_id) < 1:
            raise ValueError("Invalid value for `thread_id`, length must be greater than or equal to `1`")
        self._thread_id = thread_id

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
        if not isinstance(other, ClientThreadBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
