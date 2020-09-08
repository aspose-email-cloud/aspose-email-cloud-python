#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ContactPhoto.py">
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


class ContactPhoto(object):
    """Person&#39;s photo.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'photo_image_format': 'str',
        'base64_data': 'str',
        'discriminator': 'str'
    }

    attribute_map = {
        'photo_image_format': 'photoImageFormat',
        'base64_data': 'base64Data',
        'discriminator': 'discriminator'
    }

    def __init__(self, photo_image_format: str = None, base64_data: str = None):
        """
        Person&#39;s photo.             
        :param photo_image_format: MapiContact photo image format. Enum, available values: Undefined, Jpeg, Gif, Wmf, Bmp, Tiff
        :type photo_image_format: str
        :param base64_data: Photo serialized as base64 string.             
        :type base64_data: str
        """

        self._photo_image_format = None
        self._base64_data = None

        if photo_image_format is not None:
            self.photo_image_format = photo_image_format
        if base64_data is not None:
            self.base64_data = base64_data


    @property
    def photo_image_format(self) -> str:
        """
        MapiContact photo image format. Enum, available values: Undefined, Jpeg, Gif, Wmf, Bmp, Tiff

        :return: The photo_image_format of this ContactPhoto.
        :rtype: str
        """
        return self._photo_image_format

    @photo_image_format.setter
    def photo_image_format(self, photo_image_format: str):
        """
        MapiContact photo image format. Enum, available values: Undefined, Jpeg, Gif, Wmf, Bmp, Tiff

        :param photo_image_format: The photo_image_format of this ContactPhoto.
        :type: str
        """
        if photo_image_format is None:
            raise ValueError("Invalid value for `photo_image_format`, must not be `None`")
        self._photo_image_format = photo_image_format

    @property
    def base64_data(self) -> str:
        """
        Photo serialized as base64 string.             

        :return: The base64_data of this ContactPhoto.
        :rtype: str
        """
        return self._base64_data

    @base64_data.setter
    def base64_data(self, base64_data: str):
        """
        Photo serialized as base64 string.             

        :param base64_data: The base64_data of this ContactPhoto.
        :type: str
        """
        if base64_data is None:
            raise ValueError("Invalid value for `base64_data`, must not be `None`")
        if base64_data is not None and len(base64_data) < 1:
            raise ValueError("Invalid value for `base64_data`, length must be greater than or equal to `1`")
        self._base64_data = base64_data

    @property
    def discriminator(self) -> str:
        """
        Gets the discriminator of this ContactPhoto.

        :return: The discriminator of this ContactPhoto.
        :rtype: str
        """
        return self.__class__.__name__

    @discriminator.setter
    def discriminator(self, discriminator: str):
        """
        Sets the discriminator of this ContactPhoto.

        :param discriminator: The discriminator of this ContactPhoto.
        :type: str
        """
        pass    # setter is ignored for discriminator property

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
        if not isinstance(other, ContactPhoto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
