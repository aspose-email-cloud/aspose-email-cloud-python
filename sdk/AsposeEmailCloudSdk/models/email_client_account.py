#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailClientAccount.py">
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

from AsposeEmailCloudSdk.models.email_client_account_credentials import EmailClientAccountCredentials
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


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
        'credentials': 'EmailClientAccountCredentials',
        'cache_file': 'StorageFileLocation'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'security_options': 'securityOptions',
        'protocol_type': 'protocolType',
        'credentials': 'credentials',
        'cache_file': 'cacheFile'
    }

    def __init__(self, host: str = None, port: int = None, security_options: str = None, protocol_type: str = None, credentials: EmailClientAccountCredentials = None, cache_file: StorageFileLocation = None):
        """
        A universal email client account             
        :param host: Mail server host name or IP address             
        :type host: str
        :param port: Mail server port             
        :type port: int
        :param security_options: Email account security mode. Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto
        :type security_options: str
        :param protocol_type: Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav
        :type protocol_type: str
        :param credentials: Email client account credentials             
        :type credentials: EmailClientAccountCredentials
        :param cache_file: File with messages cache. Used to provide extra functions, which are not supported by account             
        :type cache_file: StorageFileLocation
        """

        self._host = None
        self._port = None
        self._security_options = None
        self._protocol_type = None
        self._credentials = None
        self._cache_file = None

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
        if cache_file is not None:
            self.cache_file = cache_file


    @property
    def host(self) -> str:
        """
        Mail server host name or IP address             

        :return: The host of this EmailClientAccount.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """
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
        """
        Mail server port             

        :return: The port of this EmailClientAccount.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """
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
        """
        Email account security mode. Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :return: The security_options of this EmailClientAccount.
        :rtype: str
        """
        return self._security_options

    @security_options.setter
    def security_options(self, security_options: str):
        """
        Email account security mode. Enum, available values: None, SSLExplicit, SSLImplicit, SSLAuto, Auto

        :param security_options: The security_options of this EmailClientAccount.
        :type: str
        """
        if security_options is None:
            raise ValueError("Invalid value for `security_options`, must not be `None`")
        self._security_options = security_options

    @property
    def protocol_type(self) -> str:
        """
        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :return: The protocol_type of this EmailClientAccount.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type: str):
        """
        Type of connection protocol. Enum, available values: IMAP, POP3, SMTP, EWS, WebDav

        :param protocol_type: The protocol_type of this EmailClientAccount.
        :type: str
        """
        if protocol_type is None:
            raise ValueError("Invalid value for `protocol_type`, must not be `None`")
        self._protocol_type = protocol_type

    @property
    def credentials(self) -> EmailClientAccountCredentials:
        """
        Email client account credentials             

        :return: The credentials of this EmailClientAccount.
        :rtype: EmailClientAccountCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: EmailClientAccountCredentials):
        """
        Email client account credentials             

        :param credentials: The credentials of this EmailClientAccount.
        :type: EmailClientAccountCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")
        self._credentials = credentials

    @property
    def cache_file(self) -> StorageFileLocation:
        """
        File with messages cache. Used to provide extra functions, which are not supported by account             

        :return: The cache_file of this EmailClientAccount.
        :rtype: StorageFileLocation
        """
        return self._cache_file

    @cache_file.setter
    def cache_file(self, cache_file: StorageFileLocation):
        """
        File with messages cache. Used to provide extra functions, which are not supported by account             

        :param cache_file: The cache_file of this EmailClientAccount.
        :type: StorageFileLocation
        """
        self._cache_file = cache_file

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
