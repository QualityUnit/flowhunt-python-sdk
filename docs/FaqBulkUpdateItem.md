# FaqBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faq_id** | **str** |  | 
**cat_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.faq_bulk_update_item import FaqBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of FaqBulkUpdateItem from a JSON string
faq_bulk_update_item_instance = FaqBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(FaqBulkUpdateItem.to_json())

# convert the object into a dict
faq_bulk_update_item_dict = faq_bulk_update_item_instance.to_dict()
# create an instance of FaqBulkUpdateItem from a dict
faq_bulk_update_item_from_dict = FaqBulkUpdateItem.from_dict(faq_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


