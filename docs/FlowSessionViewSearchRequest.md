# FlowSessionViewSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatbot_id** | **str** | Chatbot ID | [optional] 
**flow_id** | **str** | Agent ID | [optional] 
**tags** | **List[str]** | Tags to filter by | [optional] 
**limit** | **int** | Limit | [optional] [default to 100]
**created_at_filter** | **Dict[str, object]** | Filter for created at | [optional] 
**last_message_at_filter** | **Dict[str, object]** | Filter for last message at | [optional] 
**duration_filter** | **Dict[str, object]** | Filter for duration | [optional] 
**msg_count_filter** | **Dict[str, object]** | Filter for message count | [optional] 
**credits_filter** | **Dict[str, object]** | Filter for credits | [optional] 
**chatbot_name** | **str** | Chatbot name to match | [optional] 
**flow_name** | **str** | Agent name to match | [optional] 
**ipaddress_filter** | **Dict[str, object]** | Filter for IP address | [optional] 
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 
**positive_feedback** | **int** | Positive feedback count | [optional] 
**negative_feedback** | **int** | Negative feedback count | [optional] 

## Example

```python
from flowhunt.models.flow_session_view_search_request import FlowSessionViewSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionViewSearchRequest from a JSON string
flow_session_view_search_request_instance = FlowSessionViewSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionViewSearchRequest.to_json())

# convert the object into a dict
flow_session_view_search_request_dict = flow_session_view_search_request_instance.to_dict()
# create an instance of FlowSessionViewSearchRequest from a dict
flow_session_view_search_request_from_dict = FlowSessionViewSearchRequest.from_dict(flow_session_view_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


