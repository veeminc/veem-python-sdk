from veem.client.responses.page import PageResponse
from veem.client.responses.invoice import InvoiceResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi

class InvoiceClient(Base):

    def __init__(self, config, **kwargs):
        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(create=('post', ''),
                                       send=('post', '/{invoiceId}/approve'),
                                       cancel=('post', '/{invoiceId}/cancel'),
                                       get=('get', '/{invoiceId}')))

    def create(self, request):
        """
            Create an Invoice

            @param request: an InvoiceRequest
            @return Invoice that you just requested
            @throws VeemException If the provided InvoiceRequest is invalid, or
                                  if creation fails.
        """
        return self._response_handler(InvoiceResponse,
                                 self.client.create(
                                            access_token=self.context.token,
                                            api_route='invoices',
                                            **(request.json))
                                     )

    def send(self, invoiceId):
        """
            Send a specific invoice by id

            @param request: invoice id
            @return Invoice that you just requested
            @throws VeemException If the provided invoiceId is invalid, or
                                  if sending fails.
        """
        return self._response_handler(InvoiceResponse,
                                 self.client.send(
                                        uri_params=dict(invoiceId=invoiceId),
                                        access_token=self.context.token,
                                        api_route='invoices')
                                    )

    def cancel(self, invoiceId):
        """
            Cancel a specific invoice by id

            @param request: invoice id
            @return Invoice that you just requested
            @throws VeemException If the provided invoiceId is invalid, or
                                  if cancelling fails.
        """
        return self._response_handler(InvoiceResponse,
                                 self.client.cancel(
                                        uri_params=dict(invoiceId=invoiceId),
                                        access_token=self.context.token,
                                        api_route='invoices')
                                    )

    def get(self, invoiceId):
        """
            Get a specific invoice by id

            @param request: invoice id
            @return Invoice that you just requested
            @throws VeemException If the provided invoiceId is invalid, or
                                  if retriving fails.
        """
        return self._response_handler(InvoiceResponse,
                                 self.client.get(
                                        uri_params=dict(invoiceId=invoiceId),
                                        access_token=self.context.token,
                                        api_route='invoices')
                                    )
