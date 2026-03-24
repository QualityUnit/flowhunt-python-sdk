# DocumentSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** | Document ID | [optional] 
**cat_id** | **str** | Category ID | [optional] 
**doc_name** | **str** | Document name | [optional] 
**doc_type** | [**DocumentType**](DocumentType.md) | Document type | [optional] 
**status** | [**DocumentStatus**](DocumentStatus.md) | System status | [optional] 
**user_status** | [**UserDocumentStatus**](UserDocumentStatus.md) | User defined status of document | [optional] 
**updated_at_from** | **datetime** | Updated at from | [optional] 
**updated_at_to** | **datetime** | Updated at to | [optional] 
**limit** | **int** | Limit | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.document_search_request import DocumentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchRequest from a JSON string
document_search_request_instance = DocumentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchRequest.to_json())

# convert the object into a dict
document_search_request_dict = document_search_request_instance.to_dict()
# create an instance of DocumentSearchRequest from a dict
document_search_request_from_dict = DocumentSearchRequest.from_dict(document_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


