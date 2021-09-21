#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailDto.py">
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

from AsposeEmailCloudSdk.models.alternate_view import AlternateView
from AsposeEmailCloudSdk.models.attachment import Attachment
from AsposeEmailCloudSdk.models.linked_resource import LinkedResource
from AsposeEmailCloudSdk.models.mail_address import MailAddress


class EmailDto(object):
    """Email message representation.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alternate_views': 'list[AlternateView]',
        'attachments': 'list[Attachment]',
        'bcc': 'list[MailAddress]',
        'body': 'str',
        'body_encoding': 'str',
        'body_type': 'str',
        'cc': 'list[MailAddress]',
        '_date': 'datetime',
        'delivery_notification_options': 'list[str]',
        '_from': 'MailAddress',
        'headers': 'dict(str, str)',
        'html_body': 'str',
        'html_body_text': 'str',
        'is_body_html': 'bool',
        'is_draft': 'bool',
        'is_encrypted': 'bool',
        'is_signed': 'bool',
        'linked_resources': 'list[LinkedResource]',
        'message_id': 'str',
        'original_is_tnef': 'bool',
        'preferred_text_encoding': 'str',
        'priority': 'str',
        'read_receipt_to': 'list[MailAddress]',
        'reply_to_list': 'list[MailAddress]',
        'reverse_path': 'MailAddress',
        'sender': 'MailAddress',
        'sensitivity': 'str',
        'subject': 'str',
        'subject_encoding': 'str',
        'time_zone_offset': 'int',
        'to': 'list[MailAddress]',
        'x_mailer': 'str',
        'epilogue': 'str',
        'preamble': 'str'
    }

    attribute_map = {
        'alternate_views': 'alternateViews',
        'attachments': 'attachments',
        'bcc': 'bcc',
        'body': 'body',
        'body_encoding': 'bodyEncoding',
        'body_type': 'bodyType',
        'cc': 'cc',
        '_date': 'date',
        'delivery_notification_options': 'deliveryNotificationOptions',
        '_from': 'from',
        'headers': 'headers',
        'html_body': 'htmlBody',
        'html_body_text': 'htmlBodyText',
        'is_body_html': 'isBodyHtml',
        'is_draft': 'isDraft',
        'is_encrypted': 'isEncrypted',
        'is_signed': 'isSigned',
        'linked_resources': 'linkedResources',
        'message_id': 'messageId',
        'original_is_tnef': 'originalIsTnef',
        'preferred_text_encoding': 'preferredTextEncoding',
        'priority': 'priority',
        'read_receipt_to': 'readReceiptTo',
        'reply_to_list': 'replyToList',
        'reverse_path': 'reversePath',
        'sender': 'sender',
        'sensitivity': 'sensitivity',
        'subject': 'subject',
        'subject_encoding': 'subjectEncoding',
        'time_zone_offset': 'timeZoneOffset',
        'to': 'to',
        'x_mailer': 'xMailer',
        'epilogue': 'epilogue',
        'preamble': 'preamble'
    }

    def __init__(self, alternate_views: List[AlternateView] = None, attachments: List[Attachment] = None, bcc: List[MailAddress] = None, body: str = None, body_encoding: str = None, body_type: str = None, cc: List[MailAddress] = None, _date: datetime = None, delivery_notification_options: List[str] = None, _from: MailAddress = None, headers: Dict[str, str] = None, html_body: str = None, html_body_text: str = None, is_body_html: bool = None, is_draft: bool = None, is_encrypted: bool = None, is_signed: bool = None, linked_resources: List[LinkedResource] = None, message_id: str = None, original_is_tnef: bool = None, preferred_text_encoding: str = None, priority: str = None, read_receipt_to: List[MailAddress] = None, reply_to_list: List[MailAddress] = None, reverse_path: MailAddress = None, sender: MailAddress = None, sensitivity: str = None, subject: str = None, subject_encoding: str = None, time_zone_offset: int = None, to: List[MailAddress] = None, x_mailer: str = None, epilogue: str = None, preamble: str = None):
        """
        Email message representation.             
        :param alternate_views: Collection of alternate views of message.             
        :type alternate_views: List[AlternateView]
        :param attachments: Email message attachments.             
        :type attachments: List[Attachment]
        :param bcc: BCC recipients.             
        :type bcc: List[MailAddress]
        :param body: Email message body as plain text.             
        :type body: str
        :param body_encoding: Body encoding.             
        :type body_encoding: str
        :param body_type: The content type of message body. Enum, available values: PlainText, Html, Rtf
        :type body_type: str
        :param cc: CC recipients.             
        :type cc: List[MailAddress]
        :param _date: Message date.             
        :type _date: datetime
        :param delivery_notification_options: Delivery notifications.
        :type delivery_notification_options: List[str]
        :param _from: From address.             
        :type _from: MailAddress
        :param headers: Document headers.             
        :type headers: Dict[str, str]
        :param html_body: HTML body.             
        :type html_body: str
        :param html_body_text: Html body as plain text. Read only.             
        :type html_body_text: str
        :param is_body_html: Indicates whether the message body is in Html.             
        :type is_body_html: bool
        :param is_draft: Indicates whether or not a message has been sent.             
        :type is_draft: bool
        :param is_encrypted: Indicates whether the message is encrypted. Read only.             
        :type is_encrypted: bool
        :param is_signed: Indicates whether the message is signed. Read only.             
        :type is_signed: bool
        :param linked_resources: Linked resources of message.             
        :type linked_resources: List[LinkedResource]
        :param message_id: Message id.             
        :type message_id: str
        :param original_is_tnef: Indicates whether original EML message is in TNEF format. Read only.             
        :type original_is_tnef: bool
        :param preferred_text_encoding: Preferred encoding.             
        :type preferred_text_encoding: str
        :param priority: Email priority status. Enum, available values: High, Low, Normal
        :type priority: str
        :param read_receipt_to: Read receipt addresses.             
        :type read_receipt_to: List[MailAddress]
        :param reply_to_list: The list of addresses to reply to for the mail message.             
        :type reply_to_list: List[MailAddress]
        :param reverse_path: ReversePath address.             
        :type reverse_path: MailAddress
        :param sender: Sender address.             
        :type sender: MailAddress
        :param sensitivity: Specifies the sensitivity of a MailMessage. Enum, available values: None, Normal, Personal, Private, CompanyConfidential
        :type sensitivity: str
        :param subject: Message subject.             
        :type subject: str
        :param subject_encoding: Subject encoding.             
        :type subject_encoding: str
        :param time_zone_offset: Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the local time and UTC represented as count of ticks (10 000 per millisecond).             
        :type time_zone_offset: int
        :param to: The address collection that contains the recipients of message.             
        :type to: List[MailAddress]
        :param x_mailer: The X-Mailer the software that created the e-mail message.             
        :type x_mailer: str
        :param epilogue: Gets or sets an epilogue text. It is located after the last boundary.
        :type epilogue: str
        :param preamble: Gets or sets a preamble text. It is located before the first boundary and generally includes an explanatory note to non-MIME conformant readers.
        :type preamble: str
        """

        self._alternate_views = None
        self._attachments = None
        self._bcc = None
        self._body = None
        self._body_encoding = None
        self._body_type = None
        self._cc = None
        self.__date = None
        self._delivery_notification_options = None
        self.__from = None
        self._headers = None
        self._html_body = None
        self._html_body_text = None
        self._is_body_html = None
        self._is_draft = None
        self._is_encrypted = None
        self._is_signed = None
        self._linked_resources = None
        self._message_id = None
        self._original_is_tnef = None
        self._preferred_text_encoding = None
        self._priority = None
        self._read_receipt_to = None
        self._reply_to_list = None
        self._reverse_path = None
        self._sender = None
        self._sensitivity = None
        self._subject = None
        self._subject_encoding = None
        self._time_zone_offset = None
        self._to = None
        self._x_mailer = None
        self._epilogue = None
        self._preamble = None

        if alternate_views is not None:
            self.alternate_views = alternate_views
        if attachments is not None:
            self.attachments = attachments
        if bcc is not None:
            self.bcc = bcc
        if body is not None:
            self.body = body
        if body_encoding is not None:
            self.body_encoding = body_encoding
        if body_type is not None:
            self.body_type = body_type
        if cc is not None:
            self.cc = cc
        if _date is not None:
            self._date = _date
        if delivery_notification_options is not None:
            self.delivery_notification_options = delivery_notification_options
        if _from is not None:
            self._from = _from
        if headers is not None:
            self.headers = headers
        if html_body is not None:
            self.html_body = html_body
        if html_body_text is not None:
            self.html_body_text = html_body_text
        if is_body_html is not None:
            self.is_body_html = is_body_html
        if is_draft is not None:
            self.is_draft = is_draft
        if is_encrypted is not None:
            self.is_encrypted = is_encrypted
        if is_signed is not None:
            self.is_signed = is_signed
        if linked_resources is not None:
            self.linked_resources = linked_resources
        if message_id is not None:
            self.message_id = message_id
        if original_is_tnef is not None:
            self.original_is_tnef = original_is_tnef
        if preferred_text_encoding is not None:
            self.preferred_text_encoding = preferred_text_encoding
        if priority is not None:
            self.priority = priority
        if read_receipt_to is not None:
            self.read_receipt_to = read_receipt_to
        if reply_to_list is not None:
            self.reply_to_list = reply_to_list
        if reverse_path is not None:
            self.reverse_path = reverse_path
        if sender is not None:
            self.sender = sender
        if sensitivity is not None:
            self.sensitivity = sensitivity
        if subject is not None:
            self.subject = subject
        if subject_encoding is not None:
            self.subject_encoding = subject_encoding
        if time_zone_offset is not None:
            self.time_zone_offset = time_zone_offset
        if to is not None:
            self.to = to
        if x_mailer is not None:
            self.x_mailer = x_mailer
        if epilogue is not None:
            self.epilogue = epilogue
        if preamble is not None:
            self.preamble = preamble


    @property
    def alternate_views(self) -> List[AlternateView]:
        """
        Collection of alternate views of message.             

        :return: The alternate_views of this EmailDto.
        :rtype: list[AlternateView]
        """
        return self._alternate_views

    @alternate_views.setter
    def alternate_views(self, alternate_views: List[AlternateView]):
        """
        Collection of alternate views of message.             

        :param alternate_views: The alternate_views of this EmailDto.
        :type: list[AlternateView]
        """
        self._alternate_views = alternate_views

    @property
    def attachments(self) -> List[Attachment]:
        """
        Email message attachments.             

        :return: The attachments of this EmailDto.
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[Attachment]):
        """
        Email message attachments.             

        :param attachments: The attachments of this EmailDto.
        :type: list[Attachment]
        """
        self._attachments = attachments

    @property
    def bcc(self) -> List[MailAddress]:
        """
        BCC recipients.             

        :return: The bcc of this EmailDto.
        :rtype: list[MailAddress]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc: List[MailAddress]):
        """
        BCC recipients.             

        :param bcc: The bcc of this EmailDto.
        :type: list[MailAddress]
        """
        self._bcc = bcc

    @property
    def body(self) -> str:
        """
        Email message body as plain text.             

        :return: The body of this EmailDto.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body: str):
        """
        Email message body as plain text.             

        :param body: The body of this EmailDto.
        :type: str
        """
        self._body = body

    @property
    def body_encoding(self) -> str:
        """
        Body encoding.             

        :return: The body_encoding of this EmailDto.
        :rtype: str
        """
        return self._body_encoding

    @body_encoding.setter
    def body_encoding(self, body_encoding: str):
        """
        Body encoding.             

        :param body_encoding: The body_encoding of this EmailDto.
        :type: str
        """
        self._body_encoding = body_encoding

    @property
    def body_type(self) -> str:
        """
        The content type of message body. Enum, available values: PlainText, Html, Rtf

        :return: The body_type of this EmailDto.
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type: str):
        """
        The content type of message body. Enum, available values: PlainText, Html, Rtf

        :param body_type: The body_type of this EmailDto.
        :type: str
        """
        if body_type is None:
            raise ValueError("Invalid value for `body_type`, must not be `None`")
        self._body_type = body_type

    @property
    def cc(self) -> List[MailAddress]:
        """
        CC recipients.             

        :return: The cc of this EmailDto.
        :rtype: list[MailAddress]
        """
        return self._cc

    @cc.setter
    def cc(self, cc: List[MailAddress]):
        """
        CC recipients.             

        :param cc: The cc of this EmailDto.
        :type: list[MailAddress]
        """
        self._cc = cc

    @property
    def _date(self) -> datetime:
        """
        Message date.             

        :return: The _date of this EmailDto.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date: datetime):
        """
        Message date.             

        :param _date: The _date of this EmailDto.
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")
        self.__date = _date

    @property
    def delivery_notification_options(self) -> List[str]:
        """
        Delivery notifications. Items: Email delivery notification options. Enum, available values: Delay, Never, None, OnFailure, OnSuccess

        :return: The delivery_notification_options of this EmailDto.
        :rtype: list[str]
        """
        return self._delivery_notification_options

    @delivery_notification_options.setter
    def delivery_notification_options(self, delivery_notification_options: List[str]):
        """
        Delivery notifications. Items: Email delivery notification options. Enum, available values: Delay, Never, None, OnFailure, OnSuccess

        :param delivery_notification_options: The delivery_notification_options of this EmailDto.
        :type: list[str]
        """
        self._delivery_notification_options = delivery_notification_options

    @property
    def _from(self) -> MailAddress:
        """
        From address.             

        :return: The _from of this EmailDto.
        :rtype: MailAddress
        """
        return self.__from

    @_from.setter
    def _from(self, _from: MailAddress):
        """
        From address.             

        :param _from: The _from of this EmailDto.
        :type: MailAddress
        """
        self.__from = _from

    @property
    def headers(self) -> Dict[str, str]:
        """
        Document headers.             

        :return: The headers of this EmailDto.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, str]):
        """
        Document headers.             

        :param headers: The headers of this EmailDto.
        :type: dict(str, str)
        """
        self._headers = headers

    @property
    def html_body(self) -> str:
        """
        HTML body.             

        :return: The html_body of this EmailDto.
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body: str):
        """
        HTML body.             

        :param html_body: The html_body of this EmailDto.
        :type: str
        """
        self._html_body = html_body

    @property
    def html_body_text(self) -> str:
        """
        Html body as plain text. Read only.             

        :return: The html_body_text of this EmailDto.
        :rtype: str
        """
        return self._html_body_text

    @html_body_text.setter
    def html_body_text(self, html_body_text: str):
        """
        Html body as plain text. Read only.             

        :param html_body_text: The html_body_text of this EmailDto.
        :type: str
        """
        self._html_body_text = html_body_text

    @property
    def is_body_html(self) -> bool:
        """
        Indicates whether the message body is in Html.             

        :return: The is_body_html of this EmailDto.
        :rtype: bool
        """
        return self._is_body_html

    @is_body_html.setter
    def is_body_html(self, is_body_html: bool):
        """
        Indicates whether the message body is in Html.             

        :param is_body_html: The is_body_html of this EmailDto.
        :type: bool
        """
        if is_body_html is None:
            raise ValueError("Invalid value for `is_body_html`, must not be `None`")
        self._is_body_html = is_body_html

    @property
    def is_draft(self) -> bool:
        """
        Indicates whether or not a message has been sent.             

        :return: The is_draft of this EmailDto.
        :rtype: bool
        """
        return self._is_draft

    @is_draft.setter
    def is_draft(self, is_draft: bool):
        """
        Indicates whether or not a message has been sent.             

        :param is_draft: The is_draft of this EmailDto.
        :type: bool
        """
        if is_draft is None:
            raise ValueError("Invalid value for `is_draft`, must not be `None`")
        self._is_draft = is_draft

    @property
    def is_encrypted(self) -> bool:
        """
        Indicates whether the message is encrypted. Read only.             

        :return: The is_encrypted of this EmailDto.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted: bool):
        """
        Indicates whether the message is encrypted. Read only.             

        :param is_encrypted: The is_encrypted of this EmailDto.
        :type: bool
        """
        if is_encrypted is None:
            raise ValueError("Invalid value for `is_encrypted`, must not be `None`")
        self._is_encrypted = is_encrypted

    @property
    def is_signed(self) -> bool:
        """
        Indicates whether the message is signed. Read only.             

        :return: The is_signed of this EmailDto.
        :rtype: bool
        """
        return self._is_signed

    @is_signed.setter
    def is_signed(self, is_signed: bool):
        """
        Indicates whether the message is signed. Read only.             

        :param is_signed: The is_signed of this EmailDto.
        :type: bool
        """
        if is_signed is None:
            raise ValueError("Invalid value for `is_signed`, must not be `None`")
        self._is_signed = is_signed

    @property
    def linked_resources(self) -> List[LinkedResource]:
        """
        Linked resources of message.             

        :return: The linked_resources of this EmailDto.
        :rtype: list[LinkedResource]
        """
        return self._linked_resources

    @linked_resources.setter
    def linked_resources(self, linked_resources: List[LinkedResource]):
        """
        Linked resources of message.             

        :param linked_resources: The linked_resources of this EmailDto.
        :type: list[LinkedResource]
        """
        self._linked_resources = linked_resources

    @property
    def message_id(self) -> str:
        """
        Message id.             

        :return: The message_id of this EmailDto.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: str):
        """
        Message id.             

        :param message_id: The message_id of this EmailDto.
        :type: str
        """
        self._message_id = message_id

    @property
    def original_is_tnef(self) -> bool:
        """
        Indicates whether original EML message is in TNEF format. Read only.             

        :return: The original_is_tnef of this EmailDto.
        :rtype: bool
        """
        return self._original_is_tnef

    @original_is_tnef.setter
    def original_is_tnef(self, original_is_tnef: bool):
        """
        Indicates whether original EML message is in TNEF format. Read only.             

        :param original_is_tnef: The original_is_tnef of this EmailDto.
        :type: bool
        """
        if original_is_tnef is None:
            raise ValueError("Invalid value for `original_is_tnef`, must not be `None`")
        self._original_is_tnef = original_is_tnef

    @property
    def preferred_text_encoding(self) -> str:
        """
        Preferred encoding.             

        :return: The preferred_text_encoding of this EmailDto.
        :rtype: str
        """
        return self._preferred_text_encoding

    @preferred_text_encoding.setter
    def preferred_text_encoding(self, preferred_text_encoding: str):
        """
        Preferred encoding.             

        :param preferred_text_encoding: The preferred_text_encoding of this EmailDto.
        :type: str
        """
        self._preferred_text_encoding = preferred_text_encoding

    @property
    def priority(self) -> str:
        """
        Email priority status. Enum, available values: High, Low, Normal

        :return: The priority of this EmailDto.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority: str):
        """
        Email priority status. Enum, available values: High, Low, Normal

        :param priority: The priority of this EmailDto.
        :type: str
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")
        self._priority = priority

    @property
    def read_receipt_to(self) -> List[MailAddress]:
        """
        Read receipt addresses.             

        :return: The read_receipt_to of this EmailDto.
        :rtype: list[MailAddress]
        """
        return self._read_receipt_to

    @read_receipt_to.setter
    def read_receipt_to(self, read_receipt_to: List[MailAddress]):
        """
        Read receipt addresses.             

        :param read_receipt_to: The read_receipt_to of this EmailDto.
        :type: list[MailAddress]
        """
        self._read_receipt_to = read_receipt_to

    @property
    def reply_to_list(self) -> List[MailAddress]:
        """
        The list of addresses to reply to for the mail message.             

        :return: The reply_to_list of this EmailDto.
        :rtype: list[MailAddress]
        """
        return self._reply_to_list

    @reply_to_list.setter
    def reply_to_list(self, reply_to_list: List[MailAddress]):
        """
        The list of addresses to reply to for the mail message.             

        :param reply_to_list: The reply_to_list of this EmailDto.
        :type: list[MailAddress]
        """
        self._reply_to_list = reply_to_list

    @property
    def reverse_path(self) -> MailAddress:
        """
        ReversePath address.             

        :return: The reverse_path of this EmailDto.
        :rtype: MailAddress
        """
        return self._reverse_path

    @reverse_path.setter
    def reverse_path(self, reverse_path: MailAddress):
        """
        ReversePath address.             

        :param reverse_path: The reverse_path of this EmailDto.
        :type: MailAddress
        """
        self._reverse_path = reverse_path

    @property
    def sender(self) -> MailAddress:
        """
        Sender address.             

        :return: The sender of this EmailDto.
        :rtype: MailAddress
        """
        return self._sender

    @sender.setter
    def sender(self, sender: MailAddress):
        """
        Sender address.             

        :param sender: The sender of this EmailDto.
        :type: MailAddress
        """
        self._sender = sender

    @property
    def sensitivity(self) -> str:
        """
        Specifies the sensitivity of a MailMessage. Enum, available values: None, Normal, Personal, Private, CompanyConfidential

        :return: The sensitivity of this EmailDto.
        :rtype: str
        """
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity: str):
        """
        Specifies the sensitivity of a MailMessage. Enum, available values: None, Normal, Personal, Private, CompanyConfidential

        :param sensitivity: The sensitivity of this EmailDto.
        :type: str
        """
        if sensitivity is None:
            raise ValueError("Invalid value for `sensitivity`, must not be `None`")
        self._sensitivity = sensitivity

    @property
    def subject(self) -> str:
        """
        Message subject.             

        :return: The subject of this EmailDto.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """
        Message subject.             

        :param subject: The subject of this EmailDto.
        :type: str
        """
        self._subject = subject

    @property
    def subject_encoding(self) -> str:
        """
        Subject encoding.             

        :return: The subject_encoding of this EmailDto.
        :rtype: str
        """
        return self._subject_encoding

    @subject_encoding.setter
    def subject_encoding(self, subject_encoding: str):
        """
        Subject encoding.             

        :param subject_encoding: The subject_encoding of this EmailDto.
        :type: str
        """
        self._subject_encoding = subject_encoding

    @property
    def time_zone_offset(self) -> int:
        """
        Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the local time and UTC represented as count of ticks (10 000 per millisecond).             

        :return: The time_zone_offset of this EmailDto.
        :rtype: int
        """
        return self._time_zone_offset

    @time_zone_offset.setter
    def time_zone_offset(self, time_zone_offset: int):
        """
        Coordinated Universal Time (UTC) offset for the message dates. This property defines the time zone difference, between the local time and UTC represented as count of ticks (10 000 per millisecond).             

        :param time_zone_offset: The time_zone_offset of this EmailDto.
        :type: int
        """
        self._time_zone_offset = time_zone_offset

    @property
    def to(self) -> List[MailAddress]:
        """
        The address collection that contains the recipients of message.             

        :return: The to of this EmailDto.
        :rtype: list[MailAddress]
        """
        return self._to

    @to.setter
    def to(self, to: List[MailAddress]):
        """
        The address collection that contains the recipients of message.             

        :param to: The to of this EmailDto.
        :type: list[MailAddress]
        """
        self._to = to

    @property
    def x_mailer(self) -> str:
        """
        The X-Mailer the software that created the e-mail message.             

        :return: The x_mailer of this EmailDto.
        :rtype: str
        """
        return self._x_mailer

    @x_mailer.setter
    def x_mailer(self, x_mailer: str):
        """
        The X-Mailer the software that created the e-mail message.             

        :param x_mailer: The x_mailer of this EmailDto.
        :type: str
        """
        self._x_mailer = x_mailer

    @property
    def epilogue(self) -> str:
        """
        Gets or sets an epilogue text. It is located after the last boundary.

        :return: The epilogue of this EmailDto.
        :rtype: str
        """
        return self._epilogue

    @epilogue.setter
    def epilogue(self, epilogue: str):
        """
        Gets or sets an epilogue text. It is located after the last boundary.

        :param epilogue: The epilogue of this EmailDto.
        :type: str
        """
        self._epilogue = epilogue

    @property
    def preamble(self) -> str:
        """
        Gets or sets a preamble text. It is located before the first boundary and generally includes an explanatory note to non-MIME conformant readers.

        :return: The preamble of this EmailDto.
        :rtype: str
        """
        return self._preamble

    @preamble.setter
    def preamble(self, preamble: str):
        """
        Gets or sets a preamble text. It is located before the first boundary and generally includes an explanatory note to non-MIME conformant readers.

        :param preamble: The preamble of this EmailDto.
        :type: str
        """
        self._preamble = preamble

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
        if not isinstance(other, EmailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
