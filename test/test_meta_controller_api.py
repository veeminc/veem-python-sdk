
from __future__ import absolute_import

import unittest
import Veem

from Veem.api.meta_controller_api import MetaControllerApi  # noqa: E501
from Veem.rest import ApiException
import requests
from configuration import Configuration


class TestMetaControllerApi(unittest.TestCase):
    """MetaControllerApi unit test stubs"""

    def setUp(self):
        self.api = MetaControllerApi()  # noqa: E501
        self.config=Configuration()

    def tearDown(self):
        pass

    def testGetNormal(self):
        """Test case for get_country_currency_map_using_get

        Country Currency Map  # noqa: E501
        """
        test=MetaControllerApi(self.config.access_token)
        result=test.get_country_currency_map_using_get()
        assert result is not None
        
    def testGetBankFieldsTrue(self):
        """Test case for get_country_currency_map_using_get

        Country Currency Map  # noqa: E501
        """
        test=MetaControllerApi(self.config.access_token))
        result=test.get_country_currency_map_using_get(bankFields=True)
        assert result is not None

    def testGetBankFieldsFalse(self):
        """Test case for get_country_currency_map_using_get

        Country Currency Map  # noqa: E501
        """
        test=MetaControllerApi(self.config.access_token))
        result=test.get_country_currency_map_using_get(bankFields=False)
        assert result is not None

    def testGetBankFieldsNotBoolean(self):
        """Test case for get_country_currency_map_using_get

        Country Currency Map  # noqa: E501
        """
        test=MetaControllerApi(self.config.access_token))
        try:
            result=test.get_country_currency_map_using_get(bankFields=1)
        except AttributeError as err:
            pass






if __name__ == '__main__':
    unittest.main()
