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
base_url = 'https://localhost:19999/api/3.0/'

try:
    # Login
    api_response = api_instance.login(client_id=client_id, client_secret=client_secret)
    #use client to create new api objects
    client = looker.ApiClient(None, 'Authorization', 'token ' + api_response.access_token)
    #pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->login: %s\n" % e)

sdk = looker.RenderTaskApi(client)
dashboard_id = 12
result_format = 'pdf'
body = looker.CreateDashboardRenderTask('tiled', None) # CreateDashboardRenderTask | Dashboard render task parameters
width = 789 # int | Output width in pixels
height = 789 # int | Output height in pixels
fields = ''

try:
    # Create Dashboard Render Task
    api_response = sdk.create_dashboard_render_task(dashboard_id, result_format, body, width, height, fields=fields)
except ApiException as e:
    print("Exception when calling RenderTaskApi->create_dashboard_render_task: %s\n" % e)

render_task_id = api_response.id

print(sdk.render_task(render_task_id, fields=fields).status)

while sdk.render_task(render_task_id, fields=fields).status != 'success':
  continue

print(sdk.render_task(render_task_id, fields=fields).status)

try:
    # Create Dashboard Render Task
    api_response = sdk.render_task_results(render_task_id)
except ApiException as e:
    print("Exception when calling RenderTaskApi->render_task_results: %s\n" % e)

file = open("FunFacts.pdf","w+")
file.write(api_response)
file.close()
