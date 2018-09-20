
from __future__ import absolute_import

import unittest
import requests
import uuid
import json

import Veem
from Veem.api.contact_controller_api import ContactControllerApi  # noqa: E501
from Veem.rest import ApiException
from Veem.VeemError import VeemError
from Veem.models.contact_request import ContactRequest


class TestContactControllerApi(unittest.TestCase):

    def setUp(self):
        self.api = ContactControllerApi()  # noqa: E501

    def tearDown(self):
        pass


    def testGetBatchDoesntExists(self):

        test=ContactControllerApi()
        try:
            response=test.get_contact_batch_using_get(batch_id='12345')
        except VeemError as error:
            assert error.code==50000001#Doesn't exist

    def testCreateNotNewContact(self):

        test=ContactControllerApi()


        batch_item_id=1
        business_name='Hello INC'
        email="dhar.somsubhro+1@gmail.com"
        external_business_id=1
        first_name="Somsubhro"
        iso_country_code="US"
        last_name="Dhar"
        phone_dial_code="408"
        phone_number="312-3455"
        type="Incomplete"

        contact1=ContactRequest(business_name=business_name, iso_country_code=iso_country_code, email=email, first_name=first_name, last_name=last_name, batch_item_id=batch_item_id, phone_dial_code=phone_dial_code, phone_number=phone_number, type=type, external_business_id=external_business_id)
        contacts=[contact1.to_dict()]
        response=test.create_contacts_using_post(contacts=contacts)
        response2=test.get_contact_batch_using_get(batch_id=response.batch_id)
        assert response.total_items==1 and response2.has_errors==True

    def testCreateMultipleContacts(self):

        test=ContactControllerApi()

        batch_item_id=1
        business_name='Hello INC'
        email="dhar.somsubhro+1@gmail.com"
        external_business_id=1
        first_name="Somsubhro"
        iso_country_code="US"
        last_name="Dhar"
        phone_dial_code="408"
        phone_number="312-3455"
        type="Incomplete"

        contact1=ContactRequest(business_name=business_name, iso_country_code=iso_country_code, email=email, first_name=first_name, last_name=last_name, batch_item_id=batch_item_id, phone_dial_code=phone_dial_code, phone_number=phone_number, type=type, external_business_id=external_business_id)
        contact2=ContactRequest(business_name="what", iso_country_code="US", email="dom@dhar.com", first_name="bob", last_name="smith", batch_item_id=2, phone_dial_code="408", phone_number="145-3456", type="Incomplete", external_business_id=2)
        contacts=[contact1.to_dict(), contact2.to_dict()]
        response=test.create_contacts_using_post(contacts=contacts)
        assert response.total_items==2 and response.status=="InProgress"

    '''def testCreateBadContact(self):

        test=ContactControllerApi()
        contact2=ContactRequest(business_name="what", iso_country_code="US", email="dom@dhar.com", first_name="bob", last_name="smith", batch_item_id=2, phone_dial_code="408", phone_number="145-3456", type="Incomplete", external_business_id=2)
        contacts=[contact2.to_dict()]
        response=test.create_contacts_using_post(contacts=contacts)
        assert response.total_items==1 and response.has_errors==True'''

    def testGetMultipleContacts(self):

        test=ContactControllerApi()

        batch_item_id=1
        business_name='Hello INC'
        email="dhar.somsubhro+1@gmail.com"
        external_business_id=1
        first_name="Somsubhro"
        iso_country_code="US"
        last_name="Dhar"
        phone_dial_code="408"
        phone_number="312-3455"
        type="Incomplete"

        contact1=ContactRequest(business_name=business_name, iso_country_code=iso_country_code, email=email, first_name=first_name, last_name=last_name, batch_item_id=batch_item_id, phone_dial_code=phone_dial_code, phone_number=phone_number, type=type, external_business_id=external_business_id)
        contact2=ContactRequest(business_name="what", iso_country_code="US", email="dom@dhar.com", first_name="bob", last_name="smith", batch_item_id=2, phone_dial_code="408", phone_number="145-3456", type="Incomplete", external_business_id=2)
        contacts=[contact1.to_dict(), contact2.to_dict()]
        response=test.create_contacts_using_post(contacts=contacts)
        response2=test.get_contact_batch_using_get(batch_id=response.batch_id)
        assert response2.total_items==2

    def testGetBatchExists(self):

        test=ContactControllerApi()
        response=test.get_contact_batch_using_get(batch_id='16')
        assert response.batch_id==16 and response.total_items==1 and response.processed_items==1 and response.status=="Completed"



    def testGetExists(self):

        test=ContactControllerApi()
        response=test.get_contacts_using_get(batch_id='16')
        assert response.total_elements==25 and response.last==False and response.size==20

    def testGetDoesntExists(self):

        test=ContactControllerApi()
        try:
            response=test.get_contacts_using_get(batch_id='12345')
        except VeemError as error:
            assert error.code==50000001#Doesn't exist




if __name__ == '__main__':
    unittest.main()
