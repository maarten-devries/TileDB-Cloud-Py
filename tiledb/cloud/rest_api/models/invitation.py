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


class Invitation(object):
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
        "id": "str",
        "invitation_type": "InvitationType",
        "owner_namespace_uuid": "str",
        "user_namespace_uuid": "str",
        "organization_user_uuid": "str",
        "organization_name": "str",
        "organization_role": "OrganizationRoles",
        "array_uuid": "str",
        "array_name": "str",
        "email": "str",
        "actions": "str",
        "status": "InvitationStatus",
        "created_at": "datetime",
        "expires_at": "datetime",
        "accepted_at": "datetime",
    }

    attribute_map = {
        "id": "id",
        "invitation_type": "invitation_type",
        "owner_namespace_uuid": "owner_namespace_uuid",
        "user_namespace_uuid": "user_namespace_uuid",
        "organization_user_uuid": "organization_user_uuid",
        "organization_name": "organization_name",
        "organization_role": "organization_role",
        "array_uuid": "array_uuid",
        "array_name": "array_name",
        "email": "email",
        "actions": "actions",
        "status": "status",
        "created_at": "created_at",
        "expires_at": "expires_at",
        "accepted_at": "accepted_at",
    }

    def __init__(
        self,
        id=None,
        invitation_type=None,
        owner_namespace_uuid=None,
        user_namespace_uuid=None,
        organization_user_uuid=None,
        organization_name=None,
        organization_role=None,
        array_uuid=None,
        array_name=None,
        email=None,
        actions=None,
        status=None,
        created_at=None,
        expires_at=None,
        accepted_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._invitation_type = None
        self._owner_namespace_uuid = None
        self._user_namespace_uuid = None
        self._organization_user_uuid = None
        self._organization_name = None
        self._organization_role = None
        self._array_uuid = None
        self._array_name = None
        self._email = None
        self._actions = None
        self._status = None
        self._created_at = None
        self._expires_at = None
        self._accepted_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if invitation_type is not None:
            self.invitation_type = invitation_type
        if owner_namespace_uuid is not None:
            self.owner_namespace_uuid = owner_namespace_uuid
        if user_namespace_uuid is not None:
            self.user_namespace_uuid = user_namespace_uuid
        if organization_user_uuid is not None:
            self.organization_user_uuid = organization_user_uuid
        if organization_name is not None:
            self.organization_name = organization_name
        if organization_role is not None:
            self.organization_role = organization_role
        if array_uuid is not None:
            self.array_uuid = array_uuid
        if array_name is not None:
            self.array_name = array_name
        if email is not None:
            self.email = email
        if actions is not None:
            self.actions = actions
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if expires_at is not None:
            self.expires_at = expires_at
        if accepted_at is not None:
            self.accepted_at = accepted_at

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501

        Unique ID of invitation added to magic link  # noqa: E501

        :return: The id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.

        Unique ID of invitation added to magic link  # noqa: E501

        :param id: The id of this Invitation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invitation_type(self):
        """Gets the invitation_type of this Invitation.  # noqa: E501


        :return: The invitation_type of this Invitation.  # noqa: E501
        :rtype: InvitationType
        """
        return self._invitation_type

    @invitation_type.setter
    def invitation_type(self, invitation_type):
        """Sets the invitation_type of this Invitation.


        :param invitation_type: The invitation_type of this Invitation.  # noqa: E501
        :type: InvitationType
        """

        self._invitation_type = invitation_type

    @property
    def owner_namespace_uuid(self):
        """Gets the owner_namespace_uuid of this Invitation.  # noqa: E501

        Namespace of the owner of the invitation (user or organization)  # noqa: E501

        :return: The owner_namespace_uuid of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._owner_namespace_uuid

    @owner_namespace_uuid.setter
    def owner_namespace_uuid(self, owner_namespace_uuid):
        """Sets the owner_namespace_uuid of this Invitation.

        Namespace of the owner of the invitation (user or organization)  # noqa: E501

        :param owner_namespace_uuid: The owner_namespace_uuid of this Invitation.  # noqa: E501
        :type: str
        """

        self._owner_namespace_uuid = owner_namespace_uuid

    @property
    def user_namespace_uuid(self):
        """Gets the user_namespace_uuid of this Invitation.  # noqa: E501

        Unique ID of the user accepted the invitation  # noqa: E501

        :return: The user_namespace_uuid of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._user_namespace_uuid

    @user_namespace_uuid.setter
    def user_namespace_uuid(self, user_namespace_uuid):
        """Sets the user_namespace_uuid of this Invitation.

        Unique ID of the user accepted the invitation  # noqa: E501

        :param user_namespace_uuid: The user_namespace_uuid of this Invitation.  # noqa: E501
        :type: str
        """

        self._user_namespace_uuid = user_namespace_uuid

    @property
    def organization_user_uuid(self):
        """Gets the organization_user_uuid of this Invitation.  # noqa: E501

        Unique ID of the organization user accepted the invitation  # noqa: E501

        :return: The organization_user_uuid of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._organization_user_uuid

    @organization_user_uuid.setter
    def organization_user_uuid(self, organization_user_uuid):
        """Sets the organization_user_uuid of this Invitation.

        Unique ID of the organization user accepted the invitation  # noqa: E501

        :param organization_user_uuid: The organization_user_uuid of this Invitation.  # noqa: E501
        :type: str
        """

        self._organization_user_uuid = organization_user_uuid

    @property
    def organization_name(self):
        """Gets the organization_name of this Invitation.  # noqa: E501

        Name of the organization, does not persist in database  # noqa: E501

        :return: The organization_name of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this Invitation.

        Name of the organization, does not persist in database  # noqa: E501

        :param organization_name: The organization_name of this Invitation.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def organization_role(self):
        """Gets the organization_role of this Invitation.  # noqa: E501


        :return: The organization_role of this Invitation.  # noqa: E501
        :rtype: OrganizationRoles
        """
        return self._organization_role

    @organization_role.setter
    def organization_role(self, organization_role):
        """Sets the organization_role of this Invitation.


        :param organization_role: The organization_role of this Invitation.  # noqa: E501
        :type: OrganizationRoles
        """

        self._organization_role = organization_role

    @property
    def array_uuid(self):
        """Gets the array_uuid of this Invitation.  # noqa: E501

        Unique ID of the array  # noqa: E501

        :return: The array_uuid of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._array_uuid

    @array_uuid.setter
    def array_uuid(self, array_uuid):
        """Sets the array_uuid of this Invitation.

        Unique ID of the array  # noqa: E501

        :param array_uuid: The array_uuid of this Invitation.  # noqa: E501
        :type: str
        """

        self._array_uuid = array_uuid

    @property
    def array_name(self):
        """Gets the array_name of this Invitation.  # noqa: E501

        Name of the array, does not persist in database  # noqa: E501

        :return: The array_name of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._array_name

    @array_name.setter
    def array_name(self, array_name):
        """Sets the array_name of this Invitation.

        Name of the array, does not persist in database  # noqa: E501

        :param array_name: The array_name of this Invitation.  # noqa: E501
        :type: str
        """

        self._array_name = array_name

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501

        Email of the individual we send the invitation to  # noqa: E501

        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.

        Email of the individual we send the invitation to  # noqa: E501

        :param email: The email of this Invitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def actions(self):
        """Gets the actions of this Invitation.  # noqa: E501

        A comma separated list of ArrayActions or NamespaceActions  # noqa: E501

        :return: The actions of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Invitation.

        A comma separated list of ArrayActions or NamespaceActions  # noqa: E501

        :param actions: The actions of this Invitation.  # noqa: E501
        :type: str
        """

        self._actions = actions

    @property
    def status(self):
        """Gets the status of this Invitation.  # noqa: E501


        :return: The status of this Invitation.  # noqa: E501
        :rtype: InvitationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invitation.


        :param status: The status of this Invitation.  # noqa: E501
        :type: InvitationStatus
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Invitation.  # noqa: E501

        Datetime the invitation was created in UTC  # noqa: E501

        :return: The created_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invitation.

        Datetime the invitation was created in UTC  # noqa: E501

        :param created_at: The created_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def expires_at(self):
        """Gets the expires_at of this Invitation.  # noqa: E501

        Datetime the invitation is expected to expire in UTC  # noqa: E501

        :return: The expires_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Invitation.

        Datetime the invitation is expected to expire in UTC  # noqa: E501

        :param expires_at: The expires_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def accepted_at(self):
        """Gets the accepted_at of this Invitation.  # noqa: E501

        Datetime the invitation was accepted in UTC  # noqa: E501

        :return: The accepted_at of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._accepted_at

    @accepted_at.setter
    def accepted_at(self, accepted_at):
        """Sets the accepted_at of this Invitation.

        Datetime the invitation was accepted in UTC  # noqa: E501

        :param accepted_at: The accepted_at of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._accepted_at = accepted_at

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
        if not isinstance(other, Invitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invitation):
            return True

        return self.to_dict() != other.to_dict()
