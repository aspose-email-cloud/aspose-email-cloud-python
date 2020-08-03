#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ClientFolderCreateRequest.py">
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

from AsposeEmailCloudSdk.models.client_account_base_request import ClientAccountBaseRequest
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation


class ClientFolderCreateRequest(ClientAccountBaseRequest):
    """Email Client create folder request.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_location': 'StorageFileLocation',
        'parent_folder': 'str',
        'folder_name': 'str'
    }

    attribute_map = {
        'account_location': 'accountLocation',
        'parent_folder': 'parentFolder',
        'folder_name': 'folderName'
    }

    def __init__(self, account_location: StorageFileLocation = None, parent_folder: str = None, folder_name: str = None):
        """
        Email Client create folder request.             
        :param account_location: Email client account configuration location on storage.             
        :type account_location: StorageFileLocation
        :param parent_folder: Path to parent folder.             
        :type parent_folder: str
        :param folder_name: Folder name.             
        :type folder_name: str
        """
        super(ClientFolderCreateRequest, self).__init__()

        self._parent_folder = None
        self._folder_name = None

        if account_location is not None:
            self.account_location = account_location
        if parent_folder is not None:
            self.parent_folder = parent_folder
        if folder_name is not None:
            self.folder_name = folder_name


    @property
    def parent_folder(self) -> str:
        """
        Path to parent folder.             

        :return: The parent_folder of this ClientFolderCreateRequest.
        :rtype: str
        """
        return self._parent_folder

    @parent_folder.setter
    def parent_folder(self, parent_folder: str):
        """
        Path to parent folder.             

        :param parent_folder: The parent_folder of this ClientFolderCreateRequest.
        :type: str
        """
        self._parent_folder = parent_folder

    @property
    def folder_name(self) -> str:
        """
        Folder name.             

        :return: The folder_name of this ClientFolderCreateRequest.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name: str):
        """
        Folder name.             

        :param folder_name: The folder_name of this ClientFolderCreateRequest.
        :type: str
        """
        if folder_name is None:
            raise ValueError("Invalid value for `folder_name`, must not be `None`")
        if folder_name is not None and len(folder_name) < 1:
            raise ValueError("Invalid value for `folder_name`, length must be greater than or equal to `1`")
        self._folder_name = folder_name

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
        if not isinstance(other, ClientFolderCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
