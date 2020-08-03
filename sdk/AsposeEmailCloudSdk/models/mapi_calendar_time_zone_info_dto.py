#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarTimeZoneInfoDto.py">
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

from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_rule_dto import MapiCalendarTimeZoneRuleDto


class MapiCalendarTimeZoneInfoDto(object):
    """Represents the mapi calendar time zone rule.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bias': 'int',
        'daylight_bias': 'int',
        'daylight_date': 'MapiCalendarTimeZoneRuleDto',
        'standard_bias': 'int',
        'standard_date': 'MapiCalendarTimeZoneRuleDto',
        'time_zone_flags': 'list[str]',
        'year': 'int'
    }

    attribute_map = {
        'bias': 'bias',
        'daylight_bias': 'daylightBias',
        'daylight_date': 'daylightDate',
        'standard_bias': 'standardBias',
        'standard_date': 'standardDate',
        'time_zone_flags': 'timeZoneFlags',
        'year': 'year'
    }

    def __init__(self, bias: int = None, daylight_bias: int = None, daylight_date: MapiCalendarTimeZoneRuleDto = None, standard_bias: int = None, standard_date: MapiCalendarTimeZoneRuleDto = None, time_zone_flags: List[str] = None, year: int = None):
        """
        Represents the mapi calendar time zone rule.             
        :param bias: Time zone's offset in minutes from UTC.             
        :type bias: int
        :param daylight_bias: Offset in minutes from lBias during daylight saving time.             
        :type daylight_bias: int
        :param daylight_date: Date and local time that indicate when to begin using the DaylightBias.             
        :type daylight_date: MapiCalendarTimeZoneRuleDto
        :param standard_bias: Offset in minutes from lBias during standard time.             
        :type standard_bias: int
        :param standard_date: Date and local time that indicate when to begin using the StandardBias.             
        :type standard_date: MapiCalendarTimeZoneRuleDto
        :param time_zone_flags: Individual bit flags that specify information about this TimeZoneRule.             
        :type time_zone_flags: List[str]
        :param year: Year in which this rule is scheduled to take effect.             
        :type year: int
        """

        self._bias = None
        self._daylight_bias = None
        self._daylight_date = None
        self._standard_bias = None
        self._standard_date = None
        self._time_zone_flags = None
        self._year = None

        if bias is not None:
            self.bias = bias
        if daylight_bias is not None:
            self.daylight_bias = daylight_bias
        if daylight_date is not None:
            self.daylight_date = daylight_date
        if standard_bias is not None:
            self.standard_bias = standard_bias
        if standard_date is not None:
            self.standard_date = standard_date
        if time_zone_flags is not None:
            self.time_zone_flags = time_zone_flags
        if year is not None:
            self.year = year


    @property
    def bias(self) -> int:
        """
        Time zone's offset in minutes from UTC.             

        :return: The bias of this MapiCalendarTimeZoneInfoDto.
        :rtype: int
        """
        return self._bias

    @bias.setter
    def bias(self, bias: int):
        """
        Time zone's offset in minutes from UTC.             

        :param bias: The bias of this MapiCalendarTimeZoneInfoDto.
        :type: int
        """
        if bias is None:
            raise ValueError("Invalid value for `bias`, must not be `None`")
        self._bias = bias

    @property
    def daylight_bias(self) -> int:
        """
        Offset in minutes from lBias during daylight saving time.             

        :return: The daylight_bias of this MapiCalendarTimeZoneInfoDto.
        :rtype: int
        """
        return self._daylight_bias

    @daylight_bias.setter
    def daylight_bias(self, daylight_bias: int):
        """
        Offset in minutes from lBias during daylight saving time.             

        :param daylight_bias: The daylight_bias of this MapiCalendarTimeZoneInfoDto.
        :type: int
        """
        if daylight_bias is None:
            raise ValueError("Invalid value for `daylight_bias`, must not be `None`")
        self._daylight_bias = daylight_bias

    @property
    def daylight_date(self) -> MapiCalendarTimeZoneRuleDto:
        """
        Date and local time that indicate when to begin using the DaylightBias.             

        :return: The daylight_date of this MapiCalendarTimeZoneInfoDto.
        :rtype: MapiCalendarTimeZoneRuleDto
        """
        return self._daylight_date

    @daylight_date.setter
    def daylight_date(self, daylight_date: MapiCalendarTimeZoneRuleDto):
        """
        Date and local time that indicate when to begin using the DaylightBias.             

        :param daylight_date: The daylight_date of this MapiCalendarTimeZoneInfoDto.
        :type: MapiCalendarTimeZoneRuleDto
        """
        self._daylight_date = daylight_date

    @property
    def standard_bias(self) -> int:
        """
        Offset in minutes from lBias during standard time.             

        :return: The standard_bias of this MapiCalendarTimeZoneInfoDto.
        :rtype: int
        """
        return self._standard_bias

    @standard_bias.setter
    def standard_bias(self, standard_bias: int):
        """
        Offset in minutes from lBias during standard time.             

        :param standard_bias: The standard_bias of this MapiCalendarTimeZoneInfoDto.
        :type: int
        """
        if standard_bias is None:
            raise ValueError("Invalid value for `standard_bias`, must not be `None`")
        self._standard_bias = standard_bias

    @property
    def standard_date(self) -> MapiCalendarTimeZoneRuleDto:
        """
        Date and local time that indicate when to begin using the StandardBias.             

        :return: The standard_date of this MapiCalendarTimeZoneInfoDto.
        :rtype: MapiCalendarTimeZoneRuleDto
        """
        return self._standard_date

    @standard_date.setter
    def standard_date(self, standard_date: MapiCalendarTimeZoneRuleDto):
        """
        Date and local time that indicate when to begin using the StandardBias.             

        :param standard_date: The standard_date of this MapiCalendarTimeZoneInfoDto.
        :type: MapiCalendarTimeZoneRuleDto
        """
        self._standard_date = standard_date

    @property
    def time_zone_flags(self) -> List[str]:
        """
        Individual bit flags that specify information about this TimeZoneRule.              Items: Enumerates the individual bit flags that specify information about TimeZoneRule Enum, available values: TzRuleFlagRecurCurrentTzReg, TzRuleFlagEffectiveTzReg

        :return: The time_zone_flags of this MapiCalendarTimeZoneInfoDto.
        :rtype: list[str]
        """
        return self._time_zone_flags

    @time_zone_flags.setter
    def time_zone_flags(self, time_zone_flags: List[str]):
        """
        Individual bit flags that specify information about this TimeZoneRule.              Items: Enumerates the individual bit flags that specify information about TimeZoneRule Enum, available values: TzRuleFlagRecurCurrentTzReg, TzRuleFlagEffectiveTzReg

        :param time_zone_flags: The time_zone_flags of this MapiCalendarTimeZoneInfoDto.
        :type: list[str]
        """
        self._time_zone_flags = time_zone_flags

    @property
    def year(self) -> int:
        """
        Year in which this rule is scheduled to take effect.             

        :return: The year of this MapiCalendarTimeZoneInfoDto.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year: int):
        """
        Year in which this rule is scheduled to take effect.             

        :param year: The year of this MapiCalendarTimeZoneInfoDto.
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
        if not isinstance(other, MapiCalendarTimeZoneInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
