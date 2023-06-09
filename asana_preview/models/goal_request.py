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

class GoalRequest(object):
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
        'gid': 'str',
        'resource_type': 'str',
        'name': 'str',
        'html_notes': 'str',
        'notes': 'str',
        'due_on': 'str',
        'start_on': 'str',
        'is_workspace_level': 'bool',
        'liked': 'bool',
        'team': 'str',
        'workspace': 'str',
        'time_period': 'str',
        'owner': 'str',
        'followers': 'list[str]'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'html_notes': 'html_notes',
        'notes': 'notes',
        'due_on': 'due_on',
        'start_on': 'start_on',
        'is_workspace_level': 'is_workspace_level',
        'liked': 'liked',
        'team': 'team',
        'workspace': 'workspace',
        'time_period': 'time_period',
        'owner': 'owner',
        'followers': 'followers'
    }

    def __init__(self, gid=None, resource_type=None, name=None, html_notes=None, notes=None, due_on=None, start_on=None, is_workspace_level=None, liked=None, team=None, workspace=None, time_period=None, owner=None, followers=None):  # noqa: E501
        """GoalRequest - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._html_notes = None
        self._notes = None
        self._due_on = None
        self._start_on = None
        self._is_workspace_level = None
        self._liked = None
        self._team = None
        self._workspace = None
        self._time_period = None
        self._owner = None
        self._followers = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if html_notes is not None:
            self.html_notes = html_notes
        if notes is not None:
            self.notes = notes
        if due_on is not None:
            self.due_on = due_on
        if start_on is not None:
            self.start_on = start_on
        if is_workspace_level is not None:
            self.is_workspace_level = is_workspace_level
        if liked is not None:
            self.liked = liked
        if team is not None:
            self.team = team
        if workspace is not None:
            self.workspace = workspace
        if time_period is not None:
            self.time_period = time_period
        if owner is not None:
            self.owner = owner
        if followers is not None:
            self.followers = followers

    @property
    def gid(self):
        """Gets the gid of this GoalRequest.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this GoalRequest.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this GoalRequest.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this GoalRequest.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this GoalRequest.  # noqa: E501

        The name of the goal.  # noqa: E501

        :return: The name of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GoalRequest.

        The name of the goal.  # noqa: E501

        :param name: The name of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def html_notes(self):
        """Gets the html_notes of this GoalRequest.  # noqa: E501

        The notes of the goal with formatting as HTML.  # noqa: E501

        :return: The html_notes of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._html_notes

    @html_notes.setter
    def html_notes(self, html_notes):
        """Sets the html_notes of this GoalRequest.

        The notes of the goal with formatting as HTML.  # noqa: E501

        :param html_notes: The html_notes of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._html_notes = html_notes

    @property
    def notes(self):
        """Gets the notes of this GoalRequest.  # noqa: E501

        Free-form textual information associated with the goal (i.e. its description).  # noqa: E501

        :return: The notes of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GoalRequest.

        Free-form textual information associated with the goal (i.e. its description).  # noqa: E501

        :param notes: The notes of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def due_on(self):
        """Gets the due_on of this GoalRequest.  # noqa: E501

        The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`.  # noqa: E501

        :return: The due_on of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this GoalRequest.

        The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`.  # noqa: E501

        :param due_on: The due_on of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._due_on = due_on

    @property
    def start_on(self):
        """Gets the start_on of this GoalRequest.  # noqa: E501

        The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date.  # noqa: E501

        :return: The start_on of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_on

    @start_on.setter
    def start_on(self, start_on):
        """Sets the start_on of this GoalRequest.

        The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date.  # noqa: E501

        :param start_on: The start_on of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._start_on = start_on

    @property
    def is_workspace_level(self):
        """Gets the is_workspace_level of this GoalRequest.  # noqa: E501

        *Conditional*. This property is only present when the `workspace` provided is an organization. Whether the goal belongs to the `workspace` (and is listed as part of the workspace’s goals) or not. If it isn’t a workspace-level goal, it is a team-level goal, and is associated with the goal’s team.  # noqa: E501

        :return: The is_workspace_level of this GoalRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_workspace_level

    @is_workspace_level.setter
    def is_workspace_level(self, is_workspace_level):
        """Sets the is_workspace_level of this GoalRequest.

        *Conditional*. This property is only present when the `workspace` provided is an organization. Whether the goal belongs to the `workspace` (and is listed as part of the workspace’s goals) or not. If it isn’t a workspace-level goal, it is a team-level goal, and is associated with the goal’s team.  # noqa: E501

        :param is_workspace_level: The is_workspace_level of this GoalRequest.  # noqa: E501
        :type: bool
        """

        self._is_workspace_level = is_workspace_level

    @property
    def liked(self):
        """Gets the liked of this GoalRequest.  # noqa: E501

        True if the goal is liked by the authorized user, false if not.  # noqa: E501

        :return: The liked of this GoalRequest.  # noqa: E501
        :rtype: bool
        """
        return self._liked

    @liked.setter
    def liked(self, liked):
        """Sets the liked of this GoalRequest.

        True if the goal is liked by the authorized user, false if not.  # noqa: E501

        :param liked: The liked of this GoalRequest.  # noqa: E501
        :type: bool
        """

        self._liked = liked

    @property
    def team(self):
        """Gets the team of this GoalRequest.  # noqa: E501

        *Conditional*. This property is only present when the `workspace` provided is an organization.  # noqa: E501

        :return: The team of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this GoalRequest.

        *Conditional*. This property is only present when the `workspace` provided is an organization.  # noqa: E501

        :param team: The team of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def workspace(self):
        """Gets the workspace of this GoalRequest.  # noqa: E501

        The `gid` of a workspace.  # noqa: E501

        :return: The workspace of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this GoalRequest.

        The `gid` of a workspace.  # noqa: E501

        :param workspace: The workspace of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._workspace = workspace

    @property
    def time_period(self):
        """Gets the time_period of this GoalRequest.  # noqa: E501

        The `gid` of a time period.  # noqa: E501

        :return: The time_period of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this GoalRequest.

        The `gid` of a time period.  # noqa: E501

        :param time_period: The time_period of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._time_period = time_period

    @property
    def owner(self):
        """Gets the owner of this GoalRequest.  # noqa: E501

        The `gid` of a user.  # noqa: E501

        :return: The owner of this GoalRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GoalRequest.

        The `gid` of a user.  # noqa: E501

        :param owner: The owner of this GoalRequest.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def followers(self):
        """Gets the followers of this GoalRequest.  # noqa: E501


        :return: The followers of this GoalRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this GoalRequest.


        :param followers: The followers of this GoalRequest.  # noqa: E501
        :type: list[str]
        """

        self._followers = followers

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
        if issubclass(GoalRequest, dict):
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
        if not isinstance(other, GoalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
