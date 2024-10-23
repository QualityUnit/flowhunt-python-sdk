# SecretUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_display_name** | **str** |  | [optional] 
**secret_value** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.secret_update_request import SecretUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretUpdateRequest from a JSON string
secret_update_request_instance = SecretUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SecretUpdateRequest.to_json())

# convert the object into a dict
secret_update_request_dict = secret_update_request_instance.to_dict()
# create an instance of SecretUpdateRequest from a dict
secret_update_request_from_dict = SecretUpdateRequest.from_dict(secret_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


