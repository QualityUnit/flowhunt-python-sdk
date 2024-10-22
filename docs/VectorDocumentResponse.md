# VectorDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID | 
**workspace_id** | **str** | Workspace ID | 
**document_type** | [**VectorDocumentType**](VectorDocumentType.md) | Document type | 
**point_id** | **str** | Point ID | 
**pointer_position** | **int** | Pointer position | 
**pointer_type** | [**PointerType**](PointerType.md) | Pointer type | 
**schema_type** | **str** |  | [optional] 
**kb_key** | **str** | Knowledge key - schedule id or category id | 
**vector** | **List[float]** |  | 
**vector_id** | **int** | Vector ID | 
**data** | [**Data**](Data.md) |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.vector_document_response import VectorDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VectorDocumentResponse from a JSON string
vector_document_response_instance = VectorDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(VectorDocumentResponse.to_json())

# convert the object into a dict
vector_document_response_dict = vector_document_response_instance.to_dict()
# create an instance of VectorDocumentResponse from a dict
vector_document_response_from_dict = VectorDocumentResponse.from_dict(vector_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


