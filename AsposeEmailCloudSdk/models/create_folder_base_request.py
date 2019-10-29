#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CreateFolderBaseRequest.py">
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

from AsposeEmailCloudSdk.models.account_base_request import AccountBaseRequest
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class CreateFolderBaseRequest(AccountBaseRequest):
    """Create folder request
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'folder': 'str',
        'parent_folder': 'str'
    }

    attribute_map = {
        'folder': 'folder',
        'parent_folder': 'parentFolder'
    }

    def __init__(self, folder=None, parent_folder=None):
        """CreateFolderBaseRequest - a model defined in Swagger"""

        self._folder = None
        self._parent_folder = None
        self.discriminator = None

        if folder is not None:
            self.folder = folder
        if parent_folder is not None:
            self.parent_folder = parent_folder

    @property
    def folder(self):
        """Gets the folder of this CreateFolderBaseRequest.

        Folder name

        :return: The folder of this CreateFolderBaseRequest.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this CreateFolderBaseRequest.

        Folder name

        :param folder: The folder of this CreateFolderBaseRequest.
        :type: str
        """
        if folder is None:
            raise ValueError("Invalid value for `folder`, must not be `None`")
        if folder is not None and len(folder) < 1:
            raise ValueError("Invalid value for `folder`, length must be greater than or equal to `1`")
        self._folder = folder

    @property
    def parent_folder(self):
        """Gets the parent_folder of this CreateFolderBaseRequest.

        Parent folder path

        :return: The parent_folder of this CreateFolderBaseRequest.
        :rtype: str
        """
        return self._parent_folder

    @parent_folder.setter
    def parent_folder(self, parent_folder):
        """Sets the parent_folder of this CreateFolderBaseRequest.

        Parent folder path

        :param parent_folder: The parent_folder of this CreateFolderBaseRequest.
        :type: str
        """
        self._parent_folder = parent_folder

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
        if not isinstance(other, CreateFolderBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
