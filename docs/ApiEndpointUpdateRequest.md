# ApiEndpointUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**method** | [**ApiMethod**](ApiMethod.md) |  | 
**parameters** | **List[object]** |  | [optional] 
**request_body** | **object** |  | [optional] 
**success_response** | **object** |  | [optional] 
**description** | **str** |  | 
**security_scheme** | **List[str]** |  | [optional] 

## Example

```python
from flowhunt.models.api_endpoint_update_request import ApiEndpointUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEndpointUpdateRequest from a JSON string
api_endpoint_update_request_instance = ApiEndpointUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiEndpointUpdateRequest.to_json())

# convert the object into a dict
api_endpoint_update_request_dict = api_endpoint_update_request_instance.to_dict()
# create an instance of ApiEndpointUpdateRequest from a dict
api_endpoint_update_request_from_dict = ApiEndpointUpdateRequest.from_dict(api_endpoint_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


