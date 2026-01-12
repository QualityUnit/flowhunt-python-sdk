# AllFlowsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The agent name | [optional] 

## Example

```python
from flowhunt.models.all_flows_search_request import AllFlowsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllFlowsSearchRequest from a JSON string
all_flows_search_request_instance = AllFlowsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AllFlowsSearchRequest.to_json())

# convert the object into a dict
all_flows_search_request_dict = all_flows_search_request_instance.to_dict()
# create an instance of AllFlowsSearchRequest from a dict
all_flows_search_request_from_dict = AllFlowsSearchRequest.from_dict(all_flows_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


