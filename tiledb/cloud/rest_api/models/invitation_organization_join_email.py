# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InvitationOrganizationJoinEmail(object):
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
        "actions": "list[NamespaceActions]",
        "organization_role": "OrganizationRoles",
        "invitee_email": "list[str]",
    }

    attribute_map = {
        "actions": "actions",
        "organization_role": "organization_role",
        "invitee_email": "invitee_email",
    }

    def __init__(
        self, actions=None, organization_role=None, invitee_email=None
    ):  # noqa: E501
        """InvitationOrganizationJoinEmail - a model defined in OpenAPI"""  # noqa: E501

        self._actions = None
        self._organization_role = None
        self._invitee_email = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        self.organization_role = organization_role
        self.invitee_email = invitee_email

    @property
    def actions(self):
        """Gets the actions of this InvitationOrganizationJoinEmail.  # noqa: E501

        List of permitted actions  # noqa: E501

        :return: The actions of this InvitationOrganizationJoinEmail.  # noqa: E501
        :rtype: list[NamespaceActions]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this InvitationOrganizationJoinEmail.

        List of permitted actions  # noqa: E501

        :param actions: The actions of this InvitationOrganizationJoinEmail.  # noqa: E501
        :type: list[NamespaceActions]
        """

        self._actions = actions

    @property
    def organization_role(self):
        """Gets the organization_role of this InvitationOrganizationJoinEmail.  # noqa: E501


        :return: The organization_role of this InvitationOrganizationJoinEmail.  # noqa: E501
        :rtype: OrganizationRoles
        """
        return self._organization_role

    @organization_role.setter
    def organization_role(self, organization_role):
        """Sets the organization_role of this InvitationOrganizationJoinEmail.


        :param organization_role: The organization_role of this InvitationOrganizationJoinEmail.  # noqa: E501
        :type: OrganizationRoles
        """
        if organization_role is None:
            raise ValueError(
                "Invalid value for `organization_role`, must not be `None`"
            )  # noqa: E501

        self._organization_role = organization_role

    @property
    def invitee_email(self):
        """Gets the invitee_email of this InvitationOrganizationJoinEmail.  # noqa: E501


        :return: The invitee_email of this InvitationOrganizationJoinEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._invitee_email

    @invitee_email.setter
    def invitee_email(self, invitee_email):
        """Sets the invitee_email of this InvitationOrganizationJoinEmail.


        :param invitee_email: The invitee_email of this InvitationOrganizationJoinEmail.  # noqa: E501
        :type: list[str]
        """
        if invitee_email is None:
            raise ValueError(
                "Invalid value for `invitee_email`, must not be `None`"
            )  # noqa: E501

        self._invitee_email = invitee_email

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
        if not isinstance(other, InvitationOrganizationJoinEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
