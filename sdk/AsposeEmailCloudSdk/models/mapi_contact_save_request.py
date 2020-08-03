#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="MapiContactSaveRequest.py">
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

from AsposeEmailCloudSdk.models.mapi_contact_dto import MapiContactDto
from AsposeEmailCloudSdk.models.storage_file_location import StorageFileLocation
from AsposeEmailCloudSdk.models.storage_model_of_mapi_contact_dto import StorageModelOfMapiContactDto


class MapiContactSaveRequest(StorageModelOfMapiContactDto):
    """MapiContact save to storage request.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_file': 'StorageFileLocation',
        'value': 'MapiContactDto',
        'format': 'str'
    }

    attribute_map = {
        'storage_file': 'storageFile',
        'value': 'value',
        'format': 'format'
    }

    def __init__(self, storage_file: StorageFileLocation = None, value: MapiContactDto = None, format: str = None):
        """
        MapiContact save to storage request.             
        :param storage_file: 
        :type storage_file: StorageFileLocation
        :param value: 
        :type value: MapiContactDto
        :param format: Enumerates contact formats. Enum, available values: VCard, WebDav, Msg
        :type format: str
        """
        super(MapiContactSaveRequest, self).__init__()

        self._format = None

        if storage_file is not None:
            self.storage_file = storage_file
        if value is not None:
            self.value = value
        if format is not None:
            self.format = format


    @property
    def format(self) -> str:
        """
        Enumerates contact formats. Enum, available values: VCard, WebDav, Msg

        :return: The format of this MapiContactSaveRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str):
        """
        Enumerates contact formats. Enum, available values: VCard, WebDav, Msg

        :param format: The format of this MapiContactSaveRequest.
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")
        self._format = format

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
        if not isinstance(other, MapiContactSaveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
