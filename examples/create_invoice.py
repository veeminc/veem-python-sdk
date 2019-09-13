
from veem.client.veem import VeemClient
from veem.client.requests.invoice import InvoiceRequest

if __name__ == '__main__':

    # define a VeemClient Context Manager with yaml+file and auto login.
    with VeemClient(yaml_file='/path/to/your/configuration.yaml',
                    useClientCredentials=True) as veem:
        # define an InvoiceRequest
        invoice = InvoiceRequest(payer=dict(type='Business',
                                            email='username@yourbusiness.com',
                                            firstName='Joe',
                                            lastName='Doe',
                                            businessName='Your Business Inc.',
                                            countryCode='US',
                                            phoneCountryCode='1',
                                            phone='02222222222'),
             amount=dict(number=50, currency='USD'))
        # create an invoice
        sendInvoice = veem.inoviceClient.create(invoice)
