# MCPServerResponse

Response schema for MCP server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace ID | 
**mcp_server_id** | **str** | MCP Server ID | 
**name** | **str** | Name of the MCP server | 
**server_configuration** | [**List[MCPSubServerBinding]**](MCPSubServerBinding.md) | List of subserver bindings for the MCP server configuration | 
**is_active** | **bool** | Whether the MCP server is active | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**remote_mcp_url** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.mcp_server_response import MCPServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerResponse from a JSON string
mcp_server_response_instance = MCPServerResponse.from_json(json)
# print the JSON string representation of the object
print(MCPServerResponse.to_json())

# convert the object into a dict
mcp_server_response_dict = mcp_server_response_instance.to_dict()
# create an instance of MCPServerResponse from a dict
mcp_server_response_from_dict = MCPServerResponse.from_dict(mcp_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


