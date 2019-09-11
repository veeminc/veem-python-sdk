from veem.client.responses.page import PageResponse
from veem.client.responses.metadata import CountryInfoResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi
from veem import __API_VERSION__ as API_VERSION

class MetadataClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.url = "veem/public/v{}/country-currency-map".format(API_VERSION)
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(getCountryCurrencyMap=('get',self.url)))

    def getCountryCurrencyMap(self):
        """
            Get all supported country and currency map
        """
        return self._list_response_handler(PageResponse,
                                           CountryInfoResponse,
                                           self.client.getCountryCurrencyMap())
