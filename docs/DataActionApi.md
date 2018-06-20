# looker.DataActionApi

All URIs are relative to *https://localhost:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_remote_data_action_form**](DataActionApi.md#fetch_remote_data_action_form) | **POST** /data_actions/form | Fetch Remote Data Action Form
[**perform_data_action**](DataActionApi.md#perform_data_action) | **POST** /data_actions | Send a Data Action


# **fetch_remote_data_action_form**
> DataActionForm fetch_remote_data_action_form(body)

Fetch Remote Data Action Form

For some data actions, the remote server may supply a form requesting further user input. This endpoint takes a data action, asks the remote server to generate a form for it, and returns that form to you for presentation to the user.

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.DataActionApi()
body = NULL # object | Data Action Request

try:
    # Fetch Remote Data Action Form
    api_response = api_instance.fetch_remote_data_action_form(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataActionApi->fetch_remote_data_action_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Data Action Request | 

### Return type

[**DataActionForm**](DataActionForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_data_action**
> DataActionResponse perform_data_action(body)

Send a Data Action

Perform a data action. The data action object can be obtained from query results, and used to perform an arbitrary action.

### Example
```python
from __future__ import print_function
import time
import looker
from looker.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker.DataActionApi()
body = looker.DataActionRequest() # DataActionRequest | Data Action Request

try:
    # Send a Data Action
    api_response = api_instance.perform_data_action(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataActionApi->perform_data_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataActionRequest**](DataActionRequest.md)| Data Action Request | 

### Return type

[**DataActionResponse**](DataActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

