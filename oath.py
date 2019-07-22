import requests
import pdb
import json

# Client Name: apidev-oauth
url = 'https://login.microsoftonline.com/ec8933c6-cfb2-4dd9-bfc9-************/oauth2/token'
values =  {
            "client_id": "4b8d083c-c55a**********",
            "grant_type": "client_credentials",
            "resource": "df2a44e7-d939-4cef-*************",
            "client_secret": "YO1]h/yPwl1N***********************"    # latest secret
          }
response_data = requests.post(url, data=values)
response = response_data.json()
print '=============== Access Token ==============='
print response['access_token']
print "============================================"

order_status = 'https://westconapidev.azure-api.net/Orders/orderStatus'
headers = {'Ocp-Apim-Subscription-Key': 'fc6cc597899648fc88bd3919**********', 'Authorization': "Bearer " + response['access_token']}

order_parameters = {
          "mT_OrderStatus_API_REQ": {
            "partnerKey": "005056A1299B1EE9A*****************",
            "orderType": "W",
            "language": "EN",
            "order": {
              "orderNumber": "601*******"
            }
          }
        }

order_status_res = requests.post(order_status, data=order_parameters, headers=headers)

print order_status_res.json()
