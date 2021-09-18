#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarExceptionInfoDto.py">
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

from AsposeEmailCloudSdk.models.mapi_attachment_dto import MapiAttachmentDto


class MapiCalendarExceptionInfoDto(object):
    """An exception specifies changes to an instance of a recurring series.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'attachments': 'list[MapiAttachmentDto]',
        'body': 'str',
        'busy_status': 'str',
        'end_date_time': 'datetime',
        'has_attachment': 'bool',
        'location': 'str',
        'meeting_type': 'str',
        'original_start_date': 'datetime',
        'override_flags': 'list[str]',
        'reminder_delta': 'int',
        'reminder_set': 'bool',
        'start_date_time': 'datetime',
        'subject': 'str',
        'sub_type': 'int'
    }

    attribute_map = {
        'attachments': 'attachments',
        'body': 'body',
        'busy_status': 'busyStatus',
        'end_date_time': 'endDateTime',
        'has_attachment': 'hasAttachment',
        'location': 'location',
        'meeting_type': 'meetingType',
        'original_start_date': 'originalStartDate',
        'override_flags': 'overrideFlags',
        'reminder_delta': 'reminderDelta',
        'reminder_set': 'reminderSet',
        'start_date_time': 'startDateTime',
        'subject': 'subject',
        'sub_type': 'subType'
    }

    def __init__(self, attachments: List[MapiAttachmentDto] = None, body: str = None, busy_status: str = None, end_date_time: datetime = None, has_attachment: bool = None, location: str = None, meeting_type: str = None, original_start_date: datetime = None, override_flags: List[str] = None, reminder_delta: int = None, reminder_set: bool = None, start_date_time: datetime = None, subject: str = None, sub_type: int = None):
        """
        An exception specifies changes to an instance of a recurring series.             
        :param attachments: Attachments in the recurrence exception.             
        :type attachments: List[MapiAttachmentDto]
        :param body: Body.             
        :type body: str
        :param busy_status: Enumerates the mapi calendar possible busy status. Enum, available values: Free, Tentative, Busy, OutOfOffice
        :type busy_status: str
        :param end_date_time: End date.             
        :type end_date_time: datetime
        :param has_attachment: Value of this field specifies whether the Exception Embedded Message object contains attachments.             
        :type has_attachment: bool
        :param location: Location.             
        :type location: str
        :param meeting_type: Enumerates the appointment state. Enum, available values: Meeting, Received, Canceled
        :type meeting_type: str
        :param original_start_date: Original start date.             
        :type original_start_date: datetime
        :param override_flags: Override flags.             
        :type override_flags: List[str]
        :param reminder_delta: Reminder delta.             
        :type reminder_delta: int
        :param reminder_set: Value for the PidLidReminderSet property.             
        :type reminder_set: bool
        :param start_date_time: Start date.             
        :type start_date_time: datetime
        :param subject: Subject.             
        :type subject: str
        :param sub_type: SubType.             
        :type sub_type: int
        """

        self._attachments = None
        self._body = None
        self._busy_status = None
        self._end_date_time = None
        self._has_attachment = None
        self._location = None
        self._meeting_type = None
        self._original_start_date = None
        self._override_flags = None
        self._reminder_delta = None
        self._reminder_set = None
        self._start_date_time = None
        self._subject = None
        self._sub_type = None

        if attachments is not None:
            self.attachments = attachments
        if body is not None:
            self.body = body
        if busy_status is not None:
            self.busy_status = busy_status
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if has_attachment is not None:
            self.has_attachment = has_attachment
        if location is not None:
            self.location = location
        if meeting_type is not None:
            self.meeting_type = meeting_type
        if original_start_date is not None:
            self.original_start_date = original_start_date
        if override_flags is not None:
            self.override_flags = override_flags
        if reminder_delta is not None:
            self.reminder_delta = reminder_delta
        if reminder_set is not None:
            self.reminder_set = reminder_set
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if subject is not None:
            self.subject = subject
        if sub_type is not None:
            self.sub_type = sub_type


    @property
    def attachments(self) -> List[MapiAttachmentDto]:
        """
        Attachments in the recurrence exception.             

        :return: The attachments of this MapiCalendarExceptionInfoDto.
        :rtype: list[MapiAttachmentDto]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[MapiAttachmentDto]):
        """
        Attachments in the recurrence exception.             

        :param attachments: The attachments of this MapiCalendarExceptionInfoDto.
        :type: list[MapiAttachmentDto]
        """
        self._attachments = attachments

    @property
    def body(self) -> str:
        """
        Body.             

        :return: The body of this MapiCalendarExceptionInfoDto.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body: str):
        """
        Body.             

        :param body: The body of this MapiCalendarExceptionInfoDto.
        :type: str
        """
        self._body = body

    @property
    def busy_status(self) -> str:
        """
        Enumerates the mapi calendar possible busy status. Enum, available values: Free, Tentative, Busy, OutOfOffice

        :return: The busy_status of this MapiCalendarExceptionInfoDto.
        :rtype: str
        """
        return self._busy_status

    @busy_status.setter
    def busy_status(self, busy_status: str):
        """
        Enumerates the mapi calendar possible busy status. Enum, available values: Free, Tentative, Busy, OutOfOffice

        :param busy_status: The busy_status of this MapiCalendarExceptionInfoDto.
        :type: str
        """
        if busy_status is None:
            raise ValueError("Invalid value for `busy_status`, must not be `None`")
        self._busy_status = busy_status

    @property
    def end_date_time(self) -> datetime:
        """
        End date.             

        :return: The end_date_time of this MapiCalendarExceptionInfoDto.
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time: datetime):
        """
        End date.             

        :param end_date_time: The end_date_time of this MapiCalendarExceptionInfoDto.
        :type: datetime
        """
        if end_date_time is None:
            raise ValueError("Invalid value for `end_date_time`, must not be `None`")
        self._end_date_time = end_date_time

    @property
    def has_attachment(self) -> bool:
        """
        Value of this field specifies whether the Exception Embedded Message object contains attachments.             

        :return: The has_attachment of this MapiCalendarExceptionInfoDto.
        :rtype: bool
        """
        return self._has_attachment

    @has_attachment.setter
    def has_attachment(self, has_attachment: bool):
        """
        Value of this field specifies whether the Exception Embedded Message object contains attachments.             

        :param has_attachment: The has_attachment of this MapiCalendarExceptionInfoDto.
        :type: bool
        """
        if has_attachment is None:
            raise ValueError("Invalid value for `has_attachment`, must not be `None`")
        self._has_attachment = has_attachment

    @property
    def location(self) -> str:
        """
        Location.             

        :return: The location of this MapiCalendarExceptionInfoDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Location.             

        :param location: The location of this MapiCalendarExceptionInfoDto.
        :type: str
        """
        self._location = location

    @property
    def meeting_type(self) -> str:
        """
        Enumerates the appointment state. Enum, available values: Meeting, Received, Canceled

        :return: The meeting_type of this MapiCalendarExceptionInfoDto.
        :rtype: str
        """
        return self._meeting_type

    @meeting_type.setter
    def meeting_type(self, meeting_type: str):
        """
        Enumerates the appointment state. Enum, available values: Meeting, Received, Canceled

        :param meeting_type: The meeting_type of this MapiCalendarExceptionInfoDto.
        :type: str
        """
        if meeting_type is None:
            raise ValueError("Invalid value for `meeting_type`, must not be `None`")
        self._meeting_type = meeting_type

    @property
    def original_start_date(self) -> datetime:
        """
        Original start date.             

        :return: The original_start_date of this MapiCalendarExceptionInfoDto.
        :rtype: datetime
        """
        return self._original_start_date

    @original_start_date.setter
    def original_start_date(self, original_start_date: datetime):
        """
        Original start date.             

        :param original_start_date: The original_start_date of this MapiCalendarExceptionInfoDto.
        :type: datetime
        """
        if original_start_date is None:
            raise ValueError("Invalid value for `original_start_date`, must not be `None`")
        self._original_start_date = original_start_date

    @property
    def override_flags(self) -> List[str]:
        """
        Override flags.              Items: Specifies what data in the MapiCalendarOverride structure has a value different from the recurring series. Enum, available values: Subject, MeetingType, ReminderDelta, Reminder, Location, BusyStatus, Attachment, Subtype, AppointmentColor, ExceptionalBody

        :return: The override_flags of this MapiCalendarExceptionInfoDto.
        :rtype: list[str]
        """
        return self._override_flags

    @override_flags.setter
    def override_flags(self, override_flags: List[str]):
        """
        Override flags.              Items: Specifies what data in the MapiCalendarOverride structure has a value different from the recurring series. Enum, available values: Subject, MeetingType, ReminderDelta, Reminder, Location, BusyStatus, Attachment, Subtype, AppointmentColor, ExceptionalBody

        :param override_flags: The override_flags of this MapiCalendarExceptionInfoDto.
        :type: list[str]
        """
        self._override_flags = override_flags

    @property
    def reminder_delta(self) -> int:
        """
        Reminder delta.             

        :return: The reminder_delta of this MapiCalendarExceptionInfoDto.
        :rtype: int
        """
        return self._reminder_delta

    @reminder_delta.setter
    def reminder_delta(self, reminder_delta: int):
        """
        Reminder delta.             

        :param reminder_delta: The reminder_delta of this MapiCalendarExceptionInfoDto.
        :type: int
        """
        if reminder_delta is None:
            raise ValueError("Invalid value for `reminder_delta`, must not be `None`")
        self._reminder_delta = reminder_delta

    @property
    def reminder_set(self) -> bool:
        """
        Value for the PidLidReminderSet property.             

        :return: The reminder_set of this MapiCalendarExceptionInfoDto.
        :rtype: bool
        """
        return self._reminder_set

    @reminder_set.setter
    def reminder_set(self, reminder_set: bool):
        """
        Value for the PidLidReminderSet property.             

        :param reminder_set: The reminder_set of this MapiCalendarExceptionInfoDto.
        :type: bool
        """
        if reminder_set is None:
            raise ValueError("Invalid value for `reminder_set`, must not be `None`")
        self._reminder_set = reminder_set

    @property
    def start_date_time(self) -> datetime:
        """
        Start date.             

        :return: The start_date_time of this MapiCalendarExceptionInfoDto.
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time: datetime):
        """
        Start date.             

        :param start_date_time: The start_date_time of this MapiCalendarExceptionInfoDto.
        :type: datetime
        """
        if start_date_time is None:
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")
        self._start_date_time = start_date_time

    @property
    def subject(self) -> str:
        """
        Subject.             

        :return: The subject of this MapiCalendarExceptionInfoDto.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """
        Subject.             

        :param subject: The subject of this MapiCalendarExceptionInfoDto.
        :type: str
        """
        self._subject = subject

    @property
    def sub_type(self) -> int:
        """
        SubType.             

        :return: The sub_type of this MapiCalendarExceptionInfoDto.
        :rtype: int
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type: int):
        """
        SubType.             

        :param sub_type: The sub_type of this MapiCalendarExceptionInfoDto.
        :type: int
        """
        if sub_type is None:
            raise ValueError("Invalid value for `sub_type`, must not be `None`")
        self._sub_type = sub_type

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
        if not isinstance(other, MapiCalendarExceptionInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
