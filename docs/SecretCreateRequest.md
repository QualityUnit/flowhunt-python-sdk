# SecretCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_display_name** | **str** |  | 
**secret_value** | **str** |  | 

## Example

```python
from flowhunt-python-sdk.models.secret_create_request import SecretCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretCreateRequest from a JSON string
secret_create_request_instance = SecretCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SecretCreateRequest.to_json())

# convert the object into a dict
secret_create_request_dict = secret_create_request_instance.to_dict()
# create an instance of SecretCreateRequest from a dict
secret_create_request_from_dict = SecretCreateRequest.from_dict(secret_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


