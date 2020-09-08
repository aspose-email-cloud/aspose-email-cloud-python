#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactProfessionalPropertySetDto.py">
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


class MapiContactProfessionalPropertySetDto(object):
    """Properties are used to store professional details for the person represented by the contact             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'company_name': 'str',
        'department_name': 'str',
        'office_location': 'str',
        'manager_name': 'str',
        'assistant': 'str',
        'profession': 'str'
    }

    attribute_map = {
        'title': 'title',
        'company_name': 'companyName',
        'department_name': 'departmentName',
        'office_location': 'officeLocation',
        'manager_name': 'managerName',
        'assistant': 'assistant',
        'profession': 'profession'
    }

    def __init__(self, title: str = None, company_name: str = None, department_name: str = None, office_location: str = None, manager_name: str = None, assistant: str = None, profession: str = None):
        """
        Properties are used to store professional details for the person represented by the contact             
        :param title: Gets or sets the job title of the contact             
        :type title: str
        :param company_name: Gets or sets the company that employs the contact             
        :type company_name: str
        :param department_name: Gets or sets the name of the department to which the contact belongs             
        :type department_name: str
        :param office_location: Gets or sets the location of the office that the contact works in             
        :type office_location: str
        :param manager_name: Gets or sets the name of the contact's manager             
        :type manager_name: str
        :param assistant: Gets or sets the name of the contact's assistant             
        :type assistant: str
        :param profession: Gets or sets the profession of the contact             
        :type profession: str
        """

        self._title = None
        self._company_name = None
        self._department_name = None
        self._office_location = None
        self._manager_name = None
        self._assistant = None
        self._profession = None

        if title is not None:
            self.title = title
        if company_name is not None:
            self.company_name = company_name
        if department_name is not None:
            self.department_name = department_name
        if office_location is not None:
            self.office_location = office_location
        if manager_name is not None:
            self.manager_name = manager_name
        if assistant is not None:
            self.assistant = assistant
        if profession is not None:
            self.profession = profession


    @property
    def title(self) -> str:
        """
        Gets or sets the job title of the contact             

        :return: The title of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """
        Gets or sets the job title of the contact             

        :param title: The title of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._title = title

    @property
    def company_name(self) -> str:
        """
        Gets or sets the company that employs the contact             

        :return: The company_name of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """
        Gets or sets the company that employs the contact             

        :param company_name: The company_name of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._company_name = company_name

    @property
    def department_name(self) -> str:
        """
        Gets or sets the name of the department to which the contact belongs             

        :return: The department_name of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name: str):
        """
        Gets or sets the name of the department to which the contact belongs             

        :param department_name: The department_name of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._department_name = department_name

    @property
    def office_location(self) -> str:
        """
        Gets or sets the location of the office that the contact works in             

        :return: The office_location of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._office_location

    @office_location.setter
    def office_location(self, office_location: str):
        """
        Gets or sets the location of the office that the contact works in             

        :param office_location: The office_location of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._office_location = office_location

    @property
    def manager_name(self) -> str:
        """
        Gets or sets the name of the contact's manager             

        :return: The manager_name of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name: str):
        """
        Gets or sets the name of the contact's manager             

        :param manager_name: The manager_name of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._manager_name = manager_name

    @property
    def assistant(self) -> str:
        """
        Gets or sets the name of the contact's assistant             

        :return: The assistant of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._assistant

    @assistant.setter
    def assistant(self, assistant: str):
        """
        Gets or sets the name of the contact's assistant             

        :param assistant: The assistant of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._assistant = assistant

    @property
    def profession(self) -> str:
        """
        Gets or sets the profession of the contact             

        :return: The profession of this MapiContactProfessionalPropertySetDto.
        :rtype: str
        """
        return self._profession

    @profession.setter
    def profession(self, profession: str):
        """
        Gets or sets the profession of the contact             

        :param profession: The profession of this MapiContactProfessionalPropertySetDto.
        :type: str
        """
        self._profession = profession

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
        if not isinstance(other, MapiContactProfessionalPropertySetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
