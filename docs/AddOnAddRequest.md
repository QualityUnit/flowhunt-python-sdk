# AddOnAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proration_behavior** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.add_on_add_request import AddOnAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnAddRequest from a JSON string
add_on_add_request_instance = AddOnAddRequest.from_json(json)
# print the JSON string representation of the object
print(AddOnAddRequest.to_json())

# convert the object into a dict
add_on_add_request_dict = add_on_add_request_instance.to_dict()
# create an instance of AddOnAddRequest from a dict
add_on_add_request_from_dict = AddOnAddRequest.from_dict(add_on_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


