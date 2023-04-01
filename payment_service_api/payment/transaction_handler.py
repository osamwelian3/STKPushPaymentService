from payment_service_api.settings import Consumer_Key, Consumer_Secret, BusinessShortCode, Passkey, TransactionType, PartyB, AccountReference, TIME_ZONE
from requests.auth import HTTPBasicAuth
from .models import Token
import base64
import requests
import json
import pytz
import datetime

eat = pytz.timezone(TIME_ZONE)

class Transaction:
    consumer_key = Consumer_Key
    consumer_secret = Consumer_Secret

    def get_basic_auth(self):
        encoded_string = base64.b64encode(bytes('%s:%s' % (self.consumer_key, self.consumer_secret), 'ascii'))
        encoded_string = encoded_string.decode("utf-8")
        # encoded_string = ''.join(e for e in encoded_string if e.isalnum())
        print(encoded_string)
        return encoded_string

    def authorize(self):
        try:
            old_token = Token.objects.latest('expiry')
            print(old_token.expiry)
            if old_token.expiry > eat.localize(datetime.datetime.now()):
                return json.dumps({'access_token': old_token.access_token, 'expires_in': str((old_token.expiry-eat.localize(datetime.datetime.now())).total_seconds()).split('.')[0]})
            else:
                old_token.delete
                raise Token.DoesNotExist
        except Token.DoesNotExist as e:
            header = { 'Authorization': 'Basic '+self.get_basic_auth() }
            response = requests.get('https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers=header)
            print("+++++++"+str(e))
            print(response.text)
            data = json.loads(response.text)
            token = Token.objects.create(access_token=data['access_token'], expiry=datetime.datetime.now()+datetime.timedelta(0, int(data['expires_in'])))
            token.save()
            print(data)
            return response.text.encode('utf8')

    def get_access_token(self):
        return json.loads(self.authorize())['access_token']

    def stk_push(self, phone: str, amount: int):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + self.get_access_token()
        }

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode((str(BusinessShortCode) + str(Passkey) + timestamp).encode('ascii')).decode('utf-8') 

        payload = {
            "BusinessShortCode": BusinessShortCode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": TransactionType,
            "Amount": amount,
            "PartyA": phone,
            "PartyB": BusinessShortCode,
            "PhoneNumber": phone,
            "CallBackURL": "http://payment.pythonanywhere.com/payment/callback/",
            "AccountReference": AccountReference,
            "TransactionDesc": "Test Payment" 
        }

        response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
        print(response.text.encode('utf8'))
        return json.loads(response.text.encode('utf8'))

    def query_transaction(self, CheckoutRequestID: str):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + self.get_access_token()
        }

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode((str(BusinessShortCode) + str(Passkey) + timestamp).encode('ascii')).decode('utf-8') 

        payload = {
            "BusinessShortCode": BusinessShortCode,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": CheckoutRequestID,
        }

        response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query', headers = headers, json = payload)
        data = json.loads(response.text.encode('utf8'))
        print(data)
        return data