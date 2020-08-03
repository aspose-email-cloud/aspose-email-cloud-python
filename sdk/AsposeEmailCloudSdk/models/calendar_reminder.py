#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CalendarReminder.py">
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

from AsposeEmailCloudSdk.models.reminder_attendee import ReminderAttendee
from AsposeEmailCloudSdk.models.reminder_trigger import ReminderTrigger


class CalendarReminder(object):
    """Provides a grouping of component properties that define an alarm.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'attachments': 'list[str]',
        'attendees': 'list[ReminderAttendee]',
        'description': 'str',
        'duration': 'int',
        'repeat': 'int',
        'summary': 'str',
        'trigger': 'ReminderTrigger'
    }

    attribute_map = {
        'action': 'action',
        'attachments': 'attachments',
        'attendees': 'attendees',
        'description': 'description',
        'duration': 'duration',
        'repeat': 'repeat',
        'summary': 'summary',
        'trigger': 'trigger'
    }

    def __init__(self, action: str = None, attachments: List[str] = None, attendees: List[ReminderAttendee] = None, description: str = None, duration: int = None, repeat: int = None, summary: str = None, trigger: ReminderTrigger = None):
        """
        Provides a grouping of component properties that define an alarm.             
        :param action: Defines the action to be invoked when an alarm is triggered. Enum, available values: Audio, Display, Email, Procedure, None
        :type action: str
        :param attachments: Collection of Reminder Attachments. Could be an absolute URI or Base64 string representation of attachment content             
        :type attachments: List[str]
        :param attendees: Contains collection of ReminderAttendee objects.             
        :type attendees: List[ReminderAttendee]
        :param description: Provides a more complete description of the alarm.
        :type description: str
        :param duration: Specifies the delay period in ticks, after which the alarm will repeat.             
        :type duration: int
        :param repeat: Defines the number of time the alarm should be repeated, after the initial trigger.             
        :type repeat: int
        :param summary: Defines a short summary or subject for the alarm.
        :type summary: str
        :param trigger: Specifies when an alarm will trigger.
        :type trigger: ReminderTrigger
        """

        self._action = None
        self._attachments = None
        self._attendees = None
        self._description = None
        self._duration = None
        self._repeat = None
        self._summary = None
        self._trigger = None

        if action is not None:
            self.action = action
        if attachments is not None:
            self.attachments = attachments
        if attendees is not None:
            self.attendees = attendees
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if repeat is not None:
            self.repeat = repeat
        if summary is not None:
            self.summary = summary
        if trigger is not None:
            self.trigger = trigger


    @property
    def action(self) -> str:
        """
        Defines the action to be invoked when an alarm is triggered. Enum, available values: Audio, Display, Email, Procedure, None

        :return: The action of this CalendarReminder.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """
        Defines the action to be invoked when an alarm is triggered. Enum, available values: Audio, Display, Email, Procedure, None

        :param action: The action of this CalendarReminder.
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")
        self._action = action

    @property
    def attachments(self) -> List[str]:
        """
        Collection of Reminder Attachments. Could be an absolute URI or Base64 string representation of attachment content             

        :return: The attachments of this CalendarReminder.
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[str]):
        """
        Collection of Reminder Attachments. Could be an absolute URI or Base64 string representation of attachment content             

        :param attachments: The attachments of this CalendarReminder.
        :type: list[str]
        """
        self._attachments = attachments

    @property
    def attendees(self) -> List[ReminderAttendee]:
        """
        Contains collection of ReminderAttendee objects.             

        :return: The attendees of this CalendarReminder.
        :rtype: list[ReminderAttendee]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees: List[ReminderAttendee]):
        """
        Contains collection of ReminderAttendee objects.             

        :param attendees: The attendees of this CalendarReminder.
        :type: list[ReminderAttendee]
        """
        self._attendees = attendees

    @property
    def description(self) -> str:
        """
        Provides a more complete description of the alarm.

        :return: The description of this CalendarReminder.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """
        Provides a more complete description of the alarm.

        :param description: The description of this CalendarReminder.
        :type: str
        """
        self._description = description

    @property
    def duration(self) -> int:
        """
        Specifies the delay period in ticks, after which the alarm will repeat.             

        :return: The duration of this CalendarReminder.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """
        Specifies the delay period in ticks, after which the alarm will repeat.             

        :param duration: The duration of this CalendarReminder.
        :type: int
        """
        self._duration = duration

    @property
    def repeat(self) -> int:
        """
        Defines the number of time the alarm should be repeated, after the initial trigger.             

        :return: The repeat of this CalendarReminder.
        :rtype: int
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat: int):
        """
        Defines the number of time the alarm should be repeated, after the initial trigger.             

        :param repeat: The repeat of this CalendarReminder.
        :type: int
        """
        if repeat is None:
            raise ValueError("Invalid value for `repeat`, must not be `None`")
        self._repeat = repeat

    @property
    def summary(self) -> str:
        """
        Defines a short summary or subject for the alarm.

        :return: The summary of this CalendarReminder.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """
        Defines a short summary or subject for the alarm.

        :param summary: The summary of this CalendarReminder.
        :type: str
        """
        self._summary = summary

    @property
    def trigger(self) -> ReminderTrigger:
        """
        Specifies when an alarm will trigger.

        :return: The trigger of this CalendarReminder.
        :rtype: ReminderTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: ReminderTrigger):
        """
        Specifies when an alarm will trigger.

        :param trigger: The trigger of this CalendarReminder.
        :type: ReminderTrigger
        """
        self._trigger = trigger

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
        if not isinstance(other, CalendarReminder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
