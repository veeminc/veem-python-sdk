
from veem.models.base import Base

class Amount(Base):
    def __init__(self, number=None, currency=None, **kwargs):

        self._validate_currency_code(currency)
        self.number = number
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._validate_currency_code(value)
        self._currency = value
