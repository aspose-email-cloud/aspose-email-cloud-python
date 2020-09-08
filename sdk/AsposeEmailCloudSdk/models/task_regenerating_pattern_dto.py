#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="TaskRegeneratingPatternDto.py">
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


class TaskRegeneratingPatternDto(RecurrencePatternDto):
    """Represents the regenerating recurrence pattern that specifies how many days, weeks, months or years after the completion of the current task the next occurrence will be due.             
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
        'regenerating_type': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'occurs': 'occurs',
        'end_date': 'endDate',
        'week_start': 'weekStart',
        'discriminator': 'discriminator',
        'regenerating_type': 'regeneratingType'
    }

    def __init__(self, interval: int = None, occurs: int = None, end_date: datetime = None, week_start: str = None, regenerating_type: str = None):
        """
        Represents the regenerating recurrence pattern that specifies how many days, weeks, months or years after the completion of the current task the next occurrence will be due.             
        :param interval: Number of recurrence units.             
        :type interval: int
        :param occurs: Number of occurrences of the recurrence pattern.             
        :type occurs: int
        :param end_date: End date.             
        :type end_date: datetime
        :param week_start: Represents the day of the week. Enum, available values: None, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Day, WeekDay, WeekendDay
        :type week_start: str
        :param regenerating_type: Enumerates the types of regenerating pattern. Enum, available values: Daily, Weekly, Monthly, Yearly
        :type regenerating_type: str
        """
        super(TaskRegeneratingPatternDto, self).__init__()

        self._regenerating_type = None

        if interval is not None:
            self.interval = interval
        if occurs is not None:
            self.occurs = occurs
        if end_date is not None:
            self.end_date = end_date
        if week_start is not None:
            self.week_start = week_start
        if regenerating_type is not None:
            self.regenerating_type = regenerating_type


    @property
    def regenerating_type(self) -> str:
        """
        Enumerates the types of regenerating pattern. Enum, available values: Daily, Weekly, Monthly, Yearly

        :return: The regenerating_type of this TaskRegeneratingPatternDto.
        :rtype: str
        """
        return self._regenerating_type

    @regenerating_type.setter
    def regenerating_type(self, regenerating_type: str):
        """
        Enumerates the types of regenerating pattern. Enum, available values: Daily, Weekly, Monthly, Yearly

        :param regenerating_type: The regenerating_type of this TaskRegeneratingPatternDto.
        :type: str
        """
        if regenerating_type is None:
            raise ValueError("Invalid value for `regenerating_type`, must not be `None`")
        self._regenerating_type = regenerating_type

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
        if not isinstance(other, TaskRegeneratingPatternDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
