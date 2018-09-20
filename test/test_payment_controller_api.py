

from __future__ import absolute_import

import unittest
import requests
import uuid
import json
import Veem

from Veem.api.payment_controller_api import PaymentControllerApi  # noqa: E501
from Veem.rest import ApiException
from Veem.models.payment_request import PaymentRequest
from Veem.VeemError import VeemError
#from Veem.api.attachment_controller_api import AttachmentControllerApi  # noqa: E501



class TestPaymentControllerApi(unittest.TestCase):


    def setUp(self):
        self.api = PaymentControllerApi()

    def tearDown(self):
        pass
    def test_get_payments_by_status_using_get(self):

        test=PaymentControllerApi()
        response=test.get_payments_by_status_using_get(status='Complete')
        assert response.number_of_elements==8 and response.size==25

    def testApproveCorrectly(self):

        amount={}
        amount['currency']='USD'
        amount['number']=100

        approve_automatically=False


        payee={}
        payee['businessName']='BOb'
        payee['countryCode']='US'
        payee['email']='dhar.somsubhro+1@gmail.com'
        payee['firstName']='Som'
        payee['lastName']='Dor'
        payee['type']='Personal'
        payee['phone']='1-408-532-4578'

        payee_amount={}
        payee_amount['currency']='INR'
        payee_amount['number']=68


        purpose_of_payment='Services'

        test=PaymentControllerApi()
        request=PaymentRequest(amount=amount, approve_automatically=approve_automatically,payee=payee, payee_amount=payee_amount, purpose_of_payment=purpose_of_payment)
        response=test.create_payment_using_post(request)
        approvedResponse=test.approve_payment_using_post(response.id)
        assert approvedResponse.status=='Sent'

    def testApproveNonexistant(self):

        test=PaymentControllerApi()
        try:
            response=test.approve_payment_using_post('53126')
        except VeemError as error:
            assert error.code==100
        else:
            self.fail('VeemError not raised')

    def testCreateCorrect(self):

        amount={}
        amount['currency']='USD'
        amount['number']=100

        payee={}
        payee['businessName']='BOb'
        payee['countryCode']='US'
        payee['email']='dhar.somsubhro+1@gmail.com'
        payee['firstName']='Som'
        payee['lastName']='Dor'
        payee['type']='Personal'
        payee['phone']='1-408-532-4578'

        payee_amount={}
        payee_amount['currency']='INR'
        payee_amount['number']=68


        purpose_of_payment='Services'



        test=PaymentControllerApi()
        request=PaymentRequest(amount=amount, payee=payee, payee_amount=payee_amount, purpose_of_payment=purpose_of_payment)
        response=test.create_payment_using_post(request)
        assert response.request_id is not None and response.claim_link is not None and response.exchangeRate_fromAmount==100

    '''def testCreateWithAttachment(self):

        test=AttachmentControllerApi()
        result=test.upload_attachment_using_post(file="hello")

        amount={}
        amount['currency']='USD'
        amount['number']=100

        attachments={}
        attachments['name']=result.name
        attachments['referenceId']=result.reference_id

        payee={}
        payee['businessName']='BOb'
        payee['countryCode']='US'
        payee['email']='dhar.somsubhro+1@gmail.com'
        payee['firstName']='Som'
        payee['lastName']='Dor'
        payee['type']='Personal'
        payee['phone']='1-408-532-4578'

        payeeAmount={}
        payeeAmount['currency']='INR'
        payeeAmount['number']=68


        purposeOfPayment='Services'

        test=PaymentControllerApi()
        request=PaymentRequest(amount=amount, attachments=attachments, payee=payee, payee_amount=payeeAmount, purpose_of_payment=purposeOfPayment)

        try:
            response=test.create_payment_using_post(request)
        except VeemError as error:
            print(error.message)
        #assert response.request_id is not None and response.claim_link is not None and response.exchangeRate_fromAmount==100
    '''
    def testCreateMissingPhone(self):


        amount={}
        amount['currency']='USD'
        amount['number']=100

        approve_automatically=False


        payee={}
        payee['businessName']='BOb'
        payee['countryCode']='US'
        payee['email']='dhar.somsubhro+1@gmail.com'
        payee['firstName']='Som'
        payee['lastName']='Dor'
        payee['type']='Personal'
        #payee['phone']='1-408-532-4578'

        payee_amount={}
        payee_amount['currency']='INR'
        payee_amount['number']=68


        purpose_of_payment='Services'


        test=PaymentControllerApi()
        request=PaymentRequest(amount=amount, payee=payee, payee_amount=payee_amount, purpose_of_payment=purpose_of_payment)
        try:
            response=test.create_payment_using_post(request)
        except VeemError as error:
            assert error.message=="Phone number is empty" and error.code==50001211
        else:
            self.fail('VeemError not raised')




    def testGetExists(self):

        test=PaymentControllerApi()
        response=test.get_payment_using_get('53126')
        assert response.id==53126 and response.payee_email=="dhar.somsubhro+1@gmail.com"

    def testGetNonexistant(self):

        test=PaymentControllerApi()
        try:
            response=test.get_payment_using_get('11111')
        except VeemError as error:
            assert error.code==100 and error.message=="Payment operation failed: Not Found"
        else:
            self.fail('VeemError not raised')




    def testCancelCorrectly(self):

        amount={}
        amount['currency']='USD'
        amount['number']=100

        approve_automatically=False


        payee={}
        payee['businessName']='BOb'
        payee['countryCode']='US'
        payee['email']='dhar.somsubhro+1@gmail.com'
        payee['firstName']='Som'
        payee['lastName']='Dor'
        payee['type']='Personal'
        payee['phone']='1-408-532-4578'

        payee_amount={}
        payee_amount['currency']='INR'
        payee_amount['number']=68


        purpose_of_payment='Services'



        test=PaymentControllerApi()
        request=PaymentRequest(amount=amount, approve_automatically=approve_automatically,payee=payee, payee_amount=payee_amount, purpose_of_payment=purpose_of_payment)
        response=test.create_payment_using_post(request)
        cancelled=test.cancel_payment_using_post(response.id)
        assert cancelled.status=='Cancelled'


    def testCancelNonexistant(self):

        test=PaymentControllerApi()
        try:
            response=test.cancel_payment_using_post('53126')
        except VeemError as error:
            assert error.code==100
        else:
            self.fail('VeemError not raised')

if __name__ == '__main__':
    unittest.main()
