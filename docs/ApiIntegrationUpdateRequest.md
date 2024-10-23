# ApiIntegrationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**secret** | **object** |  | [optional] 
**endpoints** | [**List[ApiEndpointCreateRequest]**](ApiEndpointCreateRequest.md) |  | [optional] 

## Example

```python
from flowhunt.models.api_integration_update_request import ApiIntegrationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationUpdateRequest from a JSON string
api_integration_update_request_instance = ApiIntegrationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationUpdateRequest.to_json())

# convert the object into a dict
api_integration_update_request_dict = api_integration_update_request_instance.to_dict()
# create an instance of ApiIntegrationUpdateRequest from a dict
api_integration_update_request_from_dict = ApiIntegrationUpdateRequest.from_dict(api_integration_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


