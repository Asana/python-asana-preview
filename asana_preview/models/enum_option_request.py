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

class EnumOptionRequest(object):
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
        'enabled': 'bool',
        'color': 'str',
        'insert_before': 'str',
        'insert_after': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'enabled': 'enabled',
        'color': 'color',
        'insert_before': 'insert_before',
        'insert_after': 'insert_after'
    }

    def __init__(self, gid=None, resource_type=None, name=None, enabled=None, color=None, insert_before=None, insert_after=None):  # noqa: E501
        """EnumOptionRequest - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._enabled = None
        self._color = None
        self._insert_before = None
        self._insert_after = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if color is not None:
            self.color = color
        if insert_before is not None:
            self.insert_before = insert_before
        if insert_after is not None:
            self.insert_after = insert_after

    @property
    def gid(self):
        """Gets the gid of this EnumOptionRequest.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this EnumOptionRequest.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this EnumOptionRequest.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EnumOptionRequest.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this EnumOptionRequest.  # noqa: E501

        The name of the enum option.  # noqa: E501

        :return: The name of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnumOptionRequest.

        The name of the enum option.  # noqa: E501

        :param name: The name of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this EnumOptionRequest.  # noqa: E501

        Whether or not the enum option is a selectable value for the custom field.  # noqa: E501

        :return: The enabled of this EnumOptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EnumOptionRequest.

        Whether or not the enum option is a selectable value for the custom field.  # noqa: E501

        :param enabled: The enabled of this EnumOptionRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def color(self):
        """Gets the color of this EnumOptionRequest.  # noqa: E501

        The color of the enum option. Defaults to ‘none’.  # noqa: E501

        :return: The color of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EnumOptionRequest.

        The color of the enum option. Defaults to ‘none’.  # noqa: E501

        :param color: The color of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def insert_before(self):
        """Gets the insert_before of this EnumOptionRequest.  # noqa: E501

        An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.  # noqa: E501

        :return: The insert_before of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_before

    @insert_before.setter
    def insert_before(self, insert_before):
        """Sets the insert_before of this EnumOptionRequest.

        An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.  # noqa: E501

        :param insert_before: The insert_before of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._insert_before = insert_before

    @property
    def insert_after(self):
        """Gets the insert_after of this EnumOptionRequest.  # noqa: E501

        An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.  # noqa: E501

        :return: The insert_after of this EnumOptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this EnumOptionRequest.

        An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.  # noqa: E501

        :param insert_after: The insert_after of this EnumOptionRequest.  # noqa: E501
        :type: str
        """

        self._insert_after = insert_after

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
        if issubclass(EnumOptionRequest, dict):
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
        if not isinstance(other, EnumOptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
