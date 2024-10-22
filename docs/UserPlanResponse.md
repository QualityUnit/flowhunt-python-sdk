# UserPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**price_amount** | **int** |  | 
**price_currency** | **str** |  | 
**last_renewal_date** | **datetime** |  | [optional] 
**monthly_topup_credits** | **int** |  | 
**trial_end_date** | **datetime** |  | [optional] 
**subscription_plan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 

## Example

```python
from flowhunt-python-sdk.models.user_plan_response import UserPlanResponse

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


