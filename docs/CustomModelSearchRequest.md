# CustomModelSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.custom_model_search_request import CustomModelSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelSearchRequest from a JSON string
custom_model_search_request_instance = CustomModelSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CustomModelSearchRequest.to_json())

# convert the object into a dict
custom_model_search_request_dict = custom_model_search_request_instance.to_dict()
# create an instance of CustomModelSearchRequest from a dict
custom_model_search_request_from_dict = CustomModelSearchRequest.from_dict(custom_model_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


