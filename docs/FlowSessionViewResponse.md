# FlowSessionViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID | 
**chatbot_id** | **str** | Chatbot ID | [optional] 
**flow_id** | **str** | Agent ID | 
**workspace_id** | **str** | Workspace ID | 
**created_at** | **datetime** | Created at | 
**last_msg_at** | **datetime** | Last message at | [optional] 
**msg_count** | **int** | Message count | [optional] 
**credits** | **int** | Credits | [optional] 
**chatbot_name** | **str** | Chatbot name | [optional] 
**flow_name** | **str** | Agent name | [optional] 
**tags** | **List[str]** | Tags | [optional] 
**duration** | **int** | Duration | [optional] 
**ipaddress** | **str** | IP address | [optional] 
**url** | **str** | Start URL | [optional] 
**positive_feedback_count** | **int** | Positive feedback count | [optional] 
**negative_feedback_count** | **int** | Negative feedback count | [optional] 

## Example

```python
from flowhunt.models.flow_session_view_response import FlowSessionViewResponse

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


