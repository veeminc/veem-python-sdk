from veem.models.base import Base

class AccountRequest(Base):
    def __init__(self,
                 type=None,
                 email=None,
                 firstName=None,
                 lastName=None,
                 businessName=None,
                 countryCode=None,
                 phoneCountryCode=None,
                 phone=None,
                 **kwargs):

        self.type = type
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.businessName = businessName
        self.countryCode = countryCode
        self.phoneCountryCode = phoneCountryCode
        self.phone = phone
