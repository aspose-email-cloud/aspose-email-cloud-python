#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_name_parse_request.py">
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


class AiNameParseRequest(object):
    """
    Request model for ai_name_parse operation.
    Initializes a new instance.

    :param name: A name to parse.
    :type name: str
    :param language: An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian).             
    :type language: str
    :param location: A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France.             
    :type location: str
    :param encoding: A character encoding name.
    :type encoding: str
    :param script: A writing system code; starts with the ISO-15924 script name.
    :type script: str
    :param style: Name writing style. Enum, available values: Formal, Informal, Legal, Academic
    :type style: str
    """

    def __init__(self, name: str, language: str = None, location: str = None, encoding: str = None, script: str = None, style: str = None):
        """
        Request model for ai_name_parse operation.
        Initializes a new instance.

        :param name: A name to parse.
        :type name: str
        :param language: An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \"it\" or \"ita\" for Italian).             
        :type language: str
        :param location: A geographic code such as an ISO-3166 two letter country code, for example \"FR\" for France.             
        :type location: str
        :param encoding: A character encoding name.
        :type encoding: str
        :param script: A writing system code; starts with the ISO-15924 script name.
        :type script: str
        :param style: Name writing style. Enum, available values: Formal, Informal, Legal, Academic
        :type style: str
        """

        self.name = name
        self.language = language
        self.location = location
        self.encoding = encoding
        self.script = script
        self.style = style
