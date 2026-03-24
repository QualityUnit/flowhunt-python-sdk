# FlowCategoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_name** | **str** | The agent category name | 
**cat_color** | **str** | The agent category color | 

## Example

```python
from flowhunt.models.flow_category_create_request import FlowCategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCategoryCreateRequest from a JSON string
flow_category_create_request_instance = FlowCategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCategoryCreateRequest.to_json())

# convert the object into a dict
flow_category_create_request_dict = flow_category_create_request_instance.to_dict()
# create an instance of FlowCategoryCreateRequest from a dict
flow_category_create_request_from_dict = FlowCategoryCreateRequest.from_dict(flow_category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


