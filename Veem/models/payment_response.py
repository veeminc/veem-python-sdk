

import pprint
import re  # noqa: F401

import six




class PaymentResponse(object):
    
    request_id=None
    attachments_type=None
    attachments_name=None
    attachments_referenceId=None
    payee_email=None
    payee_countryCode=None
    payee_phone=None
    payeeAmount_number=None
    payeeAmount_currency=None
    status=None
    id=None
    exchangeRate_fromAmount=None
    exchangeRate_toAmount=None
    exchangeRate_fromCurrency=None
    exchangeRate_toCurrency=None
    exchangeRate_rate=None
    claim_link=None
    
    def __init__(self, request_id=None, attachments_type=None, attachments_name=None, attachments_reference_id=None, payee_email=None, payee_country_code=None, payee_phone=None, payee_amount_number=None, payee_amount_currency=None, status=None, id=None, exchange_rate_from_amount=None,exchange_rate_to_amount=None,exchange_rate_from_currency=None, exchange_rate_to_currency=None,exchange_rate_rate=None, claim_link=None):   
        if request_id is not None:
           self.request_id=request_id
        if attachments_type is not None:
            self.attachments.type=attachments_type
        if attachments_name is not None:
            self.attachments.name=attachments_name
        if attachments_reference_id is not None:
            self.attachments.referenceId=attachments_reference_id
        if payee_email is not None:
            self.payee_email=payee_email
        if payee_country_code is not None:
            self.payee_countryCode=payee_country_code
        if payee_phone is not None:
            self.payee_phone=payee_phone
        if payee_amount_number is not None:
            self.payeeAmount_number=payee_amount_number
        if payee_amount_currency is not None:
            self.payeeAmount_currency=payee_amount_currency
        if status is not None:
            self.status=status
        if id is not None:
            self.id=id
        if exchange_rate_from_amount is not None:
            self.exchangeRate_fromAmount=exchange_rate_from_amount
        if exchange_rate_to_amount is not None:
            self.exchangeRate_toAmount=exchange_rate_to_amount
        if exchange_rate_from_currency is not None:
            self.exchangeRate_fromCurrency=exchange_rate_from_currency
        if exchange_rate_to_currency is not None:
            self.exchangeRate_toCurrency=exchange_rate_to_currency
        if exchange_rate_rate is not None:
            self.exchangeRate_rate=exchange_rate_rate
        if claim_link is not None:
            self.claim_link=claim_link
        
    '''@property
    def amount(self): 
        """Gets the amount of this PaymentResponse.  # noqa: E501

        The amount and currency of the payment  # noqa: E501

        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: AlignMonetaryAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.

        The amount and currency of the payment  # noqa: E501

        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: AlignMonetaryAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def attachments(self):
        """Gets the attachments of this PaymentResponse.  # noqa: E501

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :return: The attachments of this PaymentResponse.  # noqa: E501
        :rtype: list[FileAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this PaymentResponse.

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :param attachments: The attachments of this PaymentResponse.  # noqa: E501
        :type: list[FileAttachment]
        """

        self._attachments = attachments

    @property
    def cc_emails(self):
        """Gets the cc_emails of this PaymentResponse.  # noqa: E501

        The list of emails who will be notified about the payment  # noqa: E501

        :return: The cc_emails of this PaymentResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc_emails

    @cc_emails.setter
    def cc_emails(self, cc_emails):
        """Sets the cc_emails of this PaymentResponse.

        The list of emails who will be notified about the payment  # noqa: E501

        :param cc_emails: The cc_emails of this PaymentResponse.  # noqa: E501
        :type: list[str]
        """

        self._cc_emails = cc_emails

    @property
    def claim_link(self):
        """Gets the claim_link of this PaymentResponse.  # noqa: E501

        The link that allows the recipient to claim the payment  # noqa: E501

        :return: The claim_link of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._claim_link

    @claim_link.setter
    def claim_link(self, claim_link):
        """Sets the claim_link of this PaymentResponse.

        The link that allows the recipient to claim the payment  # noqa: E501

        :param claim_link: The claim_link of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._claim_link = claim_link

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PaymentResponse.  # noqa: E501

        The exchange rate used associated with the payment  # noqa: E501

        :return: The exchange_rate of this PaymentResponse.  # noqa: E501
        :rtype: ExchangeRateResponse
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PaymentResponse.

        The exchange rate used associated with the payment  # noqa: E501

        :param exchange_rate: The exchange_rate of this PaymentResponse.  # noqa: E501
        :type: ExchangeRateResponse
        """
        if exchange_rate is None:
            raise ValueError("Invalid value for `exchange_rate`, must not be `None`")  # noqa: E501

        self._exchange_rate = exchange_rate

    @property
    def exchange_rate_quote_id(self):
        """Gets the exchange_rate_quote_id of this PaymentResponse.  # noqa: E501

        The quote id that was received earlier for the payment  # noqa: E501

        :return: The exchange_rate_quote_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate_quote_id

    @exchange_rate_quote_id.setter
    def exchange_rate_quote_id(self, exchange_rate_quote_id):
        """Sets the exchange_rate_quote_id of this PaymentResponse.

        The quote id that was received earlier for the payment  # noqa: E501

        :param exchange_rate_quote_id: The exchange_rate_quote_id of this PaymentResponse.  # noqa: E501
        :type: str
        """
        if exchange_rate_quote_id is None:
            raise ValueError("Invalid value for `exchange_rate_quote_id`, must not be `None`")  # noqa: E501

        self._exchange_rate_quote_id = exchange_rate_quote_id

    @property
    def external_invoice_ref_id(self):
        """Gets the external_invoice_ref_id of this PaymentResponse.  # noqa: E501

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :return: The external_invoice_ref_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_invoice_ref_id

    @external_invoice_ref_id.setter
    def external_invoice_ref_id(self, external_invoice_ref_id):
        """Sets the external_invoice_ref_id of this PaymentResponse.

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :param external_invoice_ref_id: The external_invoice_ref_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._external_invoice_ref_id = external_invoice_ref_id

    @property
    def id(self):
        """Gets the id of this PaymentResponse.  # noqa: E501

        The payment id  # noqa: E501

        :return: The id of this PaymentResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponse.

        The payment id  # noqa: E501

        :param id: The id of this PaymentResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def notes(self):
        """Gets the notes of this PaymentResponse.  # noqa: E501

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :return: The notes of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PaymentResponse.

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :param notes: The notes of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def payee(self):
        """Gets the payee of this PaymentResponse.  # noqa: E501

        The receiver of the payment  # noqa: E501

        :return: The payee of this PaymentResponse.  # noqa: E501
        :rtype: SimpleAccount
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this PaymentResponse.

        The receiver of the payment  # noqa: E501

        :param payee: The payee of this PaymentResponse.  # noqa: E501
        :type: SimpleAccount
        """
        if payee is None:
            raise ValueError("Invalid value for `payee`, must not be `None`")  # noqa: E501

        self._payee = payee

    @property
    def payee_amount(self):
        """Gets the payee_amount of this PaymentResponse.  # noqa: E501

        The receiving amount and currency of the payment. Deprecated please use amount instead  # noqa: E501

        :return: The payee_amount of this PaymentResponse.  # noqa: E501
        :rtype: AlignMonetaryAmount
        """
        return self._payee_amount

    @payee_amount.setter
    def payee_amount(self, payee_amount):
        """Sets the payee_amount of this PaymentResponse.

        The receiving amount and currency of the payment. Deprecated please use amount instead  # noqa: E501

        :param payee_amount: The payee_amount of this PaymentResponse.  # noqa: E501
        :type: AlignMonetaryAmount
        """

        self._payee_amount = payee_amount

    @property
    def purpose_of_payment(self):
        """Gets the purpose_of_payment of this PaymentResponse.  # noqa: E501

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :return: The purpose_of_payment of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._purpose_of_payment

    @purpose_of_payment.setter
    def purpose_of_payment(self, purpose_of_payment):
        """Sets the purpose_of_payment of this PaymentResponse.

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :param purpose_of_payment: The purpose_of_payment of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Goods", "Services", "Charitable", "Other"]  # noqa: E501
        if purpose_of_payment not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose_of_payment` ({0}), must be one of {1}"  # noqa: E501
                .format(purpose_of_payment, allowed_values)
            )

        self._purpose_of_payment = purpose_of_payment

    @property
    def push_payment_info(self):
        """Gets the push_payment_info of this PaymentResponse.  # noqa: E501

        Bank account information for push payment (if required)  # noqa: E501

        :return: The push_payment_info of this PaymentResponse.  # noqa: E501
        :rtype: PushPaymentInfoResponse
        """
        return self._push_payment_info

    @push_payment_info.setter
    def push_payment_info(self, push_payment_info):
        """Sets the push_payment_info of this PaymentResponse.

        Bank account information for push payment (if required)  # noqa: E501

        :param push_payment_info: The push_payment_info of this PaymentResponse.  # noqa: E501
        :type: PushPaymentInfoResponse
        """

        self._push_payment_info = push_payment_info

    @property
    def status(self):
        """Gets the status of this PaymentResponse.  # noqa: E501

        The status of the payment  # noqa: E501

        :return: The status of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponse.

        The status of the payment  # noqa: E501

        :param status: The status of this PaymentResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Drafted", "Sent", "Claimed", "PendingAuth", "Authorized", "InProgress", "Complete", "Cancelled", "Closed", "Reversed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def time_created(self):
        """Gets the time_created of this PaymentResponse.  # noqa: E501

        The creation time of the payment. The format would be UTC, ISO-8601  # noqa: E501

        :return: The time_created of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this PaymentResponse.

        The creation time of the payment. The format would be UTC, ISO-8601  # noqa: E501

        :param time_created: The time_created of this PaymentResponse.  # noqa: E501
        :type: datetime
        """
        if time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created'''

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
        if not isinstance(other, PaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
