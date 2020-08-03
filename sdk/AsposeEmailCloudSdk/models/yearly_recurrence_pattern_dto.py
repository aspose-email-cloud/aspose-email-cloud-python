#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="YearlyRecurrencePatternDto.py">
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


class YearlyRecurrencePatternDto(RecurrencePatternDto):
    """Yearly recurrence pattern.             
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
        'start_day': 'str',
        'start_month': 'str',
        'start_offset': 'int',
        'start_position': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'occurs': 'occurs',
        'end_date': 'endDate',
        'week_start': 'weekStart',
        'discriminator': 'discriminator',
        'start_day': 'startDay',
        'start_month': 'startMonth',
        'start_offset': 'startOffset',
        'start_position': 'startPosition'
    }

    def __init__(self, interval: int = None, occurs: int = None, end_date: datetime = None, week_start: str = None, start_day: str = None, start_month: str = None, start_offset: int = None, start_position: str = None):
        """
        Yearly recurrence pattern.             
        :param interval: Number of recurrence units.             
        :type interval: int
        :param occurs: Number of occurrences of the recurrence pattern.             
        :type occurs: int
        :param end_date: End date.             
        :type end_date: datetime
        :param week_start: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay
        :type week_start: str
        :param start_day: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay
        :type start_day: str
        :param start_month: Represents a calendar month. Enum, available values: None, January, February, March, April, May, June, July, August, September, October, November, December
        :type start_month: str
        :param start_offset: Start offset.             
        :type start_offset: int
        :param start_position: Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last
        :type start_position: str
        """
        super(YearlyRecurrencePatternDto, self).__init__()

        self._start_day = None
        self._start_month = None
        self._start_offset = None
        self._start_position = None

        if interval is not None:
            self.interval = interval
        if occurs is not None:
            self.occurs = occurs
        if end_date is not None:
            self.end_date = end_date
        if week_start is not None:
            self.week_start = week_start
        if start_day is not None:
            self.start_day = start_day
        if start_month is not None:
            self.start_month = start_month
        if start_offset is not None:
            self.start_offset = start_offset
        if start_position is not None:
            self.start_position = start_position


    @property
    def start_day(self) -> str:
        """
        Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay

        :return: The start_day of this YearlyRecurrencePatternDto.
        :rtype: str
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day: str):
        """
        Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay

        :param start_day: The start_day of this YearlyRecurrencePatternDto.
        :type: str
        """
        if start_day is None:
            raise ValueError("Invalid value for `start_day`, must not be `None`")
        self._start_day = start_day

    @property
    def start_month(self) -> str:
        """
        Represents a calendar month. Enum, available values: None, January, February, March, April, May, June, July, August, September, October, November, December

        :return: The start_month of this YearlyRecurrencePatternDto.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month: str):
        """
        Represents a calendar month. Enum, available values: None, January, February, March, April, May, June, July, August, September, October, November, December

        :param start_month: The start_month of this YearlyRecurrencePatternDto.
        :type: str
        """
        if start_month is None:
            raise ValueError("Invalid value for `start_month`, must not be `None`")
        self._start_month = start_month

    @property
    def start_offset(self) -> int:
        """
        Start offset.             

        :return: The start_offset of this YearlyRecurrencePatternDto.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset: int):
        """
        Start offset.             

        :param start_offset: The start_offset of this YearlyRecurrencePatternDto.
        :type: int
        """
        if start_offset is None:
            raise ValueError("Invalid value for `start_offset`, must not be `None`")
        self._start_offset = start_offset

    @property
    def start_position(self) -> str:
        """
        Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last

        :return: The start_position of this YearlyRecurrencePatternDto.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position: str):
        """
        Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last

        :param start_position: The start_position of this YearlyRecurrencePatternDto.
        :type: str
        """
        if start_position is None:
            raise ValueError("Invalid value for `start_position`, must not be `None`")
        self._start_position = start_position

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
        if not isinstance(other, YearlyRecurrencePatternDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
