from veem.models.base import Base

class AttachmentRequest(Base):
    def __init__(self,
                 type=None,
                 name=None,
                 referenceId=None,
                 **kwargs):

        self.type = type
        self.name = name
        self.referenceId = referenceId
