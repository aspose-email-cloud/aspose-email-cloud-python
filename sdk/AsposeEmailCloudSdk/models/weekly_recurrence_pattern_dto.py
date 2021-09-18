#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="WeeklyRecurrencePatternDto.py">
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

from AsposeEmailCloudSdk.models.recurrence_pattern_dto import RecurrencePatternDto


class WeeklyRecurrencePatternDto(RecurrencePatternDto):
    """Weekly recurrence pattern.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'interval': 'int',
        'occurs': 'int',
        'end_date': 'datetime',
        'week_start': 'str',
        'discriminator': 'str',
        'start_days': 'list[str]'
    }

    attribute_map = {
        'interval': 'interval',
        'occurs': 'occurs',
        'end_date': 'endDate',
        'week_start': 'weekStart',
        'discriminator': 'discriminator',
        'start_days': 'startDays'
    }

    def __init__(self, interval: int = None, occurs: int = None, end_date: datetime = None, week_start: str = None, start_days: List[str] = None):
        """
        Weekly recurrence pattern.             
        :param interval: Number of recurrence units.             
        :type interval: int
        :param occurs: Number of occurrences of the recurrence pattern.             
        :type occurs: int
        :param end_date: End date.             
        :type end_date: datetime
        :param week_start: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay
        :type week_start: str
        :param start_days: Start days             
        :type start_days: List[str]
        """
        super(WeeklyRecurrencePatternDto, self).__init__()

        self._start_days = None

        if interval is not None:
            self.interval = interval
        if occurs is not None:
            self.occurs = occurs
        if end_date is not None:
            self.end_date = end_date
        if week_start is not None:
            self.week_start = week_start
        if start_days is not None:
            self.start_days = start_days


    @property
    def start_days(self) -> List[str]:
        """
        Start days              Items: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay

        :return: The start_days of this WeeklyRecurrencePatternDto.
        :rtype: list[str]
        """
        return self._start_days

    @start_days.setter
    def start_days(self, start_days: List[str]):
        """
        Start days              Items: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay

        :param start_days: The start_days of this WeeklyRecurrencePatternDto.
        :type: list[str]
        """
        self._start_days = start_days

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
        if not isinstance(other, WeeklyRecurrencePatternDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
