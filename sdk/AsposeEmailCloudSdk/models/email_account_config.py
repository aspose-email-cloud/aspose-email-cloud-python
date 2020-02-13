#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailAccountConfig.py">
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

from AsposeEmailCloudSdk.models.name_value_pair import NameValuePair


class EmailAccountConfig(object):
    """Email account configuration.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_name': 'str',
        'type': 'str',
        'host': 'str',
        'port': 'int',
        'socket_type': 'str',
        'authentication_types': 'list[str]',
        'extra_info': 'list[NameValuePair]',
        'is_validated': 'bool'
    }

    attribute_map = {
        'display_name': 'displayName',
        'type': 'type',
        'host': 'host',
        'port': 'port',
        'socket_type': 'socketType',
        'authentication_types': 'authenticationTypes',
        'extra_info': 'extraInfo',
        'is_validated': 'isValidated'
    }

    def __init__(self, display_name: str = None, type: str = None, host: str = None, port: int = None, socket_type: str = None, authentication_types: List[str] = None, extra_info: List[NameValuePair] = None, is_validated: bool = None):
        """EmailAccountConfig - a model defined in Swagger"""

        self._display_name = None
        self._type = None
        self._host = None
        self._port = None
        self._socket_type = None
        self._authentication_types = None
        self._extra_info = None
        self._is_validated = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if type is not None:
            self.type = type
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if socket_type is not None:
            self.socket_type = socket_type
        if authentication_types is not None:
            self.authentication_types = authentication_types
        if extra_info is not None:
            self.extra_info = extra_info
        if is_validated is not None:
            self.is_validated = is_validated

    @property
    def display_name(self) -> str:
        """Gets the display_name of this EmailAccountConfig.

        Email account display name             

        :return: The display_name of this EmailAccountConfig.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this EmailAccountConfig.

        Email account display name             

        :param display_name: The display_name of this EmailAccountConfig.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self) -> str:
        """Gets the type of this EmailAccountConfig.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :return: The type of this EmailAccountConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this EmailAccountConfig.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :param type: The type of this EmailAccountConfig.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        self._type = type

    @property
    def host(self) -> str:
        """Gets the host of this EmailAccountConfig.

        Email account host.             

        :return: The host of this EmailAccountConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this EmailAccountConfig.

        Email account host.             

        :param host: The host of this EmailAccountConfig.
        :type: str
        """
        self._host = host

    @property
    def port(self) -> int:
        """Gets the port of this EmailAccountConfig.

        Port.             

        :return: The port of this EmailAccountConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this EmailAccountConfig.

        Port.             

        :param port: The port of this EmailAccountConfig.
        :type: int
        """
        self._port = port

    @property
    def socket_type(self) -> str:
        """Gets the socket_type of this EmailAccountConfig.

        Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :return: The socket_type of this EmailAccountConfig.
        :rtype: str
        """
        return self._socket_type

    @socket_type.setter
    def socket_type(self, socket_type: str):
        """Sets the socket_type of this EmailAccountConfig.

        Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :param socket_type: The socket_type of this EmailAccountConfig.
        :type: str
        """
        if socket_type is None:
            raise ValueError("Invalid value for `socket_type`, must not be `None`")
        self._socket_type = socket_type

    @property
    def authentication_types(self) -> List[str]:
        """Gets the authentication_types of this EmailAccountConfig.

        Supported authentication types.              Items: Email account authentication types. Enum, available values: NoAuth, OAuth2, PasswordCleartext, PasswordEncrypted, SmtpAfterPop, ClientIpAddress

        :return: The authentication_types of this EmailAccountConfig.
        :rtype: list[str]
        """
        return self._authentication_types

    @authentication_types.setter
    def authentication_types(self, authentication_types: List[str]):
        """Sets the authentication_types of this EmailAccountConfig.

        Supported authentication types.              Items: Email account authentication types. Enum, available values: NoAuth, OAuth2, PasswordCleartext, PasswordEncrypted, SmtpAfterPop, ClientIpAddress

        :param authentication_types: The authentication_types of this EmailAccountConfig.
        :type: list[str]
        """
        self._authentication_types = authentication_types

    @property
    def extra_info(self) -> List[NameValuePair]:
        """Gets the extra_info of this EmailAccountConfig.

        Extra account information.             

        :return: The extra_info of this EmailAccountConfig.
        :rtype: list[NameValuePair]
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info: List[NameValuePair]):
        """Sets the extra_info of this EmailAccountConfig.

        Extra account information.             

        :param extra_info: The extra_info of this EmailAccountConfig.
        :type: list[NameValuePair]
        """
        self._extra_info = extra_info

    @property
    def is_validated(self) -> bool:
        """Gets the is_validated of this EmailAccountConfig.

        Determines that configuration validated. Set to false if validation skipped.             

        :return: The is_validated of this EmailAccountConfig.
        :rtype: bool
        """
        return self._is_validated

    @is_validated.setter
    def is_validated(self, is_validated: bool):
        """Sets the is_validated of this EmailAccountConfig.

        Determines that configuration validated. Set to false if validation skipped.             

        :param is_validated: The is_validated of this EmailAccountConfig.
        :type: bool
        """
        if is_validated is None:
            raise ValueError("Invalid value for `is_validated`, must not be `None`")
        self._is_validated = is_validated

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
        if not isinstance(other, EmailAccountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
