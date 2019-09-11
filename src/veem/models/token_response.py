
from veem.models.base import Base

from veem.constants import Scope

class TokenResponse(Base):
    def __init__(self,
                 access_token=None,
                 user_name=None,
                 account_id=None,
                 expires_in=None,
                 token_type=None,
                 scope=None,
                 user_id=None,
                 refresh_token=None,
                 **kwargs):

        self._validate_constants(Scope, scope)

        self.accessToken = access_token
        self.username = user_name
        self.accountId = account_id
        self.expiresIn = expires_in
        self.tokenType = token_type
        self.scope = scope
        self.userId = user_id
        self.refreshToken = refresh_token
