# MCPConnectorResponse

Response shape — never includes plaintext auth secrets. Only the auth_type is exposed; the presence of a secret is signalled via ``has_credentials``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**connector_id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**transport** | **str** |  | 
**auth_type** | **str** |  | 
**has_credentials** | **bool** | True if encrypted credentials are stored on this connector | 
**headers** | **Dict[str, str]** | Non-secret custom headers | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_response import MCPConnectorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorResponse from a JSON string
mcp_connector_response_instance = MCPConnectorResponse.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorResponse.to_json())

# convert the object into a dict
mcp_connector_response_dict = mcp_connector_response_instance.to_dict()
# create an instance of MCPConnectorResponse from a dict
mcp_connector_response_from_dict = MCPConnectorResponse.from_dict(mcp_connector_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


