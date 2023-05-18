"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from asana_preview.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from asana_preview.exceptions import ApiAttributeError


def lazy_import():
    from asana_preview.model.custom_field_response_people_value_inner import CustomFieldResponsePeopleValueInner
    from asana_preview.model.job_base_new_project_template import JobBaseNewProjectTemplate
    from asana_preview.model.portfolio_response_current_status_update import PortfolioResponseCurrentStatusUpdate
    from asana_preview.model.portfolio_response_custom_field_settings_inner import PortfolioResponseCustomFieldSettingsInner
    from asana_preview.model.portfolio_response_custom_fields_inner import PortfolioResponseCustomFieldsInner
    from asana_preview.model.portfolio_response_workspace import PortfolioResponseWorkspace
    globals()['CustomFieldResponsePeopleValueInner'] = CustomFieldResponsePeopleValueInner
    globals()['JobBaseNewProjectTemplate'] = JobBaseNewProjectTemplate
    globals()['PortfolioResponseCurrentStatusUpdate'] = PortfolioResponseCurrentStatusUpdate
    globals()['PortfolioResponseCustomFieldSettingsInner'] = PortfolioResponseCustomFieldSettingsInner
    globals()['PortfolioResponseCustomFieldsInner'] = PortfolioResponseCustomFieldsInner
    globals()['PortfolioResponseWorkspace'] = PortfolioResponseWorkspace


class PortfolioResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('color',): {
            'DARK-PINK': "dark-pink",
            'DARK-GREEN': "dark-green",
            'DARK-BLUE': "dark-blue",
            'DARK-RED': "dark-red",
            'DARK-TEAL': "dark-teal",
            'DARK-BROWN': "dark-brown",
            'DARK-ORANGE': "dark-orange",
            'DARK-PURPLE': "dark-purple",
            'DARK-WARM-GRAY': "dark-warm-gray",
            'LIGHT-PINK': "light-pink",
            'LIGHT-GREEN': "light-green",
            'LIGHT-BLUE': "light-blue",
            'LIGHT-RED': "light-red",
            'LIGHT-TEAL': "light-teal",
            'LIGHT-BROWN': "light-brown",
            'LIGHT-ORANGE': "light-orange",
            'LIGHT-PURPLE': "light-purple",
            'LIGHT-WARM-GRAY': "light-warm-gray",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'gid': (str,),  # noqa: E501
            'resource_type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'color': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'created_by': (CustomFieldResponsePeopleValueInner,),  # noqa: E501
            'custom_field_settings': ([PortfolioResponseCustomFieldSettingsInner],),  # noqa: E501
            'current_status_update': (PortfolioResponseCurrentStatusUpdate,),  # noqa: E501
            'due_on': (datetime, none_type,),  # noqa: E501
            'custom_fields': ([PortfolioResponseCustomFieldsInner],),  # noqa: E501
            'members': ([CustomFieldResponsePeopleValueInner],),  # noqa: E501
            'owner': (CustomFieldResponsePeopleValueInner,),  # noqa: E501
            'start_on': (date, none_type,),  # noqa: E501
            'workspace': (PortfolioResponseWorkspace,),  # noqa: E501
            'permalink_url': (str,),  # noqa: E501
            'public': (bool,),  # noqa: E501
            'project_templates': ([JobBaseNewProjectTemplate],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'gid': 'gid',  # noqa: E501
        'resource_type': 'resource_type',  # noqa: E501
        'name': 'name',  # noqa: E501
        'color': 'color',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'custom_field_settings': 'custom_field_settings',  # noqa: E501
        'current_status_update': 'current_status_update',  # noqa: E501
        'due_on': 'due_on',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'members': 'members',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'start_on': 'start_on',  # noqa: E501
        'workspace': 'workspace',  # noqa: E501
        'permalink_url': 'permalink_url',  # noqa: E501
        'public': 'public',  # noqa: E501
        'project_templates': 'project_templates',  # noqa: E501
    }

    read_only_vars = {
        'gid',  # noqa: E501
        'resource_type',  # noqa: E501
        'created_at',  # noqa: E501
        'members',  # noqa: E501
        'permalink_url',  # noqa: E501
        'project_templates',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PortfolioResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            gid (str): Globally unique identifier of the resource, as a string.. [optional]  # noqa: E501
            resource_type (str): The base type of this resource.. [optional]  # noqa: E501
            name (str): The name of the portfolio.. [optional]  # noqa: E501
            color (str): Color of the portfolio.. [optional]  # noqa: E501
            created_at (datetime): The time at which this resource was created.. [optional]  # noqa: E501
            created_by (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            custom_field_settings ([PortfolioResponseCustomFieldSettingsInner]): Array of custom field settings applied to the portfolio.. [optional]  # noqa: E501
            current_status_update (PortfolioResponseCurrentStatusUpdate): [optional]  # noqa: E501
            due_on (datetime, none_type): The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD.. [optional]  # noqa: E501
            custom_fields ([PortfolioResponseCustomFieldsInner]): Array of Custom Fields.. [optional]  # noqa: E501
            members ([CustomFieldResponsePeopleValueInner]): [optional]  # noqa: E501
            owner (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            start_on (date, none_type): The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with `YYYY-MM-DD` format. *Note: `due_on` must be present in the request when setting or unsetting the `start_on` parameter. Additionally, `start_on` and `due_on` cannot be the same date.*. [optional]  # noqa: E501
            workspace (PortfolioResponseWorkspace): [optional]  # noqa: E501
            permalink_url (str): A url that points directly to the object within Asana.. [optional]  # noqa: E501
            public (bool): True if the portfolio is public to its workspace members.. [optional]  # noqa: E501
            project_templates ([JobBaseNewProjectTemplate]): Array of project templates that are in the portfolio. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PortfolioResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            gid (str): Globally unique identifier of the resource, as a string.. [optional]  # noqa: E501
            resource_type (str): The base type of this resource.. [optional]  # noqa: E501
            name (str): The name of the portfolio.. [optional]  # noqa: E501
            color (str): Color of the portfolio.. [optional]  # noqa: E501
            created_at (datetime): The time at which this resource was created.. [optional]  # noqa: E501
            created_by (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            custom_field_settings ([PortfolioResponseCustomFieldSettingsInner]): Array of custom field settings applied to the portfolio.. [optional]  # noqa: E501
            current_status_update (PortfolioResponseCurrentStatusUpdate): [optional]  # noqa: E501
            due_on (datetime, none_type): The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD.. [optional]  # noqa: E501
            custom_fields ([PortfolioResponseCustomFieldsInner]): Array of Custom Fields.. [optional]  # noqa: E501
            members ([CustomFieldResponsePeopleValueInner]): [optional]  # noqa: E501
            owner (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            start_on (date, none_type): The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with `YYYY-MM-DD` format. *Note: `due_on` must be present in the request when setting or unsetting the `start_on` parameter. Additionally, `start_on` and `due_on` cannot be the same date.*. [optional]  # noqa: E501
            workspace (PortfolioResponseWorkspace): [optional]  # noqa: E501
            permalink_url (str): A url that points directly to the object within Asana.. [optional]  # noqa: E501
            public (bool): True if the portfolio is public to its workspace members.. [optional]  # noqa: E501
            project_templates ([JobBaseNewProjectTemplate]): Array of project templates that are in the portfolio. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")