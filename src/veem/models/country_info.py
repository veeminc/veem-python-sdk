
from veem.models.base import Base
from veem.models.purpose_of_payment import PurposeOfPayment

from veem.utils import deseralize

class CountryInfo(Base):
    def __init__(self,
                 country=None,
                 sendingCurrencies=[],
                 receivingCurrencies=[],
                 purposeOfPaymentRequired=None,
                 invoiceAttachmentRequired=None,
                 bankFields=[],
                 purposeOfPaymentInfo=[],
                 **kwargs):

        self._validate_country_code(country)
        self._validate_currency_code(sendingCurrencies)
        self._validate_currency_code(receivingCurrencies)

        self.country = country
        self.sendingCurrencies = sendingCurrencies
        self.receivingCurrencies = receivingCurrencies
        self.purposeOfPaymentRequired = purposeOfPaymentRequired
        self.invoiceAttachmentRequired = invoiceAttachmentRequired
        self.bankFields = bankFields
        self.purposeOfPaymentInfo=[deseralize(PurposeOfPayment,
                                        p) for p in purposeOfPaymentInfo]
