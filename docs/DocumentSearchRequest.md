# DocumentSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** |  | [optional] 
**cat_id** | **str** |  | [optional] 
**doc_name** | **str** |  | [optional] 
**doc_type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**status** | [**DocumentStatus**](DocumentStatus.md) |  | [optional] 
**user_status** | [**UserDocumentStatus**](UserDocumentStatus.md) |  | [optional] 
**updated_at_from** | **datetime** |  | [optional] 
**updated_at_to** | **datetime** |  | [optional] 
**limit** | **int** |  | [optional] 

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


