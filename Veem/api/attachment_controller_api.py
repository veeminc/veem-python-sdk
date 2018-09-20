

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
import uuid


from Veem.api_client import ApiClient
from Veem.configuration import Configuration
import requests
from Veem.models.attachment_response import AttachmentResponse
import json
from Veem.VeemError import VeemError
import os.path
import magic



class AttachmentControllerApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config=Configuration()
        self.attachment_url=self.config.host+"attachments"

    def deserialize(self,response):
        name=response['name']
        referenceId=response['referenceId']
        object=AttachmentResponse(name=name, reference_id=referenceId)
        return object

    def download_attachment_using_get(self, **kwargs):  # noqa: E501
        """Downloads the referenced file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.download_attachment_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name from the upload response
        :param str reference_id: The unique reference ID from the upload response
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.download_attachment_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.download_attachment_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def download_attachment_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Downloads the referenced file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.download_attachment_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name from the upload response
        :param str reference_id: The unique reference ID from the upload response
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'reference_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_attachment_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'reference_id' in params:
            query_params.append(('referenceId', params['reference_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        header_params['Authorization']=self.config.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501
        url=self.attachment_url

        if 'name' in kwargs:
            name=kwargs['name']
        else:
            raise VeemError("Need to specify name")

        if 'reference_id' in kwargs:
            refId=kwargs['reference_id']
        else:
            raise VeemError("Need to specify referenceId")

        querystring={"name":name, "referenceId": refId}
        response = requests.post(url, params=querystring, headers=header_params)
        if(response.status_code==200):
            object=response.json()
            return object
        else:
            print(response)
            err = VeemError(response)
            raise err
            return err



    def upload_attachment_using_post(self, file, **kwargs):  # noqa: E501
        """Uploads the external attachment for an entity Payment or Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.upload_attachment_using_post(file, async=True)
        >>> result = thread.get()

        :param async bool
        :param file file: file (required)
        :return: FileAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.upload_attachment_using_post_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_attachment_using_post_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def upload_attachment_using_post_with_http_info(self, file, **kwargs):  # noqa: E501
        """Uploads the external attachment for an entity Payment or Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.upload_attachment_using_post_with_http_info(file, async=True)
        >>> result = thread.get()

        :param async bool
        :param file file: file (required)
        :return: FileAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_attachment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_attachment_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        header_params['Content-Type'] = "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        header_params['Authorization']=self.config.access_token

        header_params['X-REQUEST-ID']=str(uuid.uuid4())

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501
        url=self.attachment_url
        if os.path.isfile(file) is not True:
            raise VeemError("File doesn't exist")

        type=magic.from_file(file, mime=True)
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+file+"\"\r\nContent-Type: "+type+"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        response = requests.post(url, data=payload, headers=header_params)
        if(response.status_code==201):
            object=response.json()
            response_object=self.deserialize(object)
            return response_object
        else:
            print(response)
            err = VeemError(response)
            raise err
            return err
