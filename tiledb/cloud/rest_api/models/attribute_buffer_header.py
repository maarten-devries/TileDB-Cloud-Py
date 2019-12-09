# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AttributeBufferHeader(object):
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
        "name": "str",
        "fixed_len_buffer_size_in_bytes": "int",
        "var_len_buffer_size_in_bytes": "int",
    }

    attribute_map = {
        "name": "name",
        "fixed_len_buffer_size_in_bytes": "fixedLenBufferSizeInBytes",
        "var_len_buffer_size_in_bytes": "varLenBufferSizeInBytes",
    }

    def __init__(
        self,
        name=None,
        fixed_len_buffer_size_in_bytes=None,
        var_len_buffer_size_in_bytes=None,
    ):  # noqa: E501
        """AttributeBufferHeader - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._fixed_len_buffer_size_in_bytes = None
        self._var_len_buffer_size_in_bytes = None
        self.discriminator = None

        self.name = name
        self.fixed_len_buffer_size_in_bytes = fixed_len_buffer_size_in_bytes
        self.var_len_buffer_size_in_bytes = var_len_buffer_size_in_bytes

    @property
    def name(self):
        """Gets the name of this AttributeBufferHeader.  # noqa: E501

        Attribute name  # noqa: E501

        :return: The name of this AttributeBufferHeader.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeBufferHeader.

        Attribute name  # noqa: E501

        :param name: The name of this AttributeBufferHeader.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def fixed_len_buffer_size_in_bytes(self):
        """Gets the fixed_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501

        Number of bytes in the fixed-length attribute data buffer (offsets for var-len attributes)  # noqa: E501

        :return: The fixed_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501
        :rtype: int
        """
        return self._fixed_len_buffer_size_in_bytes

    @fixed_len_buffer_size_in_bytes.setter
    def fixed_len_buffer_size_in_bytes(self, fixed_len_buffer_size_in_bytes):
        """Sets the fixed_len_buffer_size_in_bytes of this AttributeBufferHeader.

        Number of bytes in the fixed-length attribute data buffer (offsets for var-len attributes)  # noqa: E501

        :param fixed_len_buffer_size_in_bytes: The fixed_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501
        :type: int
        """
        if fixed_len_buffer_size_in_bytes is None:
            raise ValueError(
                "Invalid value for `fixed_len_buffer_size_in_bytes`, must not be `None`"
            )  # noqa: E501

        self._fixed_len_buffer_size_in_bytes = fixed_len_buffer_size_in_bytes

    @property
    def var_len_buffer_size_in_bytes(self):
        """Gets the var_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501

        Number of bytes in the var-length attribute data buffer  # noqa: E501

        :return: The var_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501
        :rtype: int
        """
        return self._var_len_buffer_size_in_bytes

    @var_len_buffer_size_in_bytes.setter
    def var_len_buffer_size_in_bytes(self, var_len_buffer_size_in_bytes):
        """Sets the var_len_buffer_size_in_bytes of this AttributeBufferHeader.

        Number of bytes in the var-length attribute data buffer  # noqa: E501

        :param var_len_buffer_size_in_bytes: The var_len_buffer_size_in_bytes of this AttributeBufferHeader.  # noqa: E501
        :type: int
        """
        if var_len_buffer_size_in_bytes is None:
            raise ValueError(
                "Invalid value for `var_len_buffer_size_in_bytes`, must not be `None`"
            )  # noqa: E501

        self._var_len_buffer_size_in_bytes = var_len_buffer_size_in_bytes

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
        if not isinstance(other, AttributeBufferHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
