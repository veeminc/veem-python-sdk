

from __future__ import absolute_import
import requests
import re  # noqa: F401
import json


import six
from Veem.VeemError import VeemError
from Veem.models.payment_response import PaymentResponse
from Veem.models.payments_response import PaymentsResponse
from Veem.api_client import ApiClient
import uuid
from Veem.configuration import Configuration


class PaymentControllerApi(object):


    def __init__(self, api_client=None, access_token):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.payment_url=self.config.host+"payments"
        self.access_token=access_token

    def deserializePayments(self,response):
        content=response['content']
        totalElements=response['totalElements']
        totalPages=response['totalPages']
        last=response['last']
        sort=response['sort']
        first=response['first']
        numberOfElements=response['numberOfElements']
        size=response['size']
        number=response['number']
        payments=PaymentsResponse(totalElements=totalElements, totalPages=totalPages, last=last, sort=sort, first=first, numberOfElements=numberOfElements, number=number, size=size, content=content)
        return payments

    def deserialize(self,response):
            requestId=response['requestId']

            try:
                attachments=response['attachments']
                type=attachments[2]
                name=attachments[0]
                referenceId=attachments[1]
            except KeyError as k:
                type=None
                name=None
                referenceId=None

            payee=response['payee']
            email=payee['email']
            countryCode=payee['countryCode']
            phone=payee['phone']

            payeeAmount=response['payeeAmount']
            number=payeeAmount['number']
            currency=payeeAmount['currency']

            id=response['id']
            status=response['status']

            exchangeRate=response['exchangeRate']
            fromAmount=exchangeRate['fromAmount']
            toAmount=exchangeRate['toAmount']
            fromCurrency=exchangeRate['fromCurrency']
            toCurrency=exchangeRate['toCurrency']

            try:
                claimLink=response['claimLink']
            except KeyError as k:
                claimLink=None

            responseObject=PaymentResponse(request_id=requestId, payee_email=email, payee_country_code=countryCode, payee_phone=phone, payee_amount_number=number, payee_amount_currency=currency, status=status, id=id, exchange_rate_from_amount=fromAmount,exchange_rate_to_amount=toAmount,exchange_rate_from_currency=fromCurrency, exchange_rate_to_currency=toCurrency,claim_link=claimLink)
            return responseObject

    def approve_payment_using_post(self, payment_id, **kwargs):  # noqa: E501
        """approvePayment  # noqa: E501

        approve a payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.approve_payment_using_post(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.approve_payment_using_post_with_http_info(payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.approve_payment_using_post_with_http_info(payment_id, **kwargs)  # noqa: E501
            return data

    def approve_payment_using_post_with_http_info(self, payment_id, **kwargs):  # noqa: E501
        """approvePayment  # noqa: E501

        approve a payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.approve_payment_using_post_with_http_info(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method approve_payment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `approve_payment_using_post`")  # noqa: E501
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token
        url = self.payment_url+"/"+str(payment_id)+"/approve"

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501


        response = requests.request("POST", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err

    def create_payment_using_post(self, request, **kwargs):  # noqa: E501
        """createPayment  # noqa: E501

        post a payment and sends to receiver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_using_post(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param PaymentRequest request: request (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_payment_using_post_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_using_post_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def create_payment_using_post_with_http_info(self, request, **kwargs):  # noqa: E501
        """createPayment  # noqa: E501

        post a payment and sends to receiver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_using_post_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param PaymentRequest request: request (required)
        :return: PaymentResponse
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
                    " to method create_payment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_payment_using_post`")  # noqa: E501
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token
        url = self.payment_url

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501


        auth_settings = ['oauth']  # noqa: E501
        response = requests.request("POST", url,headers=header_params,data=json.dumps(request.to_dict()))
        if(response.status_code==201):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err

    def get_payment_using_get(self, payment_id, **kwargs):  # noqa: E501
        """getPayment  # noqa: E501

        get payment details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_using_get(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_payment_using_get_with_http_info(payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_using_get_with_http_info(payment_id, **kwargs)  # noqa: E501
            return data

    def get_payment_using_get_with_http_info(self, payment_id, **kwargs):  # noqa: E501
        """getPayment  # noqa: E501

        get payment details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_using_get_with_http_info(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `get_payment_using_get`")  # noqa: E501
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501
        header_params['Authorization']=self.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        url=self.payment_url+"/"+payment_id
        response = requests.request("GET", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err


    def get_payments_by_status_using_get(self, **kwargs):  # noqa: E501
        """getPaymentsByStatus  # noqa: E501

        get payments for this account, filtered by status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payments_by_status_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: status
        :param int page_number: pageNumber
        :param int page_size: pageSize
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_payments_by_status_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_payments_by_status_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_payments_by_status_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getPaymentsByStatus  # noqa: E501

        get payments for this account, filtered by status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payments_by_status_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: status
        :param int page_number: pageNumber
        :param int page_size: pageSize
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_by_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501


        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        querystring={}
        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501
        if 'status' in kwargs:
            status=kwargs['status']
            querystring = {"status":status}

        header_params['Authorization']=self.access_token
        url = self.payment_url

        response = requests.request("GET", url,headers=header_params, params=querystring)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserializePayments(object)
            return response_object
        else:
            print(response.status_code)
            err = VeemError(response)
            raise err
            return err

    def cancel_payment_using_post(self, payment_id, **kwargs):  # noqa: E501
        """cancelPayment  # noqa: E501

        cancel a payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reject_payment_using_post(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.cancel_payment_using_post_with_http_info(payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_payment_using_post_with_http_info(payment_id, **kwargs)  # noqa: E501
            return data

    def cancel_payment_using_post_with_http_info(self, payment_id, **kwargs):  # noqa: E501
        """cancelPayment  # noqa: E501

        cancel a payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reject_payment_using_post_with_http_info(payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int payment_id: paymentId (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reject_payment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `reject_payment_using_post`")  # noqa: E501
        header_params={}

        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.access_token
        url = self.payment_url+"/"+str(payment_id)+"/cancel"
        header_params['X-REQUEST-ID']=str(uuid.uuid4())
        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        response = requests.request("POST", url,headers=header_params)
        if(response.status_code==200):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            err = VeemError(response)
            raise err
            return err
