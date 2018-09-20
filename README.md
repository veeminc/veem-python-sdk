# swagger-client
Veem REST API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [veem.com](veem.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = swagger_client.AccountControllerApi()
request = [swagger_client.ContactRequest()] # list[ContactRequest] | request

try:
    # createContactInBatch
    api_response = api_instance.create_contact_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->create_contact_using_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-api.veem.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountControllerApi* | [**create_contact_using_post**](docs/AccountControllerApi.md#create_contact_using_post) | **POST** /veem/v1.0/accounts/contacts/batch | createContactInBatch
*AccountControllerApi* | [**create_contact_using_post1**](docs/AccountControllerApi.md#create_contact_using_post1) | **POST** /veem/v1.0/accounts/contacts | createContact
*AttachmentControllerApi* | [**download_attachment_using_get**](docs/AttachmentControllerApi.md#download_attachment_using_get) | **GET** /veem/v1.0/attachments | Downloads the referenced file
*AttachmentControllerApi* | [**upload_attachment_using_post**](docs/AttachmentControllerApi.md#upload_attachment_using_post) | **POST** /veem/v1.0/attachments | Uploads the external attachment for an entity Payment or Invoice
*ExchangeRateControllerApi* | [**generate_exchange_quote_using_post**](docs/ExchangeRateControllerApi.md#generate_exchange_quote_using_post) | **POST** /veem/v1.0/exchangerates/quotes | createQuote
*InvoiceControllerApi* | [**approve_invoice_using_post**](docs/InvoiceControllerApi.md#approve_invoice_using_post) | **POST** /veem/v1.0/invoices/{invoiceId}/approve | approveInvoice
*InvoiceControllerApi* | [**cancel_invoice_using_post**](docs/InvoiceControllerApi.md#cancel_invoice_using_post) | **POST** /veem/v1.0/invoices/{invoiceId}/cancel | cancelInvoice
*InvoiceControllerApi* | [**create_invoice_using_post**](docs/InvoiceControllerApi.md#create_invoice_using_post) | **POST** /veem/v1.0/invoices | createInvoice
*InvoiceControllerApi* | [**get_invoice_using_get**](docs/InvoiceControllerApi.md#get_invoice_using_get) | **GET** /veem/v1.0/invoices/{invoiceId} | getInvoice
*MetaControllerApi* | [**get_country_currency_map_using_get**](docs/MetaControllerApi.md#get_country_currency_map_using_get) | **GET** /veem/public/v1.0/country-currency-map | Country Currency Map
*MetaControllerApi* | [**hello_world_using_get**](docs/MetaControllerApi.md#hello_world_using_get) | **GET** /veem/v1.0/hello | Hello Test
*PaymentControllerApi* | [**approve_payment_using_post**](docs/PaymentControllerApi.md#approve_payment_using_post) | **POST** /veem/v1.0/payments/{paymentId}/approve | approvePayment
*PaymentControllerApi* | [**create_payment_using_post**](docs/PaymentControllerApi.md#create_payment_using_post) | **POST** /veem/v1.0/payments | createPayment
*PaymentControllerApi* | [**get_payment_using_get**](docs/PaymentControllerApi.md#get_payment_using_get) | **GET** /veem/v1.0/payments/{paymentId} | getPayment
*PaymentControllerApi* | [**get_payments_by_status_using_get**](docs/PaymentControllerApi.md#get_payments_by_status_using_get) | **GET** /veem/v1.0/payments | getPaymentsByStatus
*PaymentControllerApi* | [**reject_payment_using_post**](docs/PaymentControllerApi.md#reject_payment_using_post) | **POST** /veem/v1.0/payments/{paymentId}/cancel | cancelPayment


## Documentation For Models

 - [AlignMonetaryAmount](docs/AlignMonetaryAmount.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [ContactResponse](docs/ContactResponse.md)
 - [CountryCurrencyResponse](docs/CountryCurrencyResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExchangeRateRequest](docs/ExchangeRateRequest.md)
 - [ExchangeRateResponse](docs/ExchangeRateResponse.md)
 - [FileAttachment](docs/FileAttachment.md)
 - [InvoiceRequest](docs/InvoiceRequest.md)
 - [InvoiceResponse](docs/InvoiceResponse.md)
 - [PagePaymentResponse](docs/PagePaymentResponse.md)
 - [PaymentRequest](docs/PaymentRequest.md)
 - [PaymentResponse](docs/PaymentResponse.md)
 - [PushPaymentInfoResponse](docs/PushPaymentInfoResponse.md)
 - [SimpleAccount](docs/SimpleAccount.md)
 - [Sort](docs/Sort.md)


## Documentation For Authorization


## oauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://sandbox-api.veem.com/oauth/authorize
- **Scopes**: N/A


## Author

dev@veem.com
