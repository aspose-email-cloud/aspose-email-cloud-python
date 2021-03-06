#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="cloud_storage_group.py">
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

from __future__ import absolute_import
from AsposeEmailCloudSdk.api import *


class CloudStorageGroup(object):
    """
    Cloud file storage operations.
    """
    def __init__(self, api_client):
        self._file = FileApi(api_client)
        self._folder = FolderApi(api_client)
        self._storage = StorageApi(api_client)

    @property
    def file(self) -> FileApi:
        """
        File operations controller
        """
        return self._file

    @property
    def folder(self) -> FolderApi:
        """
        Folder operations controller
        """
        return self._folder

    @property
    def storage(self) -> StorageApi:
        """
        Storage operations controller
        """
        return self._storage
