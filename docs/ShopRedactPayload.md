# ShopRedactPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** |  | 
**shop_domain** | **str** |  | 

## Example

```python
from flowhunt.models.shop_redact_payload import ShopRedactPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ShopRedactPayload from a JSON string
shop_redact_payload_instance = ShopRedactPayload.from_json(json)
# print the JSON string representation of the object
print(ShopRedactPayload.to_json())

# convert the object into a dict
shop_redact_payload_dict = shop_redact_payload_instance.to_dict()
# create an instance of ShopRedactPayload from a dict
shop_redact_payload_from_dict = ShopRedactPayload.from_dict(shop_redact_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


