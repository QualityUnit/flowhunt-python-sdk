# CustomerRedactPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** |  | 
**shop_domain** | **str** |  | 
**customer** | **Dict[str, object]** |  | 
**orders_to_redact** | **List[int]** |  | 

## Example

```python
from flowhunt.models.customer_redact_payload import CustomerRedactPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerRedactPayload from a JSON string
customer_redact_payload_instance = CustomerRedactPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerRedactPayload.to_json())

# convert the object into a dict
customer_redact_payload_dict = customer_redact_payload_instance.to_dict()
# create an instance of CustomerRedactPayload from a dict
customer_redact_payload_from_dict = CustomerRedactPayload.from_dict(customer_redact_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


