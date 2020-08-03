#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ReminderTrigger.py">
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


class ReminderTrigger(object):
    """Specifies when an alarm will trigger.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'date_time': 'datetime',
        'duration': 'int',
        'related': 'str'
    }

    attribute_map = {
        'date_time': 'dateTime',
        'duration': 'duration',
        'related': 'related'
    }

    def __init__(self, date_time: datetime = None, duration: int = None, related: str = None):
        """
        Specifies when an alarm will trigger.
        :param date_time: A trigger set to an absolute date/time.
        :type date_time: datetime
        :param duration: Specifies a relative time in ticks for the trigger of the alarm.             
        :type duration: int
        :param related: Specify the relationship of the alarm trigger with respect to the start or end of the event. Enum, available values: Start, End
        :type related: str
        """

        self._date_time = None
        self._duration = None
        self._related = None

        if date_time is not None:
            self.date_time = date_time
        if duration is not None:
            self.duration = duration
        if related is not None:
            self.related = related


    @property
    def date_time(self) -> datetime:
        """
        A trigger set to an absolute date/time.

        :return: The date_time of this ReminderTrigger.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time: datetime):
        """
        A trigger set to an absolute date/time.

        :param date_time: The date_time of this ReminderTrigger.
        :type: datetime
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")
        self._date_time = date_time

    @property
    def duration(self) -> int:
        """
        Specifies a relative time in ticks for the trigger of the alarm.             

        :return: The duration of this ReminderTrigger.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """
        Specifies a relative time in ticks for the trigger of the alarm.             

        :param duration: The duration of this ReminderTrigger.
        :type: int
        """
        self._duration = duration

    @property
    def related(self) -> str:
        """
        Specify the relationship of the alarm trigger with respect to the start or end of the event. Enum, available values: Start, End

        :return: The related of this ReminderTrigger.
        :rtype: str
        """
        return self._related

    @related.setter
    def related(self, related: str):
        """
        Specify the relationship of the alarm trigger with respect to the start or end of the event. Enum, available values: Start, End

        :param related: The related of this ReminderTrigger.
        :type: str
        """
        if related is None:
            raise ValueError("Invalid value for `related`, must not be `None`")
        self._related = related

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
        if not isinstance(other, ReminderTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
