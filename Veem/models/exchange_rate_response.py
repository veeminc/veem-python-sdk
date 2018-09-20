

import pprint
import re  # noqa: F401

import six


class ExchangeRateResponse(object):
    to_amount=None
    from_amount=None
    from_currency=None
    expiry=None
    to_currency=None
    id=None
    rate=None
   
    

    def __init__(self, expiry=None, from_amount=None, from_currency=None, id=None, rate=None, time_created=None, to_amount=None, to_currency=None):  
        

        if to_amount is not None:
            self.to_amount=to_amount
        if from_amount is not None:
           self.from_amount=from_amount
        if from_currency is not None:
            self.from_currency=from_currency
        if to_currency is not None:
            self.to_currency=to_currency
        if id is not None:
            self.id=id
        if rate is not None:
           self.rate=rate
        if expiry is not None:
           self.expiry=expiry
       

    @property
    def expiry(self):
        """Gets the expiry of this ExchangeRateResponse.  # noqa: E501

        The expiry time of the current rate quote  # noqa: E501

        :return: The expiry of this ExchangeRateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this ExchangeRateResponse.

        The expiry time of the current rate quote  # noqa: E501

        :param expiry: The expiry of this ExchangeRateResponse.  # noqa: E501
        :type: datetime
        """
        if expiry is None:
            raise ValueError("Invalid value for `expiry`, must not be `None`")  # noqa: E501

        self._expiry = expiry

    @property
    def from_amount(self):
        """Gets the from_amount of this ExchangeRateResponse.  # noqa: E501

        The source amount, either from or to amount is allowed, the other one is calculated  # noqa: E501

        :return: The from_amount of this ExchangeRateResponse.  # noqa: E501
        :rtype: float
        """
        return self._from_amount

    @from_amount.setter
    def from_amount(self, from_amount):
        """Sets the from_amount of this ExchangeRateResponse.

        The source amount, either from or to amount is allowed, the other one is calculated  # noqa: E501

        :param from_amount: The from_amount of this ExchangeRateResponse.  # noqa: E501
        :type: float
        """

        self._from_amount = from_amount

    @property
    def from_currency(self):
        """Gets the from_currency of this ExchangeRateResponse.  # noqa: E501

        The source currency  # noqa: E501

        :return: The from_currency of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._from_currency

    @from_currency.setter
    def from_currency(self, from_currency):
        """Sets the from_currency of this ExchangeRateResponse.

        The source currency  # noqa: E501

        :param from_currency: The from_currency of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """
        if from_currency is None:
            raise ValueError("Invalid value for `from_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if from_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `from_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(from_currency, allowed_values)
            )

        self._from_currency = from_currency

    @property
    def id(self):
        """Gets the id of this ExchangeRateResponse.  # noqa: E501

        The quote id  # noqa: E501

        :return: The id of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExchangeRateResponse.

        The quote id  # noqa: E501

        :param id: The id of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def rate(self):
        """Gets the rate of this ExchangeRateResponse.  # noqa: E501

        The Veem exchange rate for current transfer  # noqa: E501

        :return: The rate of this ExchangeRateResponse.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ExchangeRateResponse.

        The Veem exchange rate for current transfer  # noqa: E501

        :param rate: The rate of this ExchangeRateResponse.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def time_created(self):
        """Gets the time_created of this ExchangeRateResponse.  # noqa: E501

        The quote generation time  # noqa: E501

        :return: The time_created of this ExchangeRateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this ExchangeRateResponse.

        The quote generation time  # noqa: E501

        :param time_created: The time_created of this ExchangeRateResponse.  # noqa: E501
        :type: datetime
        """
        if time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created

    @property
    def to_amount(self):
        """Gets the to_amount of this ExchangeRateResponse.  # noqa: E501

        The target amount, either from or to amount is allowed, the other one is calculated  # noqa: E501

        :return: The to_amount of this ExchangeRateResponse.  # noqa: E501
        :rtype: float
        """
        return self._to_amount

    @to_amount.setter
    def to_amount(self, to_amount):
        """Sets the to_amount of this ExchangeRateResponse.

        The target amount, either from or to amount is allowed, the other one is calculated  # noqa: E501

        :param to_amount: The to_amount of this ExchangeRateResponse.  # noqa: E501
        :type: float
        """
        if to_amount is None:
            raise ValueError("Invalid value for `to_amount`, must not be `None`")  # noqa: E501

        self._to_amount = to_amount

    @property
    def to_currency(self):
        """Gets the to_currency of this ExchangeRateResponse.  # noqa: E501

        The target currency  # noqa: E501

        :return: The to_currency of this ExchangeRateResponse.  # noqa: E501
        :rtype: str
        """
        return self._to_currency

    @to_currency.setter
    def to_currency(self, to_currency):
        """Sets the to_currency of this ExchangeRateResponse.

        The target currency  # noqa: E501

        :param to_currency: The to_currency of this ExchangeRateResponse.  # noqa: E501
        :type: str
        """
        if to_currency is None:
            raise ValueError("Invalid value for `to_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if to_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `to_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(to_currency, allowed_values)
            )

        self._to_currency = to_currency

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
        if not isinstance(other, ExchangeRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
