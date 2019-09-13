# import from python libraries
import uuid
import logging
import requests
from functools import partial
from urllib.parse import urljoin
from requests.auth import HTTPBasicAuth

from veem import __API_VERSION__ as API_VERSION
from veem.exceptions import VeemException

logger = logging.getLogger(__name__)

class ApiError(Exception):
    ''' ApiError

    The abstract class for ApiError

    '''
    def __init__(self, request, response):
        super(ApiError, self).__init__()
        self.request = request
        self.response = response

class ApiRequestError(ApiError):
    pass

class ApiJsonError(ApiError):
    pass

class VeemRestApi(object):

    def __init__(self, url=None, session=None, endpoints=dict()):
        self.url = url if url.endswith('/') else '%s/' % url
        self.session = session or requests.Session()
        self.endpoints = endpoints

    def __getattr__(self, attr):
        """ dunder getattr method

        magic method that use endpoints list defined at ENDPOINTS and
        functools.partial to link class method

        """
        if attr in self.endpoints:
            return partial(self._api_call, attr)
        raise AttributeError("'%s' object has no attribute '%s'" % (
                                    self.__class__.__name__, attr))

    def _generate_endpoint(self, api_route, value, **kwargs):
        value = value.format(**kwargs)
        value = value if not api_route else 'veem/v{}/{}{}'.format(
            API_VERSION, api_route, value
        )
        return value.lstrip('/')

    def _api_call(self, attr,
                  uri_params={}, access_token=None, api_route=None,
                  request_header={}, request_params={}, request_auth=[],
                  request_files={}, request_body=None,
                  request_stream=False, *args, **kwargs):
        """ _api_call method

        main method that makes the REST api call

        """
        if attr not in self.endpoints:
            raise AttributeError("'%s' object has no suitable api endpoint" % (
                                        self.__class__.__name__))
        method, endpoint = self.endpoints[attr]
        endpoint = self._generate_endpoint(api_route, endpoint, **uri_params)
        method = (method or 'get').upper()
        url = urljoin(self.url, endpoint.lstrip('/'))
        try:
            if access_token:
                self.session.headers.update(
                    {'Authorization':'Bearer %s' % getattr(
                                access_token, 'accessToken', access_token),
                     'X-REQUEST-ID': str(uuid.uuid4())})

            auth = HTTPBasicAuth(*request_auth) if request_auth else None
            # send the REST api call
            request = requests.Request(method, url,
                                       json=request_body or kwargs,
                                       files=request_files,
                                       params=request_params,
                                       auth=auth)
            prepared = request.prepare()
            prepared.headers.update(self.session.headers)
            response = self.session.send(prepared)

            # if streaming request don't bother to validate jsonize the data
            if request_stream:
                return response

            # validate response
            if not response.ok:
                raise ApiRequestError(request, response)
            json = response.json()
            if not json:
                raise ApiJsonError(request, response)
        except ApiError as ae:
            try:
                json = response.json()
            except Exception as aee:
                json = {}
            # try to unpack response exception
            try:
                response = ae.response.text
            except Exception as aee:
                response = str(aee)
            logger.error("'%s' endpoint request failed: %s" % (attr, response))
            if json:
                raise VeemException(errorResponse=json)
            return response
        except Exception as e:
            logger.error("'%s' endpoint request errored: %s" % (attr, str(e)))
            return str(e)

        return json
