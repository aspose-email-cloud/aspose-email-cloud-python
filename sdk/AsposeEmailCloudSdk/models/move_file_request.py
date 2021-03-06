#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="move_file_request.py">
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


class MoveFileRequest(object):
    """
    Request model for move_file operation.
    Initializes a new instance.

    :param src_path: Source file path e.g. '/src.ext'
    :type src_path: str
    :param dest_path: Destination file path e.g. '/dest.ext'
    :type dest_path: str
    :param src_storage_name: Source storage name
    :type src_storage_name: str
    :param dest_storage_name: Destination storage name
    :type dest_storage_name: str
    :param version_id: File version ID to move
    :type version_id: str
    """

    def __init__(self, src_path: str, dest_path: str, src_storage_name: str = None, dest_storage_name: str = None, version_id: str = None):
        """
        Request model for move_file operation.
        Initializes a new instance.

        :param src_path: Source file path e.g. '/src.ext'
        :type src_path: str
        :param dest_path: Destination file path e.g. '/dest.ext'
        :type dest_path: str
        :param src_storage_name: Source storage name
        :type src_storage_name: str
        :param dest_storage_name: Destination storage name
        :type dest_storage_name: str
        :param version_id: File version ID to move
        :type version_id: str
        """

        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name
        self.version_id = version_id
