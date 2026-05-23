# DocumentBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DocumentBulkUpdateItem]**](DocumentBulkUpdateItem.md) |  | 

## Example

```python
from flowhunt.models.document_bulk_update_request import DocumentBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBulkUpdateRequest from a JSON string
document_bulk_update_request_instance = DocumentBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentBulkUpdateRequest.to_json())

# convert the object into a dict
document_bulk_update_request_dict = document_bulk_update_request_instance.to_dict()
# create an instance of DocumentBulkUpdateRequest from a dict
document_bulk_update_request_from_dict = DocumentBulkUpdateRequest.from_dict(document_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


