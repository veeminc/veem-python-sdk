
from __future__ import absolute_import
import uuid
import json
import unittest
import requests
import Veem

from Veem.api.customer_controller_api import CustomerControllerApi  # noqa: E501
from Veem.rest import ApiException
from Veem.VeemError import VeemError


class TestCustomerControllerApi(unittest.TestCase):

    def setUp(self):
        self.api = CustomerControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def testCorrectInput(self):
        test_controller = CustomerControllerApi()
        response=test_controller.search_customers_using_get(email="dhar.somsubhro@gmail.com")
        assert response.content==[
    {
      "id": 6049,
      "firstName": "Somsubhro",
      "lastName": "Dhar",
      "name": "Hello INC",
      "email": "dhar.somsubhro@gmail.com",
      "isoCountryCode": "US",
      "isContact": True
    }
  ]

    def testEmailNotInSystem(self):
        test=CustomerControllerApi()
        response=test.search_customers_using_get(email="hello@nope.com")
        assert response.content==[] and response.number_of_elements==0

    def testNotEmail(self):
        test=CustomerControllerApi()
        try:
            response=test.search_customers_using_get(email="hello")
        except VeemError as error:
            assert error.code==50001202






if __name__ == '__main__':
    unittest.main()