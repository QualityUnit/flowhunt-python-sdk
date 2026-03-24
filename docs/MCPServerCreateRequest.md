# MCPServerCreateRequest

Request schema for creating a new MCP server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the MCP server | 
**is_active** | **bool** | Whether the MCP server is active | [optional] [default to True]
**server_configuration** | [**List[MCPSubServerBinding]**](MCPSubServerBinding.md) | List of subserver bindings for the MCP server configuration | 

## Example

```python
from flowhunt.models.mcp_server_create_request import MCPServerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerCreateRequest from a JSON string
mcp_server_create_request_instance = MCPServerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MCPServerCreateRequest.to_json())

# convert the object into a dict
mcp_server_create_request_dict = mcp_server_create_request_instance.to_dict()
# create an instance of MCPServerCreateRequest from a dict
mcp_server_create_request_from_dict = MCPServerCreateRequest.from_dict(mcp_server_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


