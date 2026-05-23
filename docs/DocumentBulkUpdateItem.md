# DocumentBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** |  | 
**user_status** | [**UserDocumentStatus**](UserDocumentStatus.md) |  | [optional] 
**cat_id** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.document_bulk_update_item import DocumentBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBulkUpdateItem from a JSON string
document_bulk_update_item_instance = DocumentBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(DocumentBulkUpdateItem.to_json())

# convert the object into a dict
document_bulk_update_item_dict = document_bulk_update_item_instance.to_dict()
# create an instance of DocumentBulkUpdateItem from a dict
document_bulk_update_item_from_dict = DocumentBulkUpdateItem.from_dict(document_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


