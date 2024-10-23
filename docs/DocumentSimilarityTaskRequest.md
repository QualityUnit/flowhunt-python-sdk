# DocumentSimilarityTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**document_type** | [**VectorDocumentType**](VectorDocumentType.md) |  | [optional] 
**pointer_type** | [**PointerType**](PointerType.md) |  | [optional] 
**schema_type** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**score_trheshold** | **float** |  | [optional] 
**with_vectors** | **bool** |  | [optional] 
**pointer_position_from** | **int** |  | [optional] 
**pointer_position_to** | **int** |  | [optional] 
**vector_id_from** | **int** |  | [optional] 
**vector_id_to** | **int** |  | [optional] 
**filter_url** | **str** |  | [optional] 
**filter_domains** | **List[str]** |  | [optional] 
**document_id** | **str** |  | [optional] 
**faq_id** | **str** |  | [optional] 
**url_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.document_similarity_task_request import DocumentSimilarityTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSimilarityTaskRequest from a JSON string
document_similarity_task_request_instance = DocumentSimilarityTaskRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSimilarityTaskRequest.to_json())

# convert the object into a dict
document_similarity_task_request_dict = document_similarity_task_request_instance.to_dict()
# create an instance of DocumentSimilarityTaskRequest from a dict
document_similarity_task_request_from_dict = DocumentSimilarityTaskRequest.from_dict(document_similarity_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


