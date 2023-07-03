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

class ProjectStatusBase(object):
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
        'color': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'title': 'title',
        'text': 'text',
        'html_text': 'html_text',
        'color': 'color'
    }

    def __init__(self, gid=None, resource_type=None, title=None, text=None, html_text=None, color=None):  # noqa: E501
        """ProjectStatusBase - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._title = None
        self._text = None
        self._html_text = None
        self._color = None
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

    @property
    def gid(self):
        """Gets the gid of this ProjectStatusBase.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectStatusBase.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectStatusBase.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectStatusBase.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectStatusBase.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectStatusBase.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def title(self):
        """Gets the title of this ProjectStatusBase.  # noqa: E501

        The title of the project status update.  # noqa: E501

        :return: The title of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectStatusBase.

        The title of the project status update.  # noqa: E501

        :param title: The title of this ProjectStatusBase.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this ProjectStatusBase.  # noqa: E501

        The text content of the status update.  # noqa: E501

        :return: The text of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ProjectStatusBase.

        The text content of the status update.  # noqa: E501

        :param text: The text of this ProjectStatusBase.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def html_text(self):
        """Gets the html_text of this ProjectStatusBase.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML.  # noqa: E501

        :return: The html_text of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._html_text

    @html_text.setter
    def html_text(self, html_text):
        """Sets the html_text of this ProjectStatusBase.

        [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML.  # noqa: E501

        :param html_text: The html_text of this ProjectStatusBase.  # noqa: E501
        :type: str
        """

        self._html_text = html_text

    @property
    def color(self):
        """Gets the color of this ProjectStatusBase.  # noqa: E501

        The color associated with the status update.  # noqa: E501

        :return: The color of this ProjectStatusBase.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectStatusBase.

        The color associated with the status update.  # noqa: E501

        :param color: The color of this ProjectStatusBase.  # noqa: E501
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
        if issubclass(ProjectStatusBase, dict):
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
        if not isinstance(other, ProjectStatusBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
