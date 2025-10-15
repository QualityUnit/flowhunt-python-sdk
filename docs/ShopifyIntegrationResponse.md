# ShopifyIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_url** | **str** |  | [optional] 
**shopify_client_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.shopify_integration_response import ShopifyIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShopifyIntegrationResponse from a JSON string
shopify_integration_response_instance = ShopifyIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(ShopifyIntegrationResponse.to_json())

# convert the object into a dict
shopify_integration_response_dict = shopify_integration_response_instance.to_dict()
# create an instance of ShopifyIntegrationResponse from a dict
shopify_integration_response_from_dict = ShopifyIntegrationResponse.from_dict(shopify_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


