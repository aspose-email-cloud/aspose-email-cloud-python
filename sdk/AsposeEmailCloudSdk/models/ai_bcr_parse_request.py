#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_bcr_parse_request.py">
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


class AiBcrParseRequest(object):
    """
    Request model for ai_bcr_parse operation.
    Initializes a new instance.

    :param file: File to parse
    :type file: str
    :param countries: Comma-separated codes of countries.
    :type countries: str
    :param languages: Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \"it\" or \"ita\" for Italian); it's \"\" by default.             
    :type languages: str
    :param is_single: Determines that image contains single VCard or more.
    :type is_single: bool
    """

    def __init__(self, file: str, countries: str = None, languages: str = None, is_single: bool = None):
        """
        Request model for ai_bcr_parse operation.
        Initializes a new instance.

        :param file: File to parse
        :type file: str
        :param countries: Comma-separated codes of countries.
        :type countries: str
        :param languages: Comma-separated ISO-639 codes of languages (either 639-1 or 639-3; i.e. \"it\" or \"ita\" for Italian); it's \"\" by default.             
        :type languages: str
        :param is_single: Determines that image contains single VCard or more.
        :type is_single: bool
        """

        self.file = file
        self.countries = countries
        self.languages = languages
        self.is_single = is_single

