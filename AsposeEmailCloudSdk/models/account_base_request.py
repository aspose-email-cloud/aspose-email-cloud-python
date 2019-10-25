#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AccountBaseRequest.py">
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

from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class AccountBaseRequest(object):
    """
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
        'storage_folder': 'StorageFolderLocation'
    }

    attribute_map = {
        'first_account': 'FirstAccount',
        'second_account': 'SecondAccount',
        'storage_folder': 'StorageFolder'
    }

    discriminator_value_class_map = {
        'DeleteFolderBaseRequest': 'DeleteFolderBaseRequest',
        'AppendEmailAccountBaseRequest': 'AppendEmailAccountBaseRequest',
        'SendEmailMimeBaseRequest': 'SendEmailMimeBaseRequest',
        'SendEmailBaseRequest': 'SendEmailBaseRequest',
        'DeleteMessageBaseRequest': 'DeleteMessageBaseRequest',
        'AppendEmailBaseRequest': 'AppendEmailBaseRequest',
        'SetMessageReadFlagAccountBaseRequest': 'SetMessageReadFlagAccountBaseRequest',
        'AppendEmailMimeBaseRequest': 'AppendEmailMimeBaseRequest',
        'CreateFolderBaseRequest': 'CreateFolderBaseRequest'
    }

    def __init__(self, first_account=None, second_account=None, storage_folder=None):
        """AccountBaseRequest - a model defined in Swagger"""

        self._first_account = None
        self._second_account = None
        self._storage_folder = None
        self.discriminator = 'Type'

        if first_account is not None:
            self.first_account = first_account
        if second_account is not None:
            self.second_account = second_account
        if storage_folder is not None:
            self.storage_folder = storage_folder

    @property
    def first_account(self):
        """Gets the first_account of this AccountBaseRequest.


        :return: The first_account of this AccountBaseRequest.
        :rtype: str
        """
        return self._first_account

    @first_account.setter
    def first_account(self, first_account):
        """Sets the first_account of this AccountBaseRequest.


        :param first_account: The first_account of this AccountBaseRequest.
        :type: str
        """
        if first_account is None:
            raise ValueError("Invalid value for `first_account`, must not be `None`")
        if first_account is not None and len(first_account) < 1:
            raise ValueError("Invalid value for `first_account`, length must be greater than or equal to `1`")
        self._first_account = first_account

    @property
    def second_account(self):
        """Gets the second_account of this AccountBaseRequest.


        :return: The second_account of this AccountBaseRequest.
        :rtype: str
        """
        return self._second_account

    @second_account.setter
    def second_account(self, second_account):
        """Sets the second_account of this AccountBaseRequest.


        :param second_account: The second_account of this AccountBaseRequest.
        :type: str
        """
        self._second_account = second_account

    @property
    def storage_folder(self):
        """Gets the storage_folder of this AccountBaseRequest.


        :return: The storage_folder of this AccountBaseRequest.
        :rtype: StorageFolderLocation
        """
        return self._storage_folder

    @storage_folder.setter
    def storage_folder(self, storage_folder):
        """Sets the storage_folder of this AccountBaseRequest.


        :param storage_folder: The storage_folder of this AccountBaseRequest.
        :type: StorageFolderLocation
        """
        self._storage_folder = storage_folder

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, AccountBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
