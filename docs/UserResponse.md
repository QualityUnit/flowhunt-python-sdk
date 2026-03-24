# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | 
**email** | **str** | Email of the user | 
**username** | **str** | Name of the user | 
**is_active** | **bool** | User is active or not | [optional] 
**avatar_url** | **str** | URL of the user&#39;s avatar | [optional] 
**api_key_workspace_id** | **str** | Workspace ID of the API Key | [optional] 
**product_plans** | [**Dict[str, SubscriptionPlan]**](SubscriptionPlan.md) | Product plans of the user | [optional] 
**billing_provider** | [**BillingProvider**](BillingProvider.md) | Billing provider for the user (S for Stripe, H for Shopify) | [optional] 
**sudoer** | **bool** | Whether the user has superuser privileges | [optional] [default to False]

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


