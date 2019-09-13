
from veem.models.base import Base

class PurposeOfPayment(Base):
    def __init__(self,
                 purposeCode=None,
                 description=None,
                 **kwargs):

        self.purposeCode = purposeCode
        self.description = description
