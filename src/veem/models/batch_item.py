
from veem.models.base import Base

from veem.utils import deseralize
from veem.exceptions import VeemSdkException
from veem.constants import BatchItemType, BatchStatus

class ErrorInfo(Base):

    def __init__(self,
                 code=None,
                 error=None,
                 message=None,
                 timestamp=None,
                 **kwargs):

        self.code = code
        self.error = error
        self.message = message
        self.timestamp = timestamp


class BatchItem(Base):
    def __init__(self,
                 id=None,
                 batchItemId=None,
                 status=None,
                 errorInfo=None,
                 paymentId=None,
                 contactId=None,
                 type=None,
                 **kwargs):

        self._validate_constants(BatchStatus, status)
        self._validate_constants(BatchItemType, type)

        self.id = id or batchItemId
        self.batchItemId = id or batchItemId
        self.status = status
        self.errorInfo = errorInfo
        self._paymentId = paymentId
        self._contactId = contactId
        self.type = type

    @property
    def paymentId(self):
        if self.type == BatchItemType.PAYMENT:
            return self._paymentId
        raise VeemSdkException(("Can't get paymentId from BatchItem with "
                                "type {}").format(self.type));

    @property
    def contactId(self):
        if self.type == BatchItemType.CONTACT:
            return self._contactId
        raise VeemSdkException(("Can't get contactId from BatchItem with "
                                "type {}").format(self.type));
