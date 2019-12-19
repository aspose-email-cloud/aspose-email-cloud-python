#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="Link.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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


class Link(object):
    """Provides information for the object link. This is supposed to be an atom:link, therefore it should have all attributes specified here http://tools.ietf.org/html/rfc4287#section-4.2.7             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'rel': 'str',
        'type': 'str',
        'title': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel',
        'type': 'type',
        'title': 'title'
    }

    def __init__(self, href: str = None, rel: str = None, type: str = None, title: str = None):
        """Link - a model defined in Swagger"""

        self._href = None
        self._rel = None
        self._type = None
        self._title = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title

    @property
    def href(self) -> str:
        """Gets the href of this Link.

        The \"href\" attribute contains the link's IRI. atom:link elements MUST have an href attribute, whose value MUST be a IRI reference             

        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this Link.

        The \"href\" attribute contains the link's IRI. atom:link elements MUST have an href attribute, whose value MUST be a IRI reference             

        :param href: The href of this Link.
        :type: str
        """
        self._href = href

    @property
    def rel(self) -> str:
        """Gets the rel of this Link.

        atom:link elements MAY have a \"rel\" attribute that indicates the link relation type.  If the \"rel\" attribute is not present, the link element MUST be interpreted as if the link relation type is \"alternate\".             

        :return: The rel of this Link.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this Link.

        atom:link elements MAY have a \"rel\" attribute that indicates the link relation type.  If the \"rel\" attribute is not present, the link element MUST be interpreted as if the link relation type is \"alternate\".             

        :param rel: The rel of this Link.
        :type: str
        """
        self._rel = rel

    @property
    def type(self) -> str:
        """Gets the type of this Link.

        On the link element, the \"type\" attribute's value is an advisory media type: it is a hint about the type of the representation that is expected to be returned when the value of the href attribute is dereferenced.  Note that the type attribute does not override the actual media type returned with the representation.             

        :return: The type of this Link.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Link.

        On the link element, the \"type\" attribute's value is an advisory media type: it is a hint about the type of the representation that is expected to be returned when the value of the href attribute is dereferenced.  Note that the type attribute does not override the actual media type returned with the representation.             

        :param type: The type of this Link.
        :type: str
        """
        self._type = type

    @property
    def title(self) -> str:
        """Gets the title of this Link.

        The \"title\" attribute conveys human-readable information about the link.  The content of the \"title\" attribute is Language-Sensitive.             

        :return: The title of this Link.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Link.

        The \"title\" attribute conveys human-readable information about the link.  The content of the \"title\" attribute is Language-Sensitive.             

        :param title: The title of this Link.
        :type: str
        """
        self._title = title

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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
