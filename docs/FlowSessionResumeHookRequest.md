# FlowSessionResumeHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_id** | **str** | The hook ID to resume | 
**message** | **str** | The user input message | 
**form_data** | **Dict[str, object]** | Form field data from form submissions | [optional] 

## Example

```python
from flowhunt.models.flow_session_resume_hook_request import FlowSessionResumeHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionResumeHookRequest from a JSON string
flow_session_resume_hook_request_instance = FlowSessionResumeHookRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionResumeHookRequest.to_json())

# convert the object into a dict
flow_session_resume_hook_request_dict = flow_session_resume_hook_request_instance.to_dict()
# create an instance of FlowSessionResumeHookRequest from a dict
flow_session_resume_hook_request_from_dict = FlowSessionResumeHookRequest.from_dict(flow_session_resume_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


