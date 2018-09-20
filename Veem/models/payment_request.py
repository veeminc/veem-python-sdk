
import pprint
import re  # noqa: F401

import six




class PaymentRequest(object):
    amount=None
    payee=None
    payee_amount=None
    purpose_of_payment=None
    attachments=None
    approve_automatically=None
    cc_emails=None
    exchange_rate=None
    exchange_rate_quote_id=None
    external_invoice_ref_id=None
    notes=None
    

    def __init__(self, amount=None, approve_automatically=None, attachments=None, cc_emails=None, exchange_rate=None, exchange_rate_quote_id=None, external_invoice_ref_id=None, notes=None, payee=None, payee_amount=None, purpose_of_payment=None):  # noqa: E501
        if amount is not None:
            self.amount = amount
        if approve_automatically is not None:
            self.approve_automatically = approve_automatically
        if attachments is not None:
            self.attachments = attachments
        if cc_emails is not None:
            self.cc_emails = cc_emails
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if exchange_rate_quote_id is not None:
            self.exchange_rate_quote_id = exchange_rate_quote_id
        if external_invoice_ref_id is not None:
            self.external_invoice_ref_id = external_invoice_ref_id
        if notes is not None:
            self.notes = notes
        if payee is not None:
            self.payee = payee
        if payee_amount is not None:
            self.payee_amount = payee_amount
        if purpose_of_payment is not None:
            self.purpose_of_payment = purpose_of_payment

    '''@property
    def amount(self):
        """Gets the amount of this PaymentRequest.  # noqa: E501

        The amount and currency of the payment  # noqa: E501

        :return: The amount of this PaymentRequest.  # noqa: E501
        :rtype: AlignMonetaryAmount
        """
        return self.amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequest.

        The amount and currency of the payment  # noqa: E501

        :param amount: The amount of this PaymentRequest.  # noqa: E501
        :type: AlignMonetaryAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self.amount = amount

    @property
    def approve_automatically(self):
        """Gets the approve_automatically of this PaymentRequest.  # noqa: E501

        Whether to automatically move the payment from drafted  # noqa: E501

        :return: The approve_automatically of this PaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self.approve_automatically

    @approve_automatically.setter
    def approve_automatically(self, approve_automatically):
        """Sets the approve_automatically of this PaymentRequest.

        Whether to automatically move the payment from drafted  # noqa: E501

        :param approve_automatically: The approve_automatically of this PaymentRequest.  # noqa: E501
        :type: bool
        """

        self.approve_automatically = approve_automatically

    @property
    def attachments(self):
        """Gets the attachments of this PaymentRequest.  # noqa: E501

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :return: The attachments of this PaymentRequest.  # noqa: E501
        :rtype: list[FileAttachment]
        """
        return self.attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this PaymentRequest.

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :param attachments: The attachments of this PaymentRequest.  # noqa: E501
        :type: list[FileAttachment]
        """

        self.attachments = attachments

    @property
    def cc_emails(self):
        """Gets the cc_emails of this PaymentRequest.  # noqa: E501

        The list of emails who will be notified about the payment  # noqa: E501

        :return: The cc_emails of this PaymentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self.cc_emails

    @cc_emails.setter
    def cc_emails(self, cc_emails):
        """Sets the cc_emails of this PaymentRequest.

        The list of emails who will be notified about the payment  # noqa: E501

        :param cc_emails: The cc_emails of this PaymentRequest.  # noqa: E501
        :type: list[str]
        """

        self.cc_emails = cc_emails

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PaymentRequest.  # noqa: E501


        :return: The exchange_rate of this PaymentRequest.  # noqa: E501
        :rtype: ExchangeRateResponse
        """
        return self.exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PaymentRequest.


        :param exchange_rate: The exchange_rate of this PaymentRequest.  # noqa: E501
        :type: ExchangeRateResponse
        """

        self.exchange_rate = exchange_rate

    @property
    def exchange_rate_quote_id(self):
        """Gets the exchange_rate_quote_id of this PaymentRequest.  # noqa: E501

        The quote id that was received earlier for the payment  # noqa: E501

        :return: The exchange_rate_quote_id of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self.exchange_rate_quote_id

    @exchange_rate_quote_id.setter
    def exchange_rate_quote_id(self, exchange_rate_quote_id):
        """Sets the exchange_rate_quote_id of this PaymentRequest.

        The quote id that was received earlier for the payment  # noqa: E501

        :param exchange_rate_quote_id: The exchange_rate_quote_id of this PaymentRequest.  # noqa: E501
        :type: str
        """
        if exchange_rate_quote_id is None:
            raise ValueError("Invalid value for `exchange_rate_quote_id`, must not be `None`")  # noqa: E501

        self.exchange_rate_quote_id = exchange_rate_quote_id

    @property
    def external_invoice_ref_id(self):
        """Gets the external_invoice_ref_id of this PaymentRequest.  # noqa: E501

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :return: The external_invoice_ref_id of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self.external_invoice_ref_id

    @external_invoice_ref_id.setter
    def external_invoice_ref_id(self, external_invoice_ref_id):
        """Sets the external_invoice_ref_id of this PaymentRequest.

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :param external_invoice_ref_id: The external_invoice_ref_id of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self.external_invoice_ref_id = external_invoice_ref_id

    @property
    def notes(self):
        """Gets the notes of this PaymentRequest.  # noqa: E501

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :return: The notes of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self.notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PaymentRequest.

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :param notes: The notes of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self.notes = notes

    @property
    def payee(self):
        """Gets the payee of this PaymentRequest.  # noqa: E501

        The receiver of the payment  # noqa: E501

        :return: The payee of this PaymentRequest.  # noqa: E501
        :rtype: SimpleAccount
        """
        return self.payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this PaymentRequest.

        The receiver of the payment  # noqa: E501

        :param payee: The payee of this PaymentRequest.  # noqa: E501
        :type: SimpleAccount
        """
        if payee is None:
            raise ValueError("Invalid value for `payee`, must not be `None`")  # noqa: E501

        self.payee = payee

    @property
    def payee_amount(self):
        """Gets the payee_amount of this PaymentRequest.  # noqa: E501

        The receiving amount and currency of the payment. Deprecated please use amount instead  # noqa: E501

        :return: The payee_amount of this PaymentRequest.  # noqa: E501
        :rtype: AlignMonetaryAmount
        """
        return self.payee_amount

    @payee_amount.setter
    def payee_amount(self, payee_amount):
        """Sets the payee_amount of this PaymentRequest.

        The receiving amount and currency of the payment. Deprecated please use amount instead  # noqa: E501

        :param payee_amount: The payee_amount of this PaymentRequest.  # noqa: E501
        :type: AlignMonetaryAmount
        """

        self.payee_amount = payee_amount

    @property
    def purpose_of_payment(self):
        """Gets the purpose_of_payment of this PaymentRequest.  # noqa: E501

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :return: The purpose_of_payment of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self.purpose_of_payment

    @purpose_of_payment.setter
    def purpose_of_payment(self, purpose_of_payment):
        """Sets the purpose_of_payment of this PaymentRequest.

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :param purpose_of_payment: The purpose_of_payment of this PaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Goods", "Services", "Charitable", "Other"]  # noqa: E501
        if purpose_of_payment not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose_of_payment` ({0}), must be one of {1}"  # noqa: E501
                .format(purpose_of_payment, allowed_values)
            )

        self.purpose_of_payment = purpose_of_payment
    '''
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if self.amount is not None:
            result['amount'] = self.amount
        if self.approve_automatically is not None:
            result['approveAutomatically'] = self.approve_automatically
        if self.attachments is not None:
            result['attachments'] = self.attachments
        if self.cc_emails is not None:
            result['ccEmails'] = self.cc_emails
        if self.exchange_rate is not None:
            result['exchangeRate'] = self.exchange_rate
        if self.exchange_rate_quote_id is not None:
            result['exchangeRateQuoteId'] = self.exchange_rate_quote_id
        if self.external_invoice_ref_id is not None:
            result['externalInvoiceRefId'] = self.external_invoice_ref_id
        if self.notes is not None:
            result['notes'] = self.notes
        if self.payee is not None:
            result['payee'] = self.payee
        if self.payee_amount is not None:
            result['payeeAmount'] = self.payee_amount
        if self.purpose_of_payment is not None:
            result['purposeOfPayment'] = self.purpose_of_payment
            
        
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentRequest):
            return False

        return self._dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
