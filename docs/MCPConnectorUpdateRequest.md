# MCPConnectorUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**transport** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**auth_payload** | [**MCPConnectorAuthPayload**](MCPConnectorAuthPayload.md) |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_update_request import MCPConnectorUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorUpdateRequest from a JSON string
mcp_connector_update_request_instance = MCPConnectorUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorUpdateRequest.to_json())

# convert the object into a dict
mcp_connector_update_request_dict = mcp_connector_update_request_instance.to_dict()
# create an instance of MCPConnectorUpdateRequest from a dict
mcp_connector_update_request_from_dict = MCPConnectorUpdateRequest.from_dict(mcp_connector_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


