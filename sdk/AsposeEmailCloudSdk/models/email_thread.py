#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailThread.py">
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

from AsposeEmailCloudSdk.models.email_dto import EmailDto


class EmailThread(object):
    """Email messages thread             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'subject': 'str',
        'messages': 'list[EmailDto]',
        'folder': 'str'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'messages': 'messages',
        'folder': 'folder'
    }

    def __init__(self, id: str = None, subject: str = None, messages: List[EmailDto] = None, folder: str = None):
        """
        Email messages thread             
        :param id: Thread identifier             
        :type id: str
        :param subject: Thread subject             
        :type subject: str
        :param messages: List of messages in thread             
        :type messages: List[EmailDto]
        :param folder: Thread folder location             
        :type folder: str
        """

        self._id = None
        self._subject = None
        self._messages = None
        self._folder = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject
        if messages is not None:
            self.messages = messages
        if folder is not None:
            self.folder = folder


    @property
    def id(self) -> str:
        """
        Thread identifier             

        :return: The id of this EmailThread.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Thread identifier             

        :param id: The id of this EmailThread.
        :type: str
        """
        self._id = id

    @property
    def subject(self) -> str:
        """
        Thread subject             

        :return: The subject of this EmailThread.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """
        Thread subject             

        :param subject: The subject of this EmailThread.
        :type: str
        """
        self._subject = subject

    @property
    def messages(self) -> List[EmailDto]:
        """
        List of messages in thread             

        :return: The messages of this EmailThread.
        :rtype: list[EmailDto]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[EmailDto]):
        """
        List of messages in thread             

        :param messages: The messages of this EmailThread.
        :type: list[EmailDto]
        """
        self._messages = messages

    @property
    def folder(self) -> str:
        """
        Thread folder location             

        :return: The folder of this EmailThread.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder: str):
        """
        Thread folder location             

        :param folder: The folder of this EmailThread.
        :type: str
        """
        self._folder = folder

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
        if not isinstance(other, EmailThread):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
