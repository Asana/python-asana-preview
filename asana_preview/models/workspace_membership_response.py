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

class WorkspaceMembershipResponse(object):
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
        'user': 'CustomFieldResponsePeopleValue',
        'workspace': 'GoalResponseWorkspace',
        'user_task_list': 'WorkspaceMembershipResponseUserTaskList',
        'is_active': 'bool',
        'is_admin': 'bool',
        'is_guest': 'bool',
        'vacation_dates': 'WorkspaceMembershipResponseVacationDates',
        'created_at': 'datetime'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'user': 'user',
        'workspace': 'workspace',
        'user_task_list': 'user_task_list',
        'is_active': 'is_active',
        'is_admin': 'is_admin',
        'is_guest': 'is_guest',
        'vacation_dates': 'vacation_dates',
        'created_at': 'created_at'
    }

    def __init__(self, gid=None, resource_type=None, user=None, workspace=None, user_task_list=None, is_active=None, is_admin=None, is_guest=None, vacation_dates=None, created_at=None):  # noqa: E501
        """WorkspaceMembershipResponse - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._user = None
        self._workspace = None
        self._user_task_list = None
        self._is_active = None
        self._is_admin = None
        self._is_guest = None
        self._vacation_dates = None
        self._created_at = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if user is not None:
            self.user = user
        if workspace is not None:
            self.workspace = workspace
        if user_task_list is not None:
            self.user_task_list = user_task_list
        if is_active is not None:
            self.is_active = is_active
        if is_admin is not None:
            self.is_admin = is_admin
        if is_guest is not None:
            self.is_guest = is_guest
        if vacation_dates is not None:
            self.vacation_dates = vacation_dates
        if created_at is not None:
            self.created_at = created_at

    @property
    def gid(self):
        """Gets the gid of this WorkspaceMembershipResponse.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this WorkspaceMembershipResponse.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this WorkspaceMembershipResponse.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this WorkspaceMembershipResponse.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this WorkspaceMembershipResponse.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this WorkspaceMembershipResponse.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def user(self):
        """Gets the user of this WorkspaceMembershipResponse.  # noqa: E501


        :return: The user of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: CustomFieldResponsePeopleValue
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkspaceMembershipResponse.


        :param user: The user of this WorkspaceMembershipResponse.  # noqa: E501
        :type: CustomFieldResponsePeopleValue
        """

        self._user = user

    @property
    def workspace(self):
        """Gets the workspace of this WorkspaceMembershipResponse.  # noqa: E501


        :return: The workspace of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: GoalResponseWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this WorkspaceMembershipResponse.


        :param workspace: The workspace of this WorkspaceMembershipResponse.  # noqa: E501
        :type: GoalResponseWorkspace
        """

        self._workspace = workspace

    @property
    def user_task_list(self):
        """Gets the user_task_list of this WorkspaceMembershipResponse.  # noqa: E501


        :return: The user_task_list of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: WorkspaceMembershipResponseUserTaskList
        """
        return self._user_task_list

    @user_task_list.setter
    def user_task_list(self, user_task_list):
        """Sets the user_task_list of this WorkspaceMembershipResponse.


        :param user_task_list: The user_task_list of this WorkspaceMembershipResponse.  # noqa: E501
        :type: WorkspaceMembershipResponseUserTaskList
        """

        self._user_task_list = user_task_list

    @property
    def is_active(self):
        """Gets the is_active of this WorkspaceMembershipResponse.  # noqa: E501

        Reflects if this user still a member of the workspace.  # noqa: E501

        :return: The is_active of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this WorkspaceMembershipResponse.

        Reflects if this user still a member of the workspace.  # noqa: E501

        :param is_active: The is_active of this WorkspaceMembershipResponse.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_admin(self):
        """Gets the is_admin of this WorkspaceMembershipResponse.  # noqa: E501

        Reflects if this user is an admin of the workspace.  # noqa: E501

        :return: The is_admin of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this WorkspaceMembershipResponse.

        Reflects if this user is an admin of the workspace.  # noqa: E501

        :param is_admin: The is_admin of this WorkspaceMembershipResponse.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_guest(self):
        """Gets the is_guest of this WorkspaceMembershipResponse.  # noqa: E501

        Reflects if this user is a guest of the workspace.  # noqa: E501

        :return: The is_guest of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_guest

    @is_guest.setter
    def is_guest(self, is_guest):
        """Sets the is_guest of this WorkspaceMembershipResponse.

        Reflects if this user is a guest of the workspace.  # noqa: E501

        :param is_guest: The is_guest of this WorkspaceMembershipResponse.  # noqa: E501
        :type: bool
        """

        self._is_guest = is_guest

    @property
    def vacation_dates(self):
        """Gets the vacation_dates of this WorkspaceMembershipResponse.  # noqa: E501


        :return: The vacation_dates of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: WorkspaceMembershipResponseVacationDates
        """
        return self._vacation_dates

    @vacation_dates.setter
    def vacation_dates(self, vacation_dates):
        """Sets the vacation_dates of this WorkspaceMembershipResponse.


        :param vacation_dates: The vacation_dates of this WorkspaceMembershipResponse.  # noqa: E501
        :type: WorkspaceMembershipResponseVacationDates
        """

        self._vacation_dates = vacation_dates

    @property
    def created_at(self):
        """Gets the created_at of this WorkspaceMembershipResponse.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this WorkspaceMembershipResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkspaceMembershipResponse.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this WorkspaceMembershipResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(WorkspaceMembershipResponse, dict):
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
        if not isinstance(other, WorkspaceMembershipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
