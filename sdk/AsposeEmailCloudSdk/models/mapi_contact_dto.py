#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactDto.py">
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
from AsposeEmailCloudSdk.models.mapi_contact_electronic_address_property_set_dto import MapiContactElectronicAddressPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_event_property_set_dto import MapiContactEventPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_name_property_set_dto import MapiContactNamePropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_other_property_set_dto import MapiContactOtherPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_personal_info_property_set_dto import MapiContactPersonalInfoPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_photo_dto import MapiContactPhotoDto
from AsposeEmailCloudSdk.models.mapi_contact_physical_address_property_set_dto import MapiContactPhysicalAddressPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_professional_property_set_dto import MapiContactProfessionalPropertySetDto
from AsposeEmailCloudSdk.models.mapi_contact_telephone_property_set_dto import MapiContactTelephonePropertySetDto
from AsposeEmailCloudSdk.models.mapi_message_item_base_dto import MapiMessageItemBaseDto
from AsposeEmailCloudSdk.models.mapi_property_dto import MapiPropertyDto
from AsposeEmailCloudSdk.models.mapi_recipient_dto import MapiRecipientDto


class MapiContactDto(MapiMessageItemBaseDto):
    """Represents outlook contact information.             
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
        'electronic_addresses': 'MapiContactElectronicAddressPropertySetDto',
        'events': 'MapiContactEventPropertySetDto',
        'name_info': 'MapiContactNamePropertySetDto',
        'other_fields': 'MapiContactOtherPropertySetDto',
        'personal_info': 'MapiContactPersonalInfoPropertySetDto',
        'photo': 'MapiContactPhotoDto',
        'physical_addresses': 'MapiContactPhysicalAddressPropertySetDto',
        'professional_info': 'MapiContactProfessionalPropertySetDto',
        'telephones': 'MapiContactTelephonePropertySetDto'
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
        'electronic_addresses': 'electronicAddresses',
        'events': 'events',
        'name_info': 'nameInfo',
        'other_fields': 'otherFields',
        'personal_info': 'personalInfo',
        'photo': 'photo',
        'physical_addresses': 'physicalAddresses',
        'professional_info': 'professionalInfo',
        'telephones': 'telephones'
    }

    def __init__(self, attachments: List[MapiAttachmentDto] = None, billing: str = None, body: str = None, body_html: str = None, body_rtf: str = None, body_type: str = None, categories: List[str] = None, companies: List[str] = None, item_id: str = None, message_class: str = None, mileage: str = None, recipients: List[MapiRecipientDto] = None, sensitivity: str = None, subject: str = None, subject_prefix: str = None, properties: List[MapiPropertyDto] = None, electronic_addresses: MapiContactElectronicAddressPropertySetDto = None, events: MapiContactEventPropertySetDto = None, name_info: MapiContactNamePropertySetDto = None, other_fields: MapiContactOtherPropertySetDto = None, personal_info: MapiContactPersonalInfoPropertySetDto = None, photo: MapiContactPhotoDto = None, physical_addresses: MapiContactPhysicalAddressPropertySetDto = None, professional_info: MapiContactProfessionalPropertySetDto = None, telephones: MapiContactTelephonePropertySetDto = None):
        """
        Represents outlook contact information.             
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
        :param electronic_addresses: Specify properties for up to three different e-mail addresses and three different fax addresses.             
        :type electronic_addresses: MapiContactElectronicAddressPropertySetDto
        :param events: Specify events associated with a contact.             
        :type events: MapiContactEventPropertySetDto
        :param name_info: The properties are used to specify the name of the person represented by the contact.             
        :type name_info: MapiContactNamePropertySetDto
        :param other_fields: Specify other fields of contact.             
        :type other_fields: MapiContactOtherPropertySetDto
        :param personal_info: Specify other additional contact information.             
        :type personal_info: MapiContactPersonalInfoPropertySetDto
        :param photo: Contact photo.             
        :type photo: MapiContactPhotoDto
        :param physical_addresses: Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address.             
        :type physical_addresses: MapiContactPhysicalAddressPropertySetDto
        :param professional_info: Properties are used to store professional details for the person represented by the contact.             
        :type professional_info: MapiContactProfessionalPropertySetDto
        :param telephones: Specify telephone numbers for the contact.             
        :type telephones: MapiContactTelephonePropertySetDto
        """
        super(MapiContactDto, self).__init__()

        self._electronic_addresses = None
        self._events = None
        self._name_info = None
        self._other_fields = None
        self._personal_info = None
        self._photo = None
        self._physical_addresses = None
        self._professional_info = None
        self._telephones = None

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
        if electronic_addresses is not None:
            self.electronic_addresses = electronic_addresses
        if events is not None:
            self.events = events
        if name_info is not None:
            self.name_info = name_info
        if other_fields is not None:
            self.other_fields = other_fields
        if personal_info is not None:
            self.personal_info = personal_info
        if photo is not None:
            self.photo = photo
        if physical_addresses is not None:
            self.physical_addresses = physical_addresses
        if professional_info is not None:
            self.professional_info = professional_info
        if telephones is not None:
            self.telephones = telephones


    @property
    def electronic_addresses(self) -> MapiContactElectronicAddressPropertySetDto:
        """
        Specify properties for up to three different e-mail addresses and three different fax addresses.             

        :return: The electronic_addresses of this MapiContactDto.
        :rtype: MapiContactElectronicAddressPropertySetDto
        """
        return self._electronic_addresses

    @electronic_addresses.setter
    def electronic_addresses(self, electronic_addresses: MapiContactElectronicAddressPropertySetDto):
        """
        Specify properties for up to three different e-mail addresses and three different fax addresses.             

        :param electronic_addresses: The electronic_addresses of this MapiContactDto.
        :type: MapiContactElectronicAddressPropertySetDto
        """
        self._electronic_addresses = electronic_addresses

    @property
    def events(self) -> MapiContactEventPropertySetDto:
        """
        Specify events associated with a contact.             

        :return: The events of this MapiContactDto.
        :rtype: MapiContactEventPropertySetDto
        """
        return self._events

    @events.setter
    def events(self, events: MapiContactEventPropertySetDto):
        """
        Specify events associated with a contact.             

        :param events: The events of this MapiContactDto.
        :type: MapiContactEventPropertySetDto
        """
        self._events = events

    @property
    def name_info(self) -> MapiContactNamePropertySetDto:
        """
        The properties are used to specify the name of the person represented by the contact.             

        :return: The name_info of this MapiContactDto.
        :rtype: MapiContactNamePropertySetDto
        """
        return self._name_info

    @name_info.setter
    def name_info(self, name_info: MapiContactNamePropertySetDto):
        """
        The properties are used to specify the name of the person represented by the contact.             

        :param name_info: The name_info of this MapiContactDto.
        :type: MapiContactNamePropertySetDto
        """
        self._name_info = name_info

    @property
    def other_fields(self) -> MapiContactOtherPropertySetDto:
        """
        Specify other fields of contact.             

        :return: The other_fields of this MapiContactDto.
        :rtype: MapiContactOtherPropertySetDto
        """
        return self._other_fields

    @other_fields.setter
    def other_fields(self, other_fields: MapiContactOtherPropertySetDto):
        """
        Specify other fields of contact.             

        :param other_fields: The other_fields of this MapiContactDto.
        :type: MapiContactOtherPropertySetDto
        """
        self._other_fields = other_fields

    @property
    def personal_info(self) -> MapiContactPersonalInfoPropertySetDto:
        """
        Specify other additional contact information.             

        :return: The personal_info of this MapiContactDto.
        :rtype: MapiContactPersonalInfoPropertySetDto
        """
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: MapiContactPersonalInfoPropertySetDto):
        """
        Specify other additional contact information.             

        :param personal_info: The personal_info of this MapiContactDto.
        :type: MapiContactPersonalInfoPropertySetDto
        """
        self._personal_info = personal_info

    @property
    def photo(self) -> MapiContactPhotoDto:
        """
        Contact photo.             

        :return: The photo of this MapiContactDto.
        :rtype: MapiContactPhotoDto
        """
        return self._photo

    @photo.setter
    def photo(self, photo: MapiContactPhotoDto):
        """
        Contact photo.             

        :param photo: The photo of this MapiContactDto.
        :type: MapiContactPhotoDto
        """
        self._photo = photo

    @property
    def physical_addresses(self) -> MapiContactPhysicalAddressPropertySetDto:
        """
        Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address.             

        :return: The physical_addresses of this MapiContactDto.
        :rtype: MapiContactPhysicalAddressPropertySetDto
        """
        return self._physical_addresses

    @physical_addresses.setter
    def physical_addresses(self, physical_addresses: MapiContactPhysicalAddressPropertySetDto):
        """
        Specify three physical addresses: Home Address, Work Address, and Other Address. One of the addresses can be marked as the Mailing Address.             

        :param physical_addresses: The physical_addresses of this MapiContactDto.
        :type: MapiContactPhysicalAddressPropertySetDto
        """
        self._physical_addresses = physical_addresses

    @property
    def professional_info(self) -> MapiContactProfessionalPropertySetDto:
        """
        Properties are used to store professional details for the person represented by the contact.             

        :return: The professional_info of this MapiContactDto.
        :rtype: MapiContactProfessionalPropertySetDto
        """
        return self._professional_info

    @professional_info.setter
    def professional_info(self, professional_info: MapiContactProfessionalPropertySetDto):
        """
        Properties are used to store professional details for the person represented by the contact.             

        :param professional_info: The professional_info of this MapiContactDto.
        :type: MapiContactProfessionalPropertySetDto
        """
        self._professional_info = professional_info

    @property
    def telephones(self) -> MapiContactTelephonePropertySetDto:
        """
        Specify telephone numbers for the contact.             

        :return: The telephones of this MapiContactDto.
        :rtype: MapiContactTelephonePropertySetDto
        """
        return self._telephones

    @telephones.setter
    def telephones(self, telephones: MapiContactTelephonePropertySetDto):
        """
        Specify telephone numbers for the contact.             

        :param telephones: The telephones of this MapiContactDto.
        :type: MapiContactTelephonePropertySetDto
        """
        self._telephones = telephones

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
        if not isinstance(other, MapiContactDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
