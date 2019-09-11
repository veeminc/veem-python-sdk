
from veem.models.base import Base

from veem.utils import deseralize
from veem.constants import AccountType

class Account(Base):
    def __init__(self,
                 type=None,
                 email=None,
                 firstName=None,
                 lastName=None,
                 businessName=None,
                 countryCode=None,
                 phoneCountryCode=None,
                 phone=None,
                 id=None,
                 name=None,
                 isContact=False,
                 accountType=None,
                 **kwargs):

        self._validate_constants(AccountType, type)
        self._validate_constants(AccountType, accountType)
        self._validate_country_code(countryCode)

        self._type = type
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.businessName = businessName
        self._countryCode = countryCode
        self.phoneCountryCode = phoneCountryCode
        self.phone = phone
        self.id = id
        self.name = name
        self.isContact = isContact
        self._accountType = accountType

    @property
    def countryCode(self):
        return self._countryCode

    @countryCode.setter
    def countryCode(self, value):
        self._validate_country_code(value)
        self._countryCode = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._validate_constants(AccountType, value)
        self._type = value

    @property
    def accountType(self):
        return self._accountType

    @accountType.setter
    def accountType(self, value):
        self._validate_constants(AccountType, value)
        self._accountType = value

    def _generate_request(self):
        return AccountRequest(
                     type=self.type,
                     email=self.email,
                     firstName=self.firstName,
                     lastName=self.lastName,
                     businessName=self.businessName,
                     countryCode=self.countryCode,
                     phoneCountryCode=self.phoneCountryCode,
                     phone=self.phone
                )
