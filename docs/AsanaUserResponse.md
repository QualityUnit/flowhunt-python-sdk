# AsanaUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_gid** | **str** |  | 
**user_name** | **str** |  | 

## Example

```python
from flowhunt.models.asana_user_response import AsanaUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaUserResponse from a JSON string
asana_user_response_instance = AsanaUserResponse.from_json(json)
# print the JSON string representation of the object
print(AsanaUserResponse.to_json())

# convert the object into a dict
asana_user_response_dict = asana_user_response_instance.to_dict()
# create an instance of AsanaUserResponse from a dict
asana_user_response_from_dict = AsanaUserResponse.from_dict(asana_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


