# MCPConnectorTestResponse

Result of a live test-connection against the connector's MCP server. ``success`` is True when the handshake succeeded and tools were enumerated (the list may still be empty if the server exposes none); otherwise ``error`` carries a human-readable reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**tools** | [**List[MCPConnectorTestTool]**](MCPConnectorTestTool.md) |  | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_test_response import MCPConnectorTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorTestResponse from a JSON string
mcp_connector_test_response_instance = MCPConnectorTestResponse.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorTestResponse.to_json())

# convert the object into a dict
mcp_connector_test_response_dict = mcp_connector_test_response_instance.to_dict()
# create an instance of MCPConnectorTestResponse from a dict
mcp_connector_test_response_from_dict = MCPConnectorTestResponse.from_dict(mcp_connector_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


