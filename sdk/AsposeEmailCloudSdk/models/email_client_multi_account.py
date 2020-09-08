#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailClientMultiAccount.py">
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

from AsposeEmailCloudSdk.models.email_client_account import EmailClientAccount


class EmailClientMultiAccount(object):
    """Email client virtual account, which contains several accounts             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'receive_accounts': 'list[EmailClientAccount]',
        'send_account': 'EmailClientAccount'
    }

    attribute_map = {
        'receive_accounts': 'receiveAccounts',
        'send_account': 'sendAccount'
    }

    def __init__(self, receive_accounts: List[EmailClientAccount] = None, send_account: EmailClientAccount = None):
        """
        Email client virtual account, which contains several accounts             
        :param receive_accounts: Email client receive accounts             
        :type receive_accounts: List[EmailClientAccount]
        :param send_account: Email client send account             
        :type send_account: EmailClientAccount
        """

        self._receive_accounts = None
        self._send_account = None

        if receive_accounts is not None:
            self.receive_accounts = receive_accounts
        if send_account is not None:
            self.send_account = send_account


    @property
    def receive_accounts(self) -> List[EmailClientAccount]:
        """
        Email client receive accounts             

        :return: The receive_accounts of this EmailClientMultiAccount.
        :rtype: list[EmailClientAccount]
        """
        return self._receive_accounts

    @receive_accounts.setter
    def receive_accounts(self, receive_accounts: List[EmailClientAccount]):
        """
        Email client receive accounts             

        :param receive_accounts: The receive_accounts of this EmailClientMultiAccount.
        :type: list[EmailClientAccount]
        """
        if receive_accounts is None:
            raise ValueError("Invalid value for `receive_accounts`, must not be `None`")
        self._receive_accounts = receive_accounts

    @property
    def send_account(self) -> EmailClientAccount:
        """
        Email client send account             

        :return: The send_account of this EmailClientMultiAccount.
        :rtype: EmailClientAccount
        """
        return self._send_account

    @send_account.setter
    def send_account(self, send_account: EmailClientAccount):
        """
        Email client send account             

        :param send_account: The send_account of this EmailClientMultiAccount.
        :type: EmailClientAccount
        """
        self._send_account = send_account

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
        if not isinstance(other, EmailClientMultiAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
