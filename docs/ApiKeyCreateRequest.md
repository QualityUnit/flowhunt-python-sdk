# ApiKeyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | User defined name of the API key | 
**valid_to** | **datetime** |  | [optional] 

## Example

```python
from flowhunt.models.api_key_create_request import ApiKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreateRequest from a JSON string
api_key_create_request_instance = ApiKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreateRequest.to_json())

# convert the object into a dict
api_key_create_request_dict = api_key_create_request_instance.to_dict()
# create an instance of ApiKeyCreateRequest from a dict
api_key_create_request_from_dict = ApiKeyCreateRequest.from_dict(api_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


