# looker.ScheduledPlanApi

All URIs are relative to *https://localhost:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_scheduled_plans**](ScheduledPlanApi.md#all_scheduled_plans) | **GET** /scheduled_plans | Get All Scheduled Plans
[**create_scheduled_plan**](ScheduledPlanApi.md#create_scheduled_plan) | **POST** /scheduled_plans | Create Scheduled Plan
[**delete_scheduled_plan**](ScheduledPlanApi.md#delete_scheduled_plan) | **DELETE** /scheduled_plans/{scheduled_plan_id} | Delete Scheduled Plan
[**scheduled_plan**](ScheduledPlanApi.md#scheduled_plan) | **GET** /scheduled_plans/{scheduled_plan_id} | Get Scheduled Plan
[**scheduled_plan_run_once**](ScheduledPlanApi.md#scheduled_plan_run_once) | **POST** /scheduled_plans/run_once | Run Scheduled Plan Once
[**scheduled_plans_for_dashboard**](ScheduledPlanApi.md#scheduled_plans_for_dashboard) | **GET** /scheduled_plans/dashboard/{dashboard_id} | Scheduled Plans for Dashboard
[**scheduled_plans_for_look**](ScheduledPlanApi.md#scheduled_plans_for_look) | **GET** /scheduled_plans/look/{look_id} | Scheduled Plans for Look
[**scheduled_plans_for_lookml_dashboard**](ScheduledPlanApi.md#scheduled_plans_for_lookml_dashboard) | **GET** /scheduled_plans/lookml_dashboard/{lookml_dashboard_id} | Scheduled Plans for LookML Dashboard
[**scheduled_plans_for_space**](ScheduledPlanApi.md#scheduled_plans_for_space) | **GET** /scheduled_plans/space/{space_id} | Scheduled Plans for Space
[**update_scheduled_plan**](ScheduledPlanApi.md#update_scheduled_plan) | **PATCH** /scheduled_plans/{scheduled_plan_id} | Update Scheduled Plan


# **all_scheduled_plans**
> list[ScheduledPlan] all_scheduled_plans(user_id=user_id, fields=fields)

Get All Scheduled Plans

### List all scheduled plans which belong to the requesting user 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All Scheduled Plans
    api_response = api_instance.all_scheduled_plans(user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->all_scheduled_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scheduled_plan**
> ScheduledPlan create_scheduled_plan(body=body)

Create Scheduled Plan

### Schedule a Look or Dashboard by creating a scheduled plan.  Admins can create scheduled plans on behalf of other users by specifying a user id. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
body = looker.ScheduledPlan() # ScheduledPlan | Scheduled Plan (optional)

try:
    # Create Scheduled Plan
    api_response = api_instance.create_scheduled_plan(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->create_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_plan**
> str delete_scheduled_plan(scheduled_plan_id)

Delete Scheduled Plan

### Delete the scheduled plan with the specified id.  Admins can delete other users' Scheduled Plans. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id

try:
    # Delete Scheduled Plan
    api_response = api_instance.delete_scheduled_plan(scheduled_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->delete_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan**
> ScheduledPlan scheduled_plan(scheduled_plan_id, fields=fields)

Get Scheduled Plan

### Get information about a scheduled plan.  Admins can fetch information about other users' Scheduled Plans. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get Scheduled Plan
    api_response = api_instance.scheduled_plan(scheduled_plan_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan_run_once**
> ScheduledPlan scheduled_plan_run_once(body=body)

Run Scheduled Plan Once

### Schedule a Look or Dashboard to run once _now_ with a scheduled plan.  This can be useful for testing a Scheduled Plan before committing to a production schedule.  Admins can create scheduled plans on behalf of other users by specifying a user id. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
body = looker.ScheduledPlan() # ScheduledPlan | Scheduled Plan (optional)

try:
    # Run Scheduled Plan Once
    api_response = api_instance.scheduled_plan_run_once(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plan_run_once: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_dashboard**
> list[ScheduledPlan] scheduled_plans_for_dashboard(dashboard_id, user_id=user_id, fields=fields)

Scheduled Plans for Dashboard

### Get scheduled plans by using a dashboard id for the requesting user or a specified user id (with :see_schedules permission) 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
dashboard_id = 789 # int | Dashboard Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Scheduled Plans for Dashboard
    api_response = api_instance.scheduled_plans_for_dashboard(dashboard_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| Dashboard Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_look**
> list[ScheduledPlan] scheduled_plans_for_look(look_id, user_id=user_id, fields=fields)

Scheduled Plans for Look

### Get scheduled plans by using a look id for the requesting user or a specified user id (with :see_schedules permission) 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
look_id = 789 # int | Look Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Scheduled Plans for Look
    api_response = api_instance.scheduled_plans_for_look(look_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Look Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_lookml_dashboard**
> list[ScheduledPlan] scheduled_plans_for_lookml_dashboard(lookml_dashboard_id, user_id=user_id, fields=fields)

Scheduled Plans for LookML Dashboard

### Get scheduled plans by using a LookML dashboard id for the requesting user or a specified user id (with :see_schedules permission) 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
lookml_dashboard_id = 789 # int | LookML Dashboard Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Scheduled Plans for LookML Dashboard
    api_response = api_instance.scheduled_plans_for_lookml_dashboard(lookml_dashboard_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_lookml_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_dashboard_id** | **int**| LookML Dashboard Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_space**
> list[ScheduledPlan] scheduled_plans_for_space(space_id, fields=fields)

Scheduled Plans for Space

### Get scheduled plans by using a space id for the requesting user. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
space_id = 789 # int | Space Id
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Scheduled Plans for Space
    api_response = api_instance.scheduled_plans_for_space(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **int**| Space Id | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_plan**
> ScheduledPlan update_scheduled_plan(scheduled_plan_id, body)

Update Scheduled Plan

### Update the scheduled plan with the specified id.  Admins can update other users' Scheduled Plans. 

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id
body = looker.ScheduledPlan() # ScheduledPlan | Scheduled Plan

try:
    # Update Scheduled Plan
    api_response = api_instance.update_scheduled_plan(scheduled_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->update_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

