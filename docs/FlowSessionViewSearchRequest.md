# FlowSessionViewSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatbot_id** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**limit** | **int** |  | [optional] 
**created_at_filter** | **Dict[str, object]** |  | [optional] 
**last_message_at_filter** | **Dict[str, object]** |  | [optional] 
**duration_filter** | **Dict[str, object]** |  | [optional] 
**msg_count_filter** | **Dict[str, object]** |  | [optional] 
**credits_filter** | **Dict[str, object]** |  | [optional] 
**chatbot_name** | **str** |  | [optional] 
**flow_name** | **str** |  | [optional] 
**ipaddress_filter** | **Dict[str, object]** |  | [optional] 

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


