from veem.client.responses.page import PageResponse
from veem.client.responses.payment import PaymentResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi

class PaymentClient(Base):

    def __init__(self, config, **kwargs):
        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(create=('post', ''),
                                       send=('post', '/{paymentId}/approve'),
                                       cancel=('post', '/{paymentId}/cancel'),
                                       get=('get', '/{paymentId}'),
                                       list=('get', '')))

    def create(self, request):
        """
            Create a Payment

            @param request: a PaymentRequest
            @return Payment that you just requested
            @throws VeemException If the provided PaymentRequest is invalid, or
                                  if creation fails.
        """
        return self._response_handler(PaymentResponse,
                                 self.client.create(
                                            access_token=self.context.token,
                                            api_route='payments',
                                            **(request.json))
                                     )

    def send(self, paymentId):
        """
            Send a specific payment by id

            @param request: payment id
            @return Payment that you just requested
            @throws VeemException If the provided paymentId is invalid, or
                                  if sending fails.
        """
        return self._response_handler(PaymentResponse,
                                 self.client.send(
                                        uri_params=dict(paymentId=paymentId),
                                        access_token=self.context.token,
                                        api_route='payments')
                                    )

    def cancel(self, paymentId):
        """
            Cancel a specific payment by id

            @param request: payment id
            @return Payment that you just requested
            @throws VeemException If the provided paymentId is invalid, or
                                  if cancelling fails.
        """
        return self._response_handler(PaymentResponse,
                                 self.client.cancel(
                                        uri_params=dict(paymentId=paymentId),
                                        access_token=self.context.token,
                                        api_route='payments')
                                    )

    def get(self, paymentId):
        """
            Get a specific payment by id

            @param request: payment id
            @return Payment that you just requested
            @throws VeemException If the provided paymentId is invalid, or
                                  if retriving fails.
        """
        return self._response_handler(PaymentResponse,
                                 self.client.get(
                                        uri_params=dict(paymentId=paymentId),
                                        access_token=self.context.token,
                                        api_route='payments')
                                    )

    def list(self, parameters={}):
        """
            Get all payments in pagination format

            @param request: a PaymentListParameters or customize dictionary with
                            listing criteria
            @return paginated Payments for your account
        """
        query = {}
        if parameters:
            query = getattr(parameters, 'json', {})
            query['sortParameters'] = ['%s:%s'%(
                    k, v) for field in query.get('sortParameters', {}).items()]
            query['paymentIds'] = ','.join(query.get('paymentIds', [])) or None
            query['status'] = ','.join(query.get('status', [])) or None
            query['sort'] = ','.join(query.pop('sortParameters', [])) or None
            query = {k:v for k,v in query.items() if v is not None}
        return self._list_response_handler(PageResponse,
                                 PaymentResponse,
                                 self.client.list(
                                                request_params=query,
                                                access_token=self.context.token,
                                                api_route='payments')
                                        )
