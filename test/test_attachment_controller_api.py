

from __future__ import absolute_import

import unittest
import uuid
import Veem
from Veem.api.attachment_controller_api import AttachmentControllerApi  # noqa: E501
from Veem.rest import ApiException
import requests
from Veem.VeemError import VeemError
from test.configuration import Configuration



class TestAttachmentControllerApi(unittest.TestCase):


    def setUp(self):
        self.config=Configuration()
        self.api = AttachmentControllerApi(self.config.access_token)  # noqa: E501


    def tearDown(self):
        pass

    def testDownloadNoName(self):

        test=AttachmentControllerApi(self.config.access_token)
        try:
            result=test.download_attachment_using_get(reference_id='1345')
        except VeemError as err:
            assert err.message=="Need to specify name"

    def testDownloadNoId(self):

        test=AttachmentControllerApi(self.config.access_token)
        try:
            result=test.download_attachment_using_get(name='1345')
        except VeemError as err:
            assert err.message=="Need to specify referenceId"

    def testUploadExists(self):

        test=AttachmentControllerApi(self.config.access_token)
        result=test.upload_attachment_using_post(file="3.PNG")
        assert result.name=="3.PNG" and result.reference_id is not None
        print(result.reference_id)

    def testDownloadExists(self):

        test=AttachmentControllerApi(self.config.access_token)
        result=test.upload_attachment_using_post(file="3.PNG")
        downloaded=test.download_attachment_using_get(name=result.name, reference_id=result.reference_id)
        print(downloaded.text)

    def testUploadNonexistant(self):

        test=AttachmentControllerApi(self.config.access_token)
        try:
            result=test.upload_attachment_using_post(file="2.png")
        except VeemError as err:
            assert err.message=="File doesn't exist"

if __name__ == '__main__':
    unittest.main()
