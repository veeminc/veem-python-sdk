

import pprint
import re  

import six


class AttachmentRequest(object):
    
    def __init__(self):

        

    @property
    def business_name(self):
        """Gets the business_name of this SimpleAccount.  # noqa: E501

        The name of the receiver's business, required when account type is business  # noqa: E501

        :return: The business_name of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this SimpleAccount.

        The name of the receiver's business, required when account type is business  # noqa: E501

        :param business_name: The business_name of this SimpleAccount.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def country_code(self):
        """Gets the country_code of this SimpleAccount.  # noqa: E501

        The 2 letter ISO country codes,ISO Alpha-2  # noqa: E501

        :return: The country_code of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SimpleAccount.

        The 2 letter ISO country codes,ISO Alpha-2  # noqa: E501

        :param country_code: The country_code of this SimpleAccount.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        allowed_values = ["UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"]  # noqa: E501
        if country_code not in allowed_values:
            raise ValueError(
                "Invalid value for `country_code` ({0}), must be one of {1}"  # noqa: E501
                .format(country_code, allowed_values)
            )

        self._country_code = country_code

    @property
    def email(self):
        """Gets the email of this SimpleAccount.  # noqa: E501

        The email of the receiver  # noqa: E501

        :return: The email of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SimpleAccount.

        The email of the receiver  # noqa: E501

        :param email: The email of this SimpleAccount.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this SimpleAccount.  # noqa: E501

        The first name of the receiver  # noqa: E501

        :return: The first_name of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SimpleAccount.

        The first name of the receiver  # noqa: E501

        :param first_name: The first_name of this SimpleAccount.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SimpleAccount.  # noqa: E501

        The last name of the receiver  # noqa: E501

        :return: The last_name of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SimpleAccount.

        The last name of the receiver  # noqa: E501

        :param last_name: The last_name of this SimpleAccount.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def type(self):
        """Gets the type of this SimpleAccount.  # noqa: E501

        The type of the receiver  # noqa: E501

        :return: The type of this SimpleAccount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimpleAccount.

        The type of the receiver  # noqa: E501

        :param type: The type of this SimpleAccount.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Incomplete", "Business", "Personal"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, SimpleAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
