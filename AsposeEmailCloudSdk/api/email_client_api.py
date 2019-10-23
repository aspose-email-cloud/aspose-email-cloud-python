#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="email_client_api.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

import six

from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.configuration import Configuration
from AsposeEmailCloudSdk.rest import ApiException


class EmailClientApi(object):
    """
    Aspose.Email Cloud API

    """

    def __init__(self, app_key=None, app_sid=None, base_url=None,
                 api_version=None, debug=False):
        """
        Initializes a new instance of the EmailClientApi class.

        :param app_key: The app key.
        :param app_sid: The app sid.
        :param base_url: The base URL.
        :param api_version: API version.
        :param debug: If debug mode is enabled. False by default.
        :param on_premise:
            True for on-premise solution with metered license usage.
            False for Aspose Cloud-hosted solution usage, default.
        """
        configuration = Configuration(app_key=app_key,
                                      app_sid=app_sid,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug)
        self.api_client = ApiClient(configuration)

    def append_email_message(self, request):
        """Adds an email from *.eml file to specified folder in email account


        :param request append_email_message_request object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'EmailPropertyResponse')

    def append_email_message_async(self, request):
        """Adds an email from *.eml file to specified folder in email account


        :param request append_email_message_request object with parameters
        :return: EmailPropertyResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'EmailPropertyResponse')

    def append_mime_message(self, request):
        """Adds an email from MIME to specified folder in email account


        :param request append_mime_message_request object with parameters
        :return: ValueResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'ValueResponse')

    def append_mime_message_async(self, request):
        """Adds an email from MIME to specified folder in email account


        :param request append_mime_message_request object with parameters
        :return: ValueResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'ValueResponse')

    def create_email_folder(self, request):
        """Create new folder in email account


        :param request create_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_email_folder_async(self, request):
        """Create new folder in email account


        :param request create_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def delete_email_folder(self, request):
        """Delete a folder in email account


        :param request delete_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_folder_async(self, request):
        """Delete a folder in email account


        :param request delete_email_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_email_message(self, request):
        """Delete message from email account by id


        :param request delete_email_message_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_email_message_async(self, request):
        """Delete message from email account by id


        :param request delete_email_message_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def fetch_email_message(self, request):
        """Fetch message mime from email account


        :param request fetch_email_message_request object with parameters
        :return: MimeResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'MimeResponse')

    def fetch_email_message_async(self, request):
        """Fetch message mime from email account


        :param request fetch_email_message_request object with parameters
        :return: MimeResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'MimeResponse')

    def list_email_folders(self, request):
        """Get folders list in email account


        :param request list_email_folders_request object with parameters
        :return: ListFoldersResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListFoldersResponse')

    def list_email_folders_async(self, request):
        """Get folders list in email account


        :param request list_email_folders_request object with parameters
        :return: ListFoldersResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListFoldersResponse')

    def list_email_messages(self, request):
        """Get messages from folder, filtered by query

        The query string should have the following view.  The example of a simple expression:   '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.  The number of simple expressions can make a compound one, ex.: (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator  At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message  Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message  Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item  Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once  The field value (<Field value>) can take the following values: For text fields - any string, For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\", For flags (fields of boolean type) - either \"True\", or \"False\"

        :param request list_email_messages_request object with parameters
        :return: ListMessagesResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ListMessagesResponse')

    def list_email_messages_async(self, request):
        """Get messages from folder, filtered by query

        The query string should have the following view.  The example of a simple expression:   '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.  The number of simple expressions can make a compound one, ex.: (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3>,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator  At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message  Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message  Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item  Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once  The field value (<Field value>) can take the following values: For text fields - any string, For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\", For flags (fields of boolean type) - either \"True\", or \"False\"

        :param request list_email_messages_request object with parameters
        :return: ListMessagesResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ListMessagesResponse')

    def save_mail_account(self, request):
        """Create email account file (*.account) with login/password authentication


        :param request save_mail_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_account_async(self, request):
        """Create email account file (*.account) with login/password authentication


        :param request save_mail_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def save_mail_o_auth_account(self, request):
        """Create email account file (*.account) with OAuth


        :param request save_mail_o_auth_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def save_mail_o_auth_account_async(self, request):
        """Create email account file (*.account) with OAuth


        :param request save_mail_o_auth_account_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email(self, request):
        """Send an email from *.eml file located on storage


        :param request send_email_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_async(self, request):
        """Send an email from *.eml file located on storage


        :param request send_email_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def send_email_mime(self, request):
        """Send an email specified by MIME in request


        :param request send_email_mime_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def send_email_mime_async(self, request):
        """Send an email specified by MIME in request


        :param request send_email_mime_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def set_email_read_flag(self, request):
        """Sets \&quot;Message is read\&quot; flag


        :param request set_email_read_flag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def set_email_read_flag_async(self, request):
        """Sets \&quot;Message is read\&quot; flag


        :param request set_email_read_flag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def __make_request(self, http_request, method, return_type):
        def call_api():
            return self.api_client.call_api(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api()
            raise

    def __make_request_async(self, http_request, method, return_type):
        def call_api_async():
            self.api_client.call_api_async(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api_async()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

