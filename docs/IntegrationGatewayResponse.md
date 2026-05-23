# IntegrationGatewayResponse

Payload returned when a gateway token is successfully resolved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Workspace that needs the integration | 
**slug** | **str** | Integration slug to set up | 
**session_id** | **str** | Chat session that triggered the request | [optional] [default to '']

## Example

```python
from flowhunt.models.integration_gateway_response import IntegrationGatewayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationGatewayResponse from a JSON string
integration_gateway_response_instance = IntegrationGatewayResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationGatewayResponse.to_json())

# convert the object into a dict
integration_gateway_response_dict = integration_gateway_response_instance.to_dict()
# create an instance of IntegrationGatewayResponse from a dict
integration_gateway_response_from_dict = IntegrationGatewayResponse.from_dict(integration_gateway_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


