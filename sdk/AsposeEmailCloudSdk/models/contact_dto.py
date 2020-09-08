#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ContactDto.py">
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

from AsposeEmailCloudSdk.models.associated_person import AssociatedPerson
from AsposeEmailCloudSdk.models.attachment import Attachment
from AsposeEmailCloudSdk.models.contact_photo import ContactPhoto
from AsposeEmailCloudSdk.models.customer_event import CustomerEvent
from AsposeEmailCloudSdk.models.email_address import EmailAddress
from AsposeEmailCloudSdk.models.instant_messenger_address import InstantMessengerAddress
from AsposeEmailCloudSdk.models.phone_number import PhoneNumber
from AsposeEmailCloudSdk.models.postal_address import PostalAddress
from AsposeEmailCloudSdk.models.url import Url


class ContactDto(object):
    """VCard document representation.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'associated_persons': 'list[AssociatedPerson]',
        'attachments': 'list[Attachment]',
        'company_name': 'str',
        'computer_network_name': 'str',
        'customer_id': 'str',
        'department_name': 'str',
        'display_name': 'str',
        'email_addresses': 'list[EmailAddress]',
        'events': 'list[CustomerEvent]',
        'file_as': 'str',
        'file_as_mapping': 'str',
        'free_busy_location': 'str',
        'gender': 'str',
        'given_name': 'str',
        'government_id_number': 'str',
        'hobbies': 'str',
        'initials': 'str',
        'instant_messengers': 'list[InstantMessengerAddress]',
        'job_title': 'str',
        'language': 'str',
        'location': 'str',
        'middle_name': 'str',
        'nickname': 'str',
        'notes': 'str',
        'notes_format': 'str',
        'office_location': 'str',
        'organizational_id_number': 'str',
        'phone_numbers': 'list[PhoneNumber]',
        'photo': 'ContactPhoto',
        'physical_addresses': 'list[PostalAddress]',
        'preferred_text_encoding': 'str',
        'prefix': 'str',
        'profession': 'str',
        'suffix': 'str',
        'surname': 'str',
        'urls': 'list[Url]'
    }

    attribute_map = {
        'associated_persons': 'associatedPersons',
        'attachments': 'attachments',
        'company_name': 'companyName',
        'computer_network_name': 'computerNetworkName',
        'customer_id': 'customerId',
        'department_name': 'departmentName',
        'display_name': 'displayName',
        'email_addresses': 'emailAddresses',
        'events': 'events',
        'file_as': 'fileAs',
        'file_as_mapping': 'fileAsMapping',
        'free_busy_location': 'freeBusyLocation',
        'gender': 'gender',
        'given_name': 'givenName',
        'government_id_number': 'governmentIdNumber',
        'hobbies': 'hobbies',
        'initials': 'initials',
        'instant_messengers': 'instantMessengers',
        'job_title': 'jobTitle',
        'language': 'language',
        'location': 'location',
        'middle_name': 'middleName',
        'nickname': 'nickname',
        'notes': 'notes',
        'notes_format': 'notesFormat',
        'office_location': 'officeLocation',
        'organizational_id_number': 'organizationalIdNumber',
        'phone_numbers': 'phoneNumbers',
        'photo': 'photo',
        'physical_addresses': 'physicalAddresses',
        'preferred_text_encoding': 'preferredTextEncoding',
        'prefix': 'prefix',
        'profession': 'profession',
        'suffix': 'suffix',
        'surname': 'surname',
        'urls': 'urls'
    }

    def __init__(self, associated_persons: List[AssociatedPerson] = None, attachments: List[Attachment] = None, company_name: str = None, computer_network_name: str = None, customer_id: str = None, department_name: str = None, display_name: str = None, email_addresses: List[EmailAddress] = None, events: List[CustomerEvent] = None, file_as: str = None, file_as_mapping: str = None, free_busy_location: str = None, gender: str = None, given_name: str = None, government_id_number: str = None, hobbies: str = None, initials: str = None, instant_messengers: List[InstantMessengerAddress] = None, job_title: str = None, language: str = None, location: str = None, middle_name: str = None, nickname: str = None, notes: str = None, notes_format: str = None, office_location: str = None, organizational_id_number: str = None, phone_numbers: List[PhoneNumber] = None, photo: ContactPhoto = None, physical_addresses: List[PostalAddress] = None, preferred_text_encoding: str = None, prefix: str = None, profession: str = None, suffix: str = None, surname: str = None, urls: List[Url] = None):
        """
        VCard document representation.             
        :param associated_persons: Associated persons.             
        :type associated_persons: List[AssociatedPerson]
        :param attachments: Document attachments.             
        :type attachments: List[Attachment]
        :param company_name: Company name.             
        :type company_name: str
        :param computer_network_name: Computer network.             
        :type computer_network_name: str
        :param customer_id: Customer id.             
        :type customer_id: str
        :param department_name: Department name.             
        :type department_name: str
        :param display_name: Display name.             
        :type display_name: str
        :param email_addresses: Person's email addresses.             
        :type email_addresses: List[EmailAddress]
        :param events: Person's events.             
        :type events: List[CustomerEvent]
        :param file_as: A name used for sorting.             
        :type file_as: str
        :param file_as_mapping: Specifies how to generate and recompute the value of the dispidFileAs property when other contact name properties change. Coincides MS-OXPROPS revision 16.2 from 7/31/2014. Enum, available values: Empty, DisplayName, FirstName, LastName, Organization, LastFirstMiddle, OrgLastFirstMiddle, LastFirstMiddleOrg, LastFirstMiddle2, LastFirstMiddle3, OrgLastFirstMiddle2, OrgLastFirstMiddle3, LastFirstMiddleOrg2, LastFirstMiddleOrg3, LastFirstMiddleGen, FirstMiddleLastGen, LastFirstMiddleGen2, BestMatch, AccordingToLocale, None
        :type file_as_mapping: str
        :param free_busy_location: URL path from which a client can retrieve free/busy information for the contact as an iCal file.             
        :type free_busy_location: str
        :param gender: Enum defines gender of a person. Enum, available values: Unspecified, Female, Male
        :type gender: str
        :param given_name: Person's given name.             
        :type given_name: str
        :param government_id_number: Government id number.             
        :type government_id_number: str
        :param hobbies: Person's hobbies.             
        :type hobbies: str
        :param initials: Person's initials.             
        :type initials: str
        :param instant_messengers: Person's instant messenger addresses.             
        :type instant_messengers: List[InstantMessengerAddress]
        :param job_title: Person's job title.             
        :type job_title: str
        :param language: Language.             
        :type language: str
        :param location: Person's location.             
        :type location: str
        :param middle_name: Person's middle name.             
        :type middle_name: str
        :param nickname: Person's nickname.             
        :type nickname: str
        :param notes: Notes.             
        :type notes: str
        :param notes_format: Defines format of a text. Enum, available values: Text, Html
        :type notes_format: str
        :param office_location: Office location.             
        :type office_location: str
        :param organizational_id_number: Contains an identifier for the mail user used within the mail user's organization.             
        :type organizational_id_number: str
        :param phone_numbers: Person's phone numbers.             
        :type phone_numbers: List[PhoneNumber]
        :param photo: Person's photo.             
        :type photo: ContactPhoto
        :param physical_addresses: Person's physical addresses.             
        :type physical_addresses: List[PostalAddress]
        :param preferred_text_encoding: Encoding for all text properties.             
        :type preferred_text_encoding: str
        :param prefix: A prefix of a full name such like Mr.(mister), Dr.(doctor) and so on.             
        :type prefix: str
        :param profession: A job position of a person in a company.             
        :type profession: str
        :param suffix: A suffix of a full name such like Jr.(junior), Sr.(senior) and so on.             
        :type suffix: str
        :param surname: Person's surname.             
        :type surname: str
        :param urls: Person's urls.             
        :type urls: List[Url]
        """

        self._associated_persons = None
        self._attachments = None
        self._company_name = None
        self._computer_network_name = None
        self._customer_id = None
        self._department_name = None
        self._display_name = None
        self._email_addresses = None
        self._events = None
        self._file_as = None
        self._file_as_mapping = None
        self._free_busy_location = None
        self._gender = None
        self._given_name = None
        self._government_id_number = None
        self._hobbies = None
        self._initials = None
        self._instant_messengers = None
        self._job_title = None
        self._language = None
        self._location = None
        self._middle_name = None
        self._nickname = None
        self._notes = None
        self._notes_format = None
        self._office_location = None
        self._organizational_id_number = None
        self._phone_numbers = None
        self._photo = None
        self._physical_addresses = None
        self._preferred_text_encoding = None
        self._prefix = None
        self._profession = None
        self._suffix = None
        self._surname = None
        self._urls = None

        if associated_persons is not None:
            self.associated_persons = associated_persons
        if attachments is not None:
            self.attachments = attachments
        if company_name is not None:
            self.company_name = company_name
        if computer_network_name is not None:
            self.computer_network_name = computer_network_name
        if customer_id is not None:
            self.customer_id = customer_id
        if department_name is not None:
            self.department_name = department_name
        if display_name is not None:
            self.display_name = display_name
        if email_addresses is not None:
            self.email_addresses = email_addresses
        if events is not None:
            self.events = events
        if file_as is not None:
            self.file_as = file_as
        if file_as_mapping is not None:
            self.file_as_mapping = file_as_mapping
        if free_busy_location is not None:
            self.free_busy_location = free_busy_location
        if gender is not None:
            self.gender = gender
        if given_name is not None:
            self.given_name = given_name
        if government_id_number is not None:
            self.government_id_number = government_id_number
        if hobbies is not None:
            self.hobbies = hobbies
        if initials is not None:
            self.initials = initials
        if instant_messengers is not None:
            self.instant_messengers = instant_messengers
        if job_title is not None:
            self.job_title = job_title
        if language is not None:
            self.language = language
        if location is not None:
            self.location = location
        if middle_name is not None:
            self.middle_name = middle_name
        if nickname is not None:
            self.nickname = nickname
        if notes is not None:
            self.notes = notes
        if notes_format is not None:
            self.notes_format = notes_format
        if office_location is not None:
            self.office_location = office_location
        if organizational_id_number is not None:
            self.organizational_id_number = organizational_id_number
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if photo is not None:
            self.photo = photo
        if physical_addresses is not None:
            self.physical_addresses = physical_addresses
        if preferred_text_encoding is not None:
            self.preferred_text_encoding = preferred_text_encoding
        if prefix is not None:
            self.prefix = prefix
        if profession is not None:
            self.profession = profession
        if suffix is not None:
            self.suffix = suffix
        if surname is not None:
            self.surname = surname
        if urls is not None:
            self.urls = urls


    @property
    def associated_persons(self) -> List[AssociatedPerson]:
        """
        Associated persons.             

        :return: The associated_persons of this ContactDto.
        :rtype: list[AssociatedPerson]
        """
        return self._associated_persons

    @associated_persons.setter
    def associated_persons(self, associated_persons: List[AssociatedPerson]):
        """
        Associated persons.             

        :param associated_persons: The associated_persons of this ContactDto.
        :type: list[AssociatedPerson]
        """
        self._associated_persons = associated_persons

    @property
    def attachments(self) -> List[Attachment]:
        """
        Document attachments.             

        :return: The attachments of this ContactDto.
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List[Attachment]):
        """
        Document attachments.             

        :param attachments: The attachments of this ContactDto.
        :type: list[Attachment]
        """
        self._attachments = attachments

    @property
    def company_name(self) -> str:
        """
        Company name.             

        :return: The company_name of this ContactDto.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """
        Company name.             

        :param company_name: The company_name of this ContactDto.
        :type: str
        """
        self._company_name = company_name

    @property
    def computer_network_name(self) -> str:
        """
        Computer network.             

        :return: The computer_network_name of this ContactDto.
        :rtype: str
        """
        return self._computer_network_name

    @computer_network_name.setter
    def computer_network_name(self, computer_network_name: str):
        """
        Computer network.             

        :param computer_network_name: The computer_network_name of this ContactDto.
        :type: str
        """
        self._computer_network_name = computer_network_name

    @property
    def customer_id(self) -> str:
        """
        Customer id.             

        :return: The customer_id of this ContactDto.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """
        Customer id.             

        :param customer_id: The customer_id of this ContactDto.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def department_name(self) -> str:
        """
        Department name.             

        :return: The department_name of this ContactDto.
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name: str):
        """
        Department name.             

        :param department_name: The department_name of this ContactDto.
        :type: str
        """
        self._department_name = department_name

    @property
    def display_name(self) -> str:
        """
        Display name.             

        :return: The display_name of this ContactDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        Display name.             

        :param display_name: The display_name of this ContactDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def email_addresses(self) -> List[EmailAddress]:
        """
        Person's email addresses.             

        :return: The email_addresses of this ContactDto.
        :rtype: list[EmailAddress]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses: List[EmailAddress]):
        """
        Person's email addresses.             

        :param email_addresses: The email_addresses of this ContactDto.
        :type: list[EmailAddress]
        """
        self._email_addresses = email_addresses

    @property
    def events(self) -> List[CustomerEvent]:
        """
        Person's events.             

        :return: The events of this ContactDto.
        :rtype: list[CustomerEvent]
        """
        return self._events

    @events.setter
    def events(self, events: List[CustomerEvent]):
        """
        Person's events.             

        :param events: The events of this ContactDto.
        :type: list[CustomerEvent]
        """
        self._events = events

    @property
    def file_as(self) -> str:
        """
        A name used for sorting.             

        :return: The file_as of this ContactDto.
        :rtype: str
        """
        return self._file_as

    @file_as.setter
    def file_as(self, file_as: str):
        """
        A name used for sorting.             

        :param file_as: The file_as of this ContactDto.
        :type: str
        """
        self._file_as = file_as

    @property
    def file_as_mapping(self) -> str:
        """
        Specifies how to generate and recompute the value of the dispidFileAs property when other contact name properties change. Coincides MS-OXPROPS revision 16.2 from 7/31/2014. Enum, available values: Empty, DisplayName, FirstName, LastName, Organization, LastFirstMiddle, OrgLastFirstMiddle, LastFirstMiddleOrg, LastFirstMiddle2, LastFirstMiddle3, OrgLastFirstMiddle2, OrgLastFirstMiddle3, LastFirstMiddleOrg2, LastFirstMiddleOrg3, LastFirstMiddleGen, FirstMiddleLastGen, LastFirstMiddleGen2, BestMatch, AccordingToLocale, None

        :return: The file_as_mapping of this ContactDto.
        :rtype: str
        """
        return self._file_as_mapping

    @file_as_mapping.setter
    def file_as_mapping(self, file_as_mapping: str):
        """
        Specifies how to generate and recompute the value of the dispidFileAs property when other contact name properties change. Coincides MS-OXPROPS revision 16.2 from 7/31/2014. Enum, available values: Empty, DisplayName, FirstName, LastName, Organization, LastFirstMiddle, OrgLastFirstMiddle, LastFirstMiddleOrg, LastFirstMiddle2, LastFirstMiddle3, OrgLastFirstMiddle2, OrgLastFirstMiddle3, LastFirstMiddleOrg2, LastFirstMiddleOrg3, LastFirstMiddleGen, FirstMiddleLastGen, LastFirstMiddleGen2, BestMatch, AccordingToLocale, None

        :param file_as_mapping: The file_as_mapping of this ContactDto.
        :type: str
        """
        if file_as_mapping is None:
            raise ValueError("Invalid value for `file_as_mapping`, must not be `None`")
        self._file_as_mapping = file_as_mapping

    @property
    def free_busy_location(self) -> str:
        """
        URL path from which a client can retrieve free/busy information for the contact as an iCal file.             

        :return: The free_busy_location of this ContactDto.
        :rtype: str
        """
        return self._free_busy_location

    @free_busy_location.setter
    def free_busy_location(self, free_busy_location: str):
        """
        URL path from which a client can retrieve free/busy information for the contact as an iCal file.             

        :param free_busy_location: The free_busy_location of this ContactDto.
        :type: str
        """
        self._free_busy_location = free_busy_location

    @property
    def gender(self) -> str:
        """
        Enum defines gender of a person. Enum, available values: Unspecified, Female, Male

        :return: The gender of this ContactDto.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """
        Enum defines gender of a person. Enum, available values: Unspecified, Female, Male

        :param gender: The gender of this ContactDto.
        :type: str
        """
        if gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")
        self._gender = gender

    @property
    def given_name(self) -> str:
        """
        Person's given name.             

        :return: The given_name of this ContactDto.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name: str):
        """
        Person's given name.             

        :param given_name: The given_name of this ContactDto.
        :type: str
        """
        self._given_name = given_name

    @property
    def government_id_number(self) -> str:
        """
        Government id number.             

        :return: The government_id_number of this ContactDto.
        :rtype: str
        """
        return self._government_id_number

    @government_id_number.setter
    def government_id_number(self, government_id_number: str):
        """
        Government id number.             

        :param government_id_number: The government_id_number of this ContactDto.
        :type: str
        """
        self._government_id_number = government_id_number

    @property
    def hobbies(self) -> str:
        """
        Person's hobbies.             

        :return: The hobbies of this ContactDto.
        :rtype: str
        """
        return self._hobbies

    @hobbies.setter
    def hobbies(self, hobbies: str):
        """
        Person's hobbies.             

        :param hobbies: The hobbies of this ContactDto.
        :type: str
        """
        self._hobbies = hobbies

    @property
    def initials(self) -> str:
        """
        Person's initials.             

        :return: The initials of this ContactDto.
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials: str):
        """
        Person's initials.             

        :param initials: The initials of this ContactDto.
        :type: str
        """
        self._initials = initials

    @property
    def instant_messengers(self) -> List[InstantMessengerAddress]:
        """
        Person's instant messenger addresses.             

        :return: The instant_messengers of this ContactDto.
        :rtype: list[InstantMessengerAddress]
        """
        return self._instant_messengers

    @instant_messengers.setter
    def instant_messengers(self, instant_messengers: List[InstantMessengerAddress]):
        """
        Person's instant messenger addresses.             

        :param instant_messengers: The instant_messengers of this ContactDto.
        :type: list[InstantMessengerAddress]
        """
        self._instant_messengers = instant_messengers

    @property
    def job_title(self) -> str:
        """
        Person's job title.             

        :return: The job_title of this ContactDto.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title: str):
        """
        Person's job title.             

        :param job_title: The job_title of this ContactDto.
        :type: str
        """
        self._job_title = job_title

    @property
    def language(self) -> str:
        """
        Language.             

        :return: The language of this ContactDto.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """
        Language.             

        :param language: The language of this ContactDto.
        :type: str
        """
        self._language = language

    @property
    def location(self) -> str:
        """
        Person's location.             

        :return: The location of this ContactDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """
        Person's location.             

        :param location: The location of this ContactDto.
        :type: str
        """
        self._location = location

    @property
    def middle_name(self) -> str:
        """
        Person's middle name.             

        :return: The middle_name of this ContactDto.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name: str):
        """
        Person's middle name.             

        :param middle_name: The middle_name of this ContactDto.
        :type: str
        """
        self._middle_name = middle_name

    @property
    def nickname(self) -> str:
        """
        Person's nickname.             

        :return: The nickname of this ContactDto.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname: str):
        """
        Person's nickname.             

        :param nickname: The nickname of this ContactDto.
        :type: str
        """
        self._nickname = nickname

    @property
    def notes(self) -> str:
        """
        Notes.             

        :return: The notes of this ContactDto.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """
        Notes.             

        :param notes: The notes of this ContactDto.
        :type: str
        """
        self._notes = notes

    @property
    def notes_format(self) -> str:
        """
        Defines format of a text. Enum, available values: Text, Html

        :return: The notes_format of this ContactDto.
        :rtype: str
        """
        return self._notes_format

    @notes_format.setter
    def notes_format(self, notes_format: str):
        """
        Defines format of a text. Enum, available values: Text, Html

        :param notes_format: The notes_format of this ContactDto.
        :type: str
        """
        if notes_format is None:
            raise ValueError("Invalid value for `notes_format`, must not be `None`")
        self._notes_format = notes_format

    @property
    def office_location(self) -> str:
        """
        Office location.             

        :return: The office_location of this ContactDto.
        :rtype: str
        """
        return self._office_location

    @office_location.setter
    def office_location(self, office_location: str):
        """
        Office location.             

        :param office_location: The office_location of this ContactDto.
        :type: str
        """
        self._office_location = office_location

    @property
    def organizational_id_number(self) -> str:
        """
        Contains an identifier for the mail user used within the mail user's organization.             

        :return: The organizational_id_number of this ContactDto.
        :rtype: str
        """
        return self._organizational_id_number

    @organizational_id_number.setter
    def organizational_id_number(self, organizational_id_number: str):
        """
        Contains an identifier for the mail user used within the mail user's organization.             

        :param organizational_id_number: The organizational_id_number of this ContactDto.
        :type: str
        """
        self._organizational_id_number = organizational_id_number

    @property
    def phone_numbers(self) -> List[PhoneNumber]:
        """
        Person's phone numbers.             

        :return: The phone_numbers of this ContactDto.
        :rtype: list[PhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers: List[PhoneNumber]):
        """
        Person's phone numbers.             

        :param phone_numbers: The phone_numbers of this ContactDto.
        :type: list[PhoneNumber]
        """
        self._phone_numbers = phone_numbers

    @property
    def photo(self) -> ContactPhoto:
        """
        Person's photo.             

        :return: The photo of this ContactDto.
        :rtype: ContactPhoto
        """
        return self._photo

    @photo.setter
    def photo(self, photo: ContactPhoto):
        """
        Person's photo.             

        :param photo: The photo of this ContactDto.
        :type: ContactPhoto
        """
        self._photo = photo

    @property
    def physical_addresses(self) -> List[PostalAddress]:
        """
        Person's physical addresses.             

        :return: The physical_addresses of this ContactDto.
        :rtype: list[PostalAddress]
        """
        return self._physical_addresses

    @physical_addresses.setter
    def physical_addresses(self, physical_addresses: List[PostalAddress]):
        """
        Person's physical addresses.             

        :param physical_addresses: The physical_addresses of this ContactDto.
        :type: list[PostalAddress]
        """
        self._physical_addresses = physical_addresses

    @property
    def preferred_text_encoding(self) -> str:
        """
        Encoding for all text properties.             

        :return: The preferred_text_encoding of this ContactDto.
        :rtype: str
        """
        return self._preferred_text_encoding

    @preferred_text_encoding.setter
    def preferred_text_encoding(self, preferred_text_encoding: str):
        """
        Encoding for all text properties.             

        :param preferred_text_encoding: The preferred_text_encoding of this ContactDto.
        :type: str
        """
        self._preferred_text_encoding = preferred_text_encoding

    @property
    def prefix(self) -> str:
        """
        A prefix of a full name such like Mr.(mister), Dr.(doctor) and so on.             

        :return: The prefix of this ContactDto.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str):
        """
        A prefix of a full name such like Mr.(mister), Dr.(doctor) and so on.             

        :param prefix: The prefix of this ContactDto.
        :type: str
        """
        self._prefix = prefix

    @property
    def profession(self) -> str:
        """
        A job position of a person in a company.             

        :return: The profession of this ContactDto.
        :rtype: str
        """
        return self._profession

    @profession.setter
    def profession(self, profession: str):
        """
        A job position of a person in a company.             

        :param profession: The profession of this ContactDto.
        :type: str
        """
        self._profession = profession

    @property
    def suffix(self) -> str:
        """
        A suffix of a full name such like Jr.(junior), Sr.(senior) and so on.             

        :return: The suffix of this ContactDto.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str):
        """
        A suffix of a full name such like Jr.(junior), Sr.(senior) and so on.             

        :param suffix: The suffix of this ContactDto.
        :type: str
        """
        self._suffix = suffix

    @property
    def surname(self) -> str:
        """
        Person's surname.             

        :return: The surname of this ContactDto.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """
        Person's surname.             

        :param surname: The surname of this ContactDto.
        :type: str
        """
        self._surname = surname

    @property
    def urls(self) -> List[Url]:
        """
        Person's urls.             

        :return: The urls of this ContactDto.
        :rtype: list[Url]
        """
        return self._urls

    @urls.setter
    def urls(self, urls: List[Url]):
        """
        Person's urls.             

        :param urls: The urls of this ContactDto.
        :type: list[Url]
        """
        self._urls = urls

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
        if not isinstance(other, ContactDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
