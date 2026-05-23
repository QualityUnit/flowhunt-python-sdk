# MCPConnectorSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter by name (case-insensitive substring match) | [optional] 

## Example

```python
from flowhunt.models.mcp_connector_search_request import MCPConnectorSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectorSearchRequest from a JSON string
mcp_connector_search_request_instance = MCPConnectorSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MCPConnectorSearchRequest.to_json())

# convert the object into a dict
mcp_connector_search_request_dict = mcp_connector_search_request_instance.to_dict()
# create an instance of MCPConnectorSearchRequest from a dict
mcp_connector_search_request_from_dict = MCPConnectorSearchRequest.from_dict(mcp_connector_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


