# FlowCategoryResponse

Agent category response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** |  | 
**cat_name** | **str** |  | 
**cat_color** | **str** |  | 

## Example

```python
from flowhunt.models.flow_category_response import FlowCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCategoryResponse from a JSON string
flow_category_response_instance = FlowCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(FlowCategoryResponse.to_json())

# convert the object into a dict
flow_category_response_dict = flow_category_response_instance.to_dict()
# create an instance of FlowCategoryResponse from a dict
flow_category_response_from_dict = FlowCategoryResponse.from_dict(flow_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


