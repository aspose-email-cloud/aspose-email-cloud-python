#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiCalendarAttendeesDto.py">
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

from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto


class MapiCalendarAttendeesDto(object):
    """Mapi calendar attendees.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'appointment_recipients': 'list[MapiRecipientDto]',
        'appointment_unsendable_recipients': 'list[MapiRecipientDto]',
        'not_allow_propose': 'bool',
        'response_requested': 'bool'
    }

    attribute_map = {
        'appointment_recipients': 'appointmentRecipients',
        'appointment_unsendable_recipients': 'appointmentUnsendableRecipients',
        'not_allow_propose': 'notAllowPropose',
        'response_requested': 'responseRequested'
    }

    def __init__(self, appointment_recipients: List[MapiRecipientDto] = None, appointment_unsendable_recipients: List[MapiRecipientDto] = None, not_allow_propose: bool = None, response_requested: bool = None):
        """
        Mapi calendar attendees.             
        :param appointment_recipients: List of attendees.             
        :type appointment_recipients: List[MapiRecipientDto]
        :param appointment_unsendable_recipients: List of unsendable attendees.             
        :type appointment_unsendable_recipients: List[MapiRecipientDto]
        :param not_allow_propose: Value indicating whether attendees are not allowed to propose a new date and/or time for the meeting.             
        :type not_allow_propose: bool
        :param response_requested: Value indicating whether a response is requested to a Message object.             
        :type response_requested: bool
        """

        self._appointment_recipients = None
        self._appointment_unsendable_recipients = None
        self._not_allow_propose = None
        self._response_requested = None

        if appointment_recipients is not None:
            self.appointment_recipients = appointment_recipients
        if appointment_unsendable_recipients is not None:
            self.appointment_unsendable_recipients = appointment_unsendable_recipients
        if not_allow_propose is not None:
            self.not_allow_propose = not_allow_propose
        if response_requested is not None:
            self.response_requested = response_requested


    @property
    def appointment_recipients(self) -> List[MapiRecipientDto]:
        """
        List of attendees.             

        :return: The appointment_recipients of this MapiCalendarAttendeesDto.
        :rtype: list[MapiRecipientDto]
        """
        return self._appointment_recipients

    @appointment_recipients.setter
    def appointment_recipients(self, appointment_recipients: List[MapiRecipientDto]):
        """
        List of attendees.             

        :param appointment_recipients: The appointment_recipients of this MapiCalendarAttendeesDto.
        :type: list[MapiRecipientDto]
        """
        self._appointment_recipients = appointment_recipients

    @property
    def appointment_unsendable_recipients(self) -> List[MapiRecipientDto]:
        """
        List of unsendable attendees.             

        :return: The appointment_unsendable_recipients of this MapiCalendarAttendeesDto.
        :rtype: list[MapiRecipientDto]
        """
        return self._appointment_unsendable_recipients

    @appointment_unsendable_recipients.setter
    def appointment_unsendable_recipients(self, appointment_unsendable_recipients: List[MapiRecipientDto]):
        """
        List of unsendable attendees.             

        :param appointment_unsendable_recipients: The appointment_unsendable_recipients of this MapiCalendarAttendeesDto.
        :type: list[MapiRecipientDto]
        """
        self._appointment_unsendable_recipients = appointment_unsendable_recipients

    @property
    def not_allow_propose(self) -> bool:
        """
        Value indicating whether attendees are not allowed to propose a new date and/or time for the meeting.             

        :return: The not_allow_propose of this MapiCalendarAttendeesDto.
        :rtype: bool
        """
        return self._not_allow_propose

    @not_allow_propose.setter
    def not_allow_propose(self, not_allow_propose: bool):
        """
        Value indicating whether attendees are not allowed to propose a new date and/or time for the meeting.             

        :param not_allow_propose: The not_allow_propose of this MapiCalendarAttendeesDto.
        :type: bool
        """
        if not_allow_propose is None:
            raise ValueError("Invalid value for `not_allow_propose`, must not be `None`")
        self._not_allow_propose = not_allow_propose

    @property
    def response_requested(self) -> bool:
        """
        Value indicating whether a response is requested to a Message object.             

        :return: The response_requested of this MapiCalendarAttendeesDto.
        :rtype: bool
        """
        return self._response_requested

    @response_requested.setter
    def response_requested(self, response_requested: bool):
        """
        Value indicating whether a response is requested to a Message object.             

        :param response_requested: The response_requested of this MapiCalendarAttendeesDto.
        :type: bool
        """
        if response_requested is None:
            raise ValueError("Invalid value for `response_requested`, must not be `None`")
        self._response_requested = response_requested

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
        if not isinstance(other, MapiCalendarAttendeesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
