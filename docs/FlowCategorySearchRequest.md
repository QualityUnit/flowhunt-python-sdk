# FlowCategorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_name** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from flowhunt.models.flow_category_search_request import FlowCategorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCategorySearchRequest from a JSON string
flow_category_search_request_instance = FlowCategorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCategorySearchRequest.to_json())

# convert the object into a dict
flow_category_search_request_dict = flow_category_search_request_instance.to_dict()
# create an instance of FlowCategorySearchRequest from a dict
flow_category_search_request_from_dict = FlowCategorySearchRequest.from_dict(flow_category_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


