# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.17.51
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud.rest_api.configuration import Configuration


class GroupSharing(object):
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
        "group_actions": "list[GroupActions]",
        "array_actions": "list[ArrayActions]",
        "namespace": "str",
        "namespace_type": "str",
    }

    attribute_map = {
        "group_actions": "group_actions",
        "array_actions": "array_actions",
        "namespace": "namespace",
        "namespace_type": "namespace_type",
    }

    def __init__(
        self,
        group_actions=None,
        array_actions=None,
        namespace=None,
        namespace_type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """GroupSharing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_actions = None
        self._array_actions = None
        self._namespace = None
        self._namespace_type = None
        self.discriminator = None

        if group_actions is not None:
            self.group_actions = group_actions
        if array_actions is not None:
            self.array_actions = array_actions
        if namespace is not None:
            self.namespace = namespace
        if namespace_type is not None:
            self.namespace_type = namespace_type

    @property
    def group_actions(self):
        """Gets the group_actions of this GroupSharing.  # noqa: E501

        List of permitted actions for the group and all subgroups  # noqa: E501

        :return: The group_actions of this GroupSharing.  # noqa: E501
        :rtype: list[GroupActions]
        """
        return self._group_actions

    @group_actions.setter
    def group_actions(self, group_actions):
        """Sets the group_actions of this GroupSharing.

        List of permitted actions for the group and all subgroups  # noqa: E501

        :param group_actions: The group_actions of this GroupSharing.  # noqa: E501
        :type: list[GroupActions]
        """

        self._group_actions = group_actions

    @property
    def array_actions(self):
        """Gets the array_actions of this GroupSharing.  # noqa: E501

        List of permitted actions for all the subarrays of the group  # noqa: E501

        :return: The array_actions of this GroupSharing.  # noqa: E501
        :rtype: list[ArrayActions]
        """
        return self._array_actions

    @array_actions.setter
    def array_actions(self, array_actions):
        """Sets the array_actions of this GroupSharing.

        List of permitted actions for all the subarrays of the group  # noqa: E501

        :param array_actions: The array_actions of this GroupSharing.  # noqa: E501
        :type: list[ArrayActions]
        """

        self._array_actions = array_actions

    @property
    def namespace(self):
        """Gets the namespace of this GroupSharing.  # noqa: E501

        namespace being granted group access can be a user or organization  # noqa: E501

        :return: The namespace of this GroupSharing.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this GroupSharing.

        namespace being granted group access can be a user or organization  # noqa: E501

        :param namespace: The namespace of this GroupSharing.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def namespace_type(self):
        """Gets the namespace_type of this GroupSharing.  # noqa: E501

        details on if the namespace is a organization or user  # noqa: E501

        :return: The namespace_type of this GroupSharing.  # noqa: E501
        :rtype: str
        """
        return self._namespace_type

    @namespace_type.setter
    def namespace_type(self, namespace_type):
        """Sets the namespace_type of this GroupSharing.

        details on if the namespace is a organization or user  # noqa: E501

        :param namespace_type: The namespace_type of this GroupSharing.  # noqa: E501
        :type: str
        """

        self._namespace_type = namespace_type

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
        if not isinstance(other, GroupSharing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupSharing):
            return True

        return self.to_dict() != other.to_dict()
