#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarEventRecurrenceDto.py">
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

from AsposeEmailCloudSdk.models.mapi_calendar_recurrence_pattern_dto import MapiCalendarRecurrencePatternDto
from AsposeEmailCloudSdk.models.mapi_calendar_time_zone_dto import MapiCalendarTimeZoneDto


class MapiCalendarEventRecurrenceDto(object):
    """Recurrence properties of calendar object.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'appointment_time_zone_definition_recur': 'MapiCalendarTimeZoneDto',
        'clip_end': 'datetime',
        'clip_start': 'datetime',
        'is_exception': 'bool',
        'recurrence_pattern': 'MapiCalendarRecurrencePatternDto',
        'time_zone_struct': 'MapiCalendarTimeZoneDto'
    }

    attribute_map = {
        'appointment_time_zone_definition_recur': 'appointmentTimeZoneDefinitionRecur',
        'clip_end': 'clipEnd',
        'clip_start': 'clipStart',
        'is_exception': 'isException',
        'recurrence_pattern': 'recurrencePattern',
        'time_zone_struct': 'timeZoneStruct'
    }

    def __init__(self, appointment_time_zone_definition_recur: MapiCalendarTimeZoneDto = None, clip_end: datetime = None, clip_start: datetime = None, is_exception: bool = None, recurrence_pattern: MapiCalendarRecurrencePatternDto = None, time_zone_struct: MapiCalendarTimeZoneDto = None):
        """
        Recurrence properties of calendar object.             
        :param appointment_time_zone_definition_recur: Time zone information that describes how to convert the meeting date and time on a recurring series to and from UTC.             
        :type appointment_time_zone_definition_recur: MapiCalendarTimeZoneDto
        :param clip_end: Date of the last instance.             
        :type clip_end: datetime
        :param clip_start: Date of the first instance.             
        :type clip_start: datetime
        :param is_exception: Value indicating whether the object represents an exception.             
        :type is_exception: bool
        :param recurrence_pattern: Recurrence pattern.             
        :type recurrence_pattern: MapiCalendarRecurrencePatternDto
        :param time_zone_struct: Time zone information for a recurring meeting.             
        :type time_zone_struct: MapiCalendarTimeZoneDto
        """

        self._appointment_time_zone_definition_recur = None
        self._clip_end = None
        self._clip_start = None
        self._is_exception = None
        self._recurrence_pattern = None
        self._time_zone_struct = None

        if appointment_time_zone_definition_recur is not None:
            self.appointment_time_zone_definition_recur = appointment_time_zone_definition_recur
        if clip_end is not None:
            self.clip_end = clip_end
        if clip_start is not None:
            self.clip_start = clip_start
        if is_exception is not None:
            self.is_exception = is_exception
        if recurrence_pattern is not None:
            self.recurrence_pattern = recurrence_pattern
        if time_zone_struct is not None:
            self.time_zone_struct = time_zone_struct


    @property
    def appointment_time_zone_definition_recur(self) -> MapiCalendarTimeZoneDto:
        """
        Time zone information that describes how to convert the meeting date and time on a recurring series to and from UTC.             

        :return: The appointment_time_zone_definition_recur of this MapiCalendarEventRecurrenceDto.
        :rtype: MapiCalendarTimeZoneDto
        """
        return self._appointment_time_zone_definition_recur

    @appointment_time_zone_definition_recur.setter
    def appointment_time_zone_definition_recur(self, appointment_time_zone_definition_recur: MapiCalendarTimeZoneDto):
        """
        Time zone information that describes how to convert the meeting date and time on a recurring series to and from UTC.             

        :param appointment_time_zone_definition_recur: The appointment_time_zone_definition_recur of this MapiCalendarEventRecurrenceDto.
        :type: MapiCalendarTimeZoneDto
        """
        self._appointment_time_zone_definition_recur = appointment_time_zone_definition_recur

    @property
    def clip_end(self) -> datetime:
        """
        Date of the last instance.             

        :return: The clip_end of this MapiCalendarEventRecurrenceDto.
        :rtype: datetime
        """
        return self._clip_end

    @clip_end.setter
    def clip_end(self, clip_end: datetime):
        """
        Date of the last instance.             

        :param clip_end: The clip_end of this MapiCalendarEventRecurrenceDto.
        :type: datetime
        """
        if clip_end is None:
            raise ValueError("Invalid value for `clip_end`, must not be `None`")
        self._clip_end = clip_end

    @property
    def clip_start(self) -> datetime:
        """
        Date of the first instance.             

        :return: The clip_start of this MapiCalendarEventRecurrenceDto.
        :rtype: datetime
        """
        return self._clip_start

    @clip_start.setter
    def clip_start(self, clip_start: datetime):
        """
        Date of the first instance.             

        :param clip_start: The clip_start of this MapiCalendarEventRecurrenceDto.
        :type: datetime
        """
        if clip_start is None:
            raise ValueError("Invalid value for `clip_start`, must not be `None`")
        self._clip_start = clip_start

    @property
    def is_exception(self) -> bool:
        """
        Value indicating whether the object represents an exception.             

        :return: The is_exception of this MapiCalendarEventRecurrenceDto.
        :rtype: bool
        """
        return self._is_exception

    @is_exception.setter
    def is_exception(self, is_exception: bool):
        """
        Value indicating whether the object represents an exception.             

        :param is_exception: The is_exception of this MapiCalendarEventRecurrenceDto.
        :type: bool
        """
        if is_exception is None:
            raise ValueError("Invalid value for `is_exception`, must not be `None`")
        self._is_exception = is_exception

    @property
    def recurrence_pattern(self) -> MapiCalendarRecurrencePatternDto:
        """
        Recurrence pattern.             

        :return: The recurrence_pattern of this MapiCalendarEventRecurrenceDto.
        :rtype: MapiCalendarRecurrencePatternDto
        """
        return self._recurrence_pattern

    @recurrence_pattern.setter
    def recurrence_pattern(self, recurrence_pattern: MapiCalendarRecurrencePatternDto):
        """
        Recurrence pattern.             

        :param recurrence_pattern: The recurrence_pattern of this MapiCalendarEventRecurrenceDto.
        :type: MapiCalendarRecurrencePatternDto
        """
        self._recurrence_pattern = recurrence_pattern

    @property
    def time_zone_struct(self) -> MapiCalendarTimeZoneDto:
        """
        Time zone information for a recurring meeting.             

        :return: The time_zone_struct of this MapiCalendarEventRecurrenceDto.
        :rtype: MapiCalendarTimeZoneDto
        """
        return self._time_zone_struct

    @time_zone_struct.setter
    def time_zone_struct(self, time_zone_struct: MapiCalendarTimeZoneDto):
        """
        Time zone information for a recurring meeting.             

        :param time_zone_struct: The time_zone_struct of this MapiCalendarEventRecurrenceDto.
        :type: MapiCalendarTimeZoneDto
        """
        self._time_zone_struct = time_zone_struct

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
        if not isinstance(other, MapiCalendarEventRecurrenceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
