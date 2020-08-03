#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactNamePropertySetDto.py">
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


class MapiContactNamePropertySetDto(object):
    """The properties are used to specify the name of the person represented by the contact             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_name': 'str',
        'display_name_prefix': 'str',
        'file_under': 'str',
        'file_under_id': 'int',
        'generation': 'str',
        'given_name': 'str',
        'initials': 'str',
        'middle_name': 'str',
        'nickname': 'str',
        'surname': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'display_name_prefix': 'displayNamePrefix',
        'file_under': 'fileUnder',
        'file_under_id': 'fileUnderId',
        'generation': 'generation',
        'given_name': 'givenName',
        'initials': 'initials',
        'middle_name': 'middleName',
        'nickname': 'nickname',
        'surname': 'surname'
    }

    def __init__(self, display_name: str = None, display_name_prefix: str = None, file_under: str = None, file_under_id: int = None, generation: str = None, given_name: str = None, initials: str = None, middle_name: str = None, nickname: str = None, surname: str = None):
        """
        The properties are used to specify the name of the person represented by the contact             
        :param display_name: Full name of the contact             
        :type display_name: str
        :param display_name_prefix: Title of the contact             
        :type display_name_prefix: str
        :param file_under: Name under which to file this contact when displaying a list of contacts             
        :type file_under: str
        :param file_under_id: Value specifying how to generate and recompute the property when other properties are changed             
        :type file_under_id: int
        :param generation: Generation suffix of the contact             
        :type generation: str
        :param given_name: Given name (first name) of the contact             
        :type given_name: str
        :param initials: Initials of the contact             
        :type initials: str
        :param middle_name: Middle name of the contact             
        :type middle_name: str
        :param nickname: Nickname of the contact             
        :type nickname: str
        :param surname: Surname (family name) of the contact             
        :type surname: str
        """

        self._display_name = None
        self._display_name_prefix = None
        self._file_under = None
        self._file_under_id = None
        self._generation = None
        self._given_name = None
        self._initials = None
        self._middle_name = None
        self._nickname = None
        self._surname = None

        if display_name is not None:
            self.display_name = display_name
        if display_name_prefix is not None:
            self.display_name_prefix = display_name_prefix
        if file_under is not None:
            self.file_under = file_under
        if file_under_id is not None:
            self.file_under_id = file_under_id
        if generation is not None:
            self.generation = generation
        if given_name is not None:
            self.given_name = given_name
        if initials is not None:
            self.initials = initials
        if middle_name is not None:
            self.middle_name = middle_name
        if nickname is not None:
            self.nickname = nickname
        if surname is not None:
            self.surname = surname


    @property
    def display_name(self) -> str:
        """
        Full name of the contact             

        :return: The display_name of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """
        Full name of the contact             

        :param display_name: The display_name of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._display_name = display_name

    @property
    def display_name_prefix(self) -> str:
        """
        Title of the contact             

        :return: The display_name_prefix of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._display_name_prefix

    @display_name_prefix.setter
    def display_name_prefix(self, display_name_prefix: str):
        """
        Title of the contact             

        :param display_name_prefix: The display_name_prefix of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._display_name_prefix = display_name_prefix

    @property
    def file_under(self) -> str:
        """
        Name under which to file this contact when displaying a list of contacts             

        :return: The file_under of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._file_under

    @file_under.setter
    def file_under(self, file_under: str):
        """
        Name under which to file this contact when displaying a list of contacts             

        :param file_under: The file_under of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._file_under = file_under

    @property
    def file_under_id(self) -> int:
        """
        Value specifying how to generate and recompute the property when other properties are changed             

        :return: The file_under_id of this MapiContactNamePropertySetDto.
        :rtype: int
        """
        return self._file_under_id

    @file_under_id.setter
    def file_under_id(self, file_under_id: int):
        """
        Value specifying how to generate and recompute the property when other properties are changed             

        :param file_under_id: The file_under_id of this MapiContactNamePropertySetDto.
        :type: int
        """
        if file_under_id is None:
            raise ValueError("Invalid value for `file_under_id`, must not be `None`")
        self._file_under_id = file_under_id

    @property
    def generation(self) -> str:
        """
        Generation suffix of the contact             

        :return: The generation of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation: str):
        """
        Generation suffix of the contact             

        :param generation: The generation of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._generation = generation

    @property
    def given_name(self) -> str:
        """
        Given name (first name) of the contact             

        :return: The given_name of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name: str):
        """
        Given name (first name) of the contact             

        :param given_name: The given_name of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._given_name = given_name

    @property
    def initials(self) -> str:
        """
        Initials of the contact             

        :return: The initials of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials: str):
        """
        Initials of the contact             

        :param initials: The initials of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._initials = initials

    @property
    def middle_name(self) -> str:
        """
        Middle name of the contact             

        :return: The middle_name of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name: str):
        """
        Middle name of the contact             

        :param middle_name: The middle_name of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._middle_name = middle_name

    @property
    def nickname(self) -> str:
        """
        Nickname of the contact             

        :return: The nickname of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname: str):
        """
        Nickname of the contact             

        :param nickname: The nickname of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._nickname = nickname

    @property
    def surname(self) -> str:
        """
        Surname (family name) of the contact             

        :return: The surname of this MapiContactNamePropertySetDto.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """
        Surname (family name) of the contact             

        :param surname: The surname of this MapiContactNamePropertySetDto.
        :type: str
        """
        self._surname = surname

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
        if not isinstance(other, MapiContactNamePropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
