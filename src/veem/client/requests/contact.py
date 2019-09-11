from veem.models.base import Base

class ContactRequest(Base):
    def __init__(self,
                 email=None,
                 type=None,
                 firstName=None,
                 lastName=None,
                 businessName=None,
                 isoCountryCode=None,
                 phoneDialCode=None,
                 phoneNumber=None,
                 externalBusinessId=None,
                 businessAddress=None,
                 bankAccount=None,
                 batchItemId=None,
                 **kwargs):

        self.email = email
        self.type = type
        self.firstName = firstName
        self.email = email
        self.type = type
        self.firstName = firstName
        self.lastName = lastName
        self.businessName = businessName
        self.isoCountryCode = isoCountryCode
        self.phoneDialCode = phoneDialCode
        self.phoneNumber = phoneNumber
        self.externalBusinessId = externalBusinessId
        self.businessAddress = businessAddress
        self.bankAccount = bankAccount
        self.batchItemId = batchItemId
