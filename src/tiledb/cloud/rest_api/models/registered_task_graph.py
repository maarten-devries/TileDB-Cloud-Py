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


class RegisteredTaskGraph(object):
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
        "uuid": "str",
        "namespace": "str",
        "name": "str",
        "readme": "str",
        "license_id": "str",
        "license_text": "str",
        "tags": "list[str]",
        "nodes": "list[TaskGraphNode]",
    }

    attribute_map = {
        "uuid": "uuid",
        "namespace": "namespace",
        "name": "name",
        "readme": "readme",
        "license_id": "license_id",
        "license_text": "license_text",
        "tags": "tags",
        "nodes": "nodes",
    }

    def __init__(
        self,
        uuid=None,
        namespace=None,
        name=None,
        readme=None,
        license_id=None,
        license_text=None,
        tags=None,
        nodes=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """RegisteredTaskGraph - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._namespace = None
        self._name = None
        self._readme = None
        self._license_id = None
        self._license_text = None
        self._tags = None
        self._nodes = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if readme is not None:
            self.readme = readme
        self.license_id = license_id
        self.license_text = license_text
        if tags is not None:
            self.tags = tags
        if nodes is not None:
            self.nodes = nodes

    @property
    def uuid(self):
        """Gets the uuid of this RegisteredTaskGraph.  # noqa: E501

        A server-assigned unique ID for the UDF, in UUID format.  # noqa: E501

        :return: The uuid of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RegisteredTaskGraph.

        A server-assigned unique ID for the UDF, in UUID format.  # noqa: E501

        :param uuid: The uuid of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def namespace(self):
        """Gets the namespace of this RegisteredTaskGraph.  # noqa: E501

        The namespace that owns this task graph log.  # noqa: E501

        :return: The namespace of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this RegisteredTaskGraph.

        The namespace that owns this task graph log.  # noqa: E501

        :param namespace: The namespace of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def name(self):
        """Gets the name of this RegisteredTaskGraph.  # noqa: E501

        The name of this graph, to appear in URLs. Must be unique per-namespace.   # noqa: E501

        :return: The name of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisteredTaskGraph.

        The name of this graph, to appear in URLs. Must be unique per-namespace.   # noqa: E501

        :param name: The name of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def readme(self):
        """Gets the readme of this RegisteredTaskGraph.  # noqa: E501

        Documentation for the task graph, in Markdown format.  # noqa: E501

        :return: The readme of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this RegisteredTaskGraph.

        Documentation for the task graph, in Markdown format.  # noqa: E501

        :param readme: The readme of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._readme = readme

    @property
    def license_id(self):
        """Gets the license_id of this RegisteredTaskGraph.  # noqa: E501

        SPDX license identifier.  # noqa: E501

        :return: The license_id of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """Sets the license_id of this RegisteredTaskGraph.

        SPDX license identifier.  # noqa: E501

        :param license_id: The license_id of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._license_id = license_id

    @property
    def license_text(self):
        """Gets the license_text of this RegisteredTaskGraph.  # noqa: E501

        Full text of the license.  # noqa: E501

        :return: The license_text of this RegisteredTaskGraph.  # noqa: E501
        :rtype: str
        """
        return self._license_text

    @license_text.setter
    def license_text(self, license_text):
        """Sets the license_text of this RegisteredTaskGraph.

        Full text of the license.  # noqa: E501

        :param license_text: The license_text of this RegisteredTaskGraph.  # noqa: E501
        :type: str
        """

        self._license_text = license_text

    @property
    def tags(self):
        """Gets the tags of this RegisteredTaskGraph.  # noqa: E501

        Optional tags to classify the graph.  # noqa: E501

        :return: The tags of this RegisteredTaskGraph.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RegisteredTaskGraph.

        Optional tags to classify the graph.  # noqa: E501

        :param tags: The tags of this RegisteredTaskGraph.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def nodes(self):
        """Gets the nodes of this RegisteredTaskGraph.  # noqa: E501

        The structure of the graph, in the form of the nodes that make it up. As with `TaskGraphLog`, nodes must topologically sorted, so that any node appears after all the nodes it depends on.   # noqa: E501

        :return: The nodes of this RegisteredTaskGraph.  # noqa: E501
        :rtype: list[TaskGraphNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this RegisteredTaskGraph.

        The structure of the graph, in the form of the nodes that make it up. As with `TaskGraphLog`, nodes must topologically sorted, so that any node appears after all the nodes it depends on.   # noqa: E501

        :param nodes: The nodes of this RegisteredTaskGraph.  # noqa: E501
        :type: list[TaskGraphNode]
        """

        self._nodes = nodes

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
        if not isinstance(other, RegisteredTaskGraph):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisteredTaskGraph):
            return True

        return self.to_dict() != other.to_dict()
