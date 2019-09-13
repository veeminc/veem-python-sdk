
from veem.models.base import Base

class AccountListParameters(Base):
    def __init__(self,
                 email=None,
                 **kwargs):

        self.email = email
