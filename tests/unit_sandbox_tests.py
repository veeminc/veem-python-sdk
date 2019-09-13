import os
import time
import uuid
import unittest
import warnings

from veem.client.veem import VeemClient
from veem.configuration import ConfigLoader

from veem.client.contact import ContactClient
from veem.client.invoice import InvoiceClient
from veem.client.payment import PaymentClient
from veem.client.customer import CustomerClient
from veem.client.metadata import MetadataClient
from veem.client.attachment import AttachmentClient
from veem.client.exchange_rate import ExchangeRateClient
from veem.client.authentication import AuthenticationClient

from veem.client.requests.contact import ContactRequest
from veem.client.requests.invoice import InvoiceRequest
from veem.client.requests.payment import PaymentRequest
from veem.client.requests.exchange_rate import ExchangeRateRequest

warnings.simplefilter("ignore", ResourceWarning)

class VeemTest(unittest.TestCase):

    def setUp(self):
        self.config_file = os.path.join(
                                os.path.dirname(os.path.realpath(__file__)),
                                'yamls',
                                'mock_config.yaml')
        self.attachment_path = os.path.join(
                                os.path.dirname(os.path.realpath(__file__)),
                                'forUpload.png')
        self.mock_config = ConfigLoader(yaml_file=self.config_file)

    def test_loading_config(self):
        config = ConfigLoader(yaml_file=self.config_file)
        self.assertEqual(config.url, 'https://sandbox-api.veem.com/')

    def test_login(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        self.assertNotEqual(self.mock_config.context.token, None)

        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            self.assertNotEqual(veem.config.context.token, None)

    def test_generate_rate(self):
        request = ExchangeRateRequest(fromAmount=500.0,
                                      fromCurrency='CAD',
                                      fromCountry='CA',
                                      toCurrency='USD',
                                      toCountry='US')
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        rate = ExchangeRateClient(self.mock_config).generate(request)
        self.assertNotEqual(rate.hashId, None)

        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            rate = veem.exchangeRateClient.generate(request)
            self.assertNotEqual(rate.hashId, None)

    def test_country_currency_map(self):
        ccMap = MetadataClient(self.mock_config).getCountryCurrencyMap()
        self.assertTrue(bool(ccMap.content))

        with VeemClient(yaml_file=self.config_file) as veem:
            rate = veem.metadataClient.getCountryCurrencyMap()
            self.assertTrue(bool(ccMap.content))

    def test_customers(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        customers = CustomerClient(self.mock_config).list('devsupport@veem.com')
        self.assertEqual(customers.content[0].email, 'devsupport@veem.com')

        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            customers = veem.customerClient.list('devsupport@veem.com')
            self.assertEqual(customers.content[0].email, 'devsupport@veem.com')

    def test_contacts(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        email_uuid = str(uuid.uuid4())
        email = 'devsupport+{}@veem.com'.format(email_uuid)
        email2 = 'devsupport+{}2@veem.com'.format(email_uuid)
        request = ContactRequest(email=email,
                                 firstName='Wei',
                                 lastName='Chen',
                                 isoCountryCode='GB',
                                 phoneNumber="370-010-0222")
        contact = ContactClient(self.mock_config).create(request)
        self.assertEqual(contact.email, email)
        contacts = ContactClient(self.mock_config).list()
        self.assertTrue(bool(contacts.content))
        self.assertTrue([c for c in contacts.content if c.email == email])
        contact = ContactClient(self.mock_config).get(contact.id)
        self.assertEqual(contact.email, email)
        request.email = email2
        request.batchItemId = 1
        batch = ContactClient(self.mock_config).createBatch([request])
        self.assertEqual(batch.status, 'InProgress')
        time.sleep(5)
        batch = ContactClient(self.mock_config).getBatch(batch.batchId)
        self.assertEqual(batch.status, 'Completed')

    def test_payments(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        request = PaymentRequest(payee=dict(type='Business',
                        email='devsupport+gbp@veem.com',
                        firstName='Wei',
                        lastName='Chen',
                        businessName='GBP Veem Wei',
                        countryCode='GB',
                        phoneCountryCode='44',
                        phone='03700100222'),
             amount=dict(number=50, currency='GBP'))
        payment = PaymentClient(self.mock_config).create(request)
        self.assertEqual(payment.payee.email, 'devsupport+gbp@veem.com')
        self.assertEqual(payment.amount.currency, 'GBP')
        self.assertEqual(payment.status, 'Drafted')
        payment = PaymentClient(self.mock_config).get(payment.id)
        self.assertEqual(payment.status, 'Drafted')
        payment = PaymentClient(self.mock_config).send(payment.id)
        self.assertEqual(payment.status, 'Sent')
        payment = PaymentClient(self.mock_config).cancel(payment.id)
        self.assertEqual(payment.status, 'Cancelled')
        payments = PaymentClient(self.mock_config).list()
        payment = payments.content[0]
        self.assertEqual(payment.amount.currency, 'GBP')
        self.assertEqual(payment.status, 'Cancelled')

        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            payment = veem.paymentClient.create(request)
            self.assertEqual(payment.payee.email, 'devsupport+gbp@veem.com')
            self.assertEqual(payment.amount.currency, 'GBP')
            self.assertEqual(payment.status, 'Drafted')
            payment = veem.paymentClient.get(payment.id)
            self.assertEqual(payment.status, 'Drafted')
            payment = veem.paymentClient.send(payment.id)
            self.assertEqual(payment.status, 'Sent')
            payment = veem.paymentClient.cancel(payment.id)
            self.assertEqual(payment.status, 'Cancelled')
            payments = veem.paymentClient.list()
            payment = payments.content[0]
            self.assertEqual(payment.status, 'Cancelled')

    def test_invoices(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        request = InvoiceRequest(payer=dict(type='Business',
                        email='devsupport+gbp@veem.com',
                        firstName='Wei',
                        lastName='Chen',
                        businessName='GBP Veem Wei',
                        countryCode='GB',
                        phoneCountryCode='44',
                        phone='03700100222'),
             status='Drafted',
             amount=dict(number=50, currency='GBP'))
        invoice = InvoiceClient(self.mock_config).create(request)
        self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
        self.assertEqual(invoice.amount.currency, 'GBP')
        # self.assertEqual(invoice.status, 'Drafted')
        invoice = InvoiceClient(self.mock_config).get(invoice.id)
        # self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
        self.assertEqual(invoice.amount.currency, 'GBP')
        # self.assertEqual(invoice.status, 'Drafted')
        # invoice = InvoiceClient(self.mock_config).send(invoice.id)
        # self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
        # self.assertEqual(invoice.amount.currency, 'GBP')
        # self.assertEqual(invoice.status, 'Sent')
        invoice = InvoiceClient(self.mock_config).cancel(invoice.id)
        self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
        self.assertEqual(invoice.amount.currency, 'GBP')
        self.assertEqual(invoice.status, 'Cancelled')

        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            invoice = veem.invoiceClient.create(request)
            self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
            self.assertEqual(invoice.amount.currency, 'GBP')
            # self.assertEqual(invoice.status, 'Drafted')
            invoice = veem.invoiceClient.get(invoice.id)
            # self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
            self.assertEqual(invoice.amount.currency, 'GBP')
            # self.assertEqual(invoice.status, 'Drafted')
            # invoice = veem.invoiceClient.send(invoice.id)
            # self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
            # self.assertEqual(invoice.amount.currency, 'GBP')
            # self.assertEqual(invoice.status, 'Sent')
            invoice = veem.invoiceClient.cancel(invoice.id)
            self.assertEqual(invoice.payer.email, 'devsupport+gbp@veem.com')
            self.assertEqual(invoice.amount.currency, 'GBP')
            self.assertEqual(invoice.status, 'Cancelled')

    def test_attachments(self):
        AuthenticationClient(self.mock_config).getTokenFromClientCredentials()
        attachment = AttachmentClient(self.mock_config).upload(
                        dict(path=self.attachment_path),
                        'invoice for shipping')
        self.assertTrue(bool(attachment.referenceId))
        attachment = AttachmentClient(self.mock_config).download(attachment)
        self.assertTrue(bool(attachment))
        with VeemClient(yaml_file=self.config_file,
                        useClientCredentials=True) as veem:
            attachment = veem.attachmentClient.upload(
                            dict(path=self.attachment_path),
                            'invoice for shipping')
            self.assertTrue(bool(attachment.referenceId))
            attachment = veem.attachmentClient.download(attachment)
            self.assertTrue(bool(attachment))

if __name__ == '__main__':
    unittest.main()
