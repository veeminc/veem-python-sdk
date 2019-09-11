
class Base(object):

    @property
    def json(self):
        return {k:v for k,v in self.__dict__.items() if not k.startswith('_')}

    @property
    def convert(self):
        return self

    def _validate_constants(self, constant, value, required=False):
        if not value and not required: return
        if isinstance(value, list):
            for v in value:
                self._validate_constants(constant, v)
            return
        if isinstance(constant, tuple) and isinstance(value, dict):
            k_constant, v_constant = constant
            for k,v in value.items():
                self._validate_constants(k_constant, k)
                self._validate_constants(k_constant, v)
            return
        if not value in constant.values():
            raise ValueError('Unsupport Constant Value %s' % value)

    def _validate_country_code(self, value, required=False):
        if not value and not required: return
        if len(str(value)) != 2:
            raise ValueError('Unsupport CountryCode %s' % value)

    def _validate_currency_code(self, value, required=False):
        if not value and not required: return
        if len(str(value)) != 3:
            raise ValueError('Unsupport CurrencyCode %s' % value)
