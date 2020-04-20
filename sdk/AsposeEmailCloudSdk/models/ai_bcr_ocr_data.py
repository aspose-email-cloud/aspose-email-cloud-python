#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiBcrOcrData.py">
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

from AsposeEmailCloudSdk.models.ai_bcr_ocr_data_part import AiBcrOcrDataPart


class AiBcrOcrData(object):
    """Image OCR results             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'image': 'str',
        'details': 'dict(str, str)',
        'data': 'list[AiBcrOcrDataPart]'
    }

    attribute_map = {
        'id': 'id',
        'image': 'image',
        'details': 'details',
        'data': 'data'
    }

    def __init__(self, id: str = None, image: str = None, details: Dict[str, str] = None, data: List[AiBcrOcrDataPart] = None):
        """
        Image OCR results             
        :param id (str) Image identifier             
        :param image (str) Image with possible pre-processing in Base64             
        :param details (Dict[str, str]) Additional details from OCR engine             
        :param data (List[AiBcrOcrDataPart]) OCR results             
        """

        self._id = None
        self._image = None
        self._details = None
        self._data = None

        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if details is not None:
            self.details = details
        if data is not None:
            self.data = data

    @property
    def id(self) -> str:
        """Gets the id of this AiBcrOcrData.

        Image identifier             

        :return: The id of this AiBcrOcrData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AiBcrOcrData.

        Image identifier             

        :param id: The id of this AiBcrOcrData.
        :type: str
        """
        self._id = id

    @property
    def image(self) -> str:
        """Gets the image of this AiBcrOcrData.

        Image with possible pre-processing in Base64             

        :return: The image of this AiBcrOcrData.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this AiBcrOcrData.

        Image with possible pre-processing in Base64             

        :param image: The image of this AiBcrOcrData.
        :type: str
        """
        self._image = image

    @property
    def details(self) -> Dict[str, str]:
        """Gets the details of this AiBcrOcrData.

        Additional details from OCR engine             

        :return: The details of this AiBcrOcrData.
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details: Dict[str, str]):
        """Sets the details of this AiBcrOcrData.

        Additional details from OCR engine             

        :param details: The details of this AiBcrOcrData.
        :type: dict(str, str)
        """
        self._details = details

    @property
    def data(self) -> List[AiBcrOcrDataPart]:
        """Gets the data of this AiBcrOcrData.

        OCR results             

        :return: The data of this AiBcrOcrData.
        :rtype: list[AiBcrOcrDataPart]
        """
        return self._data

    @data.setter
    def data(self, data: List[AiBcrOcrDataPart]):
        """Sets the data of this AiBcrOcrData.

        OCR results             

        :param data: The data of this AiBcrOcrData.
        :type: list[AiBcrOcrDataPart]
        """
        self._data = data

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
        if not isinstance(other, AiBcrOcrData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
