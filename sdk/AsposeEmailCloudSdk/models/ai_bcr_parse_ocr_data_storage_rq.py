#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiBcrParseOcrDataStorageRq.py">
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

from AsposeEmailCloudSdk.models.ai_bcr_ocr_data import AiBcrOcrData
from AsposeEmailCloudSdk.models.ai_bcr_options import AiBcrOptions
from AsposeEmailCloudSdk.models.ai_bcr_parse_ocr_data_rq import AiBcrParseOcrDataRq
from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class AiBcrParseOcrDataStorageRq(AiBcrParseOcrDataRq):
    """Parse ocr data request with storage output location             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'options': 'AiBcrOptions',
        'data': 'list[AiBcrOcrData]',
        'out_folder': 'StorageFolderLocation'
    }

    attribute_map = {
        'options': 'options',
        'data': 'data',
        'out_folder': 'outFolder'
    }

    def __init__(self, options=None, data=None, out_folder=None):
        """AiBcrParseOcrDataStorageRq - a model defined in Swagger"""
        super(AiBcrParseOcrDataStorageRq, self).__init__()

        self._out_folder = None
        self.discriminator = None

        if options is not None:
            self.options = options
        if data is not None:
            self.data = data
        if out_folder is not None:
            self.out_folder = out_folder

    @property
    def out_folder(self):
        """Gets the out_folder of this AiBcrParseOcrDataStorageRq.

        Output folder location on storage             

        :return: The out_folder of this AiBcrParseOcrDataStorageRq.
        :rtype: StorageFolderLocation
        """
        return self._out_folder

    @out_folder.setter
    def out_folder(self, out_folder):
        """Sets the out_folder of this AiBcrParseOcrDataStorageRq.

        Output folder location on storage             

        :param out_folder: The out_folder of this AiBcrParseOcrDataStorageRq.
        :type: StorageFolderLocation
        """
        if out_folder is None:
            raise ValueError("Invalid value for `out_folder`, must not be `None`")
        self._out_folder = out_folder

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
        if not isinstance(other, AiBcrParseOcrDataStorageRq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
