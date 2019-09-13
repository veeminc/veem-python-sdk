
from .amount import AmountResponse
from .account import AccountResponse
from .attachment import AttachmentResponse
from .exchange_rate import ExchangeRateResponse

from veem.models.base import Base
from veem.models.invoice import Invoice

from veem.utils import deseralize

class InvoiceResponse(Base):
    def __init__(self,
                 id=None,
                 status=None,
                 exchangeRate=None,
                 claimLink=None,
                 payer=None,
                 clientId=None,
                 amount=None,
                 notes=None,
                 externalInvoiceRefId=None,
                 ccEmails=[],
                 purposeOfPayment=None,
                 attachments=[],
                 exchangeRateQuoteId=None,
                 dueDate=None,
                 timeCreated=None,
                 **kwargs):

        self.id = id
        self.status = status
        self.exchangeRate = deseralize(ExchangeRateResponse, exchangeRate)
        self.claimLink = claimLink
        self.payer = deseralize(AccountResponse, payer)
        self.clientId = clientId
        self.amount = deseralize(AmountResponse, amount)
        self.notes = notes
        self.externalInvoiceRefId = externalInvoiceRefId
        self.ccEmails = ccEmails
        self.purposeOfPayment = purposeOfPayment
        self.attachments = [deseralize(AttachmentResponse,
                                       attach) for attach in attachments]
        self.exchangeRateQuoteId = exchangeRateQuoteId
        self.dueDate = dueDate
        self.timeCreated = timeCreated

    @property
    def convert(self):
        return Invoice(**self.json)
