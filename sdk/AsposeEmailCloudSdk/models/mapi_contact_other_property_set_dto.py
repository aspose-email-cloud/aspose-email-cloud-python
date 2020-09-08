#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactOtherPropertySetDto.py">
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


class MapiContactOtherPropertySetDto(object):
    """The properties are used to specify additional properties of contact.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'private': 'bool',
        'journal': 'bool',
        'reminder_time': 'datetime',
        'reminder_topic': 'str',
        'user_field1': 'str',
        'user_field2': 'str',
        'user_field3': 'str',
        'user_field4': 'str'
    }

    attribute_map = {
        'private': 'private',
        'journal': 'journal',
        'reminder_time': 'reminderTime',
        'reminder_topic': 'reminderTopic',
        'user_field1': 'userField1',
        'user_field2': 'userField2',
        'user_field3': 'userField3',
        'user_field4': 'userField4'
    }

    def __init__(self, private: bool = None, journal: bool = None, reminder_time: datetime = None, reminder_topic: str = None, user_field1: str = None, user_field2: str = None, user_field3: str = None, user_field4: str = None):
        """
        The properties are used to specify additional properties of contact.             
        :param private: Indicates whether the end-user wants this message object hidden from other users who have access to the message object.             
        :type private: bool
        :param journal: Specifies whether to create a journal for each action associated with this contact.             
        :type journal: bool
        :param reminder_time: Specifies the initial signal time for a reminder.             
        :type reminder_time: datetime
        :param reminder_topic: Represents the status of a meeting request.             
        :type reminder_topic: str
        :param user_field1: Specifies the first field on the contact that is intended for miscellaneous use for the contact.             
        :type user_field1: str
        :param user_field2: Specifies the second field on the contact that is intended for miscellaneous use for the contact.             
        :type user_field2: str
        :param user_field3: Specifies the third field on the contact that is intended for miscellaneous use for the contact.             
        :type user_field3: str
        :param user_field4: Specifies the forth field on the contact that is intended for miscellaneous use for the contact.             
        :type user_field4: str
        """

        self._private = None
        self._journal = None
        self._reminder_time = None
        self._reminder_topic = None
        self._user_field1 = None
        self._user_field2 = None
        self._user_field3 = None
        self._user_field4 = None

        if private is not None:
            self.private = private
        if journal is not None:
            self.journal = journal
        if reminder_time is not None:
            self.reminder_time = reminder_time
        if reminder_topic is not None:
            self.reminder_topic = reminder_topic
        if user_field1 is not None:
            self.user_field1 = user_field1
        if user_field2 is not None:
            self.user_field2 = user_field2
        if user_field3 is not None:
            self.user_field3 = user_field3
        if user_field4 is not None:
            self.user_field4 = user_field4


    @property
    def private(self) -> bool:
        """
        Indicates whether the end-user wants this message object hidden from other users who have access to the message object.             

        :return: The private of this MapiContactOtherPropertySetDto.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private: bool):
        """
        Indicates whether the end-user wants this message object hidden from other users who have access to the message object.             

        :param private: The private of this MapiContactOtherPropertySetDto.
        :type: bool
        """
        if private is None:
            raise ValueError("Invalid value for `private`, must not be `None`")
        self._private = private

    @property
    def journal(self) -> bool:
        """
        Specifies whether to create a journal for each action associated with this contact.             

        :return: The journal of this MapiContactOtherPropertySetDto.
        :rtype: bool
        """
        return self._journal

    @journal.setter
    def journal(self, journal: bool):
        """
        Specifies whether to create a journal for each action associated with this contact.             

        :param journal: The journal of this MapiContactOtherPropertySetDto.
        :type: bool
        """
        if journal is None:
            raise ValueError("Invalid value for `journal`, must not be `None`")
        self._journal = journal

    @property
    def reminder_time(self) -> datetime:
        """
        Specifies the initial signal time for a reminder.             

        :return: The reminder_time of this MapiContactOtherPropertySetDto.
        :rtype: datetime
        """
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, reminder_time: datetime):
        """
        Specifies the initial signal time for a reminder.             

        :param reminder_time: The reminder_time of this MapiContactOtherPropertySetDto.
        :type: datetime
        """
        if reminder_time is None:
            raise ValueError("Invalid value for `reminder_time`, must not be `None`")
        self._reminder_time = reminder_time

    @property
    def reminder_topic(self) -> str:
        """
        Represents the status of a meeting request.             

        :return: The reminder_topic of this MapiContactOtherPropertySetDto.
        :rtype: str
        """
        return self._reminder_topic

    @reminder_topic.setter
    def reminder_topic(self, reminder_topic: str):
        """
        Represents the status of a meeting request.             

        :param reminder_topic: The reminder_topic of this MapiContactOtherPropertySetDto.
        :type: str
        """
        self._reminder_topic = reminder_topic

    @property
    def user_field1(self) -> str:
        """
        Specifies the first field on the contact that is intended for miscellaneous use for the contact.             

        :return: The user_field1 of this MapiContactOtherPropertySetDto.
        :rtype: str
        """
        return self._user_field1

    @user_field1.setter
    def user_field1(self, user_field1: str):
        """
        Specifies the first field on the contact that is intended for miscellaneous use for the contact.             

        :param user_field1: The user_field1 of this MapiContactOtherPropertySetDto.
        :type: str
        """
        self._user_field1 = user_field1

    @property
    def user_field2(self) -> str:
        """
        Specifies the second field on the contact that is intended for miscellaneous use for the contact.             

        :return: The user_field2 of this MapiContactOtherPropertySetDto.
        :rtype: str
        """
        return self._user_field2

    @user_field2.setter
    def user_field2(self, user_field2: str):
        """
        Specifies the second field on the contact that is intended for miscellaneous use for the contact.             

        :param user_field2: The user_field2 of this MapiContactOtherPropertySetDto.
        :type: str
        """
        self._user_field2 = user_field2

    @property
    def user_field3(self) -> str:
        """
        Specifies the third field on the contact that is intended for miscellaneous use for the contact.             

        :return: The user_field3 of this MapiContactOtherPropertySetDto.
        :rtype: str
        """
        return self._user_field3

    @user_field3.setter
    def user_field3(self, user_field3: str):
        """
        Specifies the third field on the contact that is intended for miscellaneous use for the contact.             

        :param user_field3: The user_field3 of this MapiContactOtherPropertySetDto.
        :type: str
        """
        self._user_field3 = user_field3

    @property
    def user_field4(self) -> str:
        """
        Specifies the forth field on the contact that is intended for miscellaneous use for the contact.             

        :return: The user_field4 of this MapiContactOtherPropertySetDto.
        :rtype: str
        """
        return self._user_field4

    @user_field4.setter
    def user_field4(self, user_field4: str):
        """
        Specifies the forth field on the contact that is intended for miscellaneous use for the contact.             

        :param user_field4: The user_field4 of this MapiContactOtherPropertySetDto.
        :type: str
        """
        self._user_field4 = user_field4

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
        if not isinstance(other, MapiContactOtherPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
