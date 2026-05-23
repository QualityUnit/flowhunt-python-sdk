# MCPServerBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.mcp_server_bulk_delete_request import MCPServerBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerBulkDeleteRequest from a JSON string
mcp_server_bulk_delete_request_instance = MCPServerBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(MCPServerBulkDeleteRequest.to_json())

# convert the object into a dict
mcp_server_bulk_delete_request_dict = mcp_server_bulk_delete_request_instance.to_dict()
# create an instance of MCPServerBulkDeleteRequest from a dict
mcp_server_bulk_delete_request_from_dict = MCPServerBulkDeleteRequest.from_dict(mcp_server_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


