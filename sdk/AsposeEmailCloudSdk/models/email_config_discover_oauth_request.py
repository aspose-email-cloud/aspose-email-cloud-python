#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailConfigDiscoverOauthRequest.py">
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

from AsposeEmailCloudSdk.models.discover_email_config_request import DiscoverEmailConfigRequest


class EmailConfigDiscoverOauthRequest(DiscoverEmailConfigRequest):
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
        'address': 'str',
        'fast_processing': 'bool',
        'login': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'refresh_token': 'str',
        'request_url': 'str'
    }

    attribute_map = {
        'address': 'address',
        'fast_processing': 'fastProcessing',
        'login': 'login',
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'refresh_token': 'refreshToken',
        'request_url': 'requestUrl'
    }

    def __init__(self, address: str = None, fast_processing: bool = None, login: str = None, client_id: str = None, client_secret: str = None, refresh_token: str = None, request_url: str = None):
        """
        
        :param address: Email address to discover.             
        :type address: str
        :param fast_processing: Turns on fast processing. All discover systems will run in parallel. First discovered result will be returned.             
        :type fast_processing: bool
        :param login: Email account login. If not specified, address used as a login.             
        :type login: str
        :param client_id: OAuth client id.             
        :type client_id: str
        :param client_secret: OAuth client secret.             
        :type client_secret: str
        :param refresh_token: OAuth refresh token.             
        :type refresh_token: str
        :param request_url: The url to obtain access token. If not specified, will be discovered from email configuration.             
        :type request_url: str
        """
        super(EmailConfigDiscoverOauthRequest, self).__init__()

        self._client_id = None
        self._client_secret = None
        self._refresh_token = None
        self._request_url = None

        if address is not None:
            self.address = address
        if fast_processing is not None:
            self.fast_processing = fast_processing
        if login is not None:
            self.login = login
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if request_url is not None:
            self.request_url = request_url


    @property
    def client_id(self) -> str:
        """
        OAuth client id.             

        :return: The client_id of this EmailConfigDiscoverOauthRequest.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """
        OAuth client id.             

        :param client_id: The client_id of this EmailConfigDiscoverOauthRequest.
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")
        self._client_id = client_id

    @property
    def client_secret(self) -> str:
        """
        OAuth client secret.             

        :return: The client_secret of this EmailConfigDiscoverOauthRequest.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str):
        """
        OAuth client secret.             

        :param client_secret: The client_secret of this EmailConfigDiscoverOauthRequest.
        :type: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")
        if client_secret is not None and len(client_secret) < 1:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")
        self._client_secret = client_secret

    @property
    def refresh_token(self) -> str:
        """
        OAuth refresh token.             

        :return: The refresh_token of this EmailConfigDiscoverOauthRequest.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token: str):
        """
        OAuth refresh token.             

        :param refresh_token: The refresh_token of this EmailConfigDiscoverOauthRequest.
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")
        if refresh_token is not None and len(refresh_token) < 1:
            raise ValueError("Invalid value for `refresh_token`, length must be greater than or equal to `1`")
        self._refresh_token = refresh_token

    @property
    def request_url(self) -> str:
        """
        The url to obtain access token. If not specified, will be discovered from email configuration.             

        :return: The request_url of this EmailConfigDiscoverOauthRequest.
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url: str):
        """
        The url to obtain access token. If not specified, will be discovered from email configuration.             

        :param request_url: The request_url of this EmailConfigDiscoverOauthRequest.
        :type: str
        """
        self._request_url = request_url

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
        if not isinstance(other, EmailConfigDiscoverOauthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
