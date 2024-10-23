# IntegrationSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | [**IntegrationSlug**](IntegrationSlug.md) |  | [optional] 

## Example

```python
from flowhunt.models.integration_search_request import IntegrationSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSearchRequest from a JSON string
integration_search_request_instance = IntegrationSearchRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationSearchRequest.to_json())

# convert the object into a dict
integration_search_request_dict = integration_search_request_instance.to_dict()
# create an instance of IntegrationSearchRequest from a dict
integration_search_request_from_dict = IntegrationSearchRequest.from_dict(integration_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


