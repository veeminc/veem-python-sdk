
from veem.models.base import Base

class ContactListParameters(Base):
    def __init__(self,
                email=None,
                firstName=None,
                lastName=None,
                businessName=None,
                batchId=None,
                batchItemIds=None,
                pageNumber=0,
                pageSize=1,
                 **kwargs):

        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.businessName = businessName
        self.batchId = batchId
        self.batchItemIds = batchItemIds
        self.pageNumber = pageNumber
        self.pageSize = pageSize
