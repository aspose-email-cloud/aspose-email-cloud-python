#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiMessageDto.py">
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


class MapiMessageDto(MapiMessageItemBaseDto):
    """Represents an Outlook Message format document.             
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
        'message_body': 'str',
        'client_submit_time': 'datetime',
        'conversation_topic': 'str',
        'delivery_time': 'datetime',
        'display_bcc': 'str',
        'display_cc': 'str',
        'display_name': 'str',
        'display_name_prefix': 'str',
        'display_to': 'str',
        'flags': 'list[str]',
        'headers': 'dict(str, str)',
        'internet_message_id': 'str',
        'message_format': 'str',
        'normalized_subject': 'str',
        'read_receipt_requested': 'bool',
        'reply_to': 'str',
        'sender_address_type': 'str',
        'sender_email_address': 'str',
        'sender_name': 'str',
        'sender_smtp_address': 'str',
        'sent_representing_address_type': 'str',
        'sent_representing_email_address': 'str',
        'sent_representing_name': 'str',
        'sent_representing_smtp_address': 'str',
        'transport_message_headers': 'str'
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
        'message_body': 'messageBody',
        'client_submit_time': 'clientSubmitTime',
        'conversation_topic': 'conversationTopic',
        'delivery_time': 'deliveryTime',
        'display_bcc': 'displayBcc',
        'display_cc': 'displayCc',
        'display_name': 'displayName',
        'display_name_prefix': 'displayNamePrefix',
        'display_to': 'displayTo',
        'flags': 'flags',
        'headers': 'headers',
        'internet_message_id': 'internetMessageId',
        'message_format': 'messageFormat',
        'normalized_subject': 'normalizedSubject',
        'read_receipt_requested': 'readReceiptRequested',
        'reply_to': 'replyTo',
        'sender_address_type': 'senderAddressType',
        'sender_email_address': 'senderEmailAddress',
        'sender_name': 'senderName',
        'sender_smtp_address': 'senderSmtpAddress',
        'sent_representing_address_type': 'sentRepresentingAddressType',
        'sent_representing_email_address': 'sentRepresentingEmailAddress',
        'sent_representing_name': 'sentRepresentingName',
        'sent_representing_smtp_address': 'sentRepresentingSmtpAddress',
        'transport_message_headers': 'transportMessageHeaders'
    }

    def __init__(self, attachments: List[MapiAttachmentDto] = None, billing: str = None, body: str = None, body_html: str = None, body_rtf: str = None, body_type: str = None, categories: List[str] = None, companies: List[str] = None, item_id: str = None, message_class: str = None, mileage: str = None, recipients: List[MapiRecipientDto] = None, sensitivity: str = None, subject: str = None, subject_prefix: str = None, properties: List[MapiPropertyDto] = None, discriminator: str = None, message_body: str = None, client_submit_time: datetime = None, conversation_topic: str = None, delivery_time: datetime = None, display_bcc: str = None, display_cc: str = None, display_name: str = None, display_name_prefix: str = None, display_to: str = None, flags: List[str] = None, headers: Dict[str, str] = None, internet_message_id: str = None, message_format: str = None, normalized_subject: str = None, read_receipt_requested: bool = None, reply_to: str = None, sender_address_type: str = None, sender_email_address: str = None, sender_name: str = None, sender_smtp_address: str = None, sent_representing_address_type: str = None, sent_representing_email_address: str = None, sent_representing_name: str = None, sent_representing_smtp_address: str = None, transport_message_headers: str = None):
        """
        Represents an Outlook Message format document.             
        :param attachments: Message item attachments.             
        :param billing: Billing information associated with an item.             
        :param body: Message text.             
        :param body_html: Gets the BodyRtf of the message converted to HTML, if present, otherwise an empty string.             
        :param body_rtf: RTF formatted message text.             
        :param body_type: The content type of message body. Enum, available values: PlainText, Html, Rtf
        :param categories: Contains keywords or categories for the message object.             
        :param companies: Contains the names of the companies that are associated with an item.             
        :param item_id: The item id, uses with a server.             
        :param message_class: Case-sensitive string that identifies the sender-defined message class, such as IPM.Note. The message class specifies the type, purpose, or content of the message.             
        :param mileage: Contains the mileage information that is associated with an item.             
        :param recipients: Recipients of the message.             
        :param sensitivity: Contains values that indicate the message sensitivity. Enum, available values: None, Personal, Private, CompanyConfidential
        :param subject: Subject of the message.             
        :param subject_prefix: Subject prefix that typically indicates some action on a message, such as \"FW: \" for forwarding.             
        :param properties: List of MAPI properties             
        :param discriminator: 
        :param message_body: Message text             
        :param client_submit_time: Date and time the message sender submitted a message.             
        :param conversation_topic: Topic of the first message in a conversation thread.             
        :param delivery_time: Date and time a message was delivered.             
        :param display_bcc: List of the display names of any blind carbon copy (BCC) message recipients, separated by semicolons (;).             
        :param display_cc: List of the display names of any carbon copy (CC) message recipients, separated by semicolons (;).             
        :param display_name: Display name for the message.             
        :param display_name_prefix: Prefix of the display name.             
        :param display_to: List of the display names of the primary (To) message recipients, separated by semicolons (;).             
        :param flags: Message flags.             
        :param headers: Transport message headers             
        :param internet_message_id: Internet message id of the message.             
        :param message_format: Represents outlook message format. Enum, available values: Ascii, Unicode
        :param normalized_subject: Normalized subject of the message.             
        :param read_receipt_requested: Value indicating whether the read receipt is requested.
        :param reply_to: Reply to names.
        :param sender_address_type: Message sender's e-mail address type.
        :param sender_email_address: Message sender's e-mail address.
        :param sender_name: Message sender's display name.
        :param sender_smtp_address: Message sender's e-mail address.
        :param sent_representing_address_type: Address type for the messaging user represented by the sender.
        :param sent_representing_email_address: E-mail address for the messaging user represented by the sender.
        :param sent_representing_name: Display name for the messaging user represented by the sender.
        :param sent_representing_smtp_address: E-mail address for the messaging user represented by the sender.
        :param transport_message_headers: Transport-specific message envelope information.
        :type MapiMessageDto: 
        """
        super(MapiMessageDto, self).__init__()

        self._message_body = None
        self._client_submit_time = None
        self._conversation_topic = None
        self._delivery_time = None
        self._display_bcc = None
        self._display_cc = None
        self._display_name = None
        self._display_name_prefix = None
        self._display_to = None
        self._flags = None
        self._headers = None
        self._internet_message_id = None
        self._message_format = None
        self._normalized_subject = None
        self._read_receipt_requested = None
        self._reply_to = None
        self._sender_address_type = None
        self._sender_email_address = None
        self._sender_name = None
        self._sender_smtp_address = None
        self._sent_representing_address_type = None
        self._sent_representing_email_address = None
        self._sent_representing_name = None
        self._sent_representing_smtp_address = None
        self._transport_message_headers = None

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
        if message_body is not None:
            self.message_body = message_body
        if client_submit_time is not None:
            self.client_submit_time = client_submit_time
        if conversation_topic is not None:
            self.conversation_topic = conversation_topic
        if delivery_time is not None:
            self.delivery_time = delivery_time
        if display_bcc is not None:
            self.display_bcc = display_bcc
        if display_cc is not None:
            self.display_cc = display_cc
        if display_name is not None:
            self.display_name = display_name
        if display_name_prefix is not None:
            self.display_name_prefix = display_name_prefix
        if display_to is not None:
            self.display_to = display_to
        if flags is not None:
            self.flags = flags
        if headers is not None:
            self.headers = headers
        if internet_message_id is not None:
            self.internet_message_id = internet_message_id
        if message_format is not None:
            self.message_format = message_format
        if normalized_subject is not None:
            self.normalized_subject = normalized_subject
        if read_receipt_requested is not None:
            self.read_receipt_requested = read_receipt_requested
        if reply_to is not None:
            self.reply_to = reply_to
        if sender_address_type is not None:
            self.sender_address_type = sender_address_type
        if sender_email_address is not None:
            self.sender_email_address = sender_email_address
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_smtp_address is not None:
            self.sender_smtp_address = sender_smtp_address
        if sent_representing_address_type is not None:
            self.sent_representing_address_type = sent_representing_address_type
        if sent_representing_email_address is not None:
            self.sent_representing_email_address = sent_representing_email_address
        if sent_representing_name is not None:
            self.sent_representing_name = sent_representing_name
        if sent_representing_smtp_address is not None:
            self.sent_representing_smtp_address = sent_representing_smtp_address
        if transport_message_headers is not None:
            self.transport_message_headers = transport_message_headers

    @property
    def message_body(self) -> str:
        """Gets the message_body of this MapiMessageDto.

        Message text             

        :return: The message_body of this MapiMessageDto.
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body: str):
        """Sets the message_body of this MapiMessageDto.

        Message text             

        :param message_body: The message_body of this MapiMessageDto.
        :type: str
        """
        self._message_body = message_body

    @property
    def client_submit_time(self) -> datetime:
        """Gets the client_submit_time of this MapiMessageDto.

        Date and time the message sender submitted a message.             

        :return: The client_submit_time of this MapiMessageDto.
        :rtype: datetime
        """
        return self._client_submit_time

    @client_submit_time.setter
    def client_submit_time(self, client_submit_time: datetime):
        """Sets the client_submit_time of this MapiMessageDto.

        Date and time the message sender submitted a message.             

        :param client_submit_time: The client_submit_time of this MapiMessageDto.
        :type: datetime
        """
        if client_submit_time is None:
            raise ValueError("Invalid value for `client_submit_time`, must not be `None`")
        self._client_submit_time = client_submit_time

    @property
    def conversation_topic(self) -> str:
        """Gets the conversation_topic of this MapiMessageDto.

        Topic of the first message in a conversation thread.             

        :return: The conversation_topic of this MapiMessageDto.
        :rtype: str
        """
        return self._conversation_topic

    @conversation_topic.setter
    def conversation_topic(self, conversation_topic: str):
        """Sets the conversation_topic of this MapiMessageDto.

        Topic of the first message in a conversation thread.             

        :param conversation_topic: The conversation_topic of this MapiMessageDto.
        :type: str
        """
        self._conversation_topic = conversation_topic

    @property
    def delivery_time(self) -> datetime:
        """Gets the delivery_time of this MapiMessageDto.

        Date and time a message was delivered.             

        :return: The delivery_time of this MapiMessageDto.
        :rtype: datetime
        """
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time: datetime):
        """Sets the delivery_time of this MapiMessageDto.

        Date and time a message was delivered.             

        :param delivery_time: The delivery_time of this MapiMessageDto.
        :type: datetime
        """
        if delivery_time is None:
            raise ValueError("Invalid value for `delivery_time`, must not be `None`")
        self._delivery_time = delivery_time

    @property
    def display_bcc(self) -> str:
        """Gets the display_bcc of this MapiMessageDto.

        List of the display names of any blind carbon copy (BCC) message recipients, separated by semicolons (;).             

        :return: The display_bcc of this MapiMessageDto.
        :rtype: str
        """
        return self._display_bcc

    @display_bcc.setter
    def display_bcc(self, display_bcc: str):
        """Sets the display_bcc of this MapiMessageDto.

        List of the display names of any blind carbon copy (BCC) message recipients, separated by semicolons (;).             

        :param display_bcc: The display_bcc of this MapiMessageDto.
        :type: str
        """
        self._display_bcc = display_bcc

    @property
    def display_cc(self) -> str:
        """Gets the display_cc of this MapiMessageDto.

        List of the display names of any carbon copy (CC) message recipients, separated by semicolons (;).             

        :return: The display_cc of this MapiMessageDto.
        :rtype: str
        """
        return self._display_cc

    @display_cc.setter
    def display_cc(self, display_cc: str):
        """Sets the display_cc of this MapiMessageDto.

        List of the display names of any carbon copy (CC) message recipients, separated by semicolons (;).             

        :param display_cc: The display_cc of this MapiMessageDto.
        :type: str
        """
        self._display_cc = display_cc

    @property
    def display_name(self) -> str:
        """Gets the display_name of this MapiMessageDto.

        Display name for the message.             

        :return: The display_name of this MapiMessageDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this MapiMessageDto.

        Display name for the message.             

        :param display_name: The display_name of this MapiMessageDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def display_name_prefix(self) -> str:
        """Gets the display_name_prefix of this MapiMessageDto.

        Prefix of the display name.             

        :return: The display_name_prefix of this MapiMessageDto.
        :rtype: str
        """
        return self._display_name_prefix

    @display_name_prefix.setter
    def display_name_prefix(self, display_name_prefix: str):
        """Sets the display_name_prefix of this MapiMessageDto.

        Prefix of the display name.             

        :param display_name_prefix: The display_name_prefix of this MapiMessageDto.
        :type: str
        """
        self._display_name_prefix = display_name_prefix

    @property
    def display_to(self) -> str:
        """Gets the display_to of this MapiMessageDto.

        List of the display names of the primary (To) message recipients, separated by semicolons (;).             

        :return: The display_to of this MapiMessageDto.
        :rtype: str
        """
        return self._display_to

    @display_to.setter
    def display_to(self, display_to: str):
        """Sets the display_to of this MapiMessageDto.

        List of the display names of the primary (To) message recipients, separated by semicolons (;).             

        :param display_to: The display_to of this MapiMessageDto.
        :type: str
        """
        self._display_to = display_to

    @property
    def flags(self) -> List[str]:
        """Gets the flags of this MapiMessageDto.

        Message flags.              Items: Mapi message flags. Enum, available values: MsgFlagZero, MsgFlagRead, MsgFlagUnmodified, MsgFlagSubmit, MsgFlagUnsent, MsgFlagHasAttach, MsgFlagFromMe, MsgFlagAssociated, MsgFlagResend, MsgFlagNotifyRead, MsgFlagNotifyUnread, MsgFlagEverRead, MsgFlagOriginX400, MsgFlagOriginInternet, MsgFlagOriginMiscExt

        :return: The flags of this MapiMessageDto.
        :rtype: list[str]
        """
        return self._flags

    @flags.setter
    def flags(self, flags: List[str]):
        """Sets the flags of this MapiMessageDto.

        Message flags.              Items: Mapi message flags. Enum, available values: MsgFlagZero, MsgFlagRead, MsgFlagUnmodified, MsgFlagSubmit, MsgFlagUnsent, MsgFlagHasAttach, MsgFlagFromMe, MsgFlagAssociated, MsgFlagResend, MsgFlagNotifyRead, MsgFlagNotifyUnread, MsgFlagEverRead, MsgFlagOriginX400, MsgFlagOriginInternet, MsgFlagOriginMiscExt

        :param flags: The flags of this MapiMessageDto.
        :type: list[str]
        """
        self._flags = flags

    @property
    def headers(self) -> Dict[str, str]:
        """Gets the headers of this MapiMessageDto.

        Transport message headers             

        :return: The headers of this MapiMessageDto.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, str]):
        """Sets the headers of this MapiMessageDto.

        Transport message headers             

        :param headers: The headers of this MapiMessageDto.
        :type: dict(str, str)
        """
        self._headers = headers

    @property
    def internet_message_id(self) -> str:
        """Gets the internet_message_id of this MapiMessageDto.

        Internet message id of the message.             

        :return: The internet_message_id of this MapiMessageDto.
        :rtype: str
        """
        return self._internet_message_id

    @internet_message_id.setter
    def internet_message_id(self, internet_message_id: str):
        """Sets the internet_message_id of this MapiMessageDto.

        Internet message id of the message.             

        :param internet_message_id: The internet_message_id of this MapiMessageDto.
        :type: str
        """
        self._internet_message_id = internet_message_id

    @property
    def message_format(self) -> str:
        """Gets the message_format of this MapiMessageDto.

        Represents outlook message format. Enum, available values: Ascii, Unicode

        :return: The message_format of this MapiMessageDto.
        :rtype: str
        """
        return self._message_format

    @message_format.setter
    def message_format(self, message_format: str):
        """Sets the message_format of this MapiMessageDto.

        Represents outlook message format. Enum, available values: Ascii, Unicode

        :param message_format: The message_format of this MapiMessageDto.
        :type: str
        """
        if message_format is None:
            raise ValueError("Invalid value for `message_format`, must not be `None`")
        self._message_format = message_format

    @property
    def normalized_subject(self) -> str:
        """Gets the normalized_subject of this MapiMessageDto.

        Normalized subject of the message.             

        :return: The normalized_subject of this MapiMessageDto.
        :rtype: str
        """
        return self._normalized_subject

    @normalized_subject.setter
    def normalized_subject(self, normalized_subject: str):
        """Sets the normalized_subject of this MapiMessageDto.

        Normalized subject of the message.             

        :param normalized_subject: The normalized_subject of this MapiMessageDto.
        :type: str
        """
        self._normalized_subject = normalized_subject

    @property
    def read_receipt_requested(self) -> bool:
        """Gets the read_receipt_requested of this MapiMessageDto.

        Value indicating whether the read receipt is requested.

        :return: The read_receipt_requested of this MapiMessageDto.
        :rtype: bool
        """
        return self._read_receipt_requested

    @read_receipt_requested.setter
    def read_receipt_requested(self, read_receipt_requested: bool):
        """Sets the read_receipt_requested of this MapiMessageDto.

        Value indicating whether the read receipt is requested.

        :param read_receipt_requested: The read_receipt_requested of this MapiMessageDto.
        :type: bool
        """
        if read_receipt_requested is None:
            raise ValueError("Invalid value for `read_receipt_requested`, must not be `None`")
        self._read_receipt_requested = read_receipt_requested

    @property
    def reply_to(self) -> str:
        """Gets the reply_to of this MapiMessageDto.

        Reply to names.

        :return: The reply_to of this MapiMessageDto.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to: str):
        """Sets the reply_to of this MapiMessageDto.

        Reply to names.

        :param reply_to: The reply_to of this MapiMessageDto.
        :type: str
        """
        self._reply_to = reply_to

    @property
    def sender_address_type(self) -> str:
        """Gets the sender_address_type of this MapiMessageDto.

        Message sender's e-mail address type.

        :return: The sender_address_type of this MapiMessageDto.
        :rtype: str
        """
        return self._sender_address_type

    @sender_address_type.setter
    def sender_address_type(self, sender_address_type: str):
        """Sets the sender_address_type of this MapiMessageDto.

        Message sender's e-mail address type.

        :param sender_address_type: The sender_address_type of this MapiMessageDto.
        :type: str
        """
        self._sender_address_type = sender_address_type

    @property
    def sender_email_address(self) -> str:
        """Gets the sender_email_address of this MapiMessageDto.

        Message sender's e-mail address.

        :return: The sender_email_address of this MapiMessageDto.
        :rtype: str
        """
        return self._sender_email_address

    @sender_email_address.setter
    def sender_email_address(self, sender_email_address: str):
        """Sets the sender_email_address of this MapiMessageDto.

        Message sender's e-mail address.

        :param sender_email_address: The sender_email_address of this MapiMessageDto.
        :type: str
        """
        self._sender_email_address = sender_email_address

    @property
    def sender_name(self) -> str:
        """Gets the sender_name of this MapiMessageDto.

        Message sender's display name.

        :return: The sender_name of this MapiMessageDto.
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name: str):
        """Sets the sender_name of this MapiMessageDto.

        Message sender's display name.

        :param sender_name: The sender_name of this MapiMessageDto.
        :type: str
        """
        self._sender_name = sender_name

    @property
    def sender_smtp_address(self) -> str:
        """Gets the sender_smtp_address of this MapiMessageDto.

        Message sender's e-mail address.

        :return: The sender_smtp_address of this MapiMessageDto.
        :rtype: str
        """
        return self._sender_smtp_address

    @sender_smtp_address.setter
    def sender_smtp_address(self, sender_smtp_address: str):
        """Sets the sender_smtp_address of this MapiMessageDto.

        Message sender's e-mail address.

        :param sender_smtp_address: The sender_smtp_address of this MapiMessageDto.
        :type: str
        """
        self._sender_smtp_address = sender_smtp_address

    @property
    def sent_representing_address_type(self) -> str:
        """Gets the sent_representing_address_type of this MapiMessageDto.

        Address type for the messaging user represented by the sender.

        :return: The sent_representing_address_type of this MapiMessageDto.
        :rtype: str
        """
        return self._sent_representing_address_type

    @sent_representing_address_type.setter
    def sent_representing_address_type(self, sent_representing_address_type: str):
        """Sets the sent_representing_address_type of this MapiMessageDto.

        Address type for the messaging user represented by the sender.

        :param sent_representing_address_type: The sent_representing_address_type of this MapiMessageDto.
        :type: str
        """
        self._sent_representing_address_type = sent_representing_address_type

    @property
    def sent_representing_email_address(self) -> str:
        """Gets the sent_representing_email_address of this MapiMessageDto.

        E-mail address for the messaging user represented by the sender.

        :return: The sent_representing_email_address of this MapiMessageDto.
        :rtype: str
        """
        return self._sent_representing_email_address

    @sent_representing_email_address.setter
    def sent_representing_email_address(self, sent_representing_email_address: str):
        """Sets the sent_representing_email_address of this MapiMessageDto.

        E-mail address for the messaging user represented by the sender.

        :param sent_representing_email_address: The sent_representing_email_address of this MapiMessageDto.
        :type: str
        """
        self._sent_representing_email_address = sent_representing_email_address

    @property
    def sent_representing_name(self) -> str:
        """Gets the sent_representing_name of this MapiMessageDto.

        Display name for the messaging user represented by the sender.

        :return: The sent_representing_name of this MapiMessageDto.
        :rtype: str
        """
        return self._sent_representing_name

    @sent_representing_name.setter
    def sent_representing_name(self, sent_representing_name: str):
        """Sets the sent_representing_name of this MapiMessageDto.

        Display name for the messaging user represented by the sender.

        :param sent_representing_name: The sent_representing_name of this MapiMessageDto.
        :type: str
        """
        self._sent_representing_name = sent_representing_name

    @property
    def sent_representing_smtp_address(self) -> str:
        """Gets the sent_representing_smtp_address of this MapiMessageDto.

        E-mail address for the messaging user represented by the sender.

        :return: The sent_representing_smtp_address of this MapiMessageDto.
        :rtype: str
        """
        return self._sent_representing_smtp_address

    @sent_representing_smtp_address.setter
    def sent_representing_smtp_address(self, sent_representing_smtp_address: str):
        """Sets the sent_representing_smtp_address of this MapiMessageDto.

        E-mail address for the messaging user represented by the sender.

        :param sent_representing_smtp_address: The sent_representing_smtp_address of this MapiMessageDto.
        :type: str
        """
        self._sent_representing_smtp_address = sent_representing_smtp_address

    @property
    def transport_message_headers(self) -> str:
        """Gets the transport_message_headers of this MapiMessageDto.

        Transport-specific message envelope information.

        :return: The transport_message_headers of this MapiMessageDto.
        :rtype: str
        """
        return self._transport_message_headers

    @transport_message_headers.setter
    def transport_message_headers(self, transport_message_headers: str):
        """Sets the transport_message_headers of this MapiMessageDto.

        Transport-specific message envelope information.

        :param transport_message_headers: The transport_message_headers of this MapiMessageDto.
        :type: str
        """
        self._transport_message_headers = transport_message_headers

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
        if not isinstance(other, MapiMessageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
