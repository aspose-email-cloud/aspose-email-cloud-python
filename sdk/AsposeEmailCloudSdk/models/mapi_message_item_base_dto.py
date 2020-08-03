#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiMessageItemBaseDto.py">
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
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto
from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto


class MapiMessageItemBaseDto(object):
    """Base Dto for MapiMessage, MapiCalendar or MapiContact             
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
        'discriminator': 'str'
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
        'discriminator': 'discriminator'
    }

    def __init__(self, attachments: List[MapiAttachmentDto] = None, billing: str = None, body: str = None, body_html: str = None, body_rtf: str = None, body_type: str = None, categories: List[str] = None, companies: List[str] = None, item_id: str = None, message_class: str = None, mileage: str = None, recipients: List[MapiRecipientDto] = None, sensitivity: str = None, subject: str = None, subject_prefix: str = None, properties: List[MapiPropertyDto] = None, discriminator: str = None):
        """
        Base Dto for MapiMessage, MapiCalendar or MapiContact             
        :param attachments: Message item attachments.             
        :type attachments: List[MapiAttachmentDto]
        :param billing: Billing information associated with an item.             
        :type billing: str
        :param body: Message text.             
        :type body: str
        :param body_html: Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.             
        :type body_html: str
        :param body_rtf: RTF formatted message text.             
        :type body_rtf: str
        :param body_type: The content type of message body. Enum, available values: PlainText, Html, Rtf
        :type body_type: str
        :param categories: Contains keywords or categories for the message object.             
        :type categories: List[str]
        :param companies: Contains the names of the companies that are associated with an item.             
        :type companies: List[str]
        :param item_id: The item id, uses with a server.             
        :type item_id: str
        :param message_class: Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.             
        :type message_class: str
        :param mileage: Contains the mileage information that is associated with an item.             
        :type mileage: str
        :param recipients: Recipients of the message.             
        :type recipients: List[MapiRecipientDto]
        :param sensitivity: Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential
        :type sensitivity: str
        :param subject: Subject of the message.             
        :type subject: str
        :param subject_prefix: Subject prefix that typically indicates some action on a message, such as \"FW: \" for forwarding.             
        :type subject_prefix: str
        :param properties: List of MAPI properties             
        :type properties: List[MapiPropertyDto]
        :param discriminator: 
        :type discriminator: str
        """

        self._attachments = None
        self._billing = None
        self._body = None
        self._body_html = None
        self._body_rtf = None
        self._body_type = None
        self._categories = None
        self._companies = None
        self._item_id = None
        self._message_class = None
        self._mileage = None
        self._recipients = None
        self._sensitivity = None
        self._subject = None
        self._subject_prefix = None
        self._properties = None
        self._discriminator = self.__class__.__name__

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

    @property
    def attachments(self) -> List[MapiAttachmentDto]:
        """Gets the attachments of this MapiMessageItemBaseDto.

        Message item attachments.             

        :return: The attachments of this MapiMessageItemBaseDto.
        :rtype: list[MapiAttachmentDto]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[MapiAttachmentDto]):
        """Sets the attachments of this MapiMessageItemBaseDto.

        Message item attachments.             

        :param attachments: The attachments of this MapiMessageItemBaseDto.
        :type: list[MapiAttachmentDto]
        """
        self._attachments = attachments

    @property
    def billing(self) -> str:
        """Gets the billing of this MapiMessageItemBaseDto.

        Billing information associated with an item.             

        :return: The billing of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._billing

    @billing.setter
    def billing(self, billing: str):
        """Sets the billing of this MapiMessageItemBaseDto.

        Billing information associated with an item.             

        :param billing: The billing of this MapiMessageItemBaseDto.
        :type: str
        """
        self._billing = billing

    @property
    def body(self) -> str:
        """Gets the body of this MapiMessageItemBaseDto.

        Message text.             

        :return: The body of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body: str):
        """Sets the body of this MapiMessageItemBaseDto.

        Message text.             

        :param body: The body of this MapiMessageItemBaseDto.
        :type: str
        """
        self._body = body

    @property
    def body_html(self) -> str:
        """Gets the body_html of this MapiMessageItemBaseDto.

        Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.             

        :return: The body_html of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._body_html

    @body_html.setter
    def body_html(self, body_html: str):
        """Sets the body_html of this MapiMessageItemBaseDto.

        Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.             

        :param body_html: The body_html of this MapiMessageItemBaseDto.
        :type: str
        """
        self._body_html = body_html

    @property
    def body_rtf(self) -> str:
        """Gets the body_rtf of this MapiMessageItemBaseDto.

        RTF formatted message text.             

        :return: The body_rtf of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._body_rtf

    @body_rtf.setter
    def body_rtf(self, body_rtf: str):
        """Sets the body_rtf of this MapiMessageItemBaseDto.

        RTF formatted message text.             

        :param body_rtf: The body_rtf of this MapiMessageItemBaseDto.
        :type: str
        """
        self._body_rtf = body_rtf

    @property
    def body_type(self) -> str:
        """Gets the body_type of this MapiMessageItemBaseDto.

        The content type of message body. Enum, available values: PlainText, Html, Rtf

        :return: The body_type of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type: str):
        """Sets the body_type of this MapiMessageItemBaseDto.

        The content type of message body. Enum, available values: PlainText, Html, Rtf

        :param body_type: The body_type of this MapiMessageItemBaseDto.
        :type: str
        """
        if body_type is None:
            raise ValueError("Invalid value for `body_type`, must not be `None`")
        self._body_type = body_type

    @property
    def categories(self) -> List[str]:
        """Gets the categories of this MapiMessageItemBaseDto.

        Contains keywords or categories for the message object.             

        :return: The categories of this MapiMessageItemBaseDto.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]):
        """Sets the categories of this MapiMessageItemBaseDto.

        Contains keywords or categories for the message object.             

        :param categories: The categories of this MapiMessageItemBaseDto.
        :type: list[str]
        """
        self._categories = categories

    @property
    def companies(self) -> List[str]:
        """Gets the companies of this MapiMessageItemBaseDto.

        Contains the names of the companies that are associated with an item.             

        :return: The companies of this MapiMessageItemBaseDto.
        :rtype: list[str]
        """
        return self._companies

    @companies.setter
    def companies(self, companies: List[str]):
        """Sets the companies of this MapiMessageItemBaseDto.

        Contains the names of the companies that are associated with an item.             

        :param companies: The companies of this MapiMessageItemBaseDto.
        :type: list[str]
        """
        self._companies = companies

    @property
    def item_id(self) -> str:
        """Gets the item_id of this MapiMessageItemBaseDto.

        The item id, uses with a server.             

        :return: The item_id of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id: str):
        """Sets the item_id of this MapiMessageItemBaseDto.

        The item id, uses with a server.             

        :param item_id: The item_id of this MapiMessageItemBaseDto.
        :type: str
        """
        self._item_id = item_id

    @property
    def message_class(self) -> str:
        """Gets the message_class of this MapiMessageItemBaseDto.

        Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.             

        :return: The message_class of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._message_class

    @message_class.setter
    def message_class(self, message_class: str):
        """Sets the message_class of this MapiMessageItemBaseDto.

        Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.             

        :param message_class: The message_class of this MapiMessageItemBaseDto.
        :type: str
        """
        self._message_class = message_class

    @property
    def mileage(self) -> str:
        """Gets the mileage of this MapiMessageItemBaseDto.

        Contains the mileage information that is associated with an item.             

        :return: The mileage of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._mileage

    @mileage.setter
    def mileage(self, mileage: str):
        """Sets the mileage of this MapiMessageItemBaseDto.

        Contains the mileage information that is associated with an item.             

        :param mileage: The mileage of this MapiMessageItemBaseDto.
        :type: str
        """
        self._mileage = mileage

    @property
    def recipients(self) -> List[MapiRecipientDto]:
        """Gets the recipients of this MapiMessageItemBaseDto.

        Recipients of the message.             

        :return: The recipients of this MapiMessageItemBaseDto.
        :rtype: list[MapiRecipientDto]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients: List[MapiRecipientDto]):
        """Sets the recipients of this MapiMessageItemBaseDto.

        Recipients of the message.             

        :param recipients: The recipients of this MapiMessageItemBaseDto.
        :type: list[MapiRecipientDto]
        """
        self._recipients = recipients

    @property
    def sensitivity(self) -> str:
        """Gets the sensitivity of this MapiMessageItemBaseDto.

        Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential

        :return: The sensitivity of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity: str):
        """Sets the sensitivity of this MapiMessageItemBaseDto.

        Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential

        :param sensitivity: The sensitivity of this MapiMessageItemBaseDto.
        :type: str
        """
        if sensitivity is None:
            raise ValueError("Invalid value for `sensitivity`, must not be `None`")
        self._sensitivity = sensitivity

    @property
    def subject(self) -> str:
        """Gets the subject of this MapiMessageItemBaseDto.

        Subject of the message.             

        :return: The subject of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """Sets the subject of this MapiMessageItemBaseDto.

        Subject of the message.             

        :param subject: The subject of this MapiMessageItemBaseDto.
        :type: str
        """
        self._subject = subject

    @property
    def subject_prefix(self) -> str:
        """Gets the subject_prefix of this MapiMessageItemBaseDto.

        Subject prefix that typically indicates some action on a message, such as \"FW: \" for forwarding.             

        :return: The subject_prefix of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self._subject_prefix

    @subject_prefix.setter
    def subject_prefix(self, subject_prefix: str):
        """Sets the subject_prefix of this MapiMessageItemBaseDto.

        Subject prefix that typically indicates some action on a message, such as \"FW: \" for forwarding.             

        :param subject_prefix: The subject_prefix of this MapiMessageItemBaseDto.
        :type: str
        """
        self._subject_prefix = subject_prefix

    @property
    def properties(self) -> List[MapiPropertyDto]:
        """Gets the properties of this MapiMessageItemBaseDto.

        List of MAPI properties             

        :return: The properties of this MapiMessageItemBaseDto.
        :rtype: list[MapiPropertyDto]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: List[MapiPropertyDto]):
        """Sets the properties of this MapiMessageItemBaseDto.

        List of MAPI properties             

        :param properties: The properties of this MapiMessageItemBaseDto.
        :type: list[MapiPropertyDto]
        """
        self._properties = properties

    @property
    def discriminator(self) -> str:
        """Gets the discriminator of this MapiMessageItemBaseDto.


        :return: The discriminator of this MapiMessageItemBaseDto.
        :rtype: str
        """
        return self.__class__.__name__

    @discriminator.setter
    def discriminator(self, discriminator: str):
        """Sets the discriminator of this MapiMessageItemBaseDto.


        :param discriminator: The discriminator of this MapiMessageItemBaseDto.
        :type: str
        """
        if discriminator is None:
            raise ValueError("Invalid value for `discriminator`, must not be `None`")
        self._discriminator = self.__class__.__name__

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
        if not isinstance(other, MapiMessageItemBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
