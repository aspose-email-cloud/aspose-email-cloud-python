#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailClientAccount.py">
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

from AsposeEmailCloudSdk.models.email_client_account_credentials import EmailClientAccountCredentials


class EmailClientAccount(object):
    """A universal email client account             
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
        'security_options': 'str',
        'protocol_type': 'str',
        'credentials': 'EmailClientAccountCredentials'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'security_options': 'securityOptions',
        'protocol_type': 'protocolType',
        'credentials': 'credentials'
    }

    def __init__(self, host: str = None, port: int = None, security_options: str = None, protocol_type: str = None, credentials: EmailClientAccountCredentials = None):
        """
        A universal email client account             
        :param host (str) Mail server host name or IP address             
        :param port (int) Mail server port             
        :param security_options (str) Email account security mode Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto
        :param protocol_type (str) Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav
        :param credentials (EmailClientAccountCredentials) Email client account credentials             
        """

        self._host = None
        self._port = None
        self._security_options = None
        self._protocol_type = None
        self._credentials = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if security_options is not None:
            self.security_options = security_options
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if credentials is not None:
            self.credentials = credentials

    @property
    def host(self) -> str:
        """Gets the host of this EmailClientAccount.

        Mail server host name or IP address             

        :return: The host of this EmailClientAccount.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this EmailClientAccount.

        Mail server host name or IP address             

        :param host: The host of this EmailClientAccount.
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")
        if host is not None and len(host) < 1:
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `1`")
        self._host = host

    @property
    def port(self) -> int:
        """Gets the port of this EmailClientAccount.

        Mail server port             

        :return: The port of this EmailClientAccount.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this EmailClientAccount.

        Mail server port             

        :param port: The port of this EmailClientAccount.
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")
        if port is not None and port > 2147483647:
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `2147483647`")
        if port is not None and port < 1:
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")
        self._port = port

    @property
    def security_options(self) -> str:
        """Gets the security_options of this EmailClientAccount.

        Email account security mode Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :return: The security_options of this EmailClientAccount.
        :rtype: str
        """
        return self._security_options

    @security_options.setter
    def security_options(self, security_options: str):
        """Sets the security_options of this EmailClientAccount.

        Email account security mode Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :param security_options: The security_options of this EmailClientAccount.
        :type: str
        """
        if security_options is None:
            raise ValueError("Invalid value for `security_options`, must not be `None`")
        self._security_options = security_options

    @property
    def protocol_type(self) -> str:
        """Gets the protocol_type of this EmailClientAccount.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :return: The protocol_type of this EmailClientAccount.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type: str):
        """Sets the protocol_type of this EmailClientAccount.

        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :param protocol_type: The protocol_type of this EmailClientAccount.
        :type: str
        """
        if protocol_type is None:
            raise ValueError("Invalid value for `protocol_type`, must not be `None`")
        self._protocol_type = protocol_type

    @property
    def credentials(self) -> EmailClientAccountCredentials:
        """Gets the credentials of this EmailClientAccount.

        Email client account credentials             

        :return: The credentials of this EmailClientAccount.
        :rtype: EmailClientAccountCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: EmailClientAccountCredentials):
        """Sets the credentials of this EmailClientAccount.

        Email client account credentials             

        :param credentials: The credentials of this EmailClientAccount.
        :type: EmailClientAccountCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")
        self._credentials = credentials

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
        if not isinstance(other, EmailClientAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
