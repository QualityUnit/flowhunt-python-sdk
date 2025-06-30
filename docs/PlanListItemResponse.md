# PlanListItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**price_id** | **str** |  | 
**currency** | **str** |  | 
**amount_monthly** | **int** |  | 
**amount_yearly** | **int** |  | [optional] 
**recurring** | **bool** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**popular** | **bool** |  | 
**monthly_credits** | **int** |  | 
**features** | [**List[FeatureResponse]**](FeatureResponse.md) |  | 
**subscription_plan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 
**self_hosted** | **bool** |  | [optional] 
**addon** | **bool** |  | [optional] 
**addon_type** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.plan_list_item_response import PlanListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanListItemResponse from a JSON string
plan_list_item_response_instance = PlanListItemResponse.from_json(json)
# print the JSON string representation of the object
print(PlanListItemResponse.to_json())

# convert the object into a dict
plan_list_item_response_dict = plan_list_item_response_instance.to_dict()
# create an instance of PlanListItemResponse from a dict
plan_list_item_response_from_dict = PlanListItemResponse.from_dict(plan_list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


