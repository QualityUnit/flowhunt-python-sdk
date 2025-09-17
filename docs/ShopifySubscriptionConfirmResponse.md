# ShopifySubscriptionConfirmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 
**subscription_id** | **str** |  | [optional] 
**subscription_status** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.shopify_subscription_confirm_response import ShopifySubscriptionConfirmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShopifySubscriptionConfirmResponse from a JSON string
shopify_subscription_confirm_response_instance = ShopifySubscriptionConfirmResponse.from_json(json)
# print the JSON string representation of the object
print(ShopifySubscriptionConfirmResponse.to_json())

# convert the object into a dict
shopify_subscription_confirm_response_dict = shopify_subscription_confirm_response_instance.to_dict()
# create an instance of ShopifySubscriptionConfirmResponse from a dict
shopify_subscription_confirm_response_from_dict = ShopifySubscriptionConfirmResponse.from_dict(shopify_subscription_confirm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


