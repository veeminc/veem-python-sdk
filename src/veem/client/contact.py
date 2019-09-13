from collections.abc import Iterable

from veem.client.responses.page import PageResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi
from veem.models.batch import Batch
from veem.models.contact import Contact

class ContactClient(Base):

    def __init__(self, config, **kwargs):
        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(create=('post', ''),
                                       get=('get', '/{contactId}'),
                                       list=('get', ''),
                                       createBatch=('post', '/batch'),
                                       getBatch=('get', '/batch/{batchId}')))

    def create(self, request):
        """
            Create a contact

            @param request: a ContactRequest
            @return Contact that you just requested
            @throws VeemException If the provided ContactRequest is invalid, or
                                  if creation fails.
        """
        return self._response_handler(Contact,
                                 self.client.create(
                                            access_token=self.context.token,
                                            api_route='contacts',
                                            **(request.json))
                                     )

    def get(self, contactId):
        """
            Get a specific contact by id

            @param request: contact id
            @return Contact that you just requested
            @throws VeemException If the provided contactId is invalid, or
                                  if retriving fails.
        """
        return self._response_handler(Contact,
                                 self.client.get(
                                        uri_params=dict(contactId=contactId),
                                        access_token=self.context.token,
                                        api_route='contacts')
                                    )

    def list(self, parameters={}):
        """
            Get all contacts in pagination format

            @param request: a ContactListParameters
            @return paginated Contacts for your account
        """
        query = {}
        if parameters:
            query = getattr(parameters, 'json', {})
            query['batchItemIds'] = ','.join(query.get('batchItemIds',
                                                       [])) or None
            query = {k:v for k,v in query.items() if v is not None}
        return self._list_response_handler(PageResponse,
                                 Contact,
                                 self.client.list(
                                                request_params=query,
                                                access_token=self.context.token,
                                                api_route='contacts')
                                        )

    def createBatch(self, contactRequests):
        """
            Create a batch of contacts

            @param request: a list of ContactRequest
            @return contact batch
            @throws VeemException If the provided request is invalid, or
                                  if creating fails.
        """
        contactRequests = contactRequests if isinstance(
                                contactRequests, Iterable) else []
        contactRequests = [getattr(r, 'json', {}) for r in contactRequests]
        return self._response_handler(Batch,
                                 self.client.createBatch(
                                            access_token=self.context.token,
                                            api_route='contacts',
                                            request_body=contactRequests)
                                     )

    def getBatch(self, batchId):
        """
            Get a specific contacts batch

            @param request: Batch id
            @return contact batch
            @throws VeemException If the provided batchId is invalid, or
                                  if retriving fails.
        """
        return self._response_handler(Batch,
                                 self.client.getBatch(
                                        uri_params=dict(batchId=batchId),
                                        access_token=self.context.token,
                                        api_route='contacts')
                                    )
