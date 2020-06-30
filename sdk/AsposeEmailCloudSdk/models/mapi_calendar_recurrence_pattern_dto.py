#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarRecurrencePatternDto.py">
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


class MapiCalendarRecurrencePatternDto(object):
    """Mapi recurrence pattern.             
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
        'discriminator': 'str'
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
        'discriminator': 'discriminator'
    }

    def __init__(self, calendar_type: str = None, deleted_instance_dates: List[datetime] = None, end_date: datetime = None, end_type: str = None, exceptions: List[MapiCalendarExceptionInfoDto] = None, frequency: str = None, modified_instance_dates: List[datetime] = None, occurrence_count: int = None, pattern_type: str = None, period: int = None, sliding_flag: bool = None, start_date: datetime = None, week_start_day: str = None, discriminator: str = None):
        """
        Mapi recurrence pattern.             
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
        :param week_start_day (str) Day of week Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        :param discriminator (str) 
        """

        self._calendar_type = None
        self._deleted_instance_dates = None
        self._end_date = None
        self._end_type = None
        self._exceptions = None
        self._frequency = None
        self._modified_instance_dates = None
        self._occurrence_count = None
        self._pattern_type = None
        self._period = None
        self._sliding_flag = None
        self._start_date = None
        self._week_start_day = None
        self._discriminator = self.__class__.__name__

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

    @property
    def calendar_type(self) -> str:
        """Gets the calendar_type of this MapiCalendarRecurrencePatternDto.

        Enumerated the calendar type of the mapi recurrence Enum, available values: Default, CalGregorian, CalGregorianUs, CalJapan, CalTaiwan, CalKorea, CalHijri, CalThai, CalHebrew, CalGregorianMeFrench, CalGregorianArabic, CalGregorianXLitEnglish, CalGregorianXLitFrench, CalLunarJapanese, CalChineseLunar, CalSaka, CalLunarEtoChn, CalLunarEtoKor, CalLunarRokuyou, CalLunarKorean, CalUmAlQura

        :return: The calendar_type of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type: str):
        """Sets the calendar_type of this MapiCalendarRecurrencePatternDto.

        Enumerated the calendar type of the mapi recurrence Enum, available values: Default, CalGregorian, CalGregorianUs, CalJapan, CalTaiwan, CalKorea, CalHijri, CalThai, CalHebrew, CalGregorianMeFrench, CalGregorianArabic, CalGregorianXLitEnglish, CalGregorianXLitFrench, CalLunarJapanese, CalChineseLunar, CalSaka, CalLunarEtoChn, CalLunarEtoKor, CalLunarRokuyou, CalLunarKorean, CalUmAlQura

        :param calendar_type: The calendar_type of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if calendar_type is None:
            raise ValueError("Invalid value for `calendar_type`, must not be `None`")
        self._calendar_type = calendar_type

    @property
    def deleted_instance_dates(self) -> List[datetime]:
        """Gets the deleted_instance_dates of this MapiCalendarRecurrencePatternDto.

        An array of dates, each of which is the original instance date of either a deleted instance or a modified instance for this recurrence.             

        :return: The deleted_instance_dates of this MapiCalendarRecurrencePatternDto.
        :rtype: list[datetime]
        """
        return self._deleted_instance_dates

    @deleted_instance_dates.setter
    def deleted_instance_dates(self, deleted_instance_dates: List[datetime]):
        """Sets the deleted_instance_dates of this MapiCalendarRecurrencePatternDto.

        An array of dates, each of which is the original instance date of either a deleted instance or a modified instance for this recurrence.             

        :param deleted_instance_dates: The deleted_instance_dates of this MapiCalendarRecurrencePatternDto.
        :type: list[datetime]
        """
        self._deleted_instance_dates = deleted_instance_dates

    @property
    def end_date(self) -> datetime:
        """Gets the end_date of this MapiCalendarRecurrencePatternDto.

        End date of an item recurrence pattern.             

        :return: The end_date of this MapiCalendarRecurrencePatternDto.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime):
        """Sets the end_date of this MapiCalendarRecurrencePatternDto.

        End date of an item recurrence pattern.             

        :param end_date: The end_date of this MapiCalendarRecurrencePatternDto.
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")
        self._end_date = end_date

    @property
    def end_type(self) -> str:
        """Gets the end_type of this MapiCalendarRecurrencePatternDto.

        Enumerates the ending type for the recurrence. Enum, available values: None, EndAfterDate, EndAfterNOccurrences, NeverEnd

        :return: The end_type of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self._end_type

    @end_type.setter
    def end_type(self, end_type: str):
        """Sets the end_type of this MapiCalendarRecurrencePatternDto.

        Enumerates the ending type for the recurrence. Enum, available values: None, EndAfterDate, EndAfterNOccurrences, NeverEnd

        :param end_type: The end_type of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if end_type is None:
            raise ValueError("Invalid value for `end_type`, must not be `None`")
        self._end_type = end_type

    @property
    def exceptions(self) -> List[MapiCalendarExceptionInfoDto]:
        """Gets the exceptions of this MapiCalendarRecurrencePatternDto.

        An exception specifies changes to an instance of a recurring series.             

        :return: The exceptions of this MapiCalendarRecurrencePatternDto.
        :rtype: list[MapiCalendarExceptionInfoDto]
        """
        return self._exceptions

    @exceptions.setter
    def exceptions(self, exceptions: List[MapiCalendarExceptionInfoDto]):
        """Sets the exceptions of this MapiCalendarRecurrencePatternDto.

        An exception specifies changes to an instance of a recurring series.             

        :param exceptions: The exceptions of this MapiCalendarRecurrencePatternDto.
        :type: list[MapiCalendarExceptionInfoDto]
        """
        self._exceptions = exceptions

    @property
    def frequency(self) -> str:
        """Gets the frequency of this MapiCalendarRecurrencePatternDto.

        Enumerates mapi calendar recurrence frequency Enum, available values: None, Daily, Weekly, Monthly, Yearly

        :return: The frequency of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: str):
        """Sets the frequency of this MapiCalendarRecurrencePatternDto.

        Enumerates mapi calendar recurrence frequency Enum, available values: None, Daily, Weekly, Monthly, Yearly

        :param frequency: The frequency of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")
        self._frequency = frequency

    @property
    def modified_instance_dates(self) -> List[datetime]:
        """Gets the modified_instance_dates of this MapiCalendarRecurrencePatternDto.

        An array of dates, each of which is the date of a modified instance.             

        :return: The modified_instance_dates of this MapiCalendarRecurrencePatternDto.
        :rtype: list[datetime]
        """
        return self._modified_instance_dates

    @modified_instance_dates.setter
    def modified_instance_dates(self, modified_instance_dates: List[datetime]):
        """Sets the modified_instance_dates of this MapiCalendarRecurrencePatternDto.

        An array of dates, each of which is the date of a modified instance.             

        :param modified_instance_dates: The modified_instance_dates of this MapiCalendarRecurrencePatternDto.
        :type: list[datetime]
        """
        self._modified_instance_dates = modified_instance_dates

    @property
    def occurrence_count(self) -> int:
        """Gets the occurrence_count of this MapiCalendarRecurrencePatternDto.

        Number of occurrences in a recurrence.             

        :return: The occurrence_count of this MapiCalendarRecurrencePatternDto.
        :rtype: int
        """
        return self._occurrence_count

    @occurrence_count.setter
    def occurrence_count(self, occurrence_count: int):
        """Sets the occurrence_count of this MapiCalendarRecurrencePatternDto.

        Number of occurrences in a recurrence.             

        :param occurrence_count: The occurrence_count of this MapiCalendarRecurrencePatternDto.
        :type: int
        """
        if occurrence_count is None:
            raise ValueError("Invalid value for `occurrence_count`, must not be `None`")
        self._occurrence_count = occurrence_count

    @property
    def pattern_type(self) -> str:
        """Gets the pattern_type of this MapiCalendarRecurrencePatternDto.

        Enumerates the mapi calendar recurrence pattern types Enum, available values: Day, Week, Month, MonthEnd, MonthNth, HjMonth, HjMonthNth, HjMonthEnd

        :return: The pattern_type of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self._pattern_type

    @pattern_type.setter
    def pattern_type(self, pattern_type: str):
        """Sets the pattern_type of this MapiCalendarRecurrencePatternDto.

        Enumerates the mapi calendar recurrence pattern types Enum, available values: Day, Week, Month, MonthEnd, MonthNth, HjMonth, HjMonthNth, HjMonthEnd

        :param pattern_type: The pattern_type of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if pattern_type is None:
            raise ValueError("Invalid value for `pattern_type`, must not be `None`")
        self._pattern_type = pattern_type

    @property
    def period(self) -> int:
        """Gets the period of this MapiCalendarRecurrencePatternDto.

        Interval at which the meeting pattern repeats.             

        :return: The period of this MapiCalendarRecurrencePatternDto.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period: int):
        """Sets the period of this MapiCalendarRecurrencePatternDto.

        Interval at which the meeting pattern repeats.             

        :param period: The period of this MapiCalendarRecurrencePatternDto.
        :type: int
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")
        self._period = period

    @property
    def sliding_flag(self) -> bool:
        """Gets the sliding_flag of this MapiCalendarRecurrencePatternDto.

        Defines whether pattern is sliding or not.             

        :return: The sliding_flag of this MapiCalendarRecurrencePatternDto.
        :rtype: bool
        """
        return self._sliding_flag

    @sliding_flag.setter
    def sliding_flag(self, sliding_flag: bool):
        """Sets the sliding_flag of this MapiCalendarRecurrencePatternDto.

        Defines whether pattern is sliding or not.             

        :param sliding_flag: The sliding_flag of this MapiCalendarRecurrencePatternDto.
        :type: bool
        """
        if sliding_flag is None:
            raise ValueError("Invalid value for `sliding_flag`, must not be `None`")
        self._sliding_flag = sliding_flag

    @property
    def start_date(self) -> datetime:
        """Gets the start_date of this MapiCalendarRecurrencePatternDto.

        Start date of an item recurrence pattern.             

        :return: The start_date of this MapiCalendarRecurrencePatternDto.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime):
        """Sets the start_date of this MapiCalendarRecurrencePatternDto.

        Start date of an item recurrence pattern.             

        :param start_date: The start_date of this MapiCalendarRecurrencePatternDto.
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def week_start_day(self) -> str:
        """Gets the week_start_day of this MapiCalendarRecurrencePatternDto.

        Day of week Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

        :return: The week_start_day of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self._week_start_day

    @week_start_day.setter
    def week_start_day(self, week_start_day: str):
        """Sets the week_start_day of this MapiCalendarRecurrencePatternDto.

        Day of week Enum, available values: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

        :param week_start_day: The week_start_day of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if week_start_day is None:
            raise ValueError("Invalid value for `week_start_day`, must not be `None`")
        self._week_start_day = week_start_day

    @property
    def discriminator(self) -> str:
        """Gets the discriminator of this MapiCalendarRecurrencePatternDto.


        :return: The discriminator of this MapiCalendarRecurrencePatternDto.
        :rtype: str
        """
        return self.__class__.__name__

    @discriminator.setter
    def discriminator(self, discriminator: str):
        """Sets the discriminator of this MapiCalendarRecurrencePatternDto.


        :param discriminator: The discriminator of this MapiCalendarRecurrencePatternDto.
        :type: str
        """
        if discriminator is None:
            raise ValueError("Invalid value for `discriminator`, must not be `None`")
        self._discriminator = self.__class__.__name__

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
        if not isinstance(other, MapiCalendarRecurrencePatternDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
