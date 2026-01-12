# FlowSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_type** | [**FlowType**](FlowType.md) | The agent type | [optional] 
**name** | **str** | The agent name | [optional] 
**category_id** | **str** | The category ID | [optional] 
**limit** | **int** | The maximum number of agents to return | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.flow_search_request import FlowSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSearchRequest from a JSON string
flow_search_request_instance = FlowSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSearchRequest.to_json())

# convert the object into a dict
flow_search_request_dict = flow_search_request_instance.to_dict()
# create an instance of FlowSearchRequest from a dict
flow_search_request_from_dict = FlowSearchRequest.from_dict(flow_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


