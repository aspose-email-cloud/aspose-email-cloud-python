#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CalendarAsAlternateRequest.py">
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

from AsposeEmailCloudSdk.models.calendar_dto import CalendarDto


class CalendarAsAlternateRequest(object):
    """Convert iCalendar to AlternateView request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'CalendarDto',
        'action': 'str',
        'sequence_id': 'str'
    }

    attribute_map = {
        'value': 'value',
        'action': 'action',
        'sequence_id': 'sequenceId'
    }

    def __init__(self, value: CalendarDto = None, action: str = None, sequence_id: str = None):
        """
        Convert iCalendar to AlternateView request             
        :param value: iCalendar document model             
        :type value: CalendarDto
        :param action: iCalendar actions. Enum, available values: Create, Update, Cancel
        :type action: str
        :param sequence_id: iCalendar sequence id             
        :type sequence_id: str
        """

        self._value = None
        self._action = None
        self._sequence_id = None

        if value is not None:
            self.value = value
        if action is not None:
            self.action = action
        if sequence_id is not None:
            self.sequence_id = sequence_id


    @property
    def value(self) -> CalendarDto:
        """
        iCalendar document model             

        :return: The value of this CalendarAsAlternateRequest.
        :rtype: CalendarDto
        """
        return self._value

    @value.setter
    def value(self, value: CalendarDto):
        """
        iCalendar document model             

        :param value: The value of this CalendarAsAlternateRequest.
        :type: CalendarDto
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")
        self._value = value

    @property
    def action(self) -> str:
        """
        iCalendar actions. Enum, available values: Create, Update, Cancel

        :return: The action of this CalendarAsAlternateRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """
        iCalendar actions. Enum, available values: Create, Update, Cancel

        :param action: The action of this CalendarAsAlternateRequest.
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")
        if action is not None and len(action) < 1:
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `1`")
        self._action = action

    @property
    def sequence_id(self) -> str:
        """
        iCalendar sequence id             

        :return: The sequence_id of this CalendarAsAlternateRequest.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id: str):
        """
        iCalendar sequence id             

        :param sequence_id: The sequence_id of this CalendarAsAlternateRequest.
        :type: str
        """
        self._sequence_id = sequence_id

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
        if not isinstance(other, CalendarAsAlternateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
