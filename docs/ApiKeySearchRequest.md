# ApiKeySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**mask** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.api_key_search_request import ApiKeySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeySearchRequest from a JSON string
api_key_search_request_instance = ApiKeySearchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiKeySearchRequest.to_json())

# convert the object into a dict
api_key_search_request_dict = api_key_search_request_instance.to_dict()
# create an instance of ApiKeySearchRequest from a dict
api_key_search_request_from_dict = ApiKeySearchRequest.from_dict(api_key_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


