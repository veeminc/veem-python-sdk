
from veem.models.base import Base

class ExchangeRate(Base):
    def __init__(self,
                 hashId=None,
                 fromAmount=None,
                 fromCurrency=None,
                 fromCountry=None,
                 toAmount=None,
                 toCurrency=None,
                 toCountry=None,
                 rate=None,
                 expiry=None,
                 **kwargs):

        self._validate_currency_code(fromCurrency)
        self._validate_currency_code(toCurrency)

        self._validate_country_code(fromCountry)
        self._validate_country_code(toCountry)

        self.fromAmount = fromAmount
        self.fromCurrency = fromCurrency
        self.fromCountry = fromCountry
        self.toAmount = toAmount
        self.toCurrency = toCurrency
        self.toCountry = toCountry
        self.hashId = hashId
        self.rate = rate
        self.expiry = expiry

    def _generate_request(self):
        return ExchangeRateRequest(
                     fromAmount=self.fromAmount,
                     fromCurrency=self.fromCurrency,
                     fromCountry=self.fromCountry,
                     toAmount=self.toAmount,
                     toCurrency=self.toCurrency,
                     toCountry=self.toCountry,
                )
