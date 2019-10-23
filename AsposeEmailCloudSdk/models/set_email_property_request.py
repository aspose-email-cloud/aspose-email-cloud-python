#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="SetEmailPropertyRequest.py">
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

from AsposeEmailCloudSdk.models.email_property import EmailProperty
from AsposeEmailCloudSdk.models.storage_folder import StorageFolder


class SetEmailPropertyRequest(object):
    """Update email document property request
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email_property': 'EmailProperty',
        'storage_folder': 'StorageFolder'
    }

    attribute_map = {
        'email_property': 'EmailProperty',
        'storage_folder': 'StorageFolder'
    }

    def __init__(self, email_property=None, storage_folder=None):
        """SetEmailPropertyRequest - a model defined in Swagger"""

        self._email_property = None
        self._storage_folder = None
        self.discriminator = None

        if email_property is not None:
            self.email_property = email_property
        if storage_folder is not None:
            self.storage_folder = storage_folder

    @property
    def email_property(self):
        """Gets the email_property of this SetEmailPropertyRequest.

        An email property that should be updated

        :return: The email_property of this SetEmailPropertyRequest.
        :rtype: EmailProperty
        """
        return self._email_property

    @email_property.setter
    def email_property(self, email_property):
        """Sets the email_property of this SetEmailPropertyRequest.

        An email property that should be updated

        :param email_property: The email_property of this SetEmailPropertyRequest.
        :type: EmailProperty
        """
        if email_property is None:
            raise ValueError("Invalid value for `email_property`, must not be `None`")
        self._email_property = email_property

    @property
    def storage_folder(self):
        """Gets the storage_folder of this SetEmailPropertyRequest.

        An email document location in storage

        :return: The storage_folder of this SetEmailPropertyRequest.
        :rtype: StorageFolder
        """
        return self._storage_folder

    @storage_folder.setter
    def storage_folder(self, storage_folder):
        """Sets the storage_folder of this SetEmailPropertyRequest.

        An email document location in storage

        :param storage_folder: The storage_folder of this SetEmailPropertyRequest.
        :type: StorageFolder
        """
        self._storage_folder = storage_folder

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
        if not isinstance(other, SetEmailPropertyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
