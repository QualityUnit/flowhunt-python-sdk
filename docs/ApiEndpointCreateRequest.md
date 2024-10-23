# ApiEndpointCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path of the API endpoint. | 
**method** | [**ApiMethod**](ApiMethod.md) | The method of the API endpoint. | 
**parameters** | **List[object]** |  | [optional] 
**request_body** | **object** |  | [optional] 
**success_response** | **object** |  | [optional] 
**description** | **str** | The description of the API endpoint. | 
**security_scheme** | **List[str]** | The security scheme of the API endpoint. | [optional] [default to []]

## Example

```python
from flowhunt.models.api_endpoint_create_request import ApiEndpointCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEndpointCreateRequest from a JSON string
api_endpoint_create_request_instance = ApiEndpointCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiEndpointCreateRequest.to_json())

# convert the object into a dict
api_endpoint_create_request_dict = api_endpoint_create_request_instance.to_dict()
# create an instance of ApiEndpointCreateRequest from a dict
api_endpoint_create_request_from_dict = ApiEndpointCreateRequest.from_dict(api_endpoint_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


