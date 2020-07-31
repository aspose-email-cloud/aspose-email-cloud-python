
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="contact_convert_request.py">
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


class ContactConvertRequest(object):
    """
    Request model for contact_convert operation.
    Initializes a new instance.

    :param to_format (str) File format to convert to Enum, available values: VCard, WebDav, Msg
    :param from_format (str) File format to convert from Enum, available values: VCard, WebDav, Msg
    :param file (str) File to convert
    """

    def __init__(self, to_format: str, from_format: str, file: str):
        """
        Request model for contact_convert operation.
        Initializes a new instance.

        :param to_format (str) File format to convert to Enum, available values: VCard, WebDav, Msg
        :param from_format (str) File format to convert from Enum, available values: VCard, WebDav, Msg
        :param file (str) File to convert
        """

        self.to_format = to_format
        self.from_format = from_format
        self.file = file