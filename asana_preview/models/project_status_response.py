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

class ProjectStatusResponse(object):
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
        'text': 'str',
        'html_text': 'str',
        'color': 'str',
        'author': 'CustomFieldResponsePeopleValue',
        'created_at': 'datetime',
        'created_by': 'CustomFieldResponsePeopleValue',
        'modified_at': 'datetime'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'title': 'title',
        'text': 'text',
        'html_text': 'html_text',
        'color': 'color',
        'author': 'author',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'modified_at': 'modified_at'
    }

    def __init__(self, gid=None, resource_type=None, title=None, text=None, html_text=None, color=None, author=None, created_at=None, created_by=None, modified_at=None):  # noqa: E501
        """ProjectStatusResponse - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._title = None
        self._text = None
        self._html_text = None
        self._color = None
        self._author = None
        self._created_at = None
        self._created_by = None
        self._modified_at = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if title is not None:
            self.title = title
        self.text = text
        if html_text is not None:
            self.html_text = html_text
        self.color = color
        if author is not None:
            self.author = author
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def gid(self):
        """Gets the gid of this ProjectStatusResponse.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectStatusResponse.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectStatusResponse.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectStatusResponse.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def title(self):
        """Gets the title of this ProjectStatusResponse.  # noqa: E501

        The title of the project status update.  # noqa: E501

        :return: The title of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectStatusResponse.

        The title of the project status update.  # noqa: E501

        :param title: The title of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this ProjectStatusResponse.  # noqa: E501

        The text content of the status update.  # noqa: E501

        :return: The text of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ProjectStatusResponse.

        The text content of the status update.  # noqa: E501

        :param text: The text of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def html_text(self):
        """Gets the html_text of this ProjectStatusResponse.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML.  # noqa: E501

        :return: The html_text of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._html_text

    @html_text.setter
    def html_text(self, html_text):
        """Sets the html_text of this ProjectStatusResponse.

        [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML.  # noqa: E501

        :param html_text: The html_text of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """

        self._html_text = html_text

    @property
    def color(self):
        """Gets the color of this ProjectStatusResponse.  # noqa: E501

        The color associated with the status update.  # noqa: E501

        :return: The color of this ProjectStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectStatusResponse.

        The color associated with the status update.  # noqa: E501

        :param color: The color of this ProjectStatusResponse.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501
        allowed_values = ["green", "yellow", "red", "blue"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def author(self):
        """Gets the author of this ProjectStatusResponse.  # noqa: E501


        :return: The author of this ProjectStatusResponse.  # noqa: E501
        :rtype: CustomFieldResponsePeopleValue
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ProjectStatusResponse.


        :param author: The author of this ProjectStatusResponse.  # noqa: E501
        :type: CustomFieldResponsePeopleValue
        """

        self._author = author

    @property
    def created_at(self):
        """Gets the created_at of this ProjectStatusResponse.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this ProjectStatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProjectStatusResponse.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this ProjectStatusResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this ProjectStatusResponse.  # noqa: E501


        :return: The created_by of this ProjectStatusResponse.  # noqa: E501
        :rtype: CustomFieldResponsePeopleValue
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ProjectStatusResponse.


        :param created_by: The created_by of this ProjectStatusResponse.  # noqa: E501
        :type: CustomFieldResponsePeopleValue
        """

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this ProjectStatusResponse.  # noqa: E501

        The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.*  # noqa: E501

        :return: The modified_at of this ProjectStatusResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ProjectStatusResponse.

        The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.*  # noqa: E501

        :param modified_at: The modified_at of this ProjectStatusResponse.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

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
        if issubclass(ProjectStatusResponse, dict):
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
        if not isinstance(other, ProjectStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other