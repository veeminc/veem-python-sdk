
from __future__ import absolute_import

import unittest
import requests
import uuid
import json
import Veem

from Veem.api.invoice_controller_api import InvoiceControllerApi  # noqa: E501
from Veem.rest import ApiException
from Veem.models.invoice_request import InvoiceRequest
from Veem.VeemError import VeemError
from test.configuration import Configuration


class TestInvoiceControllerApi(unittest.TestCase):
    """InvoiceControllerApi unit test stubs"""

    def setUp(self):
        self.config=Configuration()
        self.api = InvoiceControllerApi(self.config.access_token)  # noqa: E501


    def tearDown(self):
        pass


    def testCreateCorrectly(self):

        amount={}
        amount['currency']='USD'
        amount['number']=30

        #exchange_rate_quote_id='DbD9nd'


        payer={}
        payer['businessName']='BOb'
        payer['countryCode']='US'
        payer['email']='dhar.somsubhro+1@gmail.com'
        payer['firstName']='Som'
        payer['lastName']='Dor'
        payer['type']='Personal'
        payer['phone']='+1-747-241-9816'

        test=InvoiceControllerApi(self.config.access_token)
        request=InvoiceRequest(amount=amount, payer=payer)  # noqa: E501
        response=test.create_invoice_using_post(request)
        assert response.amount_number==30 and response.payer_email=='dhar.somsubhro+1@gmail.com' and response.request_id is not None and response.exchangeRate_toCurrency=='USD'


    def testCreateMissingEmail(self):

        amount={}
        amount['currency']='USD'
        amount['number']=30

        #exchange_rate_quote_id='DbD9nd'


        payer={}
        payer['businessName']='BOb'
        payer['countryCode']='US'
        #payer['email']='dhar.somsubhro+1@gmail.com'
        payer['firstName']='Som'
        payer['lastName']='Dor'
        payer['type']='Personal'
        payer['phone']='+1-747-241-9816'

        test=InvoiceControllerApi(self.config.access_token)
        request=InvoiceRequest(amount=amount, payer=payer)  # noqa: E501
        try:
            response=test.create_invoice_using_post(request)
        except VeemError as err:
            assert err.code==50001202 #Email address not valid
        else:
            self.fail('VeemError not correctly raised')


    def testGetExists(self):

        test=InvoiceControllerApi(self.config.access_token)
        response=test.get_invoice_using_get('36470')
        assert response.id==36470 and response.status=="Sent"

    def testGetNonexistant(self):

        test=InvoiceControllerApi(self.config.access_token)
        try:
            response=test.get_invoice_using_get('11111')
        except VeemError as error:
            assert error.code==100 and error.message=="Invoice operation failed: Not Found"
        else:
            self.fail('VeemError not raised')

    '''def testApproveCorrectly(self):

        amount={}
        amount['currency']='USD'
        amount['number']=30

        exchange_rate_quote_id='DbD9nd'

        payer={}
        payer['businessName']='BOb'
        payer['countryCode']='US'
        payer['email']='dhar.somsubhro+1@gmail.com'
        payer['firstName']='Som'
        payer['lastName']='Dor'
        payer['type']='Personal'
        payer['phone']='+1-747-241-9816'

        test=InvoiceControllerApi()
        request=InvoiceRequest(amount=amount, exchange_rate_quote_id=exchange_rate_quote_id, payer=payer)  # noqa: E501
        response=test.create_invoice_using_post(request)
        approved=test.approve_invoice_using_post(response.id)
        assert approved.status=='Sent'
     '''

    def testApproveNonexistant(self):

        test=InvoiceControllerApi(self.config.access_token)
        try:
            response=test.approve_invoice_using_post('53126')
        except VeemError as error:
            assert error.code==100
        else:
            self.fail('VeemError not raised')


    def testCancelNonexistant(self):

        test=InvoiceControllerApi(self.config.access_token)
        try:
            response=test.cancel_invoice_using_post('53126')
        except VeemError as error:
            assert error.code==100
        else:
            self.fail('VeemError not raised')

    def testCancelCorrectly(self):

        amount={}
        amount['currency']='USD'
        amount['number']=30

        #exchange_rate_quote_id='DbD9nd'

        payer={}
        payer['businessName']='BOb'
        payer['countryCode']='US'
        payer['email']='dhar.somsubhro+1@gmail.com'
        payer['firstName']='Som'
        payer['lastName']='Dor'
        payer['type']='Personal'
        payer['phone']='+1-747-241-9816'

        test=InvoiceControllerApi(self.config.access_token)
        request=InvoiceRequest(amount=amount,payer=payer)  # noqa: E501
        response=test.create_invoice_using_post(request)
        cancelled=test.cancel_invoice_using_post(response.id)
        assert cancelled.status=='Cancelled'

if __name__ == '__main__':
    unittest.main()
