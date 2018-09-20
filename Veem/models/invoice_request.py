
import pprint
import re  # noqa: F401

import six




class InvoiceRequest(object):
    
    amount=None
    attachments=None
    cc_emails=None
    exchange_rate=None
    exchange_rate_quote_id=None
    external_invoice_ref_id=None
    notes=None
    payer=None
    purpose_of_payment=None
    
    def __init__(self, amount=None, attachments=None, cc_emails=None, exchange_rate=None, exchange_rate_quote_id=None, external_invoice_ref_id=None, notes=None, payer=None, purpose_of_payment=None):  # noqa: E501
        """InvoiceRequest - a model defined in Swagger"""  # noqa: E501

        if amount is not None:
            self.amount = amount
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
        if payer is not None:
            self.payer = payer
        if purpose_of_payment is not None:
            self.purpose_of_payment = purpose_of_payment

    '''@property
    def amount(self):
        """Gets the amount of this InvoiceRequest.  # noqa: E501

        The amount and currency of the payment  # noqa: E501

        :return: The amount of this InvoiceRequest.  # noqa: E501
        :rtype: AlignMonetaryAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceRequest.

        The amount and currency of the payment  # noqa: E501

        :param amount: The amount of this InvoiceRequest.  # noqa: E501
        :type: AlignMonetaryAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def attachments(self):
        """Gets the attachments of this InvoiceRequest.  # noqa: E501

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :return: The attachments of this InvoiceRequest.  # noqa: E501
        :rtype: list[FileAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this InvoiceRequest.

        The list of external invoices to be attached with payment. The files can be uploaded usingfile upload apis  # noqa: E501

        :param attachments: The attachments of this InvoiceRequest.  # noqa: E501
        :type: list[FileAttachment]
        """

        self._attachments = attachments

    @property
    def cc_emails(self):
        """Gets the cc_emails of this InvoiceRequest.  # noqa: E501

        The list of emails who will be notified about the payment  # noqa: E501

        :return: The cc_emails of this InvoiceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc_emails

    @cc_emails.setter
    def cc_emails(self, cc_emails):
        """Sets the cc_emails of this InvoiceRequest.

        The list of emails who will be notified about the payment  # noqa: E501

        :param cc_emails: The cc_emails of this InvoiceRequest.  # noqa: E501
        :type: list[str]
        """

        self._cc_emails = cc_emails

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this InvoiceRequest.  # noqa: E501


        :return: The exchange_rate of this InvoiceRequest.  # noqa: E501
        :rtype: ExchangeRateResponse
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this InvoiceRequest.


        :param exchange_rate: The exchange_rate of this InvoiceRequest.  # noqa: E501
        :type: ExchangeRateResponse
        """

        self._exchange_rate = exchange_rate

    @property
    def exchange_rate_quote_id(self):
        """Gets the exchange_rate_quote_id of this InvoiceRequest.  # noqa: E501

        The quote id that was received earlier for the payment  # noqa: E501

        :return: The exchange_rate_quote_id of this InvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate_quote_id

    @exchange_rate_quote_id.setter
    def exchange_rate_quote_id(self, exchange_rate_quote_id):
        """Sets the exchange_rate_quote_id of this InvoiceRequest.

        The quote id that was received earlier for the payment  # noqa: E501

        :param exchange_rate_quote_id: The exchange_rate_quote_id of this InvoiceRequest.  # noqa: E501
        :type: str
        """
        if exchange_rate_quote_id is None:
            raise ValueError("Invalid value for `exchange_rate_quote_id`, must not be `None`")  # noqa: E501

        self._exchange_rate_quote_id = exchange_rate_quote_id

    @property
    def external_invoice_ref_id(self):
        """Gets the external_invoice_ref_id of this InvoiceRequest.  # noqa: E501

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :return: The external_invoice_ref_id of this InvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_invoice_ref_id

    @external_invoice_ref_id.setter
    def external_invoice_ref_id(self, external_invoice_ref_id):
        """Sets the external_invoice_ref_id of this InvoiceRequest.

        The external invoice if for which payment is made, viewable by receiver  # noqa: E501

        :param external_invoice_ref_id: The external_invoice_ref_id of this InvoiceRequest.  # noqa: E501
        :type: str
        """

        self._external_invoice_ref_id = external_invoice_ref_id

    @property
    def notes(self):
        """Gets the notes of this InvoiceRequest.  # noqa: E501

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :return: The notes of this InvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InvoiceRequest.

        The memo/note associated with payment, viewable by receiver  # noqa: E501

        :param notes: The notes of this InvoiceRequest.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def payer(self):
        """Gets the payer of this InvoiceRequest.  # noqa: E501

        The sender of the payment  # noqa: E501

        :return: The payer of this InvoiceRequest.  # noqa: E501
        :rtype: SimpleAccount
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """Sets the payer of this InvoiceRequest.

        The sender of the payment  # noqa: E501

        :param payer: The payer of this InvoiceRequest.  # noqa: E501
        :type: SimpleAccount
        """
        if payer is None:
            raise ValueError("Invalid value for `payer`, must not be `None`")  # noqa: E501

        self._payer = payer

    @property
    def purpose_of_payment(self):
        """Gets the purpose_of_payment of this InvoiceRequest.  # noqa: E501

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :return: The purpose_of_payment of this InvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._purpose_of_payment

    @purpose_of_payment.setter
    def purpose_of_payment(self, purpose_of_payment):
        """Sets the purpose_of_payment of this InvoiceRequest.

        The purpose of payment required by banks for certain countries, applicable for following countries.SG,AE,KR,BR,CN,HK,HR,IS,ID,IN,IL,KE,PK,SA,ZA,TW,UA,VN  # noqa: E501

        :param purpose_of_payment: The purpose_of_payment of this InvoiceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Goods", "Services", "Charitable", "Other"]  # noqa: E501
        if purpose_of_payment not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose_of_payment` ({0}), must be one of {1}"  # noqa: E501
                .format(purpose_of_payment, allowed_values)
            )

        self._purpose_of_payment = purpose_of_payment'''

    def to_dict(self):
        result={}
        
        if self.amount is not None:
            result['amount'] = self.amount
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
        if self.payer is not None:
            result['payer'] = self.payer
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
        if not isinstance(other, InvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
