import six

from AsposeEmailCloudSdk.api_client import ApiClient
from AsposeEmailCloudSdk.rest import ApiException


class ApiBase(object):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @staticmethod
    def _select_header_accept(accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'

        return ', '.join(accepts)

    @staticmethod
    def _select_header_content_type(content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'

        return content_types[0]

    @staticmethod
    def _lowercase_first_letter(string):
        """
        Converts first letter of the string to lowercase

        :param string: initial string
        :return: initial string with first character in lowercase
        """
        if not string:
            return string

        return string[0].lower() + string[1:]

    def _make_request(self, http_request, method, return_type):
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
                self._request_token()
                return call_api()
            raise

    def _request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['client_id']),
                       ('client_secret', config.api_key['client_secret'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True,
                                        host=config.get_auth_url())
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version
