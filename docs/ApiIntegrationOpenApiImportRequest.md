# ApiIntegrationOpenApiImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openapi_url** | **str** | The openapi url of the API integration. | 

## Example

```python
from flowhunt.models.api_integration_open_api_import_request import ApiIntegrationOpenApiImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationOpenApiImportRequest from a JSON string
api_integration_open_api_import_request_instance = ApiIntegrationOpenApiImportRequest.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationOpenApiImportRequest.to_json())

# convert the object into a dict
api_integration_open_api_import_request_dict = api_integration_open_api_import_request_instance.to_dict()
# create an instance of ApiIntegrationOpenApiImportRequest from a dict
api_integration_open_api_import_request_from_dict = ApiIntegrationOpenApiImportRequest.from_dict(api_integration_open_api_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


