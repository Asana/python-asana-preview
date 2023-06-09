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

class PortfolioResponseCustomFieldSettings(object):
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
        'project': 'CustomFieldSettingResponseProject',
        'is_important': 'bool',
        'parent': 'CustomFieldSettingResponseParent',
        'custom_field': 'CustomFieldSettingResponseCustomField'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'project': 'project',
        'is_important': 'is_important',
        'parent': 'parent',
        'custom_field': 'custom_field'
    }

    def __init__(self, gid=None, resource_type=None, project=None, is_important=None, parent=None, custom_field=None):  # noqa: E501
        """PortfolioResponseCustomFieldSettings - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._project = None
        self._is_important = None
        self._parent = None
        self._custom_field = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if project is not None:
            self.project = project
        if is_important is not None:
            self.is_important = is_important
        if parent is not None:
            self.parent = parent
        if custom_field is not None:
            self.custom_field = custom_field

    @property
    def gid(self):
        """Gets the gid of this PortfolioResponseCustomFieldSettings.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this PortfolioResponseCustomFieldSettings.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this PortfolioResponseCustomFieldSettings.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PortfolioResponseCustomFieldSettings.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def project(self):
        """Gets the project of this PortfolioResponseCustomFieldSettings.  # noqa: E501


        :return: The project of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: CustomFieldSettingResponseProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this PortfolioResponseCustomFieldSettings.


        :param project: The project of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: CustomFieldSettingResponseProject
        """

        self._project = project

    @property
    def is_important(self):
        """Gets the is_important of this PortfolioResponseCustomFieldSettings.  # noqa: E501

        `is_important` is used in the Asana web application to determine if this custom field is displayed in the list/grid view of a project or portfolio.  # noqa: E501

        :return: The is_important of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: bool
        """
        return self._is_important

    @is_important.setter
    def is_important(self, is_important):
        """Sets the is_important of this PortfolioResponseCustomFieldSettings.

        `is_important` is used in the Asana web application to determine if this custom field is displayed in the list/grid view of a project or portfolio.  # noqa: E501

        :param is_important: The is_important of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: bool
        """

        self._is_important = is_important

    @property
    def parent(self):
        """Gets the parent of this PortfolioResponseCustomFieldSettings.  # noqa: E501


        :return: The parent of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: CustomFieldSettingResponseParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this PortfolioResponseCustomFieldSettings.


        :param parent: The parent of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: CustomFieldSettingResponseParent
        """

        self._parent = parent

    @property
    def custom_field(self):
        """Gets the custom_field of this PortfolioResponseCustomFieldSettings.  # noqa: E501


        :return: The custom_field of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :rtype: CustomFieldSettingResponseCustomField
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this PortfolioResponseCustomFieldSettings.


        :param custom_field: The custom_field of this PortfolioResponseCustomFieldSettings.  # noqa: E501
        :type: CustomFieldSettingResponseCustomField
        """

        self._custom_field = custom_field

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
        if issubclass(PortfolioResponseCustomFieldSettings, dict):
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
        if not isinstance(other, PortfolioResponseCustomFieldSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
