# FlowSessionViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID | 
**chatbot_id** | **str** |  | [optional] 
**flow_id** | **str** | Flow ID | 
**workspace_id** | **str** | Workspace ID | 
**created_at** | **datetime** | Created at | 
**last_msg_at** | **datetime** |  | [optional] 
**msg_count** | **int** |  | [optional] 
**credits** | **int** |  | [optional] 
**chatbot_name** | **str** |  | [optional] 
**flow_name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**duration** | **int** |  | [optional] 
**ipaddress** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.flow_session_view_response import FlowSessionViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionViewResponse from a JSON string
flow_session_view_response_instance = FlowSessionViewResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionViewResponse.to_json())

# convert the object into a dict
flow_session_view_response_dict = flow_session_view_response_instance.to_dict()
# create an instance of FlowSessionViewResponse from a dict
flow_session_view_response_from_dict = FlowSessionViewResponse.from_dict(flow_session_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


