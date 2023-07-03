# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user': 'EventResponseUser',
        'resource': 'EventResponseResource',
        'type': 'str',
        'action': 'str',
        'parent': 'EventResponseParent',
        'created_at': 'datetime',
        'change': 'EventResponseChange'
    }

    attribute_map = {
        'user': 'user',
        'resource': 'resource',
        'type': 'type',
        'action': 'action',
        'parent': 'parent',
        'created_at': 'created_at',
        'change': 'change'
    }

    def __init__(self, user=None, resource=None, type=None, action=None, parent=None, created_at=None, change=None):  # noqa: E501
        """EventResponse - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._resource = None
        self._type = None
        self._action = None
        self._parent = None
        self._created_at = None
        self._change = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if resource is not None:
            self.resource = resource
        if type is not None:
            self.type = type
        if action is not None:
            self.action = action
        if parent is not None:
            self.parent = parent
        if created_at is not None:
            self.created_at = created_at
        if change is not None:
            self.change = change

    @property
    def user(self):
        """Gets the user of this EventResponse.  # noqa: E501


        :return: The user of this EventResponse.  # noqa: E501
        :rtype: EventResponseUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EventResponse.


        :param user: The user of this EventResponse.  # noqa: E501
        :type: EventResponseUser
        """

        self._user = user

    @property
    def resource(self):
        """Gets the resource of this EventResponse.  # noqa: E501


        :return: The resource of this EventResponse.  # noqa: E501
        :rtype: EventResponseResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this EventResponse.


        :param resource: The resource of this EventResponse.  # noqa: E501
        :type: EventResponseResource
        """

        self._resource = resource

    @property
    def type(self):
        """Gets the type of this EventResponse.  # noqa: E501

        *Deprecated: Refer to the resource_type of the resource.* The type of the resource that generated the event.  # noqa: E501

        :return: The type of this EventResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventResponse.

        *Deprecated: Refer to the resource_type of the resource.* The type of the resource that generated the event.  # noqa: E501

        :param type: The type of this EventResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def action(self):
        """Gets the action of this EventResponse.  # noqa: E501

        The type of action taken on the **resource** that triggered the event.  This can be one of `changed`, `added`, `removed`, `deleted`, or `undeleted` depending on the nature of the event.  # noqa: E501

        :return: The action of this EventResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EventResponse.

        The type of action taken on the **resource** that triggered the event.  This can be one of `changed`, `added`, `removed`, `deleted`, or `undeleted` depending on the nature of the event.  # noqa: E501

        :param action: The action of this EventResponse.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def parent(self):
        """Gets the parent of this EventResponse.  # noqa: E501


        :return: The parent of this EventResponse.  # noqa: E501
        :rtype: EventResponseParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this EventResponse.


        :param parent: The parent of this EventResponse.  # noqa: E501
        :type: EventResponseParent
        """

        self._parent = parent

    @property
    def created_at(self):
        """Gets the created_at of this EventResponse.  # noqa: E501

        The timestamp when the event occurred.  # noqa: E501

        :return: The created_at of this EventResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EventResponse.

        The timestamp when the event occurred.  # noqa: E501

        :param created_at: The created_at of this EventResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def change(self):
        """Gets the change of this EventResponse.  # noqa: E501


        :return: The change of this EventResponse.  # noqa: E501
        :rtype: EventResponseChange
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this EventResponse.


        :param change: The change of this EventResponse.  # noqa: E501
        :type: EventResponseChange
        """

        self._change = change

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EventResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
