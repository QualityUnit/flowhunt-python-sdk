# GeneralMCPSubserverCapabilitiesResponse

General response schema for MCP subserver capabilities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability_id** | **str** | ID of the capability | 
**name** | **str** | Name of the capability | 
**description** | **str** | Description of the capability | [optional] 

## Example

```python
from flowhunt.models.general_mcp_subserver_capabilities_response import GeneralMCPSubserverCapabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralMCPSubserverCapabilitiesResponse from a JSON string
general_mcp_subserver_capabilities_response_instance = GeneralMCPSubserverCapabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print(GeneralMCPSubserverCapabilitiesResponse.to_json())

# convert the object into a dict
general_mcp_subserver_capabilities_response_dict = general_mcp_subserver_capabilities_response_instance.to_dict()
# create an instance of GeneralMCPSubserverCapabilitiesResponse from a dict
general_mcp_subserver_capabilities_response_from_dict = GeneralMCPSubserverCapabilitiesResponse.from_dict(general_mcp_subserver_capabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


