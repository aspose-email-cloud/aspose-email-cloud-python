
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="copy_folder_request.py">
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


class CopyFolderRequest(object):
    """
    Request model for copy_folder operation.
    Initializes a new instance.

    :param src_path (str) Source folder path e.g. '/src'
    :param dest_path (str) Destination folder path e.g. '/dst'
    :param src_storage_name (str) Source storage name
    :param dest_storage_name (str) Destination storage name
    """

    def __init__(self, src_path: str, dest_path: str, src_storage_name: str = None, dest_storage_name: str = None):
        """
        Request model for copy_folder operation.
        Initializes a new instance.

        :param src_path (str) Source folder path e.g. '/src'
        :param dest_path (str) Destination folder path e.g. '/dst'
        :param src_storage_name (str) Source storage name
        :param dest_storage_name (str) Destination storage name
        """

        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name
