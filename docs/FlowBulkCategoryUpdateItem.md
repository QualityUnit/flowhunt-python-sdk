# FlowBulkCategoryUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**category_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_bulk_category_update_item import FlowBulkCategoryUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBulkCategoryUpdateItem from a JSON string
flow_bulk_category_update_item_instance = FlowBulkCategoryUpdateItem.from_json(json)
# print the JSON string representation of the object
print(FlowBulkCategoryUpdateItem.to_json())

# convert the object into a dict
flow_bulk_category_update_item_dict = flow_bulk_category_update_item_instance.to_dict()
# create an instance of FlowBulkCategoryUpdateItem from a dict
flow_bulk_category_update_item_from_dict = FlowBulkCategoryUpdateItem.from_dict(flow_bulk_category_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


