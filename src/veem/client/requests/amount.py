from veem.models.base import Base

class AmountRequest(Base):
    def __init__(self,
                 number=None,
                 currency=None,
                 **kwargs):

        self.number = number
        self.currency = currency
