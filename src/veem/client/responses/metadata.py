from veem.models.base import Base
from veem.models.country_info import CountryInfo
from veem.models.purpose_of_payment import PurposeOfPayment

from veem.utils import deseralize

class CountryInfoResponse(Base):
    def __init__(self,
                 bankFields=None,
                 country=None,
                 invoiceAttachmentRequired=None,
                 purposeOfPaymentInfo=[],
                 purposeOfPaymentRequired=None,
                 receivingCurrencies=[],
                 sendingCurrencies=[],
                 **kwargs):

        self.bankFields = bankFields
        self.country = country
        self.purposeOfPaymentInfo = [deseralize(PurposeOfPayment,
                                       info) for info in purposeOfPaymentInfo]
        self.purposeOfPaymentRequired = purposeOfPaymentRequired
        self.invoiceAttachmentRequired = invoiceAttachmentRequired
        self.receivingCurrencies = receivingCurrencies
        self.sendingCurrencies = sendingCurrencies

    @property
    def convert(self):
        return CountryInfo(**self.json)
