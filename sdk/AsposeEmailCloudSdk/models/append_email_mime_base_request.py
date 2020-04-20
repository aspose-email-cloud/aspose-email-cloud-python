#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AppendEmailMimeBaseRequest.py">
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

from AsposeEmailCloudSdk.models.append_email_account_base_request import AppendEmailAccountBaseRequest
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class AppendEmailMimeBaseRequest(AppendEmailAccountBaseRequest):
    """Append email from MIME string to account request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_account': 'str',
        'second_account': 'str',
        'storage_folder': 'StorageFolderLocation',
        'folder': 'str',
        'mark_as_sent': 'bool',
        'base64_mime_message': 'str'
    }

    attribute_map = {
        'first_account': 'firstAccount',
        'second_account': 'secondAccount',
        'storage_folder': 'storageFolder',
        'folder': 'folder',
        'mark_as_sent': 'markAsSent',
        'base64_mime_message': 'base64MimeMessage'
    }

    def __init__(self, first_account: str = None, second_account: str = None, storage_folder: StorageFolderLocation = None, folder: str = None, mark_as_sent: bool = None, base64_mime_message: str = None):
        """
        Append email from MIME string to account request             
        :param first_account (str) First account storage file name             
        :param second_account (str) Additional email account (for example, FirstAccount could be IMAP, and second one could be SMTP)             
        :param storage_folder (StorageFolderLocation) Storage folder location of account files             
        :param folder (str) Email account folder to store a message             
        :param mark_as_sent (bool) Mark message as sent             
        :param base64_mime_message (str) Email document serialized as MIME string             
        """
        super(AppendEmailMimeBaseRequest, self).__init__()

        self._base64_mime_message = None

        if first_account is not None:
            self.first_account = first_account
        if second_account is not None:
            self.second_account = second_account
        if storage_folder is not None:
            self.storage_folder = storage_folder
        if folder is not None:
            self.folder = folder
        if mark_as_sent is not None:
            self.mark_as_sent = mark_as_sent
        if base64_mime_message is not None:
            self.base64_mime_message = base64_mime_message

    @property
    def base64_mime_message(self) -> str:
        """Gets the base64_mime_message of this AppendEmailMimeBaseRequest.

        Email document serialized as MIME string             

        :return: The base64_mime_message of this AppendEmailMimeBaseRequest.
        :rtype: str
        """
        return self._base64_mime_message

    @base64_mime_message.setter
    def base64_mime_message(self, base64_mime_message: str):
        """Sets the base64_mime_message of this AppendEmailMimeBaseRequest.

        Email document serialized as MIME string             

        :param base64_mime_message: The base64_mime_message of this AppendEmailMimeBaseRequest.
        :type: str
        """
        if base64_mime_message is None:
            raise ValueError("Invalid value for `base64_mime_message`, must not be `None`")
        if base64_mime_message is not None and len(base64_mime_message) < 1:
            raise ValueError("Invalid value for `base64_mime_message`, length must be greater than or equal to `1`")
        self._base64_mime_message = base64_mime_message

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
        if not isinstance(other, AppendEmailMimeBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
