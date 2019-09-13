
from veem.models.base import Base
from veem.models.address import Address
from veem.models.bank_account import BankAccount

from veem.utils import deseralize
from veem.constants import AccountType

class Contact(Base):
    def __init__(self,
                 id=None,
                 externalId=None,
                 contactAccountId=None,
                 email=None,
                 firstName=None,
                 lastName=None,
                 businessName=None,
                 countryCode=None,
                 dialCode=None,
                 phoneNumber=None,
                 batchItemId=None,
                 type=None,
                 bankAccount=None,
                 address=None,
                 **kwargs):

        self._validate_constants(AccountType, type)
        self._validate_country_code(countryCode)

        self.id = id
        self.externalId = externalId
        self.contactAccountId = contactAccountId
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.businessName = businessName
        self.countryCode = countryCode
        self.dialCode = dialCode
        self.phoneNumber = phoneNumber
        self.batchItemId = batchItemId
        self.type = type
        self.bankAccount = deseralize(BankAccount, bankAccount)
        self.address = deseralize(Address, address)
