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

class UpdateTimeTrackingEntryRequest(object):
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
        'duration_minutes': 'int',
        'entered_on': 'date'
    }

    attribute_map = {
        'duration_minutes': 'duration_minutes',
        'entered_on': 'entered_on'
    }

    def __init__(self, duration_minutes=None, entered_on=None):  # noqa: E501
        """UpdateTimeTrackingEntryRequest - a model defined in Swagger"""  # noqa: E501
        self._duration_minutes = None
        self._entered_on = None
        self.discriminator = None
        if duration_minutes is not None:
            self.duration_minutes = duration_minutes
        if entered_on is not None:
            self.entered_on = entered_on

    @property
    def duration_minutes(self):
        """Gets the duration_minutes of this UpdateTimeTrackingEntryRequest.  # noqa: E501

        *Optional*. Time in minutes tracked by the entry  # noqa: E501

        :return: The duration_minutes of this UpdateTimeTrackingEntryRequest.  # noqa: E501
        :rtype: int
        """
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, duration_minutes):
        """Sets the duration_minutes of this UpdateTimeTrackingEntryRequest.

        *Optional*. Time in minutes tracked by the entry  # noqa: E501

        :param duration_minutes: The duration_minutes of this UpdateTimeTrackingEntryRequest.  # noqa: E501
        :type: int
        """

        self._duration_minutes = duration_minutes

    @property
    def entered_on(self):
        """Gets the entered_on of this UpdateTimeTrackingEntryRequest.  # noqa: E501

        *Optional*. The day that this entry is logged on. Defaults to today if no day specified  # noqa: E501

        :return: The entered_on of this UpdateTimeTrackingEntryRequest.  # noqa: E501
        :rtype: date
        """
        return self._entered_on

    @entered_on.setter
    def entered_on(self, entered_on):
        """Sets the entered_on of this UpdateTimeTrackingEntryRequest.

        *Optional*. The day that this entry is logged on. Defaults to today if no day specified  # noqa: E501

        :param entered_on: The entered_on of this UpdateTimeTrackingEntryRequest.  # noqa: E501
        :type: date
        """

        self._entered_on = entered_on

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
        if issubclass(UpdateTimeTrackingEntryRequest, dict):
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
        if not isinstance(other, UpdateTimeTrackingEntryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
