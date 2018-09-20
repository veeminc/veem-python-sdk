# coding: utf-8

"""
    Veem API

    Veem REST API  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: dev@veem.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ErrorResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'error': 'str',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error',
        'message': 'message'
    }

    def __init__(self, code=None, error=None, message=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._error = None
        self._message = None
        self.discriminator = None

        self.code = code
        self.error = error
        self.message = message

    @property
    def code(self):
        """Gets the code of this ErrorResponse.  # noqa: E501

        The error code, different than HTTP status codes  # noqa: E501

        :return: The code of this ErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorResponse.

        The error code, different than HTTP status codes  # noqa: E501

        :param code: The code of this ErrorResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def error(self):
        """Gets the error of this ErrorResponse.  # noqa: E501

        The short message  # noqa: E501

        :return: The error of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ErrorResponse.

        The short message  # noqa: E501

        :param error: The error of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def message(self):
        """Gets the message of this ErrorResponse.  # noqa: E501

        The detailed, developer friendly message  # noqa: E501

        :return: The message of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorResponse.

        The detailed, developer friendly message  # noqa: E501

        :param message: The message of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
