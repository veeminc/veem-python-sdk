from veem.models.base import Base

class AddressRequest(Base):
    def __init__(self,
                 line1=None,
                 line2=None,
                 city=None,
                 stateProvince=None,
                 postalCode=None,
                 **kwargs):

        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.stateProvince = stateProvince
        self.postalCode = postalCode
