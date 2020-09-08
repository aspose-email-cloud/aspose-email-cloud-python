#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarTimeZoneRuleDto.py">
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


class MapiCalendarTimeZoneRuleDto(object):
    """Represents time zone rule that indicate when to begin using the Standard/Daylight time.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_date': 'datetime',
        'day_of_week': 'str',
        'hour': 'int',
        'milliseconds': 'int',
        'minute': 'int',
        'month': 'int',
        'position': 'str',
        'seconds': 'int',
        'year': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'day_of_week': 'dayOfWeek',
        'hour': 'hour',
        'milliseconds': 'milliseconds',
        'minute': 'minute',
        'month': 'month',
        'position': 'position',
        'seconds': 'seconds',
        'year': 'year'
    }

    def __init__(self, _date: datetime = None, day_of_week: str = None, hour: int = None, milliseconds: int = None, minute: int = None, month: int = None, position: str = None, seconds: int = None, year: int = None):
        """
        Represents time zone rule that indicate when to begin using the Standard/Daylight time.             
        :param _date: Date and time that indicate when to begin using the Standard/Daylight time.             
        :type _date: datetime
        :param day_of_week: Day of week. Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        :type day_of_week: str
        :param hour: Hour.             
        :type hour: int
        :param milliseconds: Milliseconds.             
        :type milliseconds: int
        :param minute: Minute.             
        :type minute: int
        :param month: Month.             
        :type month: int
        :param position: Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last
        :type position: str
        :param seconds: Seconds.             
        :type seconds: int
        :param year: Year.             
        :type year: int
        """

        self.__date = None
        self._day_of_week = None
        self._hour = None
        self._milliseconds = None
        self._minute = None
        self._month = None
        self._position = None
        self._seconds = None
        self._year = None

        if _date is not None:
            self._date = _date
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if hour is not None:
            self.hour = hour
        if milliseconds is not None:
            self.milliseconds = milliseconds
        if minute is not None:
            self.minute = minute
        if month is not None:
            self.month = month
        if position is not None:
            self.position = position
        if seconds is not None:
            self.seconds = seconds
        if year is not None:
            self.year = year


    @property
    def _date(self) -> datetime:
        """
        Date and time that indicate when to begin using the Standard/Daylight time.             

        :return: The _date of this MapiCalendarTimeZoneRuleDto.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date: datetime):
        """
        Date and time that indicate when to begin using the Standard/Daylight time.             

        :param _date: The _date of this MapiCalendarTimeZoneRuleDto.
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")
        self.__date = _date

    @property
    def day_of_week(self) -> str:
        """
        Day of week. Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

        :return: The day_of_week of this MapiCalendarTimeZoneRuleDto.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week: str):
        """
        Day of week. Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

        :param day_of_week: The day_of_week of this MapiCalendarTimeZoneRuleDto.
        :type: str
        """
        if day_of_week is None:
            raise ValueError("Invalid value for `day_of_week`, must not be `None`")
        self._day_of_week = day_of_week

    @property
    def hour(self) -> int:
        """
        Hour.             

        :return: The hour of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour: int):
        """
        Hour.             

        :param hour: The hour of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if hour is None:
            raise ValueError("Invalid value for `hour`, must not be `None`")
        self._hour = hour

    @property
    def milliseconds(self) -> int:
        """
        Milliseconds.             

        :return: The milliseconds of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds: int):
        """
        Milliseconds.             

        :param milliseconds: The milliseconds of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if milliseconds is None:
            raise ValueError("Invalid value for `milliseconds`, must not be `None`")
        self._milliseconds = milliseconds

    @property
    def minute(self) -> int:
        """
        Minute.             

        :return: The minute of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute: int):
        """
        Minute.             

        :param minute: The minute of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if minute is None:
            raise ValueError("Invalid value for `minute`, must not be `None`")
        self._minute = minute

    @property
    def month(self) -> int:
        """
        Month.             

        :return: The month of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month: int):
        """
        Month.             

        :param month: The month of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")
        if month is not None and month > 12:
            raise ValueError("Invalid value for `month`, must be a value less than or equal to `12`")
        if month is not None and month < 0:
            raise ValueError("Invalid value for `month`, must be a value greater than or equal to `0`")
        self._month = month

    @property
    def position(self) -> str:
        """
        Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last

        :return: The position of this MapiCalendarTimeZoneRuleDto.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position: str):
        """
        Day positions, typically found in a month. Enum, available values: None, First, Second, Third, Fourth, Last

        :param position: The position of this MapiCalendarTimeZoneRuleDto.
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")
        self._position = position

    @property
    def seconds(self) -> int:
        """
        Seconds.             

        :return: The seconds of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        """
        Seconds.             

        :param seconds: The seconds of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")
        self._seconds = seconds

    @property
    def year(self) -> int:
        """
        Year.             

        :return: The year of this MapiCalendarTimeZoneRuleDto.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year: int):
        """
        Year.             

        :param year: The year of this MapiCalendarTimeZoneRuleDto.
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")
        self._year = year

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
        if not isinstance(other, MapiCalendarTimeZoneRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
