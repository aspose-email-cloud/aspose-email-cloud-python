#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="email_cloud.py">
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

from AsposeEmailCloudSdk import Configuration, ApiClient
from AsposeEmailCloudSdk.api import *


class EmailCloud(object):
    """
    Aspose.Email Cloud API.
    """

    def __init__(self, client_secret=None, client_id=None, base_url=None,
                 api_version=None, debug=False):
        """
        Initializes a new instance of the EmailCloud class.

        :param client_secret: The client secret.
        :type client_secret: str
        :param client_id: The client id.
        :type client_id: str
        :param base_url: The base URL.
        :type base_url: str
        :param api_version: API version.
        :type api_version: str
        :param debug: If debug mode is enabled. False by default.
        :type debug: bool
        """
        configuration = Configuration(client_secret=client_secret,
                                      client_id=client_id,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug)
        api_client = ApiClient(configuration)



    
        self._calendar = CalendarApi(api_client)
    
        self._contact = ContactApi(api_client)
    
        self._email = EmailApi(api_client)
    
        self._disposable_email = DisposableEmailApi(api_client)
    
        self._email_config = EmailConfigApi(api_client)
    
    
        self._mapi = MapiGroup(api_client)
    
        self._client = ClientGroup(api_client)
    
        self._ai = AiGroup(api_client)
    
        self._cloud_storage = CloudStorageGroup(api_client)
    

    
    @property
    def calendar(self) -> CalendarApi:
        """
        iCalendar document operations.
        """
        return self._calendar
    
    @property
    def contact(self) -> ContactApi:
        """
        Contact document operations. Supported formats: VCard, MSG, WebDav
        """
        return self._contact
    
    @property
    def email(self) -> EmailApi:
        """
        Email document (*.eml) operations.
        """
        return self._email
    
    @property
    def disposable_email(self) -> DisposableEmailApi:
        """
        Checks if an email is a disposable one
        """
        return self._disposable_email
    
    @property
    def email_config(self) -> EmailConfigApi:
        """
        Email server configuration discovery.
        """
        return self._email_config
    

    
    @property
    def mapi(self) -> MapiGroup:
        """
        MAPI operations.
        """
        return self._mapi
    
    @property
    def client(self) -> ClientGroup:
        """
        Builtin Email client operations.
        """
        return self._client
    
    @property
    def ai(self) -> AiGroup:
        """
        AI powered operations.
        """
        return self._ai
    
    @property
    def cloud_storage(self) -> CloudStorageGroup:
        """
        Cloud file storage operations.
        """
        return self._cloud_storage
    
