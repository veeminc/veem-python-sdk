
from veem.models.base import Base

class VeemErrorResponse(Base):
    def __init__(self,
                 message=None,
                 code=None,
                 logTag=None,
                 timestamp=None,
                 fileName=None,
                 lineNumber=None,
                 **kwargs):

        self.message = message
        self.code = code
        self.logTag = logTag
        self.timestamp = timestamp
        self.fileName = fileName
        self.lineNumber = lineNumber
