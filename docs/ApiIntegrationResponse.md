# ApiIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The ID of the API integration. | 
**servers** | **List[str]** | The servers of the API integration. | 
**name** | **str** | The name of the API integration. | 
**description** | **str** | The description of the API integration. | 
**secret** | **object** |  | 

## Example

```python
from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationResponse from a JSON string
api_integration_response_instance = ApiIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationResponse.to_json())

# convert the object into a dict
api_integration_response_dict = api_integration_response_instance.to_dict()
# create an instance of ApiIntegrationResponse from a dict
api_integration_response_from_dict = ApiIntegrationResponse.from_dict(api_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


