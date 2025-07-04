# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | 
**email** | **str** | Email of the user | 
**username** | **str** | Name of the user | 
**is_active** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**api_key_workspace_id** | **str** |  | [optional] 
**product_plans** | [**Dict[str, SubscriptionPlan]**](SubscriptionPlan.md) |  | [optional] 

## Example

```python
from flowhunt.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


