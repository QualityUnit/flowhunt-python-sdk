# DocumentCategoryBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.document_category_bulk_delete_request import DocumentCategoryBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCategoryBulkDeleteRequest from a JSON string
document_category_bulk_delete_request_instance = DocumentCategoryBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCategoryBulkDeleteRequest.to_json())

# convert the object into a dict
document_category_bulk_delete_request_dict = document_category_bulk_delete_request_instance.to_dict()
# create an instance of DocumentCategoryBulkDeleteRequest from a dict
document_category_bulk_delete_request_from_dict = DocumentCategoryBulkDeleteRequest.from_dict(document_category_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


