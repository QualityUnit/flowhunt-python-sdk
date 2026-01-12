# QuerySimilarityTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** | The post back URL where to send the response in body | [optional] 
**document_type** | [**VectorDocumentType**](VectorDocumentType.md) | Document type | [optional] 
**pointer_type** | [**PointerType**](PointerType.md) | Pointer type | [optional] 
**schema_type** | **str** | Schema type | [optional] 
**limit** | **int** | Number of documents to return | [optional] [default to 10]
**score_trheshold** | **float** | Score threshold | [optional] [default to 0.8]
**with_vectors** | **bool** | Whether to return vectors | [optional] [default to False]
**pointer_position_from** | **int** | Pointer position from | [optional] 
**pointer_position_to** | **int** | Pointer position to | [optional] 
**vector_id_from** | **int** | Vector id from | [optional] 
**vector_id_to** | **int** | Vector id to | [optional] 
**filter_url** | **str** | Return just documents matching given substring in url | [optional] 
**filter_domains** | **List[str]** | Return just documents from given domains | [optional] 
**query** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.query_similarity_task_request import QuerySimilarityTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySimilarityTaskRequest from a JSON string
query_similarity_task_request_instance = QuerySimilarityTaskRequest.from_json(json)
# print the JSON string representation of the object
print(QuerySimilarityTaskRequest.to_json())

# convert the object into a dict
query_similarity_task_request_dict = query_similarity_task_request_instance.to_dict()
# create an instance of QuerySimilarityTaskRequest from a dict
query_similarity_task_request_from_dict = QuerySimilarityTaskRequest.from_dict(query_similarity_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


