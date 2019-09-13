
class VeemException(Exception):

    def __init__(self, errorResponse=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errorCode = getattr(errorResponse, 'errorCode', None)
        self.message = getattr(errorResponse, 'message', None)
        self.timestamp = getattr(errorResponse, 'timestamp', None)
        self.logTag = getattr(errorResponse, 'logTag', None)
        self.fileName = getattr(errorResponse, 'fileName', None)
        self.lineNumber = getattr(errorResponse, 'lineNumber', None)
        if isinstance(errorResponse, dict):
            for key in ('errorCode', 'message', 'timestamp', 'logTag',
                        'fileName', 'lineNumber'):
                setattr(self, key,
                        errorResponse.get(key, getattr(self, key, None)))

class VeemBadRequestException(VeemException):
    pass

class VeemConflictException(VeemException):
    pass

class VeemForbiddenException(VeemException):
    pass

class VeemInternalException(VeemException):
    pass

class VeemNotFoundException(VeemException):
    pass

class VeemConflictException(VeemException):
    pass

class VeemSdkException(VeemException):
    pass

class VeemUnauthorizedException(VeemException):
    pass
