# Veem Python SDK
Veem REST API

For more information, please visit [veem.com](veem.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install veem-python

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-api.veem.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentControllerApi* | [**download_attachment_using_get**](Veem/api/AttachmentControllerApi.py#download_attachment_using_get) | **GET** /veem/v1.0/attachments | Downloads the referenced file
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

