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
    from asana_preview.model.custom_field_base_enum_options_inner import CustomFieldBaseEnumOptionsInner
    from asana_preview.model.custom_field_response_people_value_inner import CustomFieldResponsePeopleValueInner
    from asana_preview.model.goal_response_likes_inner import GoalResponseLikesInner
    from asana_preview.model.story_response_assignee import StoryResponseAssignee
    from asana_preview.model.story_response_custom_field import StoryResponseCustomField
    from asana_preview.model.story_response_new_date_value import StoryResponseNewDateValue
    from asana_preview.model.story_response_old_date_value import StoryResponseOldDateValue
    from asana_preview.model.story_response_old_dates import StoryResponseOldDates
    from asana_preview.model.story_response_old_enum_value import StoryResponseOldEnumValue
    from asana_preview.model.story_response_old_section import StoryResponseOldSection
    from asana_preview.model.story_response_previews_inner import StoryResponsePreviewsInner
    from asana_preview.model.story_response_project import StoryResponseProject
    from asana_preview.model.story_response_story import StoryResponseStory
    from asana_preview.model.story_response_tag import StoryResponseTag
    from asana_preview.model.story_response_target import StoryResponseTarget
    from asana_preview.model.story_response_task import StoryResponseTask
    globals()['CustomFieldBaseEnumOptionsInner'] = CustomFieldBaseEnumOptionsInner
    globals()['CustomFieldResponsePeopleValueInner'] = CustomFieldResponsePeopleValueInner
    globals()['GoalResponseLikesInner'] = GoalResponseLikesInner
    globals()['StoryResponseAssignee'] = StoryResponseAssignee
    globals()['StoryResponseCustomField'] = StoryResponseCustomField
    globals()['StoryResponseNewDateValue'] = StoryResponseNewDateValue
    globals()['StoryResponseOldDateValue'] = StoryResponseOldDateValue
    globals()['StoryResponseOldDates'] = StoryResponseOldDates
    globals()['StoryResponseOldEnumValue'] = StoryResponseOldEnumValue
    globals()['StoryResponseOldSection'] = StoryResponseOldSection
    globals()['StoryResponsePreviewsInner'] = StoryResponsePreviewsInner
    globals()['StoryResponseProject'] = StoryResponseProject
    globals()['StoryResponseStory'] = StoryResponseStory
    globals()['StoryResponseTag'] = StoryResponseTag
    globals()['StoryResponseTarget'] = StoryResponseTarget
    globals()['StoryResponseTask'] = StoryResponseTask


