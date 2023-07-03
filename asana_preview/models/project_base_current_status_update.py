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

class ProjectBaseCurrentStatusUpdate(object):
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
        'title': 'str',
        'resource_subtype': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'title': 'title',
        'resource_subtype': 'resource_subtype'
    }

    def __init__(self, gid=None, resource_type=None, title=None, resource_subtype=None):  # noqa: E501
        """ProjectBaseCurrentStatusUpdate - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._title = None
        self._resource_subtype = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if title is not None:
            self.title = title
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype

    @property
    def gid(self):
        """Gets the gid of this ProjectBaseCurrentStatusUpdate.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectBaseCurrentStatusUpdate.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectBaseCurrentStatusUpdate.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectBaseCurrentStatusUpdate.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def title(self):
        """Gets the title of this ProjectBaseCurrentStatusUpdate.  # noqa: E501

        The title of the status update.  # noqa: E501

        :return: The title of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectBaseCurrentStatusUpdate.

        The title of the status update.  # noqa: E501

        :param title: The title of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this ProjectBaseCurrentStatusUpdate.  # noqa: E501

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The `resource_subtype`s for `status` objects represent the type of their parent.  # noqa: E501

        :return: The resource_subtype of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this ProjectBaseCurrentStatusUpdate.

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The `resource_subtype`s for `status` objects represent the type of their parent.  # noqa: E501

        :param resource_subtype: The resource_subtype of this ProjectBaseCurrentStatusUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["project_status_update", "portfolio_status_update", "goal_status_update"]  # noqa: E501
        if resource_subtype not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_subtype` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_subtype, allowed_values)
            )

        self._resource_subtype = resource_subtype

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
        if issubclass(ProjectBaseCurrentStatusUpdate, dict):
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
        if not isinstance(other, ProjectBaseCurrentStatusUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
