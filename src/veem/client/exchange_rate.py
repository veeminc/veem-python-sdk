from veem.client.responses.exchange_rate import ExchangeRateResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi

class ExchangeRateClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(generate=('post', '/quotes')))

    def generate(self, request):
        """
            Generate exchange rate.

            @param request: an ExchangeRateRequest with from/to amount, country
                            and currency
            @return generated Fx Quote with expiry from Veem
        """
        return self._response_handler(
                        ExchangeRateResponse,
                        self.client.generate(access_token=self.context.token,
                                        api_route='exchangerates',
                                        **request.json)
                            )
