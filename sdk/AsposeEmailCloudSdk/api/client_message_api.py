
#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="client_message_api.py">
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

from AsposeEmailCloudSdk.api.api_base import ApiBase
from AsposeEmailCloudSdk.models import *


class ClientMessageApi(ApiBase):
    """
    Aspose.Email Cloud API. ClientMessageApi operations.

    """

    def __init__(self, api_client):
        super(ApiBase, self).__init__(api_client)
            
    def append(self, request: ClientMessageAppendRequest) -> ValueTOfString:
        """Add email message to specified folder in email account.             

        :param request ClientMessageAppendRequest Append email request.
        :return: ValueTOfString
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `append`")

        collection_formats = {}
        path = '/email/client/message/append'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'POST', 'ValueTOfString')
            
    def append_file(self, request: ClientMessageAppendFileRequest) -> ValueTOfString:
        """Add email message from file to specified folder in email account.             


        :param request ClientMessageAppendFileRequest object with parameters
        :return: ValueTOfString
        """
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `append_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `append_file`")

        collection_formats = {}
        path = '/email/client/message/file/append'

        query_params = []
        if request.account is not None:
            query_params.append((self._lowercase_first_letter('account'), request.account))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.account_storage_folder is not None:
            query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.mark_as_sent is not None:
            query_params.append((self._lowercase_first_letter('markAsSent'), request.mark_as_sent))

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'POST', 'ValueTOfString')
            
    def delete(self, request: ClientMessageDeleteRequest):
        """Delete message.             

        :param request ClientMessageDeleteRequest Delete message request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `delete`")

        collection_formats = {}
        path = '/email/client/message'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'DELETE', None)
            
    def fetch(self, request: ClientMessageFetchRequest) -> MailMessageBase:
        """Fetch message from email account             


        :param request ClientMessageFetchRequest object with parameters
        :return: MailMessageBase
        """
        # verify the required parameter 'message_id' is set
        if request.message_id is None:
            raise ValueError("Missing the required parameter `message_id` when calling `fetch`")
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `fetch`")

        collection_formats = {}
        path = '/email/client/message'

        query_params = []
        if request.message_id is not None:
            query_params.append((self._lowercase_first_letter('messageId'), request.message_id))
        if request.account is not None:
            query_params.append((self._lowercase_first_letter('account'), request.account))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.account_storage_folder is not None:
            query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        if request.type is not None:
            query_params.append((self._lowercase_first_letter('type'), request.type))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'MailMessageBase')
            
    def fetch_file(self, request: ClientMessageFetchFileRequest) -> str:
        """Fetch message as file from email account             


        :param request ClientMessageFetchFileRequest object with parameters
        :return: str
        """
        # verify the required parameter 'message_id' is set
        if request.message_id is None:
            raise ValueError("Missing the required parameter `message_id` when calling `fetch_file`")
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `fetch_file`")

        collection_formats = {}
        path = '/email/client/message/file'

        query_params = []
        if request.message_id is not None:
            query_params.append((self._lowercase_first_letter('messageId'), request.message_id))
        if request.account is not None:
            query_params.append((self._lowercase_first_letter('account'), request.account))
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.account_storage_folder is not None:
            query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'file')
            
    def list(self, request: ClientMessageListRequest) -> MailMessageBaseList:
        """Get messages from folder, filtered by query             

        The query string should have the following view.      The example of a simple expression:       '<Field name>' <Comparison operator> '<Field value>',  where &lt;Field Name&gt; - the name of a message field through which filtering is made, &lt;Comparison operator&gt; - comparison operators, as their name implies, allow to compare message field and specified value, &lt;Field value&gt; - value to be compared with a message field.      The number of simple expressions can make a compound one, ex.:     (<Simple expression 1> & <Simple expression 2>) | <Simple expression 3     >,  where \"&amp;\" - logical-AND operator, \"|\" - logical-OR operator      At present the following values are allowed as a field name (<Field name>):  \"To\" - represents a TO field of message, \"Text\" - represents string in the header or body of the message, \"Bcc\" - represents a BCC field of message, \"Body\" - represents a string in the body of message, \"Cc\" - represents a CC field of message, \"From\" - represents a From field of message, \"Subject\" - represents a string in the subject of message, \"InternalDate\" - represents an internal date of message, \"SentDate\" - represents a sent date of message      Additionally, the following field names are allowed for IMAP-protocol:  \"Answered\" - represents an /Answered flag of message \"Seen\" - represents a /Seen flag of message \"Flagged\" - represents a /Flagged flag of message \"Draft\" - represents a /Draft flag of message \"Deleted\" - represents a Deleted/ flag of message \"Recent\" - represents a Deleted/ flag of message \"MessageSize\" - represents a size (in bytes) of message      Additionally, the following field names are allowed for Exchange:  \"IsRead\" - Indicates whether the message has been read \"HasAttachment\" - Indicates whether or not the message has attachments \"IsSubmitted\" - Indicates whether the message has been submitted to the Outbox \"ContentClass\" - represents a content class of item      Additionally, the following field names are allowed for pst/ost files:  \"MessageClass\" - Represents a message class \"ContainerClass\" - Represents a folder container class \"Importance\" - Represents a message importance \"MessageSize\" - represents a size (in bytes) of message \"FolderName\" - represents a folder name \"ContentsCount\" - represents a total number of items in the folder \"UnreadContentsCount\" - represents the number of unread items in the folder. \"Subfolders\" - Indicates whether or not the folder has subfolders \"Read\" - the message is marked as having been read \"HasAttachment\" - the message has at least one attachment \"Unsent\" - the message is still being composed \"Unmodified\" - the message has not been modified since it was first saved (if unsent) or it was delivered (if sent) \"FromMe\" - the user receiving the message was also the user who sent the message \"Resend\" - the message includes a request for a resend operation with a non-delivery report \"NotifyRead\" - the user who sent the message has requested notification when a recipient first reads it \"NotifyUnread\" - the user who sent the message has requested notification when a recipient deletes it before reading or the Message object expires \"EverRead\" - the message has been read at least once      The field value (<Field value>) can take the following values:     For text fields - any string,     For date type fields - the string of \"d-MMM-yyy\" format, ex. \"10-Feb-2009\",     For flags (fields of boolean type) - either \"True\", or \"False\"              

        :param request ClientMessageListRequest object with parameters
        :return: MailMessageBaseList
        """
        # verify the required parameter 'folder' is set
        if request.folder is None:
            raise ValueError("Missing the required parameter `folder` when calling `list`")
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `list`")

        collection_formats = {}
        path = '/email/client/message/list'

        query_params = []
        if request.folder is not None:
            query_params.append((self._lowercase_first_letter('folder'), request.folder))
        if request.account is not None:
            query_params.append((self._lowercase_first_letter('account'), request.account))
        if request.query_string is not None:
            query_params.append((self._lowercase_first_letter('queryString'), request.query_string))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.account_storage_folder is not None:
            query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        if request.recursive is not None:
            query_params.append((self._lowercase_first_letter('recursive'), request.recursive))
        if request.type is not None:
            query_params.append((self._lowercase_first_letter('type'), request.type))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'MailMessageBaseList')
            
    def move(self, request: ClientMessageMoveRequest):
        """Move message to another folder.             

        :param request ClientMessageMoveRequest Move message request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `move`")

        collection_formats = {}
        path = '/email/client/message/move'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', None)
            
    def send(self, request: ClientMessageSendRequest):
        """Send an email specified by model in request.             

        :param request ClientMessageSendRequest Send email request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `send`")

        collection_formats = {}
        path = '/email/client/message'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'POST', None)
            
    def send_file(self, request: ClientMessageSendFileRequest):
        """Send an email file.             


        :param request ClientMessageSendFileRequest object with parameters
        :return: None
        """
        # verify the required parameter 'account' is set
        if request.account is None:
            raise ValueError("Missing the required parameter `account` when calling `send_file`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `send_file`")

        collection_formats = {}
        path = '/email/client/message/file'

        query_params = []
        if request.account is not None:
            query_params.append((self._lowercase_first_letter('account'), request.account))
        if request.storage is not None:
            query_params.append((self._lowercase_first_letter('storage'), request.storage))
        if request.account_storage_folder is not None:
            query_params.append((self._lowercase_first_letter('accountStorageFolder'), request.account_storage_folder))
        if request.format is not None:
            query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'POST', None)
            
    def set_is_read(self, request: ClientMessageSetIsReadRequest):
        """Mark message as read or unread.             

        :param request ClientMessageSetIsReadRequest Delete message request.
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `set_is_read`")

        collection_formats = {}
        path = '/email/client/message/set-is-read'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', None)
