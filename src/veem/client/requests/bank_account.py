from .address import AddressRequest
from veem.models.base import Base

class BankAccountRequest(Base):
    def __init__(self,
                 routingNumber=None,
                 bankName=None,
                 bankAccountNumber=None,
                 currencyCode=None,
                 isoCountryCode=None,
                 iban=None,
                 swiftBic=None,
                 beneficiaryName=None,
                 bsbBankCode=None,
                 branchCode=None,
                 transitCode=None,
                 bankInstitutionNumber=None,
                 bankIfscBranchCode=None,
                 sortCode=None,
                 bankCode=None,
                 clabe=None,
                 bankCnaps=None,
                 bankAddress=None,
                 **kwargs):

        self.routingNumber = routingNumber
        self.bankName = bankName
        self.bankAccountNumber = bankAccountNumber
        self.currencyCode = currencyCode
        self.isoCountryCode = isoCountryCode
        self.iban = iban
        self.swiftBic = swiftBic
        self.beneficiaryName = beneficiaryName
        self.bsbBankCode = bsbBankCode
        self.branchCode = branchCode
        self.transitCode = transitCode
        self.bankInstitutionNumber = bankInstitutionNumber
        self.bankIfscBranchCode = bankIfscBranchCode
        self.sortCode = sortCode
        self.bankCode = bankCode
        self.clabe = clabe
        self.bankCnaps = bankCnaps
        self.bankAddress = bankAddress
