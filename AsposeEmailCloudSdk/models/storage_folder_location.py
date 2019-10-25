#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="StorageFolderLocation.py">
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


class StorageFolderLocation(object):
    """A storage folder location information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage': 'str',
        'folder_path': 'str'
    }

    attribute_map = {
        'storage': 'Storage',
        'folder_path': 'FolderPath'
    }

    discriminator_value_class_map = {
        'StorageFileLocation': 'StorageFileLocation'
    }

    def __init__(self, storage=None, folder_path=None):
        """StorageFolderLocation - a model defined in Swagger"""

        self._storage = None
        self._folder_path = None
        self.discriminator = 'Type'

        if storage is not None:
            self.storage = storage
        if folder_path is not None:
            self.folder_path = folder_path

    @property
    def storage(self):
        """Gets the storage of this StorageFolderLocation.

        A storage name

        :return: The storage of this StorageFolderLocation.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this StorageFolderLocation.

        A storage name

        :param storage: The storage of this StorageFolderLocation.
        :type: str
        """
        self._storage = storage

    @property
    def folder_path(self):
        """Gets the folder_path of this StorageFolderLocation.

        A path to a folder in specified storage

        :return: The folder_path of this StorageFolderLocation.
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this StorageFolderLocation.

        A path to a folder in specified storage

        :param folder_path: The folder_path of this StorageFolderLocation.
        :type: str
        """
        self._folder_path = folder_path

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, StorageFolderLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
