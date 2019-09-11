
import requests

class VeemContext(object):

    def __init__(self,
                 client_id=None, client_secret=None,
                 authorizationCode=None, redirectUrl=None,
                 **kwargs):

        self.clientId = client_id
        self.clientSecret = client_secret
        self.authorizationCode = authorizationCode
        self.redirectUrl = redirectUrl
        self.session = requests.Session()
        self.token = None
