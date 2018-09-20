

import pprint
import re  # noqa: F401

import six


class ExchangeRateRequest(object):

    from_amount=None
    from_currency=None
    to_country=None
    to_currency=None
    to_amount=None
    recipient_account_email=None
    
    
    
    
    def __init__(self, from_amount=None, from_currency=None, recipient_account_email=None, to_amount=None, to_country=None, to_currency=None):
        if to_amount is not None:
            self.to_amount=to_amount
        if from_amount is not None:
           self.from_amount=from_amount
        if from_currency is not None:
            self.from_currency=from_currency
        if to_currency is not None:
            self.to_currency=to_currency
        if to_country is not None:
            self.to_country=to_country
        if recipient_account_email is not None:
           self.recipient_account_email=recipient_account_email
        
        
    '''@property
    def from_amount(self):
        """Gets the from_amount of this ExchangeRateRequest.  # noqa: E501

        The source amount, either `from` or `to` amount is allowed, the other one is calculated  # noqa: E501

        :return: The from_amount of this ExchangeRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._from_amount

    @from_amount.setter
    def from_amount(self, from_amount):
        """Sets the from_amount of this ExchangeRateRequest.

        The source amount, either `from` or `to` amount is allowed, the other one is calculated  # noqa: E501

        :param from_amount: The from_amount of this ExchangeRateRequest.  # noqa: E501
        :type: float
        """

        self._from_amount = from_amount

    @property
    def from_currency(self):
        """Gets the from_currency of this ExchangeRateRequest.  # noqa: E501

        The source currency  # noqa: E501

        :return: The from_currency of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_currency

    @from_currency.setter
    def from_currency(self, from_currency):
        """Sets the from_currency of this ExchangeRateRequest.

        The source currency  # noqa: E501

        :param from_currency: The from_currency of this ExchangeRateRequest.  # noqa: E501
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
    def recipient_account_email(self):
        """Gets the recipient_account_email of this ExchangeRateRequest.  # noqa: E501

        The email of recipient to get discounted rate  # noqa: E501

        :return: The recipient_account_email of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_account_email

    @recipient_account_email.setter
    def recipient_account_email(self, recipient_account_email):
        """Sets the recipient_account_email of this ExchangeRateRequest.

        The email of recipient to get discounted rate  # noqa: E501

        :param recipient_account_email: The recipient_account_email of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """

        self._recipient_account_email = recipient_account_email

    @property
    def to_amount(self):
        """Gets the to_amount of this ExchangeRateRequest.  # noqa: E501

        The target amount, either `from` or `to` amount is allowed, the other one is calculated  # noqa: E501

        :return: The to_amount of this ExchangeRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._to_amount

    @to_amount.setter
    def to_amount(self, to_amount):
        """Sets the to_amount of this ExchangeRateRequest.

        The target amount, either `from` or `to` amount is allowed, the other one is calculated  # noqa: E501

        :param to_amount: The to_amount of this ExchangeRateRequest.  # noqa: E501
        :type: float
        """

        self._to_amount = to_amount

    @property
    def to_country(self):
        """Gets the to_country of this ExchangeRateRequest.  # noqa: E501

        The destination country to ensure Veem can support transfer to  # noqa: E501

        :return: The to_country of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_country

    @to_country.setter
    def to_country(self, to_country):
        """Sets the to_country of this ExchangeRateRequest.

        The destination country to ensure Veem can support transfer to  # noqa: E501

        :param to_country: The to_country of this ExchangeRateRequest.  # noqa: E501
        :type: str
        """
        if to_country is None:
            raise ValueError("Invalid value for `to_country`, must not be `None`")  # noqa: E501
        allowed_values = ["UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"]  # noqa: E501
        if to_country not in allowed_values:
            raise ValueError(
                "Invalid value for `to_country` ({0}), must be one of {1}"  # noqa: E501
                .format(to_country, allowed_values)
            )

        self._to_country = to_country

    @property
    def to_currency(self):
        """Gets the to_currency of this ExchangeRateRequest.  # noqa: E501

        The target currency  # noqa: E501

        :return: The to_currency of this ExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_currency

    @to_currency.setter
    def to_currency(self, to_currency):
        """Sets the to_currency of this ExchangeRateRequest.

        The target currency  # noqa: E501

        :param to_currency: The to_currency of this ExchangeRateRequest.  # noqa: E501
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

        self._to_currency = to_currency'''

    def to_dict(self):
        """Returns the model properties as a dict"""
        
        result = {}

        if self.to_amount is not None:
            result['toAmount']=self.to_amount
        if self.from_amount is not None:
            result['fromAmount']=self.from_amount
        if self.from_currency is not None:
            result['fromCurrency']=self.from_currency
        if self.to_currency is not None:
            result['toCurrency']=self.to_currency
        if self.to_country is not None:
            result['toCountry']=self.to_country
        if self.recipient_account_email is not None:
            result['recipientAccountEmail']=self.recipient_account_email
            
        
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExchangeRateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
