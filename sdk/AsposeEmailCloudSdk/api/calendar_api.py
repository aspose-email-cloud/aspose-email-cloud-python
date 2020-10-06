#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="calendar_api.py">
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


class CalendarApi(ApiBase):
    """
    Aspose.Email Cloud API. CalendarApi operations.

    """

    def __init__(self, api_client):
        super(CalendarApi, self).__init__(api_client)

    def as_alternate(self, request: CalendarAsAlternateRequest) -> AlternateView:
        """Convert iCalendar to AlternateView             

        :param request: iCalendar to AlternateView request
        :type request: CalendarAsAlternateRequest
        :return: AlternateView
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `as_alternate`")

        collection_formats = {}
        path = '/email/Calendar/as-alternate'

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

        return self._make_request(http_request_object, 'PUT', 'AlternateView')

    def as_file(self, request: CalendarAsFileRequest) -> str:
        """Converts calendar model to specified format and returns as file.             

        :param request: Calendar model and format to convert.
        :type request: CalendarAsFileRequest
        :return: str
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `as_file`")

        collection_formats = {}
        path = '/email/Calendar/as-file'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = request
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'file')

    def as_mapi(self, calendar_dto: CalendarDto) -> MapiCalendarDto:
        """Converts CalendarDto to MapiCalendarDto.             

        :param calendar_dto: iCalendar model calendar representation.
        :type calendar_dto: CalendarDto
        :return: MapiCalendarDto
        """
        # verify the required parameter 'calendar_dto' is set
        if calendar_dto is None:
            raise ValueError("Missing the required parameter `calendar_dto` when calling `as_mapi`")

        collection_formats = {}
        path = '/email/Calendar/as-mapi'

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])
        body_params = calendar_dto
        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, None, None, header_params, None, body_params, None, None, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'MapiCalendarDto')

    def convert(self, request: CalendarConvertRequest) -> str:
        """Converts calendar document to specified format and returns as file.             


        :param request: CalendarConvertRequest object with parameters
        :type request: CalendarConvertRequest
        :return: str
        """
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `convert`")
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `convert`")

        collection_formats = {}
        path = '/email/Calendar/convert'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('format') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self._lowercase_first_letter('format'), request.format))

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), request.file))

        header_params = {}
        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'file')

    def from_file(self, request: CalendarFromFileRequest) -> CalendarDto:
        """Converts calendar document to a model representation.             


        :param request: CalendarFromFileRequest object with parameters
        :type request: CalendarFromFileRequest
        :return: CalendarDto
        """
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `from_file`")

        collection_formats = {}
        path = '/email/Calendar/from-file'
        path_params = {}

        query_params = []

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'PUT', 'CalendarDto')

    def get(self, request: CalendarGetRequest) -> CalendarDto:
        """Get calendar file from storage.             


        :param request: CalendarGetRequest object with parameters
        :type request: CalendarGetRequest
        :return: CalendarDto
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get`")

        collection_formats = {}
        path = '/email/Calendar'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('fileName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'CalendarDto')

    def get_as_alternate(self, request: CalendarGetAsAlternateRequest) -> AlternateView:
        """Get iCalendar from storage as AlternateView             


        :param request: CalendarGetAsAlternateRequest object with parameters
        :type request: CalendarGetAsAlternateRequest
        :return: AlternateView
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get_as_alternate`")
        # verify the required parameter 'calendar_action' is set
        if request.calendar_action is None:
            raise ValueError("Missing the required parameter `calendar_action` when calling `get_as_alternate`")

        collection_formats = {}
        path = '/email/Calendar/as-alternate'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('fileName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        path_parameter = '{' + self._lowercase_first_letter('calendarAction') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.calendar_action if request.calendar_action is not None else '')
        else:
            if request.calendar_action is not None:
                query_params.append((self._lowercase_first_letter('calendarAction'), request.calendar_action))
        path_parameter = '{' + self._lowercase_first_letter('sequenceId') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.sequence_id if request.sequence_id is not None else '')
        else:
            if request.sequence_id is not None:
                query_params.append((self._lowercase_first_letter('sequenceId'), request.sequence_id))
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'AlternateView')

    def get_as_file(self, request: CalendarGetAsFileRequest) -> str:
        """Converts calendar document from storage to specified format and returns as file.             


        :param request: CalendarGetAsFileRequest object with parameters
        :type request: CalendarGetAsFileRequest
        :return: str
        """
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `get_as_file`")
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_as_file`")

        collection_formats = {}
        path = '/email/Calendar/as-file'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('fileName') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self._lowercase_first_letter('fileName'), request.file_name))
        path_parameter = '{' + self._lowercase_first_letter('format') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self._lowercase_first_letter('format'), request.format))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'file')

    def get_list(self, request: CalendarGetListRequest) -> CalendarStorageList:
        """Get iCalendar list from storage folder.             


        :param request: CalendarGetListRequest object with parameters
        :type request: CalendarGetListRequest
        :return: CalendarStorageList
        """
        # verify the required parameter 'folder' is set
        if request.folder is None:
            raise ValueError("Missing the required parameter `folder` when calling `get_list`")

        collection_formats = {}
        path = '/email/Calendar/list'
        path_params = {}

        query_params = []
        path_parameter = '{' + self._lowercase_first_letter('folder') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), request.folder))
        path_parameter = '{' + self._lowercase_first_letter('itemsPerPage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.items_per_page if request.items_per_page is not None else '')
        else:
            if request.items_per_page is not None:
                query_params.append((self._lowercase_first_letter('itemsPerPage'), request.items_per_page))
        path_parameter = '{' + self._lowercase_first_letter('pageNumber') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.page_number if request.page_number is not None else '')
        else:
            if request.page_number is not None:
                query_params.append((self._lowercase_first_letter('pageNumber'), request.page_number))
        path_parameter = '{' + self._lowercase_first_letter('storage') + '}'
        if path_parameter in path:
            path = path.replace(path_parameter, request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), request.storage))

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

        http_request_object = HttpRequest(path, path_params, query_params, header_params, form_params, None, local_var_files,
                                          collection_formats, auth_settings)

        return self._make_request(http_request_object, 'GET', 'CalendarStorageList')

    def save(self, request: CalendarSaveRequest):
        """Save iCalendar             

        :param request: iCalendar create/update request
        :type request: CalendarSaveRequest
        :return: None
        """
        # verify the required parameter 'request' is set
        if request is None:
            raise ValueError("Missing the required parameter `request` when calling `save`")

        collection_formats = {}
        path = '/email/Calendar'

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

