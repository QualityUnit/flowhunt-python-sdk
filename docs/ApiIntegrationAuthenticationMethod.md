# ApiIntegrationAuthenticationMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**ApiIntegrationAuthType**](ApiIntegrationAuthType.md) | The authentication type of the API integration. | 
**description** | **str** | The description of the authentication type. | 
**beta** | **bool** | Whether the authentication type is in beta or not. | [optional] [default to False]
**link** | **str** | The link of the authentication type documentation. | 
**recommended_for_internal_assistant** | **bool** | Whether the authentication type is recommended for  | [optional] [default to False]
**recommended_for_public_facing_bot** | **bool** | Whether the authentication type is recommended for  | [optional] [default to False]

## Example

```python
from flowhunt.models.api_integration_authentication_method import ApiIntegrationAuthenticationMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationAuthenticationMethod from a JSON string
api_integration_authentication_method_instance = ApiIntegrationAuthenticationMethod.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationAuthenticationMethod.to_json())

# convert the object into a dict
api_integration_authentication_method_dict = api_integration_authentication_method_instance.to_dict()
# create an instance of ApiIntegrationAuthenticationMethod from a dict
api_integration_authentication_method_from_dict = ApiIntegrationAuthenticationMethod.from_dict(api_integration_authentication_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


