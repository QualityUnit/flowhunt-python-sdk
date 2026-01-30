# MCPCapabilityBinding

Represents a binding between an MCP server and a capability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability_id** | **str** |  | 

## Example

```python
from flowhunt.models.mcp_capability_binding import MCPCapabilityBinding

# TODO update the JSON string below
json = "{}"
# create an instance of MCPCapabilityBinding from a JSON string
mcp_capability_binding_instance = MCPCapabilityBinding.from_json(json)
# print the JSON string representation of the object
print(MCPCapabilityBinding.to_json())

# convert the object into a dict
mcp_capability_binding_dict = mcp_capability_binding_instance.to_dict()
# create an instance of MCPCapabilityBinding from a dict
mcp_capability_binding_from_dict = MCPCapabilityBinding.from_dict(mcp_capability_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


