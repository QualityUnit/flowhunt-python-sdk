# GeneralMCPSubserverResponse

General response schema for MCP subserver binding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** | ID of the MCP subserver | 
**name** | **str** | Name of the MCP subserver | 
**description** | **str** | Description of the MCP subserver | [optional] 
**status** | **str** | Status of the MCP subserver | 
**icon** | **str** | Icon URL for the MCP subserver | [optional] 
**version** | **str** | Version of the MCP subserver | 
**capabilities** | [**List[GeneralMCPSubserverCapabilitiesResponse]**](GeneralMCPSubserverCapabilitiesResponse.md) | List of capabilities for the MCP subserver | [optional] 
**integration_slug** | [**IntegrationSlug**](IntegrationSlug.md) | Integration slug for the MCP subserver | 

## Example

```python
from flowhunt.models.general_mcp_subserver_response import GeneralMCPSubserverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralMCPSubserverResponse from a JSON string
general_mcp_subserver_response_instance = GeneralMCPSubserverResponse.from_json(json)
# print the JSON string representation of the object
print(GeneralMCPSubserverResponse.to_json())

# convert the object into a dict
general_mcp_subserver_response_dict = general_mcp_subserver_response_instance.to_dict()
# create an instance of GeneralMCPSubserverResponse from a dict
general_mcp_subserver_response_from_dict = GeneralMCPSubserverResponse.from_dict(general_mcp_subserver_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


