# ApiKeyBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** |  | 
**valid_to** | **datetime** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.api_key_bulk_update_item import ApiKeyBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyBulkUpdateItem from a JSON string
api_key_bulk_update_item_instance = ApiKeyBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(ApiKeyBulkUpdateItem.to_json())

# convert the object into a dict
api_key_bulk_update_item_dict = api_key_bulk_update_item_instance.to_dict()
# create an instance of ApiKeyBulkUpdateItem from a dict
api_key_bulk_update_item_from_dict = ApiKeyBulkUpdateItem.from_dict(api_key_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


