from veem.models.base import Base

class PaymentApprovalResponse(Base):
    def __init__(self,
                 status=None,
                 approverNumber=None,
                 approverNumberRequired=None,
                 userApprovalResponseList=[],
                 **kwargs):

        self.status = status
        self.approverNumber = approverNumber
        self.approverNumberRequired = approverNumberRequired
        self.userApprovalResponseList = userApprovalResponseList
