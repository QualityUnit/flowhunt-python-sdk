# ApiEndpointSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**method** | [**ApiMethod**](ApiMethod.md) |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.api_endpoint_search_request import ApiEndpointSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEndpointSearchRequest from a JSON string
api_endpoint_search_request_instance = ApiEndpointSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiEndpointSearchRequest.to_json())

# convert the object into a dict
api_endpoint_search_request_dict = api_endpoint_search_request_instance.to_dict()
# create an instance of ApiEndpointSearchRequest from a dict
api_endpoint_search_request_from_dict = ApiEndpointSearchRequest.from_dict(api_endpoint_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


