# CustomerDataRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** |  | 
**shop_domain** | **str** |  | 
**orders_requested** | **List[int]** |  | 
**customer** | **Dict[str, object]** |  | 
**data_request** | **Dict[str, object]** |  | 

## Example

```python
from flowhunt.models.customer_data_request_payload import CustomerDataRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDataRequestPayload from a JSON string
customer_data_request_payload_instance = CustomerDataRequestPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerDataRequestPayload.to_json())

# convert the object into a dict
customer_data_request_payload_dict = customer_data_request_payload_instance.to_dict()
# create an instance of CustomerDataRequestPayload from a dict
customer_data_request_payload_from_dict = CustomerDataRequestPayload.from_dict(customer_data_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


