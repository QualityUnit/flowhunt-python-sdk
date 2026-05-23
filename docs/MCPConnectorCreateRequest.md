# MCPConnectorCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Slug-shaped label: must be lowercase ascii — letters, digits, and single underscores between words only (e.g. &#39;betmana_mcp&#39;, &#39;my_mcp_server&#39;) | 
**url** | **str** | MCP server URL | 
**transport** | **str** | Transport: &#39;streamable_http&#39; or &#39;sse&#39; | 
**auth_type** | **str** | Auth type: &#39;none&#39; | &#39;bearer&#39; | &#39;basic&#39; | &#39;custom_header&#39; | &#39;oauth&#39; | [optional] [default to 'none']
**auth_payload** | [**MCPConnectorAuthPayload**](MCPConnectorAuthPayload.md) | Auth credentials (encrypted at rest) | [optional] 
**headers** | **Dict[str, str]** | Custom non-secret request headers | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_create_request import MCPConnectorCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorCreateRequest from a JSON string
mcp_connector_create_request_instance = MCPConnectorCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorCreateRequest.to_json())

# convert the object into a dict
mcp_connector_create_request_dict = mcp_connector_create_request_instance.to_dict()
# create an instance of MCPConnectorCreateRequest from a dict
mcp_connector_create_request_from_dict = MCPConnectorCreateRequest.from_dict(mcp_connector_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


