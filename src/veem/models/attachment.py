
from veem.models.base import Base

from veem.constants import AttachmentType

class Attachment(Base):
    def __init__(self,
                 type=None,
                 name=None,
                 referenceId=None,
                 path=None,
                 **kwargs):

        self.type = type
        self.name = name
        self.referenceId = referenceId
        self.path = path

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._validate_constants(AttachmentType, value)
        self._type = value
