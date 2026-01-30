# AgentGridFieldRequest

Schema for a single field in an agent grid schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name (must be snake_case: lowercase letters, numbers, underscores only) | 
**field_type** | [**AgentGridFieldType**](AgentGridFieldType.md) | Field type | 
**required** | **bool** | Whether the field is required | [optional] [default to False]

## Example

```python
from flowhunt.models.agent_grid_field_request import AgentGridFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridFieldRequest from a JSON string
agent_grid_field_request_instance = AgentGridFieldRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGridFieldRequest.to_json())

# convert the object into a dict
agent_grid_field_request_dict = agent_grid_field_request_instance.to_dict()
# create an instance of AgentGridFieldRequest from a dict
agent_grid_field_request_from_dict = AgentGridFieldRequest.from_dict(agent_grid_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


