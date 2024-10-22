# ApiIntegrationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[str]** | The servers of the API integration. | 
**name** | **str** | The name of the API integration. | 
**description** | **str** | The description of the API integration. | 

## Example

```python
from flowhunt-python-sdk.models.api_integration_create_request import ApiIntegrationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationCreateRequest from a JSON string
api_integration_create_request_instance = ApiIntegrationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationCreateRequest.to_json())

# convert the object into a dict
api_integration_create_request_dict = api_integration_create_request_instance.to_dict()
# create an instance of ApiIntegrationCreateRequest from a dict
api_integration_create_request_from_dict = ApiIntegrationCreateRequest.from_dict(api_integration_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


