#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiBcrParseStorageRequest.py">
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

from AsposeEmailCloudSdk.models.ai_bcr_image_storage_file import AiBcrImageStorageFile
from AsposeEmailCloudSdk.models.ai_bcr_options import AiBcrOptions
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class AiBcrParseStorageRequest(object):
    """Parse business card images from Storage request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'out_folder': 'StorageFolderLocation',
        'images': 'list[AiBcrImageStorageFile]',
        'options': 'AiBcrOptions'
    }

    attribute_map = {
        'out_folder': 'outFolder',
        'images': 'images',
        'options': 'options'
    }

    def __init__(self, out_folder: StorageFolderLocation = None, images: List[AiBcrImageStorageFile] = None, options: AiBcrOptions = None):
        """
        Parse business card images from Storage request             
        :param out_folder: Parse output folder location on storage             
        :type out_folder: StorageFolderLocation
        :param images: Images to parse.             
        :type images: List[AiBcrImageStorageFile]
        :param options: Recognition options.             
        :type options: AiBcrOptions
        """

        self._out_folder = None
        self._images = None
        self._options = None

        if out_folder is not None:
            self.out_folder = out_folder
        if images is not None:
            self.images = images
        if options is not None:
            self.options = options


    @property
    def out_folder(self) -> StorageFolderLocation:
        """
        Parse output folder location on storage             

        :return: The out_folder of this AiBcrParseStorageRequest.
        :rtype: StorageFolderLocation
        """
        return self._out_folder

    @out_folder.setter
    def out_folder(self, out_folder: StorageFolderLocation):
        """
        Parse output folder location on storage             

        :param out_folder: The out_folder of this AiBcrParseStorageRequest.
        :type: StorageFolderLocation
        """
        if out_folder is None:
            raise ValueError("Invalid value for `out_folder`, must not be `None`")
        self._out_folder = out_folder

    @property
    def images(self) -> List[AiBcrImageStorageFile]:
        """
        Images to parse.             

        :return: The images of this AiBcrParseStorageRequest.
        :rtype: list[AiBcrImageStorageFile]
        """
        return self._images

    @images.setter
    def images(self, images: List[AiBcrImageStorageFile]):
        """
        Images to parse.             

        :param images: The images of this AiBcrParseStorageRequest.
        :type: list[AiBcrImageStorageFile]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")
        self._images = images

    @property
    def options(self) -> AiBcrOptions:
        """
        Recognition options.             

        :return: The options of this AiBcrParseStorageRequest.
        :rtype: AiBcrOptions
        """
        return self._options

    @options.setter
    def options(self, options: AiBcrOptions):
        """
        Recognition options.             

        :param options: The options of this AiBcrParseStorageRequest.
        :type: AiBcrOptions
        """
        self._options = options

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
        if not isinstance(other, AiBcrParseStorageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
