# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud.rest_api.configuration import Configuration


class Token(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "token": "str",
        "name": "str",
        "issued_at": "datetime",
        "expires_at": "datetime",
        "scope": "str",
    }

    attribute_map = {
        "token": "token",
        "name": "name",
        "issued_at": "issued_at",
        "expires_at": "expires_at",
        "scope": "scope",
    }

    def __init__(
        self,
        token=None,
        name=None,
        issued_at=None,
        expires_at=None,
        scope="*",
        local_vars_configuration=None,
    ):  # noqa: E501
        """Token - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._name = None
        self._issued_at = None
        self._expires_at = None
        self._scope = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if name is not None:
            self.name = name
        if issued_at is not None:
            self.issued_at = issued_at
        if expires_at is not None:
            self.expires_at = expires_at
        if scope is not None:
            self.scope = scope

    @property
    def token(self):
        """Gets the token of this Token.  # noqa: E501

        A api token  # noqa: E501

        :return: The token of this Token.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Token.

        A api token  # noqa: E501

        :param token: The token of this Token.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def name(self):
        """Gets the name of this Token.  # noqa: E501

        Name of token to revoke  # noqa: E501

        :return: The name of this Token.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Token.

        Name of token to revoke  # noqa: E501

        :param name: The name of this Token.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def issued_at(self):
        """Gets the issued_at of this Token.  # noqa: E501

        datetime the token was created  # noqa: E501

        :return: The issued_at of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this Token.

        datetime the token was created  # noqa: E501

        :param issued_at: The issued_at of this Token.  # noqa: E501
        :type: datetime
        """

        self._issued_at = issued_at

    @property
    def expires_at(self):
        """Gets the expires_at of this Token.  # noqa: E501

        datetime the token when token will expire  # noqa: E501

        :return: The expires_at of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Token.

        datetime the token when token will expire  # noqa: E501

        :param expires_at: The expires_at of this Token.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def scope(self):
        """Gets the scope of this Token.  # noqa: E501

        Optional scope to limit token, defaults to all permissions, current supported values are password_reset or *  # noqa: E501

        :return: The scope of this Token.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Token.

        Optional scope to limit token, defaults to all permissions, current supported values are password_reset or *  # noqa: E501

        :param scope: The scope of this Token.  # noqa: E501
        :type: str
        """

        self._scope = scope

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, Token):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Token):
            return True

        return self.to_dict() != other.to_dict()
