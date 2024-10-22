# FlowSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_type** | [**FlowType**](FlowType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.flow_search_request import FlowSearchRequest

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


