from veem.models.base import Base
from veem.models.exchange_rate import ExchangeRate

class ExchangeRateResponse(Base):
    def __init__(self,
                 id=None,
                 fromAmount=None,
                 fromCurrency=None,
                 fromCountry=None,
                 toAmount=None,
                 toCurrency=None,
                 toCountry=None,
                 rate=None,
                 expiry=None,
                 timeCreated=None,
                 **kwargs):

        self.id = id
        self.fromAmount = fromAmount
        self.fromCurrency = fromCurrency
        self.fromCountry = fromCountry
        self.toAmount = toAmount
        self.toCurrency = toCurrency
        self.toCountry = toCountry
        self.rate = rate
        self.expiry = expiry
        self.timeCreated = timeCreated

    @property
    def convert(self):
        return ExchangeRate(hashId=self.id, **self.json)
