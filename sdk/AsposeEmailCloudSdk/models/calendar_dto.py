#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CalendarDto.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

from AsposeEmailCloudSdk.models.attachment import Attachment
from AsposeEmailCloudSdk.models.calendar_reminder import CalendarReminder
from AsposeEmailCloudSdk.models.mail_address import MailAddress


class CalendarDto(object):
    """iCalendar document representation             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'attachments': 'list[Attachment]',
        'attendees': 'list[MailAddress]',
        'description': 'str',
        'end_date': 'datetime',
        'end_time_zone': 'str',
        'flags': 'list[str]',
        'is_description_html': 'bool',
        'location': 'str',
        'method': 'str',
        'microsoft_busy_status': 'str',
        'microsoft_intended_status': 'str',
        'optional_attendees': 'list[MailAddress]',
        'organizer': 'MailAddress',
        'recurrence_string': 'str',
        'reminders': 'list[CalendarReminder]',
        'sequence_id': 'str',
        'start_date': 'datetime',
        'start_time_zone': 'str',
        'status': 'str',
        'summary': 'str',
        'transparency': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'attendees': 'attendees',
        'description': 'description',
        'end_date': 'endDate',
        'end_time_zone': 'endTimeZone',
        'flags': 'flags',
        'is_description_html': 'isDescriptionHtml',
        'location': 'location',
        'method': 'method',
        'microsoft_busy_status': 'microsoftBusyStatus',
        'microsoft_intended_status': 'microsoftIntendedStatus',
        'optional_attendees': 'optionalAttendees',
        'organizer': 'organizer',
        'recurrence_string': 'recurrenceString',
        'reminders': 'reminders',
        'sequence_id': 'sequenceId',
        'start_date': 'startDate',
        'start_time_zone': 'startTimeZone',
        'status': 'status',
        'summary': 'summary',
        'transparency': 'transparency'
    }

    def __init__(self, attachments: List[Attachment] = None, attendees: List[MailAddress] = None, description: str = None, end_date: datetime = None, end_time_zone: str = None, flags: List[str] = None, is_description_html: bool = None, location: str = None, method: str = None, microsoft_busy_status: str = None, microsoft_intended_status: str = None, optional_attendees: List[MailAddress] = None, organizer: MailAddress = None, recurrence_string: str = None, reminders: List[CalendarReminder] = None, sequence_id: str = None, start_date: datetime = None, start_time_zone: str = None, status: str = None, summary: str = None, transparency: str = None):
        """CalendarDto - a model defined in Swagger"""

        self._attachments = None
        self._attendees = None
        self._description = None
        self._end_date = None
        self._end_time_zone = None
        self._flags = None
        self._is_description_html = None
        self._location = None
        self._method = None
        self._microsoft_busy_status = None
        self._microsoft_intended_status = None
        self._optional_attendees = None
        self._organizer = None
        self._recurrence_string = None
        self._reminders = None
        self._sequence_id = None
        self._start_date = None
        self._start_time_zone = None
        self._status = None
        self._summary = None
        self._transparency = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if attendees is not None:
            self.attendees = attendees
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if end_time_zone is not None:
            self.end_time_zone = end_time_zone
        if flags is not None:
            self.flags = flags
        if is_description_html is not None:
            self.is_description_html = is_description_html
        if location is not None:
            self.location = location
        if method is not None:
            self.method = method
        if microsoft_busy_status is not None:
            self.microsoft_busy_status = microsoft_busy_status
        if microsoft_intended_status is not None:
            self.microsoft_intended_status = microsoft_intended_status
        if optional_attendees is not None:
            self.optional_attendees = optional_attendees
        if organizer is not None:
            self.organizer = organizer
        if recurrence_string is not None:
            self.recurrence_string = recurrence_string
        if reminders is not None:
            self.reminders = reminders
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if start_date is not None:
            self.start_date = start_date
        if start_time_zone is not None:
            self.start_time_zone = start_time_zone
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if transparency is not None:
            self.transparency = transparency

    @property
    def attachments(self) -> List[Attachment]:
        """Gets the attachments of this CalendarDto.

        Document attachments

        :return: The attachments of this CalendarDto.
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[Attachment]):
        """Sets the attachments of this CalendarDto.

        Document attachments

        :param attachments: The attachments of this CalendarDto.
        :type: list[Attachment]
        """
        self._attachments = attachments

    @property
    def attendees(self) -> List[MailAddress]:
        """Gets the attendees of this CalendarDto.

        Event attendees

        :return: The attendees of this CalendarDto.
        :rtype: list[MailAddress]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees: List[MailAddress]):
        """Sets the attendees of this CalendarDto.

        Event attendees

        :param attendees: The attendees of this CalendarDto.
        :type: list[MailAddress]
        """
        if attendees is None:
            raise ValueError("Invalid value for `attendees`, must not be `None`")
        self._attendees = attendees

    @property
    def description(self) -> str:
        """Gets the description of this CalendarDto.

        Description

        :return: The description of this CalendarDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this CalendarDto.

        Description

        :param description: The description of this CalendarDto.
        :type: str
        """
        self._description = description

    @property
    def end_date(self) -> datetime:
        """Gets the end_date of this CalendarDto.

        End date

        :return: The end_date of this CalendarDto.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime):
        """Sets the end_date of this CalendarDto.

        End date

        :param end_date: The end_date of this CalendarDto.
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")
        self._end_date = end_date

    @property
    def end_time_zone(self) -> str:
        """Gets the end_time_zone of this CalendarDto.

        End time zone

        :return: The end_time_zone of this CalendarDto.
        :rtype: str
        """
        return self._end_time_zone

    @end_time_zone.setter
    def end_time_zone(self, end_time_zone: str):
        """Sets the end_time_zone of this CalendarDto.

        End time zone

        :param end_time_zone: The end_time_zone of this CalendarDto.
        :type: str
        """
        self._end_time_zone = end_time_zone

    @property
    def flags(self) -> List[str]:
        """Gets the flags of this CalendarDto.

        Appointment flags

        :return: The flags of this CalendarDto.
        :rtype: list[str]
        """
        return self._flags

    @flags.setter
    def flags(self, flags: List[str]):
        """Sets the flags of this CalendarDto.

        Appointment flags

        :param flags: The flags of this CalendarDto.
        :type: list[str]
        """
        self._flags = flags

    @property
    def is_description_html(self) -> bool:
        """Gets the is_description_html of this CalendarDto.

        Indicates if description is in HTML format

        :return: The is_description_html of this CalendarDto.
        :rtype: bool
        """
        return self._is_description_html

    @is_description_html.setter
    def is_description_html(self, is_description_html: bool):
        """Sets the is_description_html of this CalendarDto.

        Indicates if description is in HTML format

        :param is_description_html: The is_description_html of this CalendarDto.
        :type: bool
        """
        if is_description_html is None:
            raise ValueError("Invalid value for `is_description_html`, must not be `None`")
        self._is_description_html = is_description_html

    @property
    def location(self) -> str:
        """Gets the location of this CalendarDto.

        Location

        :return: The location of this CalendarDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this CalendarDto.

        Location

        :param location: The location of this CalendarDto.
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")
        if location is not None and len(location) < 1:
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")
        self._location = location

    @property
    def method(self) -> str:
        """Gets the method of this CalendarDto.

        Defines the iCalendar object method type associated with the calendar document. Enum, available values: None, Publish, Request, Reply, Add, Cancel, Refresh, Counter, DeclineCounter

        :return: The method of this CalendarDto.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this CalendarDto.

        Defines the iCalendar object method type associated with the calendar document. Enum, available values: None, Publish, Request, Reply, Add, Cancel, Refresh, Counter, DeclineCounter

        :param method: The method of this CalendarDto.
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")
        self._method = method

    @property
    def microsoft_busy_status(self) -> str:
        """Gets the microsoft_busy_status of this CalendarDto.

        Specifies the BUSY status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof

        :return: The microsoft_busy_status of this CalendarDto.
        :rtype: str
        """
        return self._microsoft_busy_status

    @microsoft_busy_status.setter
    def microsoft_busy_status(self, microsoft_busy_status: str):
        """Sets the microsoft_busy_status of this CalendarDto.

        Specifies the BUSY status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof

        :param microsoft_busy_status: The microsoft_busy_status of this CalendarDto.
        :type: str
        """
        if microsoft_busy_status is None:
            raise ValueError("Invalid value for `microsoft_busy_status`, must not be `None`")
        self._microsoft_busy_status = microsoft_busy_status

    @property
    def microsoft_intended_status(self) -> str:
        """Gets the microsoft_intended_status of this CalendarDto.

        Specifies the INTENDED status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof

        :return: The microsoft_intended_status of this CalendarDto.
        :rtype: str
        """
        return self._microsoft_intended_status

    @microsoft_intended_status.setter
    def microsoft_intended_status(self, microsoft_intended_status: str):
        """Sets the microsoft_intended_status of this CalendarDto.

        Specifies the INTENDED status. Enum, available values: NotDefined, Free, Tentative, Busy, Oof

        :param microsoft_intended_status: The microsoft_intended_status of this CalendarDto.
        :type: str
        """
        if microsoft_intended_status is None:
            raise ValueError("Invalid value for `microsoft_intended_status`, must not be `None`")
        self._microsoft_intended_status = microsoft_intended_status

    @property
    def optional_attendees(self) -> List[MailAddress]:
        """Gets the optional_attendees of this CalendarDto.

        Optional attendees             

        :return: The optional_attendees of this CalendarDto.
        :rtype: list[MailAddress]
        """
        return self._optional_attendees

    @optional_attendees.setter
    def optional_attendees(self, optional_attendees: List[MailAddress]):
        """Sets the optional_attendees of this CalendarDto.

        Optional attendees             

        :param optional_attendees: The optional_attendees of this CalendarDto.
        :type: list[MailAddress]
        """
        self._optional_attendees = optional_attendees

    @property
    def organizer(self) -> MailAddress:
        """Gets the organizer of this CalendarDto.

        Event organizer             

        :return: The organizer of this CalendarDto.
        :rtype: MailAddress
        """
        return self._organizer

    @organizer.setter
    def organizer(self, organizer: MailAddress):
        """Sets the organizer of this CalendarDto.

        Event organizer             

        :param organizer: The organizer of this CalendarDto.
        :type: MailAddress
        """
        if organizer is None:
            raise ValueError("Invalid value for `organizer`, must not be `None`")
        self._organizer = organizer

    @property
    def recurrence_string(self) -> str:
        """Gets the recurrence_string of this CalendarDto.

        String representation of recurrence pattern (See iCalendar RFC, \"Recurrence rule\" section). For example:               For daily recurrence:         \"FREQ=DAILY;COUNT=10;WKST=MO\"                   For monthly recurrence:         \"BYSETPOS=1;BYDAY=MO,TU,WE,TH,FR;FREQ=MONTHLY;INTERVAL=10;WKST=MO\"                   For yearly recurrence:         \"BYMONTHDAY=30;BYMONTH=1;FREQ=YEARLY;WKST=MO\"                   

        :return: The recurrence_string of this CalendarDto.
        :rtype: str
        """
        return self._recurrence_string

    @recurrence_string.setter
    def recurrence_string(self, recurrence_string: str):
        """Sets the recurrence_string of this CalendarDto.

        String representation of recurrence pattern (See iCalendar RFC, \"Recurrence rule\" section). For example:               For daily recurrence:         \"FREQ=DAILY;COUNT=10;WKST=MO\"                   For monthly recurrence:         \"BYSETPOS=1;BYDAY=MO,TU,WE,TH,FR;FREQ=MONTHLY;INTERVAL=10;WKST=MO\"                   For yearly recurrence:         \"BYMONTHDAY=30;BYMONTH=1;FREQ=YEARLY;WKST=MO\"                   

        :param recurrence_string: The recurrence_string of this CalendarDto.
        :type: str
        """
        self._recurrence_string = recurrence_string

    @property
    def reminders(self) -> List[CalendarReminder]:
        """Gets the reminders of this CalendarDto.

        Reminders

        :return: The reminders of this CalendarDto.
        :rtype: list[CalendarReminder]
        """
        return self._reminders

    @reminders.setter
    def reminders(self, reminders: List[CalendarReminder]):
        """Sets the reminders of this CalendarDto.

        Reminders

        :param reminders: The reminders of this CalendarDto.
        :type: list[CalendarReminder]
        """
        self._reminders = reminders

    @property
    def sequence_id(self) -> str:
        """Gets the sequence_id of this CalendarDto.

        The sequence id. Read only.

        :return: The sequence_id of this CalendarDto.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id: str):
        """Sets the sequence_id of this CalendarDto.

        The sequence id. Read only.

        :param sequence_id: The sequence_id of this CalendarDto.
        :type: str
        """
        self._sequence_id = sequence_id

    @property
    def start_date(self) -> datetime:
        """Gets the start_date of this CalendarDto.

        Start date

        :return: The start_date of this CalendarDto.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime):
        """Sets the start_date of this CalendarDto.

        Start date

        :param start_date: The start_date of this CalendarDto.
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def start_time_zone(self) -> str:
        """Gets the start_time_zone of this CalendarDto.

        Start time zone

        :return: The start_time_zone of this CalendarDto.
        :rtype: str
        """
        return self._start_time_zone

    @start_time_zone.setter
    def start_time_zone(self, start_time_zone: str):
        """Sets the start_time_zone of this CalendarDto.

        Start time zone

        :param start_time_zone: The start_time_zone of this CalendarDto.
        :type: str
        """
        self._start_time_zone = start_time_zone

    @property
    def status(self) -> str:
        """Gets the status of this CalendarDto.

        Defines the overall status or confirmation for the calendar document. Enum, available values: NotDefined, Cancelled, Tentative, Confirmed

        :return: The status of this CalendarDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this CalendarDto.

        Defines the overall status or confirmation for the calendar document. Enum, available values: NotDefined, Cancelled, Tentative, Confirmed

        :param status: The status of this CalendarDto.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        self._status = status

    @property
    def summary(self) -> str:
        """Gets the summary of this CalendarDto.

        Summary

        :return: The summary of this CalendarDto.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """Sets the summary of this CalendarDto.

        Summary

        :param summary: The summary of this CalendarDto.
        :type: str
        """
        self._summary = summary

    @property
    def transparency(self) -> str:
        """Gets the transparency of this CalendarDto.

        Specifies whether or not this appointment is intended to be visible in availability searches. Enum, available values: NotDefined, Transparent, Opaque

        :return: The transparency of this CalendarDto.
        :rtype: str
        """
        return self._transparency

    @transparency.setter
    def transparency(self, transparency: str):
        """Sets the transparency of this CalendarDto.

        Specifies whether or not this appointment is intended to be visible in availability searches. Enum, available values: NotDefined, Transparent, Opaque

        :param transparency: The transparency of this CalendarDto.
        :type: str
        """
        if transparency is None:
            raise ValueError("Invalid value for `transparency`, must not be `None`")
        self._transparency = transparency

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
        if not isinstance(other, CalendarDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
