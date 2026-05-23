# DocumentBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | 

## Example

```python
from flowhunt.models.document_bulk_delete_request import DocumentBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBulkDeleteRequest from a JSON string
document_bulk_delete_request_instance = DocumentBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentBulkDeleteRequest.to_json())

# convert the object into a dict
document_bulk_delete_request_dict = document_bulk_delete_request_instance.to_dict()
# create an instance of DocumentBulkDeleteRequest from a dict
document_bulk_delete_request_from_dict = DocumentBulkDeleteRequest.from_dict(document_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


