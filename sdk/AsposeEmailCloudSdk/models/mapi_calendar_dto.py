#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarDto.py">
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
from AsposeEmailCloudSdk.models.mapi_message_item_base_dto import MapiMessageItemBaseDto
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto
from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto


class MapiCalendarDto(MapiMessageItemBaseDto):
    """Represents the mapi calendar object             
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
        'billing': 'str',
        'body': 'str',
        'body_html': 'str',
        'body_rtf': 'str',
        'body_type': 'str',
        'categories': 'list[str]',
        'companies': 'list[str]',
        'item_id': 'str',
        'message_class': 'str',
        'mileage': 'str',
        'recipients': 'list[MapiRecipientDto]',
        'sensitivity': 'str',
        'subject': 'str',
        'subject_prefix': 'str',
        'properties': 'list[MapiPropertyDto]',
        'discriminator': 'str',
        'appointment_counter_proposal': 'bool',
        'attendees': 'object',
        'busy_status': 'str',
        'client_intent': 'list[str]',
        'end_date': 'datetime',
        'end_date_time_zone': 'object',
        'is_all_day': 'bool',
        'key_words': 'str',
        'location': 'str',
        'recurrence': 'object',
        'reminder_delta': 'int',
        'reminder_file_parameter': 'str',
        'reminder_set': 'bool',
        'sequence': 'int',
        'start_date': 'datetime',
        'start_date_time_zone': 'object',
        'uid': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'billing': 'billing',
        'body': 'body',
        'body_html': 'bodyHtml',
        'body_rtf': 'bodyRtf',
        'body_type': 'bodyType',
        'categories': 'categories',
        'companies': 'companies',
        'item_id': 'itemId',
        'message_class': 'messageClass',
        'mileage': 'mileage',
        'recipients': 'recipients',
        'sensitivity': 'sensitivity',
        'subject': 'subject',
        'subject_prefix': 'subjectPrefix',
        'properties': 'properties',
        'discriminator': 'discriminator',
        'appointment_counter_proposal': 'appointmentCounterProposal',
        'attendees': 'attendees',
        'busy_status': 'busyStatus',
        'client_intent': 'clientIntent',
        'end_date': 'endDate',
        'end_date_time_zone': 'endDateTimeZone',
        'is_all_day': 'isAllDay',
        'key_words': 'keyWords',
        'location': 'location',
        'recurrence': 'recurrence',
        'reminder_delta': 'reminderDelta',
        'reminder_file_parameter': 'reminderFileParameter',
        'reminder_set': 'reminderSet',
        'sequence': 'sequence',
        'start_date': 'startDate',
        'start_date_time_zone': 'startDateTimeZone',
        'uid': 'uid'
    }

    def __init__(self, attachments: List[MapiAttachmentDto] = None, billing: str = None, body: str = None, body_html: str = None, body_rtf: str = None, body_type: str = None, categories: List[str] = None, companies: List[str] = None, item_id: str = None, message_class: str = None, mileage: str = None, recipients: List[MapiRecipientDto] = None, sensitivity: str = None, subject: str = None, subject_prefix: str = None, properties: List[MapiPropertyDto] = None, discriminator: str = None, appointment_counter_proposal: bool = None, attendees: object = None, busy_status: str = None, client_intent: List[str] = None, end_date: datetime = None, end_date_time_zone: object = None, is_all_day: bool = None, key_words: str = None, location: str = None, recurrence: object = None, reminder_delta: int = None, reminder_file_parameter: str = None, reminder_set: bool = None, sequence: int = None, start_date: datetime = None, start_date_time_zone: object = None, uid: str = None):
        """
        Represents the mapi calendar object             
        :param attachments (List[MapiAttachmentDto]) Message item attachments.             
        :param billing (str) Billing information associated with an item.             
        :param body (str) Message text.             
        :param body_html (str) Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.             
        :param body_rtf (str) RTF formatted message text.             
        :param body_type (str) The content type of message body. Enum, available values: PlainText, Html, Rtf
        :param categories (List[str]) Contains keywords or categories for the message object.             
        :param companies (List[str]) Contains the names of the companies that are associated with an item.             
        :param item_id (str) The item id, uses with a server.             
        :param message_class (str) Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.             
        :param mileage (str) Contains the mileage information that is associated with an item.             
        :param recipients (List[MapiRecipientDto]) Recipients of the message.             
        :param sensitivity (str) Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential
        :param subject (str) Subject of the message.             
        :param subject_prefix (str) Subject prefix that typically indicates some action on a message, such as \"FW: \" for forwarding.             
        :param properties (List[MapiPropertyDto]) List of MAPI properties             
        :param discriminator (str) 
        :param appointment_counter_proposal (bool) Value indicating whether a Meeting Response object is a counter proposal.             
        :param attendees (object) Attendees             
        :param busy_status (str) Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice
        :param client_intent (List[str]) Actions the user has taken on this Meeting object.             
        :param end_date (datetime) End date and time of the event. If the date is not set, default value for DateTime is returned.             
        :param end_date_time_zone (object) Time zone information that indicates the time zone of the EndDate property.             
        :param is_all_day (bool) Value indicating whether the event is an all-day event.             
        :param key_words (str) Categories of the calendar object.             
        :param location (str) Location of the event.             
        :param recurrence (object) Recurrence properties.             
        :param reminder_delta (int) Interval, in minutes, between the time at which the reminder first becomes overdue and the start time of the Calendar object.             
        :param reminder_file_parameter (str) Full path of the sound that a client SHOULD play when the reminder becomes overdue.             
        :param reminder_set (bool) Value indicating whether a reminder is set on the object.             
        :param sequence (int) Sequence number.             
        :param start_date (datetime) Start date and time of the event. If the date is not set, default value for DateTime is returned.             
        :param start_date_time_zone (object) Time zone information that indicates the time zone of the StartDate property.             
        :param uid (str) Unique identifier.             
        """
        super(MapiCalendarDto, self).__init__()

        self._appointment_counter_proposal = None
        self._attendees = None
        self._busy_status = None
        self._client_intent = None
        self._end_date = None
        self._end_date_time_zone = None
        self._is_all_day = None
        self._key_words = None
        self._location = None
        self._recurrence = None
        self._reminder_delta = None
        self._reminder_file_parameter = None
        self._reminder_set = None
        self._sequence = None
        self._start_date = None
        self._start_date_time_zone = None
        self._uid = None

        if attachments is not None:
            self.attachments = attachments
        if billing is not None:
            self.billing = billing
        if body is not None:
            self.body = body
        if body_html is not None:
            self.body_html = body_html
        if body_rtf is not None:
            self.body_rtf = body_rtf
        if body_type is not None:
            self.body_type = body_type
        if categories is not None:
            self.categories = categories
        if companies is not None:
            self.companies = companies
        if item_id is not None:
            self.item_id = item_id
        if message_class is not None:
            self.message_class = message_class
        if mileage is not None:
            self.mileage = mileage
        if recipients is not None:
            self.recipients = recipients
        if sensitivity is not None:
            self.sensitivity = sensitivity
        if subject is not None:
            self.subject = subject
        if subject_prefix is not None:
            self.subject_prefix = subject_prefix
        if properties is not None:
            self.properties = properties
        if discriminator is not None:
            self.discriminator = discriminator
        if appointment_counter_proposal is not None:
            self.appointment_counter_proposal = appointment_counter_proposal
        if attendees is not None:
            self.attendees = attendees
        if busy_status is not None:
            self.busy_status = busy_status
        if client_intent is not None:
            self.client_intent = client_intent
        if end_date is not None:
            self.end_date = end_date
        if end_date_time_zone is not None:
            self.end_date_time_zone = end_date_time_zone
        if is_all_day is not None:
            self.is_all_day = is_all_day
        if key_words is not None:
            self.key_words = key_words
        if location is not None:
            self.location = location
        if recurrence is not None:
            self.recurrence = recurrence
        if reminder_delta is not None:
            self.reminder_delta = reminder_delta
        if reminder_file_parameter is not None:
            self.reminder_file_parameter = reminder_file_parameter
        if reminder_set is not None:
            self.reminder_set = reminder_set
        if sequence is not None:
            self.sequence = sequence
        if start_date is not None:
            self.start_date = start_date
        if start_date_time_zone is not None:
            self.start_date_time_zone = start_date_time_zone
        if uid is not None:
            self.uid = uid

    @property
    def appointment_counter_proposal(self) -> bool:
        """Gets the appointment_counter_proposal of this MapiCalendarDto.

        Value indicating whether a Meeting Response object is a counter proposal.             

        :return: The appointment_counter_proposal of this MapiCalendarDto.
        :rtype: bool
        """
        return self._appointment_counter_proposal

    @appointment_counter_proposal.setter
    def appointment_counter_proposal(self, appointment_counter_proposal: bool):
        """Sets the appointment_counter_proposal of this MapiCalendarDto.

        Value indicating whether a Meeting Response object is a counter proposal.             

        :param appointment_counter_proposal: The appointment_counter_proposal of this MapiCalendarDto.
        :type: bool
        """
        if appointment_counter_proposal is None:
            raise ValueError("Invalid value for `appointment_counter_proposal`, must not be `None`")
        self._appointment_counter_proposal = appointment_counter_proposal

    @property
    def attendees(self) -> object:
        """Gets the attendees of this MapiCalendarDto.

        Attendees             

        :return: The attendees of this MapiCalendarDto.
        :rtype: object
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees: object):
        """Sets the attendees of this MapiCalendarDto.

        Attendees             

        :param attendees: The attendees of this MapiCalendarDto.
        :type: object
        """
        self._attendees = attendees

    @property
    def busy_status(self) -> str:
        """Gets the busy_status of this MapiCalendarDto.

        Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice

        :return: The busy_status of this MapiCalendarDto.
        :rtype: str
        """
        return self._busy_status

    @busy_status.setter
    def busy_status(self, busy_status: str):
        """Sets the busy_status of this MapiCalendarDto.

        Enumerates the mapi calendar possible busy status Enum, available values: Free, Tentative, Busy, OutOfOffice

        :param busy_status: The busy_status of this MapiCalendarDto.
        :type: str
        """
        if busy_status is None:
            raise ValueError("Invalid value for `busy_status`, must not be `None`")
        self._busy_status = busy_status

    @property
    def client_intent(self) -> List[str]:
        """Gets the client_intent of this MapiCalendarDto.

        Actions the user has taken on this Meeting object.              Items: Enumerates the actions the user can taken on the Meeting object Enum, available values: Manager, Delegate, DeletedWithNoResponse, DeletedExceptionWithNoResponse, RespondedTentative, RespondedAccept, RespondedDecline, ModifiedStartTime, ModifiedEndTime, ModifiedLocation, RespondedExceptionDecline, Canceled, ExceptionCanceled

        :return: The client_intent of this MapiCalendarDto.
        :rtype: list[str]
        """
        return self._client_intent

    @client_intent.setter
    def client_intent(self, client_intent: List[str]):
        """Sets the client_intent of this MapiCalendarDto.

        Actions the user has taken on this Meeting object.              Items: Enumerates the actions the user can taken on the Meeting object Enum, available values: Manager, Delegate, DeletedWithNoResponse, DeletedExceptionWithNoResponse, RespondedTentative, RespondedAccept, RespondedDecline, ModifiedStartTime, ModifiedEndTime, ModifiedLocation, RespondedExceptionDecline, Canceled, ExceptionCanceled

        :param client_intent: The client_intent of this MapiCalendarDto.
        :type: list[str]
        """
        self._client_intent = client_intent

    @property
    def end_date(self) -> datetime:
        """Gets the end_date of this MapiCalendarDto.

        End date and time of the event. If the date is not set, default value for DateTime is returned.             

        :return: The end_date of this MapiCalendarDto.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime):
        """Sets the end_date of this MapiCalendarDto.

        End date and time of the event. If the date is not set, default value for DateTime is returned.             

        :param end_date: The end_date of this MapiCalendarDto.
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")
        self._end_date = end_date

    @property
    def end_date_time_zone(self) -> object:
        """Gets the end_date_time_zone of this MapiCalendarDto.

        Time zone information that indicates the time zone of the EndDate property.             

        :return: The end_date_time_zone of this MapiCalendarDto.
        :rtype: object
        """
        return self._end_date_time_zone

    @end_date_time_zone.setter
    def end_date_time_zone(self, end_date_time_zone: object):
        """Sets the end_date_time_zone of this MapiCalendarDto.

        Time zone information that indicates the time zone of the EndDate property.             

        :param end_date_time_zone: The end_date_time_zone of this MapiCalendarDto.
        :type: object
        """
        self._end_date_time_zone = end_date_time_zone

    @property
    def is_all_day(self) -> bool:
        """Gets the is_all_day of this MapiCalendarDto.

        Value indicating whether the event is an all-day event.             

        :return: The is_all_day of this MapiCalendarDto.
        :rtype: bool
        """
        return self._is_all_day

    @is_all_day.setter
    def is_all_day(self, is_all_day: bool):
        """Sets the is_all_day of this MapiCalendarDto.

        Value indicating whether the event is an all-day event.             

        :param is_all_day: The is_all_day of this MapiCalendarDto.
        :type: bool
        """
        if is_all_day is None:
            raise ValueError("Invalid value for `is_all_day`, must not be `None`")
        self._is_all_day = is_all_day

    @property
    def key_words(self) -> str:
        """Gets the key_words of this MapiCalendarDto.

        Categories of the calendar object.             

        :return: The key_words of this MapiCalendarDto.
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words: str):
        """Sets the key_words of this MapiCalendarDto.

        Categories of the calendar object.             

        :param key_words: The key_words of this MapiCalendarDto.
        :type: str
        """
        self._key_words = key_words

    @property
    def location(self) -> str:
        """Gets the location of this MapiCalendarDto.

        Location of the event.             

        :return: The location of this MapiCalendarDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this MapiCalendarDto.

        Location of the event.             

        :param location: The location of this MapiCalendarDto.
        :type: str
        """
        self._location = location

    @property
    def recurrence(self) -> object:
        """Gets the recurrence of this MapiCalendarDto.

        Recurrence properties.             

        :return: The recurrence of this MapiCalendarDto.
        :rtype: object
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence: object):
        """Sets the recurrence of this MapiCalendarDto.

        Recurrence properties.             

        :param recurrence: The recurrence of this MapiCalendarDto.
        :type: object
        """
        self._recurrence = recurrence

    @property
    def reminder_delta(self) -> int:
        """Gets the reminder_delta of this MapiCalendarDto.

        Interval, in minutes, between the time at which the reminder first becomes overdue and the start time of the Calendar object.             

        :return: The reminder_delta of this MapiCalendarDto.
        :rtype: int
        """
        return self._reminder_delta

    @reminder_delta.setter
    def reminder_delta(self, reminder_delta: int):
        """Sets the reminder_delta of this MapiCalendarDto.

        Interval, in minutes, between the time at which the reminder first becomes overdue and the start time of the Calendar object.             

        :param reminder_delta: The reminder_delta of this MapiCalendarDto.
        :type: int
        """
        if reminder_delta is None:
            raise ValueError("Invalid value for `reminder_delta`, must not be `None`")
        self._reminder_delta = reminder_delta

    @property
    def reminder_file_parameter(self) -> str:
        """Gets the reminder_file_parameter of this MapiCalendarDto.

        Full path of the sound that a client SHOULD play when the reminder becomes overdue.             

        :return: The reminder_file_parameter of this MapiCalendarDto.
        :rtype: str
        """
        return self._reminder_file_parameter

    @reminder_file_parameter.setter
    def reminder_file_parameter(self, reminder_file_parameter: str):
        """Sets the reminder_file_parameter of this MapiCalendarDto.

        Full path of the sound that a client SHOULD play when the reminder becomes overdue.             

        :param reminder_file_parameter: The reminder_file_parameter of this MapiCalendarDto.
        :type: str
        """
        self._reminder_file_parameter = reminder_file_parameter

    @property
    def reminder_set(self) -> bool:
        """Gets the reminder_set of this MapiCalendarDto.

        Value indicating whether a reminder is set on the object.             

        :return: The reminder_set of this MapiCalendarDto.
        :rtype: bool
        """
        return self._reminder_set

    @reminder_set.setter
    def reminder_set(self, reminder_set: bool):
        """Sets the reminder_set of this MapiCalendarDto.

        Value indicating whether a reminder is set on the object.             

        :param reminder_set: The reminder_set of this MapiCalendarDto.
        :type: bool
        """
        if reminder_set is None:
            raise ValueError("Invalid value for `reminder_set`, must not be `None`")
        self._reminder_set = reminder_set

    @property
    def sequence(self) -> int:
        """Gets the sequence of this MapiCalendarDto.

        Sequence number.             

        :return: The sequence of this MapiCalendarDto.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        """Sets the sequence of this MapiCalendarDto.

        Sequence number.             

        :param sequence: The sequence of this MapiCalendarDto.
        :type: int
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")
        self._sequence = sequence

    @property
    def start_date(self) -> datetime:
        """Gets the start_date of this MapiCalendarDto.

        Start date and time of the event. If the date is not set, default value for DateTime is returned.             

        :return: The start_date of this MapiCalendarDto.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime):
        """Sets the start_date of this MapiCalendarDto.

        Start date and time of the event. If the date is not set, default value for DateTime is returned.             

        :param start_date: The start_date of this MapiCalendarDto.
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def start_date_time_zone(self) -> object:
        """Gets the start_date_time_zone of this MapiCalendarDto.

        Time zone information that indicates the time zone of the StartDate property.             

        :return: The start_date_time_zone of this MapiCalendarDto.
        :rtype: object
        """
        return self._start_date_time_zone

    @start_date_time_zone.setter
    def start_date_time_zone(self, start_date_time_zone: object):
        """Sets the start_date_time_zone of this MapiCalendarDto.

        Time zone information that indicates the time zone of the StartDate property.             

        :param start_date_time_zone: The start_date_time_zone of this MapiCalendarDto.
        :type: object
        """
        self._start_date_time_zone = start_date_time_zone

    @property
    def uid(self) -> str:
        """Gets the uid of this MapiCalendarDto.

        Unique identifier.             

        :return: The uid of this MapiCalendarDto.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this MapiCalendarDto.

        Unique identifier.             

        :param uid: The uid of this MapiCalendarDto.
        :type: str
        """
        self._uid = uid

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
        if not isinstance(other, MapiCalendarDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
