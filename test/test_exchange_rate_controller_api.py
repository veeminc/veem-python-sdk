from __future__ import absolute_import

import sys
import Veem
import uuid
import json
import unittest
import requests
from Veem.api.exchange_rate_controller_api import ExchangeRateControllerApi  # noqa: E501
from Veem.rest import ApiException
from Veem.models.exchange_rate_request import ExchangeRateRequest
from Veem.VeemError import VeemError
from test.configuration import Configuration


class TestExchangeRateControllerApi(unittest.TestCase):
    """ExchangeRateControllerApi unit test stubs"""

    def setUp(self):
        self.config=Configuration()
        self.api = ExchangeRateControllerApi(self.config.access_token)  # noqa: E501


    def tearDown(self):
        pass

    def testCorrectInput(self):
        """Test case for generate_exchange_quote_using_post

        """
        test_controller = ExchangeRateControllerApi(self.config.access_token)

        request = ExchangeRateRequest(to_amount=100.0,from_currency='USD', to_country='IN', to_currency='INR', recipient_account_email='hi@gm.com')
        response=test_controller.create_quote_using_post(request)
        assert response.id is not None and response.expiry is not None and response.to_currency=='INR' and response.rate>50 and response.rate<100


    def testNeitherAmount(self):
        test_controller = ExchangeRateControllerApi(self.config.access_token)
        request = ExchangeRateRequest(from_currency='USD', to_country='IN', to_currency='INR', recipient_account_email='hi@gm.com')
        try:
            response=test_controller.create_quote_using_post(request)
        except VeemError as error:
            assert error.code==50001403
        else:
            self.fail('VeemError not raised correctly')

    def testBothAmounts(self):
        test_controller = ExchangeRateControllerApi(self.config.access_token)
        request = ExchangeRateRequest(to_amount=100.0,from_amount=100.0,from_currency='USD', to_country='IN', to_currency='INR', recipient_account_email='hi@gm.com')
        try:
            response=test_controller.create_quote_using_post(request)
        except VeemError as error:
            assert error.code==50001402
        else:
            self.fail('VeemError not raised correctly')

    def testMissingOthers(self):
        test_controller = ExchangeRateControllerApi(self.config.access_token)
        request = ExchangeRateRequest(to_amount=100.0, to_country='IN', to_currency='INR', recipient_account_email='hi@gm.com')
        try:
            response=test_controller.create_quote_using_post(request)
        except VeemError as error:
           assert error.code==100
        else:
            self.fail('VeemError not raised correctly')



if __name__ == '__main__':
    unittest.main()
