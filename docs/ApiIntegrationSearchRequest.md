# ApiIntegrationSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.api_integration_search_request import ApiIntegrationSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIntegrationSearchRequest from a JSON string
api_integration_search_request_instance = ApiIntegrationSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiIntegrationSearchRequest.to_json())

# convert the object into a dict
api_integration_search_request_dict = api_integration_search_request_instance.to_dict()
# create an instance of ApiIntegrationSearchRequest from a dict
api_integration_search_request_from_dict = ApiIntegrationSearchRequest.from_dict(api_integration_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


