

import pprint
import re  # noqa: F401

import six


class ContactResponse(object):
    batch_id=None
    total_items=None
    processed_items=None
    has_errors=None
    status=None
    batch_items=None

    def __init__(self, batchItems=None, batchId=None, totalItems=None, processedItems=None, hasErrors=None, status=None):  # noqa: E501
        if batchItems is not None:
            self.batch_items=batchItems
        if batchId is not None:
            self.batch_id=batchId
        if totalItems is not None:
            self.total_items=totalItems
        if processedItems is not None:
            self.processed_items=processedItems
        if hasErrors is not None:
            self.has_errors=hasErrors
        if status is not None:
            self.status=status

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContactResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
