# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tiledb.cloud.rest_api.configuration import Configuration


class NotebookStatus(object):
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
        "namespace": "str",
        "uptime": "int",
        "cpu_usage": "int",
        "memory_usage": "int",
        "memory_limit": "int",
        "cpu_count": "int",
    }

    attribute_map = {
        "namespace": "namespace",
        "uptime": "uptime",
        "cpu_usage": "cpu_usage",
        "memory_usage": "memory_usage",
        "memory_limit": "memory_limit",
        "cpu_count": "cpu_count",
    }

    def __init__(
        self,
        namespace=None,
        uptime=None,
        cpu_usage=None,
        memory_usage=None,
        memory_limit=None,
        cpu_count=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """NotebookStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._namespace = None
        self._uptime = None
        self._cpu_usage = None
        self._memory_usage = None
        self._memory_limit = None
        self._cpu_count = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if uptime is not None:
            self.uptime = uptime
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if cpu_count is not None:
            self.cpu_count = cpu_count

    @property
    def namespace(self):
        """Gets the namespace of this NotebookStatus.  # noqa: E501

        namespace of notebook  # noqa: E501

        :return: The namespace of this NotebookStatus.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this NotebookStatus.

        namespace of notebook  # noqa: E501

        :param namespace: The namespace of this NotebookStatus.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def uptime(self):
        """Gets the uptime of this NotebookStatus.  # noqa: E501

        duration notebook has been running in seconds  # noqa: E501

        :return: The uptime of this NotebookStatus.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this NotebookStatus.

        duration notebook has been running in seconds  # noqa: E501

        :param uptime: The uptime of this NotebookStatus.  # noqa: E501
        :type: int
        """

        self._uptime = uptime

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this NotebookStatus.  # noqa: E501

        current cpu usage in millicpu  # noqa: E501

        :return: The cpu_usage of this NotebookStatus.  # noqa: E501
        :rtype: int
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this NotebookStatus.

        current cpu usage in millicpu  # noqa: E501

        :param cpu_usage: The cpu_usage of this NotebookStatus.  # noqa: E501
        :type: int
        """

        self._cpu_usage = cpu_usage

    @property
    def memory_usage(self):
        """Gets the memory_usage of this NotebookStatus.  # noqa: E501

        memory usage in bytes  # noqa: E501

        :return: The memory_usage of this NotebookStatus.  # noqa: E501
        :rtype: int
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        """Sets the memory_usage of this NotebookStatus.

        memory usage in bytes  # noqa: E501

        :param memory_usage: The memory_usage of this NotebookStatus.  # noqa: E501
        :type: int
        """

        self._memory_usage = memory_usage

    @property
    def memory_limit(self):
        """Gets the memory_limit of this NotebookStatus.  # noqa: E501

        memory allocated to notebook server in bytes  # noqa: E501

        :return: The memory_limit of this NotebookStatus.  # noqa: E501
        :rtype: int
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this NotebookStatus.

        memory allocated to notebook server in bytes  # noqa: E501

        :param memory_limit: The memory_limit of this NotebookStatus.  # noqa: E501
        :type: int
        """

        self._memory_limit = memory_limit

    @property
    def cpu_count(self):
        """Gets the cpu_count of this NotebookStatus.  # noqa: E501

        millicpu allocated to notebook server  # noqa: E501

        :return: The cpu_count of this NotebookStatus.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this NotebookStatus.

        millicpu allocated to notebook server  # noqa: E501

        :param cpu_count: The cpu_count of this NotebookStatus.  # noqa: E501
        :type: int
        """

        self._cpu_count = cpu_count

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
        if not isinstance(other, NotebookStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotebookStatus):
            return True

        return self.to_dict() != other.to_dict()
