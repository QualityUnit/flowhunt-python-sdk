# ApiEndpointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | The ID of the API endpoint. | 
**path** | **str** | The path of the API endpoint. | 
**description** | **str** | The description of the API endpoint. | 
**method** | [**ApiMethod**](ApiMethod.md) | The method of the API endpoint. | 
**parameters** | [**AnyOf**](AnyOf.md) | The parameters of the API endpoint. | [optional] 
**request_body** | [**AnyOf**](AnyOf.md) | The request body of the API endpoint. | [optional] 
**success_response** | [**AnyOf**](AnyOf.md) | The success response of the API endpoint. | [optional] 
**security_scheme** | **List[str]** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.api_endpoint_response import ApiEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEndpointResponse from a JSON string
api_endpoint_response_instance = ApiEndpointResponse.from_json(json)
# print the JSON string representation of the object
print(ApiEndpointResponse.to_json())

# convert the object into a dict
api_endpoint_response_dict = api_endpoint_response_instance.to_dict()
# create an instance of ApiEndpointResponse from a dict
api_endpoint_response_from_dict = ApiEndpointResponse.from_dict(api_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


