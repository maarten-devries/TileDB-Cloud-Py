# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.2.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OrganizationUser(object):
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
        'user_id': 'str',
        'organization_id': 'str',
        'username': 'str',
        'organization_name': 'str',
        'role': 'OrganizationRoles',
        'allowed_actions': 'list[NamespaceActions]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'organization_id': 'organization_id',
        'username': 'username',
        'organization_name': 'organization_name',
        'role': 'role',
        'allowed_actions': 'allowed_actions'
    }

    def __init__(self, user_id=None, organization_id=None, username=None, organization_name=None, role=None, allowed_actions=None):  # noqa: E501
        """OrganizationUser - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._organization_id = None
        self._username = None
        self._organization_name = None
        self._role = None
        self._allowed_actions = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if organization_id is not None:
            self.organization_id = organization_id
        if username is not None:
            self.username = username
        if organization_name is not None:
            self.organization_name = organization_name
        if role is not None:
            self.role = role
        if allowed_actions is not None:
            self.allowed_actions = allowed_actions

    @property
    def user_id(self):
        """Gets the user_id of this OrganizationUser.  # noqa: E501

        unique id of user  # noqa: E501

        :return: The user_id of this OrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrganizationUser.

        unique id of user  # noqa: E501

        :param user_id: The user_id of this OrganizationUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def organization_id(self):
        """Gets the organization_id of this OrganizationUser.  # noqa: E501

        unique id of organization  # noqa: E501

        :return: The organization_id of this OrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this OrganizationUser.

        unique id of organization  # noqa: E501

        :param organization_id: The organization_id of this OrganizationUser.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def username(self):
        """Gets the username of this OrganizationUser.  # noqa: E501

        username for user  # noqa: E501

        :return: The username of this OrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this OrganizationUser.

        username for user  # noqa: E501

        :param username: The username of this OrganizationUser.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def organization_name(self):
        """Gets the organization_name of this OrganizationUser.  # noqa: E501

        name of organization  # noqa: E501

        :return: The organization_name of this OrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this OrganizationUser.

        name of organization  # noqa: E501

        :param organization_name: The organization_name of this OrganizationUser.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def role(self):
        """Gets the role of this OrganizationUser.  # noqa: E501


        :return: The role of this OrganizationUser.  # noqa: E501
        :rtype: OrganizationRoles
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OrganizationUser.


        :param role: The role of this OrganizationUser.  # noqa: E501
        :type: OrganizationRoles
        """

        self._role = role

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this OrganizationUser.  # noqa: E501

        list of actions user is allowed to do on this organization  # noqa: E501

        :return: The allowed_actions of this OrganizationUser.  # noqa: E501
        :rtype: list[NamespaceActions]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this OrganizationUser.

        list of actions user is allowed to do on this organization  # noqa: E501

        :param allowed_actions: The allowed_actions of this OrganizationUser.  # noqa: E501
        :type: list[NamespaceActions]
        """

        self._allowed_actions = allowed_actions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, OrganizationUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
