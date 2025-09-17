# UserPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **int** |  | 
**price_currency** | **str** |  | 
**monthly_topup_credits** | **int** |  | 
**current_period_end** | **datetime** |  | 
**subscription_plans** | [**Dict[str, SubscriptionPlan]**](SubscriptionPlan.md) |  | 
**can_remove_branding** | **bool** |  | 
**extra_workspaces_count** | **int** |  | [optional] 
**extra_credits_count** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.user_plan_response import UserPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlanResponse from a JSON string
user_plan_response_instance = UserPlanResponse.from_json(json)
# print the JSON string representation of the object
print(UserPlanResponse.to_json())

# convert the object into a dict
user_plan_response_dict = user_plan_response_instance.to_dict()
# create an instance of UserPlanResponse from a dict
user_plan_response_from_dict = UserPlanResponse.from_dict(user_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


