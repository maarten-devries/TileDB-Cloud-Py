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


class ArrayActivityLog(object):
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
        "event_at": "datetime",
        "action": "ActivityEventType",
        "username": "str",
        "bytes_sent": "int",
        "bytes_received": "int",
        "array_task_id": "str",
        "query_ranges": "str",
    }

    attribute_map = {
        "event_at": "event_at",
        "action": "action",
        "username": "username",
        "bytes_sent": "bytes_sent",
        "bytes_received": "bytes_received",
        "array_task_id": "array_task_id",
        "query_ranges": "query_ranges",
    }

    def __init__(
        self,
        event_at=None,
        action=None,
        username=None,
        bytes_sent=None,
        bytes_received=None,
        array_task_id=None,
        query_ranges=None,
    ):  # noqa: E501
        """ArrayActivityLog - a model defined in OpenAPI"""  # noqa: E501

        self._event_at = None
        self._action = None
        self._username = None
        self._bytes_sent = None
        self._bytes_received = None
        self._array_task_id = None
        self._query_ranges = None
        self.discriminator = None

        if event_at is not None:
            self.event_at = event_at
        if action is not None:
            self.action = action
        if username is not None:
            self.username = username
        if bytes_sent is not None:
            self.bytes_sent = bytes_sent
        if bytes_received is not None:
            self.bytes_received = bytes_received
        if array_task_id is not None:
            self.array_task_id = array_task_id
        if query_ranges is not None:
            self.query_ranges = query_ranges

    @property
    def event_at(self):
        """Gets the event_at of this ArrayActivityLog.  # noqa: E501

        time event took place (RFC3339)  # noqa: E501

        :return: The event_at of this ArrayActivityLog.  # noqa: E501
        :rtype: datetime
        """
        return self._event_at

    @event_at.setter
    def event_at(self, event_at):
        """Sets the event_at of this ArrayActivityLog.

        time event took place (RFC3339)  # noqa: E501

        :param event_at: The event_at of this ArrayActivityLog.  # noqa: E501
        :type: datetime
        """

        self._event_at = event_at

    @property
    def action(self):
        """Gets the action of this ArrayActivityLog.  # noqa: E501


        :return: The action of this ArrayActivityLog.  # noqa: E501
        :rtype: ActivityEventType
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ArrayActivityLog.


        :param action: The action of this ArrayActivityLog.  # noqa: E501
        :type: ActivityEventType
        """

        self._action = action

    @property
    def username(self):
        """Gets the username of this ArrayActivityLog.  # noqa: E501

        User who performed action  # noqa: E501

        :return: The username of this ArrayActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ArrayActivityLog.

        User who performed action  # noqa: E501

        :param username: The username of this ArrayActivityLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def bytes_sent(self):
        """Gets the bytes_sent of this ArrayActivityLog.  # noqa: E501

        Bytes sent to client  # noqa: E501

        :return: The bytes_sent of this ArrayActivityLog.  # noqa: E501
        :rtype: int
        """
        return self._bytes_sent

    @bytes_sent.setter
    def bytes_sent(self, bytes_sent):
        """Sets the bytes_sent of this ArrayActivityLog.

        Bytes sent to client  # noqa: E501

        :param bytes_sent: The bytes_sent of this ArrayActivityLog.  # noqa: E501
        :type: int
        """

        self._bytes_sent = bytes_sent

    @property
    def bytes_received(self):
        """Gets the bytes_received of this ArrayActivityLog.  # noqa: E501

        Bytes recieved from client  # noqa: E501

        :return: The bytes_received of this ArrayActivityLog.  # noqa: E501
        :rtype: int
        """
        return self._bytes_received

    @bytes_received.setter
    def bytes_received(self, bytes_received):
        """Sets the bytes_received of this ArrayActivityLog.

        Bytes recieved from client  # noqa: E501

        :param bytes_received: The bytes_received of this ArrayActivityLog.  # noqa: E501
        :type: int
        """

        self._bytes_received = bytes_received

    @property
    def array_task_id(self):
        """Gets the array_task_id of this ArrayActivityLog.  # noqa: E501

        uuid of associated array task  # noqa: E501

        :return: The array_task_id of this ArrayActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._array_task_id

    @array_task_id.setter
    def array_task_id(self, array_task_id):
        """Sets the array_task_id of this ArrayActivityLog.

        uuid of associated array task  # noqa: E501

        :param array_task_id: The array_task_id of this ArrayActivityLog.  # noqa: E501
        :type: str
        """

        self._array_task_id = array_task_id

    @property
    def query_ranges(self):
        """Gets the query_ranges of this ArrayActivityLog.  # noqa: E501

        ranges for query  # noqa: E501

        :return: The query_ranges of this ArrayActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._query_ranges

    @query_ranges.setter
    def query_ranges(self, query_ranges):
        """Sets the query_ranges of this ArrayActivityLog.

        ranges for query  # noqa: E501

        :param query_ranges: The query_ranges of this ArrayActivityLog.  # noqa: E501
        :type: str
        """

        self._query_ranges = query_ranges

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
        if not isinstance(other, ArrayActivityLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
