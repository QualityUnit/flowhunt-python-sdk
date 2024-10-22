# NewPasswordRequest

Payload for resetting password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from flowhunt-python-sdk.models.new_password_request import NewPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewPasswordRequest from a JSON string
new_password_request_instance = NewPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(NewPasswordRequest.to_json())

# convert the object into a dict
new_password_request_dict = new_password_request_instance.to_dict()
# create an instance of NewPasswordRequest from a dict
new_password_request_from_dict = NewPasswordRequest.from_dict(new_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


