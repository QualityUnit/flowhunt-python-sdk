# MCPSubServerBinding

Represents a binding between an MCP server and an MCP sub server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subserver_id** | **str** |  | 
**capabilities** | [**List[MCPCapabilityBinding]**](MCPCapabilityBinding.md) |  | 

## Example

```python
from flowhunt.models.mcp_sub_server_binding import MCPSubServerBinding

# TODO update the JSON string below
json = "{}"
# create an instance of MCPSubServerBinding from a JSON string
mcp_sub_server_binding_instance = MCPSubServerBinding.from_json(json)
# print the JSON string representation of the object
print(MCPSubServerBinding.to_json())

# convert the object into a dict
mcp_sub_server_binding_dict = mcp_sub_server_binding_instance.to_dict()
# create an instance of MCPSubServerBinding from a dict
mcp_sub_server_binding_from_dict = MCPSubServerBinding.from_dict(mcp_sub_server_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


