# PlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**price_id** | **str** |  | 
**currency** | **str** |  | 
**amount** | **int** |  | 
**recurring** | **bool** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**popular** | **bool** |  | 
**features** | [**List[FeatureResponse]**](FeatureResponse.md) |  | 
**subscription_plan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 
**self_hosted** | **bool** |  | [optional] 

## Example

```python
from flowhunt.models.plan_response import PlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponse from a JSON string
plan_response_instance = PlanResponse.from_json(json)
# print the JSON string representation of the object
print(PlanResponse.to_json())

# convert the object into a dict
plan_response_dict = plan_response_instance.to_dict()
# create an instance of PlanResponse from a dict
plan_response_from_dict = PlanResponse.from_dict(plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


