#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AsposeResponse.py">
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

import pprint
import re
import six


class AsposeResponse(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status'
    }

    discriminator_value_class_map = {
        'EmailDocumentResponse': 'EmailDocumentResponse',
        'MimeResponse': 'MimeResponse',
        'ValueResponse': 'ValueResponse',
        'EmailPropertyResponse': 'EmailPropertyResponse',
        'FaultResponse': 'FaultResponse',
        'ListFoldersResponse': 'ListFoldersResponse',
        'ListMessagesResponse': 'ListMessagesResponse'
    }

    def __init__(self, code=None, status=None):
        """AsposeResponse - a model defined in Swagger"""

        self._code = None
        self._status = None
        self.discriminator = 'Type'

        if code is not None:
            self.code = code
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this AsposeResponse.


        :return: The code of this AsposeResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AsposeResponse.


        :param code: The code of this AsposeResponse.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        allowed_values = ["Continue", "SwitchingProtocols", "Processing", "EarlyHints", "OK", "Created", "Accepted", "NonAuthoritativeInformation", "NoContent", "ResetContent", "PartialContent", "MultiStatus", "AlreadyReported", "IMUsed", "MultipleChoices", "Ambiguous", "MovedPermanently", "Moved", "Found", "Redirect", "SeeOther", "RedirectMethod", "NotModified", "UseProxy", "Unused", "TemporaryRedirect", "RedirectKeepVerb", "PermanentRedirect", "BadRequest", "Unauthorized", "PaymentRequired", "Forbidden", "NotFound", "MethodNotAllowed", "NotAcceptable", "ProxyAuthenticationRequired", "RequestTimeout", "Conflict", "Gone", "LengthRequired", "PreconditionFailed", "RequestEntityTooLarge", "RequestUriTooLong", "UnsupportedMediaType", "RequestedRangeNotSatisfiable", "ExpectationFailed", "MisdirectedRequest", "UnprocessableEntity", "Locked", "FailedDependency", "UpgradeRequired", "PreconditionRequired", "TooManyRequests", "RequestHeaderFieldsTooLarge", "UnavailableForLegalReasons", "InternalServerError", "NotImplemented", "BadGateway", "ServiceUnavailable", "GatewayTimeout", "HttpVersionNotSupported", "VariantAlsoNegotiates", "InsufficientStorage", "LoopDetected", "NotExtended", "NetworkAuthenticationRequired"]
        if not code.isdigit():
            if code not in allowed_values:
                raise ValueError(
                    "Invalid value for `code` ({0}), must be one of {1}"
                    .format(code, allowed_values))
            self._code = code
        else:
            self._code = allowed_values[int(code) if six.PY3 else long(code)]

    @property
    def status(self):
        """Gets the status of this AsposeResponse.


        :return: The status of this AsposeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AsposeResponse.


        :param status: The status of this AsposeResponse.
        :type: str
        """
        self._status = status

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AsposeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
