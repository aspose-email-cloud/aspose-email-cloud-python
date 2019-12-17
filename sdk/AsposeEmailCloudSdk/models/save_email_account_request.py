#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="SaveEmailAccountRequest.py">
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

from AsposeEmailCloudSdk.models.email_account_request import EmailAccountRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class SaveEmailAccountRequest(EmailAccountRequest):
    """Save email account settings with login/password authentication request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'host': 'str',
        'port': 'int',
        'login': 'str',
        'security_options': 'str',
        'protocol_type': 'str',
        'description': 'str',
        'storage_file': 'StorageFileLocation',
        'password': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'login': 'login',
        'security_options': 'securityOptions',
        'protocol_type': 'protocolType',
        'description': 'description',
        'storage_file': 'storageFile',
        'password': 'password'
    }

    def __init__(self, host=None, port=None, login=None, security_options=None, protocol_type=None, description=None, storage_file=None, password=None):
        """SaveEmailAccountRequest - a model defined in Swagger"""
        super(SaveEmailAccountRequest, self).__init__()

        self._password = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if login is not None:
            self.login = login
        if security_options is not None:
            self.security_options = security_options
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if description is not None:
            self.description = description
        if storage_file is not None:
            self.storage_file = storage_file
        if password is not None:
            self.password = password

    @property
    def password(self):
        """Gets the password of this SaveEmailAccountRequest.

        Email account password             

        :return: The password of this SaveEmailAccountRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SaveEmailAccountRequest.

        Email account password             

        :param password: The password of this SaveEmailAccountRequest.
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")
        self._password = password

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
        if not isinstance(other, SaveEmailAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other