# FlowSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID | 
**created_at** | **datetime** | Session created at | 

## Example

```python
from flowhunt.models.flow_session_response import FlowSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionResponse from a JSON string
flow_session_response_instance = FlowSessionResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionResponse.to_json())

# convert the object into a dict
flow_session_response_dict = flow_session_response_instance.to_dict()
# create an instance of FlowSessionResponse from a dict
flow_session_response_from_dict = FlowSessionResponse.from_dict(flow_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


