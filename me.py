from __future__ import print_function
import time
import looker
import os
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ApiAuthApi()
client_id = os.environ['API_ID'] # str | client_id part of API3 Key. (optional)
client_secret = os.environ['API_KEY'] # str | client_secret part of API3 Key. (optional)

try:
    # Login
    api_response = api_instance.login(client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->login: %s\n" % e)

print(api_instance.get_current_user()['id'])
