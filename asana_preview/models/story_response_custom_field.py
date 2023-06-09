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

class StoryResponseCustomField(object):
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
        'resource_subtype': 'str',
        'type': 'str',
        'enum_options': 'list[CustomFieldBaseEnumOptions]',
        'enabled': 'bool',
        'is_formula_field': 'bool',
        'date_value': 'CustomFieldBaseDateValue',
        'enum_value': 'CustomFieldBaseEnumValue',
        'multi_enum_values': 'list[CustomFieldBaseEnumOptions]',
        'number_value': 'float',
        'text_value': 'str',
        'display_value': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'resource_subtype': 'resource_subtype',
        'type': 'type',
        'enum_options': 'enum_options',
        'enabled': 'enabled',
        'is_formula_field': 'is_formula_field',
        'date_value': 'date_value',
        'enum_value': 'enum_value',
        'multi_enum_values': 'multi_enum_values',
        'number_value': 'number_value',
        'text_value': 'text_value',
        'display_value': 'display_value'
    }

    def __init__(self, gid=None, resource_type=None, name=None, resource_subtype=None, type=None, enum_options=None, enabled=None, is_formula_field=None, date_value=None, enum_value=None, multi_enum_values=None, number_value=None, text_value=None, display_value=None):  # noqa: E501
        """StoryResponseCustomField - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._resource_subtype = None
        self._type = None
        self._enum_options = None
        self._enabled = None
        self._is_formula_field = None
        self._date_value = None
        self._enum_value = None
        self._multi_enum_values = None
        self._number_value = None
        self._text_value = None
        self._display_value = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if type is not None:
            self.type = type
        if enum_options is not None:
            self.enum_options = enum_options
        if enabled is not None:
            self.enabled = enabled
        if is_formula_field is not None:
            self.is_formula_field = is_formula_field
        if date_value is not None:
            self.date_value = date_value
        if enum_value is not None:
            self.enum_value = enum_value
        if multi_enum_values is not None:
            self.multi_enum_values = multi_enum_values
        if number_value is not None:
            self.number_value = number_value
        if text_value is not None:
            self.text_value = text_value
        if display_value is not None:
            self.display_value = display_value

    @property
    def gid(self):
        """Gets the gid of this StoryResponseCustomField.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this StoryResponseCustomField.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this StoryResponseCustomField.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this StoryResponseCustomField.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this StoryResponseCustomField.  # noqa: E501

        The name of the custom field.  # noqa: E501

        :return: The name of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoryResponseCustomField.

        The name of the custom field.  # noqa: E501

        :param name: The name of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this StoryResponseCustomField.  # noqa: E501

        The type of the custom field. Must be one of the given values.   # noqa: E501

        :return: The resource_subtype of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this StoryResponseCustomField.

        The type of the custom field. Must be one of the given values.   # noqa: E501

        :param resource_subtype: The resource_subtype of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "enum", "multi_enum", "number", "date", "people"]  # noqa: E501
        if resource_subtype not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_subtype` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_subtype, allowed_values)
            )

        self._resource_subtype = resource_subtype

    @property
    def type(self):
        """Gets the type of this StoryResponseCustomField.  # noqa: E501

        *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.   # noqa: E501

        :return: The type of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoryResponseCustomField.

        *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.   # noqa: E501

        :param type: The type of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "enum", "multi_enum", "number", "date", "people"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def enum_options(self):
        """Gets the enum_options of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. Only relevant for custom fields of type `enum`. This array specifies the possible values which an `enum` custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield).  # noqa: E501

        :return: The enum_options of this StoryResponseCustomField.  # noqa: E501
        :rtype: list[CustomFieldBaseEnumOptions]
        """
        return self._enum_options

    @enum_options.setter
    def enum_options(self, enum_options):
        """Sets the enum_options of this StoryResponseCustomField.

        *Conditional*. Only relevant for custom fields of type `enum`. This array specifies the possible values which an `enum` custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield).  # noqa: E501

        :param enum_options: The enum_options of this StoryResponseCustomField.  # noqa: E501
        :type: list[CustomFieldBaseEnumOptions]
        """

        self._enum_options = enum_options

    @property
    def enabled(self):
        """Gets the enabled of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. Determines if the custom field is enabled or not.  # noqa: E501

        :return: The enabled of this StoryResponseCustomField.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this StoryResponseCustomField.

        *Conditional*. Determines if the custom field is enabled or not.  # noqa: E501

        :param enabled: The enabled of this StoryResponseCustomField.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def is_formula_field(self):
        """Gets the is_formula_field of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. This flag describes whether a custom field is a formula custom field.  # noqa: E501

        :return: The is_formula_field of this StoryResponseCustomField.  # noqa: E501
        :rtype: bool
        """
        return self._is_formula_field

    @is_formula_field.setter
    def is_formula_field(self, is_formula_field):
        """Sets the is_formula_field of this StoryResponseCustomField.

        *Conditional*. This flag describes whether a custom field is a formula custom field.  # noqa: E501

        :param is_formula_field: The is_formula_field of this StoryResponseCustomField.  # noqa: E501
        :type: bool
        """

        self._is_formula_field = is_formula_field

    @property
    def date_value(self):
        """Gets the date_value of this StoryResponseCustomField.  # noqa: E501


        :return: The date_value of this StoryResponseCustomField.  # noqa: E501
        :rtype: CustomFieldBaseDateValue
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this StoryResponseCustomField.


        :param date_value: The date_value of this StoryResponseCustomField.  # noqa: E501
        :type: CustomFieldBaseDateValue
        """

        self._date_value = date_value

    @property
    def enum_value(self):
        """Gets the enum_value of this StoryResponseCustomField.  # noqa: E501


        :return: The enum_value of this StoryResponseCustomField.  # noqa: E501
        :rtype: CustomFieldBaseEnumValue
        """
        return self._enum_value

    @enum_value.setter
    def enum_value(self, enum_value):
        """Sets the enum_value of this StoryResponseCustomField.


        :param enum_value: The enum_value of this StoryResponseCustomField.  # noqa: E501
        :type: CustomFieldBaseEnumValue
        """

        self._enum_value = enum_value

    @property
    def multi_enum_values(self):
        """Gets the multi_enum_values of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. Only relevant for custom fields of type `multi_enum`. This object is the chosen values of a `multi_enum` custom field.  # noqa: E501

        :return: The multi_enum_values of this StoryResponseCustomField.  # noqa: E501
        :rtype: list[CustomFieldBaseEnumOptions]
        """
        return self._multi_enum_values

    @multi_enum_values.setter
    def multi_enum_values(self, multi_enum_values):
        """Sets the multi_enum_values of this StoryResponseCustomField.

        *Conditional*. Only relevant for custom fields of type `multi_enum`. This object is the chosen values of a `multi_enum` custom field.  # noqa: E501

        :param multi_enum_values: The multi_enum_values of this StoryResponseCustomField.  # noqa: E501
        :type: list[CustomFieldBaseEnumOptions]
        """

        self._multi_enum_values = multi_enum_values

    @property
    def number_value(self):
        """Gets the number_value of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. This number is the value of a `number` custom field.  # noqa: E501

        :return: The number_value of this StoryResponseCustomField.  # noqa: E501
        :rtype: float
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this StoryResponseCustomField.

        *Conditional*. This number is the value of a `number` custom field.  # noqa: E501

        :param number_value: The number_value of this StoryResponseCustomField.  # noqa: E501
        :type: float
        """

        self._number_value = number_value

    @property
    def text_value(self):
        """Gets the text_value of this StoryResponseCustomField.  # noqa: E501

        *Conditional*. This string is the value of a `text` custom field.  # noqa: E501

        :return: The text_value of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this StoryResponseCustomField.

        *Conditional*. This string is the value of a `text` custom field.  # noqa: E501

        :param text_value: The text_value of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """

        self._text_value = text_value

    @property
    def display_value(self):
        """Gets the display_value of this StoryResponseCustomField.  # noqa: E501

        A string representation for the value of the custom field. Integrations that don't require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types.  # noqa: E501

        :return: The display_value of this StoryResponseCustomField.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this StoryResponseCustomField.

        A string representation for the value of the custom field. Integrations that don't require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types.  # noqa: E501

        :param display_value: The display_value of this StoryResponseCustomField.  # noqa: E501
        :type: str
        """

        self._display_value = display_value

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
        if issubclass(StoryResponseCustomField, dict):
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
        if not isinstance(other, StoryResponseCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
