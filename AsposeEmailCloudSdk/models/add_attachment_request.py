#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AddAttachmentRequest.py">
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

from AsposeEmailCloudSdk.models.storage_folder_location import StorageFolderLocation


class AddAttachmentRequest(object):
    """Add attachment request
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_folder': 'StorageFolderLocation',
        'attachment_folder': 'StorageFolderLocation'
    }

    attribute_map = {
        'document_folder': 'DocumentFolder',
        'attachment_folder': 'AttachmentFolder'
    }

    def __init__(self, document_folder=None, attachment_folder=None):
        """AddAttachmentRequest - a model defined in Swagger"""

        self._document_folder = None
        self._attachment_folder = None
        self.discriminator = None

        if document_folder is not None:
            self.document_folder = document_folder
        if attachment_folder is not None:
            self.attachment_folder = attachment_folder

    @property
    def document_folder(self):
        """Gets the document_folder of this AddAttachmentRequest.

        Storage folder location of document

        :return: The document_folder of this AddAttachmentRequest.
        :rtype: StorageFolderLocation
        """
        return self._document_folder

    @document_folder.setter
    def document_folder(self, document_folder):
        """Sets the document_folder of this AddAttachmentRequest.

        Storage folder location of document

        :param document_folder: The document_folder of this AddAttachmentRequest.
        :type: StorageFolderLocation
        """
        self._document_folder = document_folder

    @property
    def attachment_folder(self):
        """Gets the attachment_folder of this AddAttachmentRequest.

        Storage folder location of an attachment

        :return: The attachment_folder of this AddAttachmentRequest.
        :rtype: StorageFolderLocation
        """
        return self._attachment_folder

    @attachment_folder.setter
    def attachment_folder(self, attachment_folder):
        """Sets the attachment_folder of this AddAttachmentRequest.

        Storage folder location of an attachment

        :param attachment_folder: The attachment_folder of this AddAttachmentRequest.
        :type: StorageFolderLocation
        """
        self._attachment_folder = attachment_folder

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
        if not isinstance(other, AddAttachmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
