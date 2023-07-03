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

class PortfolioAddItemRequest(object):
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
        'item': 'str',
        'insert_before': 'str',
        'insert_after': 'str'
    }

    attribute_map = {
        'item': 'item',
        'insert_before': 'insert_before',
        'insert_after': 'insert_after'
    }

    def __init__(self, item=None, insert_before=None, insert_after=None):  # noqa: E501
        """PortfolioAddItemRequest - a model defined in Swagger"""  # noqa: E501
        self._item = None
        self._insert_before = None
        self._insert_after = None
        self.discriminator = None
        self.item = item
        if insert_before is not None:
            self.insert_before = insert_before
        if insert_after is not None:
            self.insert_after = insert_after

    @property
    def item(self):
        """Gets the item of this PortfolioAddItemRequest.  # noqa: E501

        The item to add to the portfolio.  # noqa: E501

        :return: The item of this PortfolioAddItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this PortfolioAddItemRequest.

        The item to add to the portfolio.  # noqa: E501

        :param item: The item of this PortfolioAddItemRequest.  # noqa: E501
        :type: str
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def insert_before(self):
        """Gets the insert_before of this PortfolioAddItemRequest.  # noqa: E501

        An id of an item in this portfolio. The new item will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :return: The insert_before of this PortfolioAddItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_before

    @insert_before.setter
    def insert_before(self, insert_before):
        """Sets the insert_before of this PortfolioAddItemRequest.

        An id of an item in this portfolio. The new item will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :param insert_before: The insert_before of this PortfolioAddItemRequest.  # noqa: E501
        :type: str
        """

        self._insert_before = insert_before

    @property
    def insert_after(self):
        """Gets the insert_after of this PortfolioAddItemRequest.  # noqa: E501

        An id of an item in this portfolio. The new item will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :return: The insert_after of this PortfolioAddItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this PortfolioAddItemRequest.

        An id of an item in this portfolio. The new item will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :param insert_after: The insert_after of this PortfolioAddItemRequest.  # noqa: E501
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
        if issubclass(PortfolioAddItemRequest, dict):
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
        if not isinstance(other, PortfolioAddItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
