#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="delete_file_request.py">
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


class DeleteFileRequest(object):
    """
    Request model for delete_file operation.
    Initializes a new instance.

    :param path: File path e.g. '/folder/file.ext'
    :type path: str
    :param storage_name: Storage name
    :type storage_name: str
    :param version_id: File version ID to delete
    :type version_id: str
    """

    def __init__(self, path: str, storage_name: str = None, version_id: str = None):
        """
        Request model for delete_file operation.
        Initializes a new instance.

        :param path: File path e.g. '/folder/file.ext'
        :type path: str
        :param storage_name: Storage name
        :type storage_name: str
        :param version_id: File version ID to delete
        :type version_id: str
        """

        self.path = path
        self.storage_name = storage_name
        self.version_id = version_id
