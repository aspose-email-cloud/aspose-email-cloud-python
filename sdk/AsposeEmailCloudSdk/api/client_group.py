#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_group.py">
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


class ClientGroup(object):
    """
    Builtin Email client operations.
    """
    def __init__(self, api_client):
        self._account = ClientAccountApi(api_client)
        self._folder = ClientFolderApi(api_client)
        self._message = ClientMessageApi(api_client)
        self._thread = ClientThreadApi(api_client)

    @property
    def account(self) -> ClientAccountApi:
        """
        Email server account for built-in client operations.
        """
        return self._account

    @property
    def folder(self) -> ClientFolderApi:
        """
        Email client folder operations.
        """
        return self._folder

    @property
    def message(self) -> ClientMessageApi:
        """
        Email client message operations.
        """
        return self._message

    @property
    def thread(self) -> ClientThreadApi:
        """
        Email client thread operations.
        """
        return self._thread
