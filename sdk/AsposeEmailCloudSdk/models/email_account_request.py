#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailAccountRequest.py">
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
from typing import List, Set, Dict, Tuple, Optional
from datetime import datetime

from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class EmailAccountRequest(object):
    """Email account settings request             
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
        'storage_file': 'StorageFileLocation'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'login': 'login',
        'security_options': 'securityOptions',
        'protocol_type': 'protocolType',
        'description': 'description',
        'storage_file': 'storageFile'
    }

    discriminator_value_class_map = {
        'SaveEmailAccountRequest': 'SaveEmailAccountRequest',
        'SaveOAuthEmailAccountRequest': 'SaveOAuthEmailAccountRequest'
    }

    def __init__(self, host: str = None, port: int = None, login: str = None, security_options: str = None, protocol_type: str = None, description: str = None, storage_file: StorageFileLocation = None):
        """EmailAccountRequest - a model defined in Swagger"""

        self._host = None
        self._port = None
        self._login = None
        self._security_options = None
        self._protocol_type = None
        self._description = None
        self._storage_file = None
        self.discriminator = 'Type'

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

    @property
    def host(self) -> str:
        """Gets the host of this EmailAccountRequest.

        Email account host             

        :return: The host of this EmailAccountRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this EmailAccountRequest.

        Email account host             

        :param host: The host of this EmailAccountRequest.
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")
        if host is not None and len(host) < 1:
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `1`")
        self._host = host

    @property
    def port(self) -> int:
        """Gets the port of this EmailAccountRequest.

        Email account port             

        :return: The port of this EmailAccountRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this EmailAccountRequest.

        Email account port             

        :param port: The port of this EmailAccountRequest.
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")
        self._port = port

    @property
    def login(self) -> str:
        """Gets the login of this EmailAccountRequest.

        Email account login             

        :return: The login of this EmailAccountRequest.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """Sets the login of this EmailAccountRequest.

        Email account login             

        :param login: The login of this EmailAccountRequest.
        :type: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")
        if login is not None and len(login) < 1:
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `1`")
        self._login = login

    @property
    def security_options(self) -> str:
        """Gets the security_options of this EmailAccountRequest.

        Security mode for a mail client Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :return: The security_options of this EmailAccountRequest.
        :rtype: str
        """
        return self._security_options

    @security_options.setter
    def security_options(self, security_options: str):
        """Sets the security_options of this EmailAccountRequest.

        Security mode for a mail client Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :param security_options: The security_options of this EmailAccountRequest.
        :type: str
        """
        if security_options is None:
            raise ValueError("Invalid value for `security_options`, must not be `None`")
        if security_options is not None and len(security_options) < 1:
            raise ValueError("Invalid value for `security_options`, length must be greater than or equal to `1`")
        self._security_options = security_options

    @property
    def protocol_type(self) -> str:
        """Gets the protocol_type of this EmailAccountRequest.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :return: The protocol_type of this EmailAccountRequest.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type: str):
        """Sets the protocol_type of this EmailAccountRequest.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :param protocol_type: The protocol_type of this EmailAccountRequest.
        :type: str
        """
        if protocol_type is None:
            raise ValueError("Invalid value for `protocol_type`, must not be `None`")
        if protocol_type is not None and len(protocol_type) < 1:
            raise ValueError("Invalid value for `protocol_type`, length must be greater than or equal to `1`")
        self._protocol_type = protocol_type

    @property
    def description(self) -> str:
        """Gets the description of this EmailAccountRequest.

        Email account description             

        :return: The description of this EmailAccountRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this EmailAccountRequest.

        Email account description             

        :param description: The description of this EmailAccountRequest.
        :type: str
        """
        self._description = description

    @property
    def storage_file(self) -> StorageFileLocation:
        """Gets the storage_file of this EmailAccountRequest.

        A storage file location info to store email account             

        :return: The storage_file of this EmailAccountRequest.
        :rtype: StorageFileLocation
        """
        return self._storage_file

    @storage_file.setter
    def storage_file(self, storage_file: StorageFileLocation):
        """Sets the storage_file of this EmailAccountRequest.

        A storage file location info to store email account             

        :param storage_file: The storage_file of this EmailAccountRequest.
        :type: StorageFileLocation
        """
        if storage_file is None:
            raise ValueError("Invalid value for `storage_file`, must not be `None`")
        self._storage_file = storage_file

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
        if not isinstance(other, EmailAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
