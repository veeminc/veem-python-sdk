
from __future__ import absolute_import

import re  # noqa: F401
import requests
# python 2 and python 3 compatibility library
import six
import uuid

from Veem.api_client import ApiClient
import json
from Veem.VeemError import VeemError
from Veem.models.customer_response import CustomerResponse
from Veem.configuration import Configuration



class CustomerControllerApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.customer_url=self.config.host+"customers"

    def deserialize(self, response):
        totalElements=response['totalElements']
        totalPages=response['totalPages']
        last=response['last']
        sort=response['sort']
        first=response['first']
        numberOfElements=response['numberOfElements']
        size=response['size']
        number=response['number']
        content=response['content']
        responseObject=CustomerResponse(totalElements=totalElements, totalPages=totalPages, last=last, sort=sort, first=first, numberOfElements=numberOfElements, number=number, size=size, content=content)
        return responseObject

    def search_customers_using_get(self, email, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_customers_using_get_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.search_customers_using_get_with_http_info(email, **kwargs)  # noqa: E501
            return data


    def search_customers_using_get_with_http_info(self, email, **kwargs):  # noqa: E501

        all_params = ['email']  # noqa: E501
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
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `search_customers_using_get`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.config.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        querystring = {"email":email}
        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url = self.customer_url
        response = requests.request("GET", url, headers=header_params,params=querystring)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err
