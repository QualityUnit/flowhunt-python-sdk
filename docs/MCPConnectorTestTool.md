# MCPConnectorTestTool

One tool advertised by the connector's MCP server during a test connection. Trimmed to fields the UI actually displays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**input_schema** | **Dict[str, object]** | JSON schema of the tool&#39;s arguments, if available | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_test_tool import MCPConnectorTestTool

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorTestTool from a JSON string
mcp_connector_test_tool_instance = MCPConnectorTestTool.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorTestTool.to_json())

# convert the object into a dict
mcp_connector_test_tool_dict = mcp_connector_test_tool_instance.to_dict()
# create an instance of MCPConnectorTestTool from a dict
mcp_connector_test_tool_from_dict = MCPConnectorTestTool.from_dict(mcp_connector_test_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


