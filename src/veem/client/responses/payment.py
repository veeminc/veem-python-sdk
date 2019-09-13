
from .amount import AmountResponse
from .account import AccountResponse
from .attachment import AttachmentResponse
from .exchange_rate import ExchangeRateResponse
from .payment_approval import PaymentApprovalResponse
from .push_payment_info import PushPaymentInfoResponse

from veem.models.base import Base
from veem.models.payment import Payment

from veem.utils import deseralize

class PaymentResponse(Base):
    def __init__(self,
                 id=None,
                 requestId=None,
                 claimLink=None,
                 externalInvoiceRefId=None,
                 payee=None,
                 payer=None,
                 status=None,
                 amount=None,
                 payeeAmount=None,
                 exchangeRate=None,
                 exchangeRateResponse=None,
                 attachments=[],
                 batchItemId=None,
                 ccEmails=[],
                 exchangeRateQuoteId=None,
                 purposeOfPayment=None,
                 pushPaymentInfoResponse=None,
                 paymentApprovalResponse=None,
                 timeCreated=None,
                 timeUpdated=None,
                 timeSent=None,
                 **kwargs):

        self.id = id
        self.requestId = requestId
        self.claimLink = claimLink
        self.externalInvoiceRefId = externalInvoiceRefId
        self.payee = deseralize(AccountResponse, payee)
        self.payer = deseralize(AccountResponse, payer)
        self.status = status
        self.payeeAmount = deseralize(AmountResponse, payeeAmount)
        self.amount = deseralize(AmountResponse, amount) or self.payeeAmount
        self.exchangeRateResponse = deseralize(ExchangeRateResponse,
                                               exchangeRateResponse)
        self.exchangeRate = deseralize(ExchangeRateResponse, exchangeRate) \
                            or self.exchangeRateResponse
        self.attachments = [deseralize(AttachmentResponse,
                                       attach) for attach in attachments]
        self.batchItemId = batchItemId
        self.ccEmails = ccEmails
        self.exchangeRateQuoteId = exchangeRateQuoteId
        self.purposeOfPayment = purposeOfPayment
        self.pushPaymentInfoResponse = deseralize(PushPaymentInfoResponse,
                                                  pushPaymentInfoResponse)
        self.paymentApprovalResponse = deseralize(PaymentApprovalResponse,
                                                  paymentApprovalResponse)
        self.timeCreated = timeCreated
        self.timeUpdated = timeUpdated
        self.timeSent = timeSent

    @property
    def convert(self):
        return Payment(pushPaymentInfo=self.pushPaymentInfoResponse,
                       paymentApproval=self.paymentApprovalResponse,
                       **self.json)
