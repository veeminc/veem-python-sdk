# Veem Python SDK
Veem REST API

For more information, please visit [veem.com](veem.com)
For developer documentation, please visit [developer website](developer.veem.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### (test version) - pip install --extra-index-url https://testpypi.python.org/pypi veem-python
### (final version) - pip install veem-python

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-api.veem.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentControllerApi* | [**download_attachment_using_get**](Veem/api/attachment_controller_api.py#download_attachment_using_get) | **GET** /veem/v1.0/attachments | Downloads the referenced file
*AttachmentControllerApi* | [**upload_attachment_using_post**](Veem/api/attachment_controller_api.py#upload_attachment_using_post) | **POST** /veem/v1.0/attachments | Uploads the external attachment for an entity Payment or Invoice
*ExchangeRateControllerApi* | [**generate_exchange_quote_using_post**](Veem/api/exchange_rate_controller_api.py#generate_exchange_quote_using_post) | **POST** /veem/v1.0/exchangerates/quotes | createQuote
*InvoiceControllerApi* | [**approve_invoice_using_post**](Veem/api/invoice_controller_api.py#approve_invoice_using_post) | **POST** /veem/v1.0/invoices/{invoiceId}/approve | approveInvoice
*InvoiceControllerApi* | [**cancel_invoice_using_post**](Veem/api/invoice_controller_api.py#cancel_invoice_using_post) | **POST** /veem/v1.0/invoices/{invoiceId}/cancel | cancelInvoice
*InvoiceControllerApi* | [**create_invoice_using_post**](Veem/api/invoice_controller_api.py#create_invoice_using_post) | **POST** /veem/v1.0/invoices | createInvoice
*InvoiceControllerApi* | [**get_invoice_using_get**](Veem/api/invoice_controller_api.py#get_invoice_using_get) | **GET** /veem/v1.0/invoices/{invoiceId} | getInvoice
*MetaControllerApi* | [**get_country_currency_map_using_get**](Veem/api/meta_controller_api.py#get_country_currency_map_using_get) | **GET** /veem/public/v1.0/country-currency-map | Country Currency Map
*PaymentControllerApi* | [**approve_payment_using_post**](Veem/api/payment_controller_api.py#approve_payment_using_post) | **POST** /veem/v1.0/payments/{paymentId}/approve | approvePayment
*PaymentControllerApi* | [**create_payment_using_post**](Veem/api/payment_controller_api.py#create_payment_using_post) | **POST** /veem/v1.0/payments | createPayment
*PaymentControllerApi* | [**get_payment_using_get**](Veem/api/payment_controller_api.py#get_payment_using_get) | **GET** /veem/v1.0/payments/{paymentId} | getPayment
*PaymentControllerApi* | [**get_payments_by_status_using_get**](Veem/api/payment_controller_api.py#get_payments_by_status_using_get) | **GET** /veem/v1.0/payments | getPaymentsByStatus
*PaymentControllerApi* | [**reject_payment_using_post**](Veem/api/payment_controller_api.py#reject_payment_using_post) | **POST** /veem/v1.0/payments/{paymentId}/cancel | cancelPayment


## Documentation For Models

 - [AlignMonetaryAmount](Veem/models/align_monetary_amount.py)
 - [ContactRequest](Veem/models/contact_request.py)
 - [ContactListResponse](Veem/models/contact_list_response.py)
 - [ContactResponse](Veem/models/contact_response.py)
 - [CountryCurrencyResponse](Veem/models/country_currency_response.py)
 - [CustomerResponse](Veem/models/customer_response.py)
 - [ExchangeRateRequest](Veem/models/exchange_rate_request.py)
 - [ExchangeRateResponse](Veem/models/exchange_rate_response.py)
 - [InvoiceRequest](Veem/models/invoice_request.py)
 - [InvoiceResponse](Veem/models/invoice_response.py)
 - [PaymentRequest](Veem/models/payment_request.py)
 - [PaymentResponse](Veem/models/payment_response.py)
 - [PaymentsReponse](Veem/models/payments_response.py)



## Documentation For Authorization


## oauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://sandbox-api.veem.com/oauth/authorize
- **Scopes**: N/A


## Author

devsupport@veem.com

