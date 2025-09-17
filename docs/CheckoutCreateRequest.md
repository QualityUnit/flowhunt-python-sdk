# CheckoutCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**interval** | **str** |  | 
**recurring** | **bool** |  | [optional] [default to True]
**workspace_id** | **str** |  | 

## Example

```python
from flowhunt.models.checkout_create_request import CheckoutCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCreateRequest from a JSON string
checkout_create_request_instance = CheckoutCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutCreateRequest.to_json())

# convert the object into a dict
checkout_create_request_dict = checkout_create_request_instance.to_dict()
# create an instance of CheckoutCreateRequest from a dict
checkout_create_request_from_dict = CheckoutCreateRequest.from_dict(checkout_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


