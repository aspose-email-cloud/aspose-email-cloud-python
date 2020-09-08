#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarTimeZoneDto.py">
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

from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_info_dto import MapiCalendarTimeZoneInfoDto


class MapiCalendarTimeZoneDto(object):
    """Represents the mapi calendar time zone information.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key_name': 'str',
        'time_zone_rules': 'list[MapiCalendarTimeZoneInfoDto]'
    }

    attribute_map = {
        'key_name': 'keyName',
        'time_zone_rules': 'timeZoneRules'
    }

    def __init__(self, key_name: str = None, time_zone_rules: List[MapiCalendarTimeZoneInfoDto] = None):
        """
        Represents the mapi calendar time zone information.             
        :param key_name: Human-readable description of the time zone.             
        :type key_name: str
        :param time_zone_rules: Time zone rules             
        :type time_zone_rules: List[MapiCalendarTimeZoneInfoDto]
        """

        self._key_name = None
        self._time_zone_rules = None

        if key_name is not None:
            self.key_name = key_name
        if time_zone_rules is not None:
            self.time_zone_rules = time_zone_rules


    @property
    def key_name(self) -> str:
        """
        Human-readable description of the time zone.             

        :return: The key_name of this MapiCalendarTimeZoneDto.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name: str):
        """
        Human-readable description of the time zone.             

        :param key_name: The key_name of this MapiCalendarTimeZoneDto.
        :type: str
        """
        self._key_name = key_name

    @property
    def time_zone_rules(self) -> List[MapiCalendarTimeZoneInfoDto]:
        """
        Time zone rules             

        :return: The time_zone_rules of this MapiCalendarTimeZoneDto.
        :rtype: list[MapiCalendarTimeZoneInfoDto]
        """
        return self._time_zone_rules

    @time_zone_rules.setter
    def time_zone_rules(self, time_zone_rules: List[MapiCalendarTimeZoneInfoDto]):
        """
        Time zone rules             

        :param time_zone_rules: The time_zone_rules of this MapiCalendarTimeZoneDto.
        :type: list[MapiCalendarTimeZoneInfoDto]
        """
        self._time_zone_rules = time_zone_rules

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
        if not isinstance(other, MapiCalendarTimeZoneDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
