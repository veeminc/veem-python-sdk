from .amount import AmountResponse

from veem.models.base import Base

from veem.utils import deseralize

class PushPaymentInfoResponse(Base):
    def __init__(self,
                 amount=None,
                 reference=None,
                 pushPaymentInfo=None,
                 **kwargs):

        self.amount = deseralize(AmountResponse, amount)
        self.reference = reference
        self.pushPaymentInfo = pushPaymentInfo
