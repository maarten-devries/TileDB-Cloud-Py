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


class AssetLocations(object):
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
        "arrays": "StorageLocation",
        "files": "StorageLocation",
        "groups": "StorageLocation",
        "ml_models": "StorageLocation",
        "notebooks": "StorageLocation",
        "task_graphs": "StorageLocation",
        "udfs": "StorageLocation",
    }

    attribute_map = {
        "arrays": "arrays",
        "files": "files",
        "groups": "groups",
        "ml_models": "ml_models",
        "notebooks": "notebooks",
        "task_graphs": "task_graphs",
        "udfs": "udfs",
    }

    def __init__(
        self,
        arrays=None,
        files=None,
        groups=None,
        ml_models=None,
        notebooks=None,
        task_graphs=None,
        udfs=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """AssetLocations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arrays = None
        self._files = None
        self._groups = None
        self._ml_models = None
        self._notebooks = None
        self._task_graphs = None
        self._udfs = None
        self.discriminator = None

        if arrays is not None:
            self.arrays = arrays
        if files is not None:
            self.files = files
        if groups is not None:
            self.groups = groups
        if ml_models is not None:
            self.ml_models = ml_models
        if notebooks is not None:
            self.notebooks = notebooks
        if task_graphs is not None:
            self.task_graphs = task_graphs
        if udfs is not None:
            self.udfs = udfs

    @property
    def arrays(self):
        """Gets the arrays of this AssetLocations.  # noqa: E501


        :return: The arrays of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._arrays

    @arrays.setter
    def arrays(self, arrays):
        """Sets the arrays of this AssetLocations.


        :param arrays: The arrays of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._arrays = arrays

    @property
    def files(self):
        """Gets the files of this AssetLocations.  # noqa: E501


        :return: The files of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this AssetLocations.


        :param files: The files of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._files = files

    @property
    def groups(self):
        """Gets the groups of this AssetLocations.  # noqa: E501


        :return: The groups of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AssetLocations.


        :param groups: The groups of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._groups = groups

    @property
    def ml_models(self):
        """Gets the ml_models of this AssetLocations.  # noqa: E501


        :return: The ml_models of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._ml_models

    @ml_models.setter
    def ml_models(self, ml_models):
        """Sets the ml_models of this AssetLocations.


        :param ml_models: The ml_models of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._ml_models = ml_models

    @property
    def notebooks(self):
        """Gets the notebooks of this AssetLocations.  # noqa: E501


        :return: The notebooks of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        """Sets the notebooks of this AssetLocations.


        :param notebooks: The notebooks of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._notebooks = notebooks

    @property
    def task_graphs(self):
        """Gets the task_graphs of this AssetLocations.  # noqa: E501


        :return: The task_graphs of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._task_graphs

    @task_graphs.setter
    def task_graphs(self, task_graphs):
        """Sets the task_graphs of this AssetLocations.


        :param task_graphs: The task_graphs of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._task_graphs = task_graphs

    @property
    def udfs(self):
        """Gets the udfs of this AssetLocations.  # noqa: E501


        :return: The udfs of this AssetLocations.  # noqa: E501
        :rtype: StorageLocation
        """
        return self._udfs

    @udfs.setter
    def udfs(self, udfs):
        """Sets the udfs of this AssetLocations.


        :param udfs: The udfs of this AssetLocations.  # noqa: E501
        :type: StorageLocation
        """

        self._udfs = udfs

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
        if not isinstance(other, AssetLocations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetLocations):
            return True

        return self.to_dict() != other.to_dict()
