from __future__ import absolute_import

import sys


import re  # noqa: F401
import requests
# python 2 and python 3 compatibility library
import six
import uuid
from Veem.api_client import ApiClient
import json
from Veem.VeemError import VeemError
from Veem.models.exchange_rate_response import ExchangeRateResponse
from Veem.configuration import Configuration


class ExchangeRateControllerApi(object):


    def __init__(self, access_token,api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.exchange_url=self.config.host+"exchangerates/quotes"
        self.access_token=access_token

    def create_quote_using_post(self, request, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.generate_exchange_quote_using_post_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_exchange_quote_using_post_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def deserialize(self,response):
            id=response['id']
            fromAmount=response['fromAmount']
            toAmount=response['toAmount']
            expiry=response['expiry']
            rate=response['rate']
            fromCurrency=response['fromCurrency']
            toCurrency=response['toCurrency']
            responseObject=ExchangeRateResponse(id=id, from_amount=fromAmount, to_amount=toAmount, expiry=expiry, rate=rate, from_currency=fromCurrency, to_currency=toCurrency)
            return responseObject

    def generate_exchange_quote_using_post_with_http_info(self, request, **kwargs):  # noqa: E501
        """createQuote  # noqa: E501

        Submits a request to generate an exchange rate quote  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.generate_exchange_quote_using_post_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param ExchangeRateRequest request: request (required)
        :return: ExchangeRateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
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
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `generate_exchange_quote_using_post`")  # noqa: E501

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url=self.exchange_url
        response = requests.request("POST", url, headers=header_params,data=json.dumps(request.to_dict()))
        if(response.status_code==201):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err
