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

class JobResponse(object):
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
        'resource_subtype': 'str',
        'status': 'str',
        'new_project': 'JobBaseNewProject',
        'new_task': 'JobBaseNewTask',
        'new_project_template': 'JobBaseNewProjectTemplate'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'resource_subtype': 'resource_subtype',
        'status': 'status',
        'new_project': 'new_project',
        'new_task': 'new_task',
        'new_project_template': 'new_project_template'
    }

    def __init__(self, gid=None, resource_type=None, resource_subtype=None, status=None, new_project=None, new_task=None, new_project_template=None):  # noqa: E501
        """JobResponse - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._resource_subtype = None
        self._status = None
        self._new_project = None
        self._new_task = None
        self._new_project_template = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if status is not None:
            self.status = status
        if new_project is not None:
            self.new_project = new_project
        if new_task is not None:
            self.new_task = new_task
        if new_project_template is not None:
            self.new_project_template = new_project_template

    @property
    def gid(self):
        """Gets the gid of this JobResponse.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this JobResponse.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this JobResponse.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this JobResponse.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JobResponse.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this JobResponse.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this JobResponse.  # noqa: E501

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :return: The resource_subtype of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this JobResponse.

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :param resource_subtype: The resource_subtype of this JobResponse.  # noqa: E501
        :type: str
        """

        self._resource_subtype = resource_subtype

    @property
    def status(self):
        """Gets the status of this JobResponse.  # noqa: E501

        The current status of this job. The value is one of: `not_started`, `in_progress`, `succeeded`, or `failed`.  # noqa: E501

        :return: The status of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobResponse.

        The current status of this job. The value is one of: `not_started`, `in_progress`, `succeeded`, or `failed`.  # noqa: E501

        :param status: The status of this JobResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_started", "in_progress", "succeeded", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def new_project(self):
        """Gets the new_project of this JobResponse.  # noqa: E501


        :return: The new_project of this JobResponse.  # noqa: E501
        :rtype: JobBaseNewProject
        """
        return self._new_project

    @new_project.setter
    def new_project(self, new_project):
        """Sets the new_project of this JobResponse.


        :param new_project: The new_project of this JobResponse.  # noqa: E501
        :type: JobBaseNewProject
        """

        self._new_project = new_project

    @property
    def new_task(self):
        """Gets the new_task of this JobResponse.  # noqa: E501


        :return: The new_task of this JobResponse.  # noqa: E501
        :rtype: JobBaseNewTask
        """
        return self._new_task

    @new_task.setter
    def new_task(self, new_task):
        """Sets the new_task of this JobResponse.


        :param new_task: The new_task of this JobResponse.  # noqa: E501
        :type: JobBaseNewTask
        """

        self._new_task = new_task

    @property
    def new_project_template(self):
        """Gets the new_project_template of this JobResponse.  # noqa: E501


        :return: The new_project_template of this JobResponse.  # noqa: E501
        :rtype: JobBaseNewProjectTemplate
        """
        return self._new_project_template

    @new_project_template.setter
    def new_project_template(self, new_project_template):
        """Sets the new_project_template of this JobResponse.


        :param new_project_template: The new_project_template of this JobResponse.  # noqa: E501
        :type: JobBaseNewProjectTemplate
        """

        self._new_project_template = new_project_template

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
        if issubclass(JobResponse, dict):
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
        if not isinstance(other, JobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other