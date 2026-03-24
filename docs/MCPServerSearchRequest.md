# MCPServerSearchRequest

Request schema for searching MCP servers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the MCP server | [optional] 
**active_only** | **bool** | Whether the MCP server is active | [optional] 

## Example

```python
from flowhunt.models.mcp_server_search_request import MCPServerSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerSearchRequest from a JSON string
mcp_server_search_request_instance = MCPServerSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MCPServerSearchRequest.to_json())

# convert the object into a dict
mcp_server_search_request_dict = mcp_server_search_request_instance.to_dict()
# create an instance of MCPServerSearchRequest from a dict
mcp_server_search_request_from_dict = MCPServerSearchRequest.from_dict(mcp_server_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


