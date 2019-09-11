
from veem.client.veem import VeemClient
from veem.client.requests.exchange_rate import ExchangeRateRequest

if __name__ == '__main__':

    # define a VeemClient Context Manager with yaml+file and auto login.
    with VeemClient(yaml_file='/path/to/your/configuration.yaml',
                    useClientCredentials=True) as veem:
        # define an ExchangeRateRequest
        request = ExchangeRateRequest(fromAmount=500.0,
                                      fromCurrency='CAD',
                                      fromCountry='CA',
                                      toCurrency='USD',
                                      toCountry='US')
        # request the fx rate
        rate = veem.exchangeRateClient.generate(request)
