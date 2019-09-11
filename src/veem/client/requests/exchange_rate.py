from veem.models.base import Base

class ExchangeRateRequest(Base):
    def __init__(self,
                 fromAmount=None,
                 fromCurrency=None,
                 fromCountry=None,
                 toAmount=None,
                 toCurrency=None,
                 toCountry=None,
                 **kwargs):

        self.fromAmount = fromAmount
        self.fromCurrency = fromCurrency
        self.fromCountry = fromCountry
        self.toAmount = toAmount
        self.toCurrency = toCurrency
        self.toCountry = toCountry
