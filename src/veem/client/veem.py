from veem.configuration import ConfigLoader

from veem.client.payment import PaymentClient
from veem.client.invoice import InvoiceClient
from veem.client.contact import ContactClient
from veem.client.metadata import MetadataClient
from veem.client.customer import CustomerClient
from veem.client.attachment import AttachmentClient
from veem.client.exchange_rate import ExchangeRateClient
from veem.client.authentication import AuthenticationClient

class VeemClient(object):
    """
        The Context Manager for Veem SDK Client
    """
    def __init__(self,
                 yaml_file=None,
                 configs=None,
                 useClientCredentials=False,
                 useAuthorizationCode=False,
                 **kwargs):
        self.config = ConfigLoader(yaml_file=yaml_file, configs=configs)

        self.paymentClient = PaymentClient(self.config, **kwargs)
        self.invoiceClient = InvoiceClient(self.config, **kwargs)
        self.contactClient = ContactClient(self.config, **kwargs)
        self.metadataClient = MetadataClient(self.config, **kwargs)
        self.customerClient = CustomerClient(self.config, **kwargs)
        self.attachmentClient = AttachmentClient(self.config, **kwargs)
        self.exchangeRateClient = ExchangeRateClient(self.config, **kwargs)
        self.authenticationClient = AuthenticationClient(self.config, **kwargs)

        if useClientCredentials:
            self.authenticationClient.getTokenFromClientCredentials()
        elif useAuthorizationCode:
            self.authenticationClient.getTokenFromAuthorizationCode()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return False
