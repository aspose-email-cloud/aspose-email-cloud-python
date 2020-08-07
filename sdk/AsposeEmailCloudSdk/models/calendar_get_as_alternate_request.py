#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="calendar_get_as_alternate_request.py">
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


class CalendarGetAsAlternateRequest(object):
    """
    Request model for calendar_get_as_alternate operation.
    Initializes a new instance.

    :param file_name: iCalendar file name in storage
    :type file_name: str
    :param calendar_action: iCalendar method type Enum, available values: Create, Update, Cancel
    :type calendar_action: str
    :param sequence_id: The sequence id
    :type sequence_id: str
    :param folder: Path to folder in storage
    :type folder: str
    :param storage: Storage name
    :type storage: str
    """

    def __init__(self, file_name: str, calendar_action: str, sequence_id: str = None, folder: str = None, storage: str = None):
        """
        Request model for calendar_get_as_alternate operation.
        Initializes a new instance.

        :param file_name: iCalendar file name in storage
        :type file_name: str
        :param calendar_action: iCalendar method type Enum, available values: Create, Update, Cancel
        :type calendar_action: str
        :param sequence_id: The sequence id
        :type sequence_id: str
        :param folder: Path to folder in storage
        :type folder: str
        :param storage: Storage name
        :type storage: str
        """

        self.file_name = file_name
        self.calendar_action = calendar_action
        self.sequence_id = sequence_id
        self.folder = folder
        self.storage = storage
