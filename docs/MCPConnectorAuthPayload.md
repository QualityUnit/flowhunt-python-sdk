# MCPConnectorAuthPayload

Plaintext auth payload — only ever crosses the wire on create/update. Never returned in responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Bearer token | [optional] 
**username** | **str** | Basic-auth username | [optional] 
**password** | **str** | Basic-auth password | [optional] 
**header_name** | **str** | Custom auth header name | [optional] 
**header_value** | **str** | Custom auth header value | [optional] 
**token_url** | **str** | OAuth token endpoint | [optional] 
**client_id** | **str** | OAuth client_id | [optional] 
**client_secret** | **str** | OAuth client_secret | [optional] 
**scope** | **str** | OAuth scope | [optional] 
**grant_type** | **str** | OAuth grant_type (default client_credentials) | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_auth_payload import MCPConnectorAuthPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorAuthPayload from a JSON string
mcp_connector_auth_payload_instance = MCPConnectorAuthPayload.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorAuthPayload.to_json())

# convert the object into a dict
mcp_connector_auth_payload_dict = mcp_connector_auth_payload_instance.to_dict()
# create an instance of MCPConnectorAuthPayload from a dict
mcp_connector_auth_payload_from_dict = MCPConnectorAuthPayload.from_dict(mcp_connector_auth_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