class StoryResponse(ModelNormal):
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
        ('sticker_name',): {
            'GREEN_CHECKMARK': "green_checkmark",
            'PEOPLE_DANCING': "people_dancing",
            'DANCING_UNICORN': "dancing_unicorn",
            'HEART': "heart",
            'PARTY_POPPER': "party_popper",
            'PEOPLE_WAVING_FLAGS': "people_waving_flags",
            'SPLASHING_NARWHAL': "splashing_narwhal",
            'TROPHY': "trophy",
            'YETI_RIDING_UNICORN': "yeti_riding_unicorn",
            'CELEBRATING_PEOPLE': "celebrating_people",
            'DETERMINED_CLIMBERS': "determined_climbers",
            'PHOENIX_SPREADING_LOVE': "phoenix_spreading_love",
        },
        ('type',): {
            'COMMENT': "comment",
            'SYSTEM': "system",
        },
        ('source',): {
            'WEB': "web",
            'EMAIL': "email",
            'MOBILE': "mobile",
            'API': "api",
            'UNKNOWN': "unknown",
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
            'created_at': (datetime,),  # noqa: E501
            'resource_subtype': (str,),  # noqa: E501
            'text': (str,),  # noqa: E501
            'html_text': (str,),  # noqa: E501
            'is_pinned': (bool,),  # noqa: E501
            'sticker_name': (str,),  # noqa: E501
            'created_by': (CustomFieldResponsePeopleValueInner,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'is_editable': (bool,),  # noqa: E501
            'is_edited': (bool,),  # noqa: E501
            'hearted': (bool,),  # noqa: E501
            'hearts': ([GoalResponseLikesInner],),  # noqa: E501
            'num_hearts': (int,),  # noqa: E501
            'liked': (bool,),  # noqa: E501
            'likes': ([GoalResponseLikesInner],),  # noqa: E501
            'num_likes': (int,),  # noqa: E501
            'previews': ([StoryResponsePreviewsInner],),  # noqa: E501
            'old_name': (str,),  # noqa: E501
            'new_name': (str,),  # noqa: E501
            'old_dates': (StoryResponseOldDates,),  # noqa: E501
            'new_dates': (StoryResponseOldDates,),  # noqa: E501
            'old_resource_subtype': (str,),  # noqa: E501
            'new_resource_subtype': (str,),  # noqa: E501
            'story': (StoryResponseStory,),  # noqa: E501
            'assignee': (StoryResponseAssignee,),  # noqa: E501
            'follower': (StoryResponseAssignee,),  # noqa: E501
            'old_section': (StoryResponseOldSection,),  # noqa: E501
            'new_section': (StoryResponseOldSection,),  # noqa: E501
            'task': (StoryResponseTask,),  # noqa: E501
            'project': (StoryResponseProject,),  # noqa: E501
            'tag': (StoryResponseTag,),  # noqa: E501
            'custom_field': (StoryResponseCustomField,),  # noqa: E501
            'old_text_value': (str,),  # noqa: E501
            'new_text_value': (str,),  # noqa: E501
            'old_number_value': (int,),  # noqa: E501
            'new_number_value': (int,),  # noqa: E501
            'old_enum_value': (StoryResponseOldEnumValue,),  # noqa: E501
            'new_enum_value': (StoryResponseOldEnumValue,),  # noqa: E501
            'old_date_value': (StoryResponseOldDateValue,),  # noqa: E501
            'new_date_value': (StoryResponseNewDateValue,),  # noqa: E501
            'old_people_value': ([CustomFieldResponsePeopleValueInner],),  # noqa: E501
            'new_people_value': ([CustomFieldResponsePeopleValueInner],),  # noqa: E501
            'old_multi_enum_values': ([CustomFieldBaseEnumOptionsInner],),  # noqa: E501
            'new_multi_enum_values': ([CustomFieldBaseEnumOptionsInner],),  # noqa: E501
            'new_approval_status': (str,),  # noqa: E501
            'old_approval_status': (str,),  # noqa: E501
            'duplicate_of': (StoryResponseTask,),  # noqa: E501
            'duplicated_from': (StoryResponseTask,),  # noqa: E501
            'dependency': (StoryResponseTask,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'target': (StoryResponseTarget,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'gid': 'gid',  # noqa: E501
        'resource_type': 'resource_type',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'resource_subtype': 'resource_subtype',  # noqa: E501
        'text': 'text',  # noqa: E501
        'html_text': 'html_text',  # noqa: E501
        'is_pinned': 'is_pinned',  # noqa: E501
        'sticker_name': 'sticker_name',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'type': 'type',  # noqa: E501
        'is_editable': 'is_editable',  # noqa: E501
        'is_edited': 'is_edited',  # noqa: E501
        'hearted': 'hearted',  # noqa: E501
        'hearts': 'hearts',  # noqa: E501
        'num_hearts': 'num_hearts',  # noqa: E501
        'liked': 'liked',  # noqa: E501
        'likes': 'likes',  # noqa: E501
        'num_likes': 'num_likes',  # noqa: E501
        'previews': 'previews',  # noqa: E501
        'old_name': 'old_name',  # noqa: E501
        'new_name': 'new_name',  # noqa: E501
        'old_dates': 'old_dates',  # noqa: E501
        'new_dates': 'new_dates',  # noqa: E501
        'old_resource_subtype': 'old_resource_subtype',  # noqa: E501
        'new_resource_subtype': 'new_resource_subtype',  # noqa: E501
        'story': 'story',  # noqa: E501
        'assignee': 'assignee',  # noqa: E501
        'follower': 'follower',  # noqa: E501
        'old_section': 'old_section',  # noqa: E501
        'new_section': 'new_section',  # noqa: E501
        'task': 'task',  # noqa: E501
        'project': 'project',  # noqa: E501
        'tag': 'tag',  # noqa: E501
        'custom_field': 'custom_field',  # noqa: E501
        'old_text_value': 'old_text_value',  # noqa: E501
        'new_text_value': 'new_text_value',  # noqa: E501
        'old_number_value': 'old_number_value',  # noqa: E501
        'new_number_value': 'new_number_value',  # noqa: E501
        'old_enum_value': 'old_enum_value',  # noqa: E501
        'new_enum_value': 'new_enum_value',  # noqa: E501
        'old_date_value': 'old_date_value',  # noqa: E501
        'new_date_value': 'new_date_value',  # noqa: E501
        'old_people_value': 'old_people_value',  # noqa: E501
        'new_people_value': 'new_people_value',  # noqa: E501
        'old_multi_enum_values': 'old_multi_enum_values',  # noqa: E501
        'new_multi_enum_values': 'new_multi_enum_values',  # noqa: E501
        'new_approval_status': 'new_approval_status',  # noqa: E501
        'old_approval_status': 'old_approval_status',  # noqa: E501
        'duplicate_of': 'duplicate_of',  # noqa: E501
        'duplicated_from': 'duplicated_from',  # noqa: E501
        'dependency': 'dependency',  # noqa: E501
        'source': 'source',  # noqa: E501
        'target': 'target',  # noqa: E501
    }

    read_only_vars = {
        'gid',  # noqa: E501
        'resource_type',  # noqa: E501
        'created_at',  # noqa: E501
        'resource_subtype',  # noqa: E501
        'type',  # noqa: E501
        'is_editable',  # noqa: E501
        'is_edited',  # noqa: E501
        'hearted',  # noqa: E501
        'hearts',  # noqa: E501
        'num_hearts',  # noqa: E501
        'liked',  # noqa: E501
        'likes',  # noqa: E501
        'num_likes',  # noqa: E501
        'previews',  # noqa: E501
        'new_name',  # noqa: E501
        'old_resource_subtype',  # noqa: E501
        'new_resource_subtype',  # noqa: E501
        'old_text_value',  # noqa: E501
        'new_text_value',  # noqa: E501
        'old_number_value',  # noqa: E501
        'new_number_value',  # noqa: E501
        'old_people_value',  # noqa: E501
        'new_people_value',  # noqa: E501
        'old_multi_enum_values',  # noqa: E501
        'new_multi_enum_values',  # noqa: E501
        'new_approval_status',  # noqa: E501
        'old_approval_status',  # noqa: E501
        'source',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """StoryResponse - a model defined in OpenAPI

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
            created_at (datetime): The time at which this resource was created.. [optional]  # noqa: E501
            resource_subtype (str): The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.. [optional]  # noqa: E501
            text (str): The plain text of the comment to add. Cannot be used with html_text.. [optional]  # noqa: E501
            html_text (str): [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator.. [optional]  # noqa: E501
            is_pinned (bool): *Conditional*. Whether the story should be pinned on the resource.. [optional]  # noqa: E501
            sticker_name (str): The name of the sticker in this story. `null` if there is no sticker.. [optional]  # noqa: E501
            created_by (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            is_editable (bool): *Conditional*. Whether the text of the story can be edited after creation.. [optional]  # noqa: E501
            is_edited (bool): *Conditional*. Whether the text of the story has been edited after creation.. [optional]  # noqa: E501
            hearted (bool): *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not.. [optional]  # noqa: E501
            hearts ([GoalResponseLikesInner]): *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story.. [optional]  # noqa: E501
            num_hearts (int): *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story.. [optional]  # noqa: E501
            liked (bool): *Conditional*. True if the story is liked by the authorized user, false if not.. [optional]  # noqa: E501
            likes ([GoalResponseLikesInner]): *Conditional*. Array of likes for users who have liked this story.. [optional]  # noqa: E501
            num_likes (int): *Conditional*. The number of users who have liked this story.. [optional]  # noqa: E501
            previews ([StoryResponsePreviewsInner]): *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.*. [optional]  # noqa: E501
            old_name (str): *Conditional*'. [optional]  # noqa: E501
            new_name (str): *Conditional*. [optional]  # noqa: E501
            old_dates (StoryResponseOldDates): [optional]  # noqa: E501
            new_dates (StoryResponseOldDates): [optional]  # noqa: E501
            old_resource_subtype (str): *Conditional*. [optional]  # noqa: E501
            new_resource_subtype (str): *Conditional*. [optional]  # noqa: E501
            story (StoryResponseStory): [optional]  # noqa: E501
            assignee (StoryResponseAssignee): [optional]  # noqa: E501
            follower (StoryResponseAssignee): [optional]  # noqa: E501
            old_section (StoryResponseOldSection): [optional]  # noqa: E501
            new_section (StoryResponseOldSection): [optional]  # noqa: E501
            task (StoryResponseTask): [optional]  # noqa: E501
            project (StoryResponseProject): [optional]  # noqa: E501
            tag (StoryResponseTag): [optional]  # noqa: E501
            custom_field (StoryResponseCustomField): [optional]  # noqa: E501
            old_text_value (str): *Conditional*. [optional]  # noqa: E501
            new_text_value (str): *Conditional*. [optional]  # noqa: E501
            old_number_value (int): *Conditional*. [optional]  # noqa: E501
            new_number_value (int): *Conditional*. [optional]  # noqa: E501
            old_enum_value (StoryResponseOldEnumValue): [optional]  # noqa: E501
            new_enum_value (StoryResponseOldEnumValue): [optional]  # noqa: E501
            old_date_value (StoryResponseOldDateValue): [optional]  # noqa: E501
            new_date_value (StoryResponseNewDateValue): [optional]  # noqa: E501
            old_people_value ([CustomFieldResponsePeopleValueInner]): *Conditional*. The old value of a people custom field story.. [optional]  # noqa: E501
            new_people_value ([CustomFieldResponsePeopleValueInner]): *Conditional*. The new value of a people custom field story.. [optional]  # noqa: E501
            old_multi_enum_values ([CustomFieldBaseEnumOptionsInner]): *Conditional*. The old value of a multi-enum custom field story.. [optional]  # noqa: E501
            new_multi_enum_values ([CustomFieldBaseEnumOptionsInner]): *Conditional*. The new value of a multi-enum custom field story.. [optional]  # noqa: E501
            new_approval_status (str): *Conditional*. The new value of approval status.. [optional]  # noqa: E501
            old_approval_status (str): *Conditional*. The old value of approval status.. [optional]  # noqa: E501
            duplicate_of (StoryResponseTask): [optional]  # noqa: E501
            duplicated_from (StoryResponseTask): [optional]  # noqa: E501
            dependency (StoryResponseTask): [optional]  # noqa: E501
            source (str): The component of the Asana product the user used to trigger the story.. [optional]  # noqa: E501
            target (StoryResponseTarget): [optional]  # noqa: E501
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
        """StoryResponse - a model defined in OpenAPI

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
            created_at (datetime): The time at which this resource was created.. [optional]  # noqa: E501
            resource_subtype (str): The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.. [optional]  # noqa: E501
            text (str): The plain text of the comment to add. Cannot be used with html_text.. [optional]  # noqa: E501
            html_text (str): [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator.. [optional]  # noqa: E501
            is_pinned (bool): *Conditional*. Whether the story should be pinned on the resource.. [optional]  # noqa: E501
            sticker_name (str): The name of the sticker in this story. `null` if there is no sticker.. [optional]  # noqa: E501
            created_by (CustomFieldResponsePeopleValueInner): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            is_editable (bool): *Conditional*. Whether the text of the story can be edited after creation.. [optional]  # noqa: E501
            is_edited (bool): *Conditional*. Whether the text of the story has been edited after creation.. [optional]  # noqa: E501
            hearted (bool): *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not.. [optional]  # noqa: E501
            hearts ([GoalResponseLikesInner]): *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story.. [optional]  # noqa: E501
            num_hearts (int): *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story.. [optional]  # noqa: E501
            liked (bool): *Conditional*. True if the story is liked by the authorized user, false if not.. [optional]  # noqa: E501
            likes ([GoalResponseLikesInner]): *Conditional*. Array of likes for users who have liked this story.. [optional]  # noqa: E501
            num_likes (int): *Conditional*. The number of users who have liked this story.. [optional]  # noqa: E501
            previews ([StoryResponsePreviewsInner]): *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.*. [optional]  # noqa: E501
            old_name (str): *Conditional*'. [optional]  # noqa: E501
            new_name (str): *Conditional*. [optional]  # noqa: E501
            old_dates (StoryResponseOldDates): [optional]  # noqa: E501
            new_dates (StoryResponseOldDates): [optional]  # noqa: E501
            old_resource_subtype (str): *Conditional*. [optional]  # noqa: E501
            new_resource_subtype (str): *Conditional*. [optional]  # noqa: E501
            story (StoryResponseStory): [optional]  # noqa: E501
            assignee (StoryResponseAssignee): [optional]  # noqa: E501
            follower (StoryResponseAssignee): [optional]  # noqa: E501
            old_section (StoryResponseOldSection): [optional]  # noqa: E501
            new_section (StoryResponseOldSection): [optional]  # noqa: E501
            task (StoryResponseTask): [optional]  # noqa: E501
            project (StoryResponseProject): [optional]  # noqa: E501
            tag (StoryResponseTag): [optional]  # noqa: E501
            custom_field (StoryResponseCustomField): [optional]  # noqa: E501
            old_text_value (str): *Conditional*. [optional]  # noqa: E501
            new_text_value (str): *Conditional*. [optional]  # noqa: E501
            old_number_value (int): *Conditional*. [optional]  # noqa: E501
            new_number_value (int): *Conditional*. [optional]  # noqa: E501
            old_enum_value (StoryResponseOldEnumValue): [optional]  # noqa: E501
            new_enum_value (StoryResponseOldEnumValue): [optional]  # noqa: E501
            old_date_value (StoryResponseOldDateValue): [optional]  # noqa: E501
            new_date_value (StoryResponseNewDateValue): [optional]  # noqa: E501
            old_people_value ([CustomFieldResponsePeopleValueInner]): *Conditional*. The old value of a people custom field story.. [optional]  # noqa: E501
            new_people_value ([CustomFieldResponsePeopleValueInner]): *Conditional*. The new value of a people custom field story.. [optional]  # noqa: E501
            old_multi_enum_values ([CustomFieldBaseEnumOptionsInner]): *Conditional*. The old value of a multi-enum custom field story.. [optional]  # noqa: E501
            new_multi_enum_values ([CustomFieldBaseEnumOptionsInner]): *Conditional*. The new value of a multi-enum custom field story.. [optional]  # noqa: E501
            new_approval_status (str): *Conditional*. The new value of approval status.. [optional]  # noqa: E501
            old_approval_status (str): *Conditional*. The old value of approval status.. [optional]  # noqa: E501
            duplicate_of (StoryResponseTask): [optional]  # noqa: E501
            duplicated_from (StoryResponseTask): [optional]  # noqa: E501
            dependency (StoryResponseTask): [optional]  # noqa: E501
            source (str): The component of the Asana product the user used to trigger the story.. [optional]  # noqa: E501
            target (StoryResponseTarget): [optional]  # noqa: E501
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
