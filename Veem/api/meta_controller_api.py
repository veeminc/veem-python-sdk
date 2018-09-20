

from __future__ import absolute_import

import re  # noqa: F401


import six
import json
import uuid
from Veem.api_client import ApiClient
from Veem.VeemError import VeemError
import requests
from Veem.configuration import Configuration

class MetaControllerApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()

    def get_country_currency_map_using_get(self, **kwargs):  # noqa: E501
        """Country Currency Map  # noqa: E501

        Returns a list of countries supported and currencies for each  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_currency_map_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[CountryCurrencyResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_country_currency_map_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_country_currency_map_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_country_currency_map_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Country Currency Map  # noqa: E501

        Returns a list of countries supported and currencies for each  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_currency_map_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[CountryCurrencyResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bankFields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_country_currency_map_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        header_params['Authorization']=self.config.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        querystring={}
        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501
        if 'bankFields' in kwargs:
            if kwargs['bankFields']==False:
                querystring = {"bankFields":"false"}
            elif kwargs['bankFields']==True:
                querystring = {"bankFields":"true"}
            else:
                raise ValueError("Must enter a boolean for bankFields")

        url = "https://sandbox-api.veem.com//veem/public/v1.0/country-currency-map"

        response = requests.request("GET", url, headers=header_params, params=querystring)

        if(response.status_code==200):
            object=response.json()
            return object
        else:
            err = VeemError(response)
            raise err
            return err
