# SecretSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_display_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.secret_search_request import SecretSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretSearchRequest from a JSON string
secret_search_request_instance = SecretSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SecretSearchRequest.to_json())

# convert the object into a dict
secret_search_request_dict = secret_search_request_instance.to_dict()
# create an instance of SecretSearchRequest from a dict
secret_search_request_from_dict = SecretSearchRequest.from_dict(secret_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


