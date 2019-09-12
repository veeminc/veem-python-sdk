Veem-Python-Sdk
===============

The Veem Python SDK provides an interface to make it easier to call [Veem Global Payments APIs](https://developer.veem.com/reference).

## Version information
- Latest SDK Version: ```3.0.0```
- Latest supported API Endpoint Version: ```v1.1```


## Documentation

- [Veem Global Payments APIs](https://developer.veem.com/reference)
- [Developer Dashboard](https://developer.veem.com/page/dev-dashboard-sandbox)


## System Requirements
1. The SDK works on **Python 2.7, Python 3.4 and beyond**.
2. A [developer](https://developer.veem.com/page/dev-dashboard-sandbox) account
3. An [application with a customer account](https://developer.veem.com/page/dev-dashboard-sandbox)
   and the associated client id and secret (Authorization flow / Client
   Credentials flow)

## First Use Instructions
1. pypi install with command: ```pip install veem```
2. Import the package to your python

Or

1. Clone the GitHub repo to your computer.
2. Run installation with command ```python setup.py install```
3. Import the package to your python script


## Configuration YAML
Veem Python SDK utilize configuration YAML file to manage your SDK credential.
Here is the sample content:
```
client_id: VeemTester-1234abcd
client_secret: 8djduf8e-d798-3534-afe3-123sdc3r4fe
url: https://sandbox-api.veem.com/
authorizationCode: VeemAbckeieifh
redirectUrl: http://your-veem-redirct.yourbusiness.com
```


## Testing the Code

To test the code locally, follow the steps below:

1. cd to the project directory
2. Client can either integrate with Authorization flow or Client Credential Flow;
3. For Authorization flow, fill in the `clientId`, `clientSecret`,
   `authorizationCode`, and `redirectUrl`(optional) in your configuration yaml.
4. For Client Credentials flow, fill in the `clientId`, and `clientSecret` in
   your configuration yaml.
5. To exercise all Veem Global Payment APIs, fill access_token received from
   either step 3 or 4 to your configuration yaml.
6. Save the configuration yaml to a readable location or passing the content of
   yaml file as a yaml loadable string.

## Getting the OAuth Tokens

In order to get the access tokens from the Developer Portal;

**Sign In with Veem** - Sign into [developer Portal ](https://developer.veem.com/page/dev-dashboard-sandbox).

**Create an Application**- Create a new application by providing the `Name`, `OAuth2 Redirection URLs` and `Payment Status Webhooks`.

**Create a Customer**- Create a new customer by providing `Business Name`, `Country` and `Primary Email`

**Get Credentials**- Go the Application and select the `Customer` and copy the `Access Token`.

In order to get the `access token` programmatically, get the client id, client secrets (Optional redirect url for Authorization flow).

```
from veem.configuration import ConfigLoader
from veem.client.authentication import AuthenticationClient

# loading SDK configuration from your yaml file
config = ConfigLoader(yaml_file='/path/to/your/configuration.yaml')
# login to Veem server with client credentials
tokenResponse= AuthenticationClient(config).getTokenFromClientCredentials()
```

## Invoice Client Example

The following example is to send invoice using `Invoice Client`

```

from veem.client.veem import VeemClient
from veem.client.requests.invoice import InvoiceRequest

# define a VeemClient Context Manager with yaml+file and auto login.
with VeemClient(yaml_file='/path/to/your/configuration.yaml',
                useClientCredentials=True) as veem:
    # define an InvoiceRequest
    invoice = InvoiceRequest(payer=dict(type='Business',
                                        email='username@yourbusiness.com',
                                        firstName='Joe',
                                        lastName='Doe',
                                        businessName='Your Business Inc.',
                                        countryCode='US',
                                        phoneCountryCode='1',
                                        phone='02222222222'),
         amount=dict(number=50, currency='USD'))
    # create an invoice
    sentInvoice = veem.inoviceClient.create(invoice)

```

**More Examples can be found under examples folder**
