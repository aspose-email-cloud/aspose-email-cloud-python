#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="HierarchicalObjectResponse.py">
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

from AsposeEmailCloudSdk.models.hierarchical_object import HierarchicalObject
from AsposeEmailCloudSdk.models.storage_file import StorageFile


class HierarchicalObjectResponse(object):
    """Document represented as hierarchical set of properties response
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hierarchical_object': 'HierarchicalObject',
        'storage_file': 'StorageFile'
    }

    attribute_map = {
        'hierarchical_object': 'HierarchicalObject',
        'storage_file': 'StorageFile'
    }

    def __init__(self, hierarchical_object=None, storage_file=None):
        """HierarchicalObjectResponse - a model defined in Swagger"""

        self._hierarchical_object = None
        self._storage_file = None
        self.discriminator = None

        if hierarchical_object is not None:
            self.hierarchical_object = hierarchical_object
        if storage_file is not None:
            self.storage_file = storage_file

    @property
    def hierarchical_object(self):
        """Gets the hierarchical_object of this HierarchicalObjectResponse.

        Document properties

        :return: The hierarchical_object of this HierarchicalObjectResponse.
        :rtype: HierarchicalObject
        """
        return self._hierarchical_object

    @hierarchical_object.setter
    def hierarchical_object(self, hierarchical_object):
        """Sets the hierarchical_object of this HierarchicalObjectResponse.

        Document properties

        :param hierarchical_object: The hierarchical_object of this HierarchicalObjectResponse.
        :type: HierarchicalObject
        """
        self._hierarchical_object = hierarchical_object

    @property
    def storage_file(self):
        """Gets the storage_file of this HierarchicalObjectResponse.

        Document location in storage

        :return: The storage_file of this HierarchicalObjectResponse.
        :rtype: StorageFile
        """
        return self._storage_file

    @storage_file.setter
    def storage_file(self, storage_file):
        """Sets the storage_file of this HierarchicalObjectResponse.

        Document location in storage

        :param storage_file: The storage_file of this HierarchicalObjectResponse.
        :type: StorageFile
        """
        self._storage_file = storage_file

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
        if not isinstance(other, HierarchicalObjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
