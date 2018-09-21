
from __future__ import absolute_import

import re  # noqa: F401
import requests
# python 2 and python 3 compatibility library
import six
import uuid


from Veem.api_client import ApiClient
import json
from Veem.VeemError import VeemError
from Veem.models.contact_response import ContactResponse
from Veem.configuration import Configuration
from Veem.models.contact_list_response import ContactListResponse



class ContactControllerApi(object):


    def __init__(self, api_client=None, acess_token):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.contact_url=self.config.host+"contacts"
        self.access_token=access_token

    def deserialize(self, response):
        batchId=response['batchId']
        totalItems=response['totalItems']
        processedItems=response['processedItems']
        hasErrors=response['hasErrors']
        status=response['status']
        try:
            batchItems=response['batchItems']
        except KeyError as k:
            batchItems=None
        contactResponseObject=ContactResponse(batchItems=batchItems,batchId=batchId, totalItems=totalItems, processedItems=processedItems, hasErrors=hasErrors, status=status)
        return contactResponseObject

    def deserialize_list(self, response):
        content=response['content']
        totalElements=response['totalElements']
        last=response['last']
        first=response['first']
        totalPages=response['totalPages']
        numberOfElements=response['numberOfElements']
        size=response['size']
        number=response['number']
        list_response=ContactListResponse(content=content, totalElements=totalElements, totalPages=totalPages, first=first, last=last, size=size, number=number, numberOfElements=numberOfElements)
        return list_response

    def get_contact_batch_using_get(self, batch_id, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_contact_batch_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contact_batch_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
            return data


    def get_contact_batch_using_get_with_http_info(self, batch_id, **kwargs):  # noqa: E501

        all_params = ['batch_id', 'include_items']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_exchange_quote_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('batch_id' not in params or
                params['batch_id'] is None):
            raise ValueError("Missing the required parameter `batch_id` when calling `get_contatct_batch_using_get`")  # noqa: E501

        header_params={}
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        querystring=None


        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.contact_url+"/batch/"+str(batch_id)
        response = requests.request("GET", url, headers=header_params,params=querystring)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err

    def get_contacts_using_get(self, batch_id, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_contacts_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contacts_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
            return data


    def get_contacts_using_get_with_http_info(self, batch_id, **kwargs):  # noqa: E501

        all_params = ['batch_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_exchange_quote_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('batch_id' not in params or
                params['batch_id'] is None):
            raise ValueError("Missing the required parameter `batch_id` when calling `get_contatct_batch_using_get`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        querystring=None


        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.contact_url
        response = requests.request("GET", url, headers=header_params,params=batch_id)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize_list(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err



    def create_contacts_using_post(self, contacts, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_contacts_using_post_with_http_info(contacts, **kwargs)  # noqa: E501
        else:
            (data) = self.create_contacts_using_post_with_http_info(contacts, **kwargs)  # noqa: E501
            return data


    def create_contacts_using_post_with_http_info(self, contacts,**kwargs):  # noqa: E501

        all_params = ['contacts']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_exchange_quote_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        querystring=None

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.contact_url+"/batch"
        response = requests.request("POST", url, headers=header_params,data=json.dumps(contacts))
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err
