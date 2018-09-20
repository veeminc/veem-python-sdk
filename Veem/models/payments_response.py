

import pprint
import re  # noqa: F401

import six


class PaymentsResponse(object):
    content=None
    total_elements=None
    total_pages=None
    last=None
    sort=None
    first=None
    number_of_elements=None
    size=None
    number=None
   
    
    def __init__(self, content=None, totalElements=None, totalPages=None, last=None, sort=None, first=None, numberOfElements=None, size=None, number=None):  
        

        if content is not None:
            self.content=content
        if totalElements is not None:
           self.total_elements=totalElements
        if totalPages is not None:
            self.total_pages=totalPages
        if last is not None:
            self.last=last
        if sort is not None:
            self.sort=sort
        if first is not None:
           self.first=first
        if numberOfElements is not None:
           self.number_of_elements=numberOfElements
        if size is not None:
            self.size=size
        if number is not None:
            self.number=number
       

   

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
        if not isinstance(other, CustomerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == ot