# AgentGridFieldResponse

Schema for a single field in an agent grid schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name | 
**field_type** | [**AgentGridFieldType**](AgentGridFieldType.md) | Field type | 
**required** | **bool** | Whether the field is required | 

## Example

```python
from flowhunt.models.agent_grid_field_response import AgentGridFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGridFieldResponse from a JSON string
agent_grid_field_response_instance = AgentGridFieldResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGridFieldResponse.to_json())

# convert the object into a dict
agent_grid_field_response_dict = agent_grid_field_response_instance.to_dict()
# create an instance of AgentGridFieldResponse from a dict
agent_grid_field_response_from_dict = AgentGridFieldResponse.from_dict(agent_grid_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


