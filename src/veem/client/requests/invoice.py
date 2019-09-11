
from .amount import AmountRequest
from .account import AccountRequest
from .attachment import AttachmentRequest

from veem.models.base import Base

from veem.utils import deseralize

class InvoiceRequest(Base):
    def __init__(self,
                 id=None,
                 status=None,
                 timeCreated=None,
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
                 **kwargs):

        self.id = id
        self.status = status
        self.timeCreated = timeCreated
        self.claimLink = claimLink
        self.payer = deseralize(AccountRequest, payer).json
        self.clientId = clientId
        self.amount = deseralize(AmountRequest, amount).json
        self.notes = notes
        self.externalInvoiceRefId = externalInvoiceRefId
        self.ccEmails = ccEmails
        self.purposeOfPayment = purposeOfPayment
        self.attachments = [deseralize(AttachmentRequest,
                                       attach).json for attach in attachments]
        self.exchangeRateQuoteId = exchangeRateQuoteId
        self.dueDate = dueDate
