
from veem.models.base import Base

from veem.constants import ApprovalStatus

class Approver(Base):
    def __init__(self,
                 status=None,
                 email=None,
                 firstName=None,
                 lastName=None,
                 middleName=None,
                 **kwargs):

        self._validate_constants(ApprovalStatus, status)

        self.status = status
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
