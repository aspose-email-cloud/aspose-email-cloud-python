#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="mapi_contact_get_request.py">
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

from AsposeEmailCloudSdk.models import *


class MapiContactGetRequest(object):
    """
    Request model for mapi_contact_get operation.
    Initializes a new instance.

    :param format: Contact document format. Enum, available values: VCard, WebDav, Msg
    :type format: str
    :param file_name: Contact document file name.
    :type file_name: str
    :param folder: Path to folder in storage.
    :type folder: str
    :param storage: Storage name.
    :type storage: str
    """

    def __init__(self, format: str, file_name: str, folder: str = None, storage: str = None):
        """
        Request model for mapi_contact_get operation.
        Initializes a new instance.

        :param format: Contact document format. Enum, available values: VCard, WebDav, Msg
        :type format: str
        :param file_name: Contact document file name.
        :type file_name: str
        :param folder: Path to folder in storage.
        :type folder: str
        :param storage: Storage name.
        :type storage: str
        """

        self.format = format
        self.file_name = file_name
        self.folder = folder
        self.storage = storage

