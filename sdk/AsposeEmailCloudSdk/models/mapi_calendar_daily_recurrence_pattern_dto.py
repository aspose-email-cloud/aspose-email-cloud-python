#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarDailyRecurrencePatternDto.py">
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

from AsposeEmailCloudSdk.models.mapi_calendar_exception_info_dto import MapiCalendarExceptionInfoDto
from AsposeEmailCloudSdk.models.mapi_calendar_recurrence_pattern_dto import MapiCalendarRecurrencePatternDto


class MapiCalendarDailyRecurrencePatternDto(MapiCalendarRecurrencePatternDto):
    """Represents the daily recurrence pattern of the mapi calendar.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'calendar_type': 'str',
        'deleted_instance_dates': 'list[datetime]',
        'end_date': 'datetime',
        'end_type': 'str',
        'exceptions': 'list[MapiCalendarExceptionInfoDto]',
        'frequency': 'str',
        'modified_instance_dates': 'list[datetime]',
        'occurrence_count': 'int',
        'pattern_type': 'str',
        'period': 'int',
        'sliding_flag': 'bool',
        'start_date': 'datetime',
        'week_start_day': 'str',
        'discriminator': 'str',
        'day_of_week': 'list[str]'
    }

    attribute_map = {
        'calendar_type': 'calendarType',
        'deleted_instance_dates': 'deletedInstanceDates',
        'end_date': 'endDate',
        'end_type': 'endType',
        'exceptions': 'exceptions',
        'frequency': 'frequency',
        'modified_instance_dates': 'modifiedInstanceDates',
        'occurrence_count': 'occurrenceCount',
        'pattern_type': 'patternType',
        'period': 'period',
        'sliding_flag': 'slidingFlag',
        'start_date': 'startDate',
        'week_start_day': 'weekStartDay',
        'discriminator': 'discriminator',
        'day_of_week': 'dayOfWeek'
    }

    def __init__(self, calendar_type: str = None, deleted_instance_dates: List[datetime] = None, end_date: datetime = None, end_type: str = None, exceptions: List[MapiCalendarExceptionInfoDto] = None, frequency: str = None, modified_instance_dates: List[datetime] = None, occurrence_count: int = None, pattern_type: str = None, period: int = None, sliding_flag: bool = None, start_date: datetime = None, week_start_day: str = None, discriminator: str = None, day_of_week: List[str] = None):
        """
        Represents the daily recurrence pattern of the mapi calendar.             
        :param calendar_type (str) Enumerated the calendar type of the mapi recurrence Enum, available values: Default, CalGregorian, CalGregorianUs, CalJapan, CalTaiwan, CalKorea, CalHijri, CalThai, CalHebrew, CalGregorianMeFrench, CalGregorianArabic, CalGregorianXLitEnglish, CalGregorianXLitFrench, CalLunarJapanese, CalChineseLunar, CalSaka, CalLunarEtoChn, CalLunarEtoKor, CalLunarRokuyou, CalLunarKorean, CalUmAlQura
        :param deleted_instance_dates (List[datetime]) An array of dates, each of which is the original instance date of either a deleted instance or a modified instance for this recurrence.             
        :param end_date (datetime) End date of an item recurrence pattern.             
        :param end_type (str) Enumerates the ending type for the recurrence. Enum, available values: None, EndAfterDate, EndAfterNOccurrences, NeverEnd
        :param exceptions (List[MapiCalendarExceptionInfoDto]) An exception specifies changes to an instance of a recurring series.             
        :param frequency (str) Enumerates mapi calendar recurrence frequency Enum, available values: None, Daily, Weekly, Monthly, Yearly
        :param modified_instance_dates (List[datetime]) An array of dates, each of which is the date of a modified instance.             
        :param occurrence_count (int) Number of occurrences in a recurrence.             
        :param pattern_type (str) Enumerates the mapi calendar recurrence pattern types Enum, available values: Day, Week, Month, MonthEnd, MonthNth, HjMonth, HjMonthNth, HjMonthEnd
        :param period (int) Interval at which the meeting pattern repeats.             
        :param sliding_flag (bool) Defines whether pattern is sliding or not.             
        :param start_date (datetime) Start date of an item recurrence pattern.             
        :param week_start_day (str) Day of week. Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        :param discriminator (str) 
        :param day_of_week (List[str]) Days of week at which the event occurs.             
        """
        super(MapiCalendarDailyRecurrencePatternDto, self).__init__()

        self._day_of_week = None

        if calendar_type is not None:
            self.calendar_type = calendar_type
        if deleted_instance_dates is not None:
            self.deleted_instance_dates = deleted_instance_dates
        if end_date is not None:
            self.end_date = end_date
        if end_type is not None:
            self.end_type = end_type
        if exceptions is not None:
            self.exceptions = exceptions
        if frequency is not None:
            self.frequency = frequency
        if modified_instance_dates is not None:
            self.modified_instance_dates = modified_instance_dates
        if occurrence_count is not None:
            self.occurrence_count = occurrence_count
        if pattern_type is not None:
            self.pattern_type = pattern_type
        if period is not None:
            self.period = period
        if sliding_flag is not None:
            self.sliding_flag = sliding_flag
        if start_date is not None:
            self.start_date = start_date
        if week_start_day is not None:
            self.week_start_day = week_start_day
        if discriminator is not None:
            self.discriminator = discriminator
        if day_of_week is not None:
            self.day_of_week = day_of_week

    @property
    def day_of_week(self) -> List[str]:
        """Gets the day_of_week of this MapiCalendarDailyRecurrencePatternDto.

        Days of week at which the event occurs.              Items: Enumerates the days of week of the mapi calendar recurrence pattern Enum, available values: Saturday, Friday, Thursday, Wednesday, Tuesday, Monday, Sunday

        :return: The day_of_week of this MapiCalendarDailyRecurrencePatternDto.
        :rtype: list[str]
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week: List[str]):
        """Sets the day_of_week of this MapiCalendarDailyRecurrencePatternDto.

        Days of week at which the event occurs.              Items: Enumerates the days of week of the mapi calendar recurrence pattern Enum, available values: Saturday, Friday, Thursday, Wednesday, Tuesday, Monday, Sunday

        :param day_of_week: The day_of_week of this MapiCalendarDailyRecurrencePatternDto.
        :type: list[str]
        """
        self._day_of_week = day_of_week

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
        if not isinstance(other, MapiCalendarDailyRecurrencePatternDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
