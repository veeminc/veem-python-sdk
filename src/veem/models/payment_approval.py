
from veem.models.base import Base
from veem.models.approver import Approver

from veem.utils import deseralize
from veem.constants import ApprovalStatus

class PaymentApproval(Base):
    def __init__(self,
                 approversCompleted=None,
                 status=None,
                 approversRequired=None,
                 approvers=[],
                 **kwargs):

        self._validate_constants(ApprovalStatus, status)

        self.approversCompleted = approversCompleted
        self.status = status
        self.approversRequired = approversRequired
        self.approvers = [deseralize(Approver,
                                     apr) for apr in approvers]
