# FlowSessionViewUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | New tags value | [optional] 

## Example

```python
from flowhunt.models.flow_session_view_update_request import FlowSessionViewUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionViewUpdateRequest from a JSON string
flow_session_view_update_request_instance = FlowSessionViewUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowSessionViewUpdateRequest.to_json())

# convert the object into a dict
flow_session_view_update_request_dict = flow_session_view_update_request_instance.to_dict()
# create an instance of FlowSessionViewUpdateRequest from a dict
flow_session_view_update_request_from_dict = FlowSessionViewUpdateRequest.from_dict(flow_session_view_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


