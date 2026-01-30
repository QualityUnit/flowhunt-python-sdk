# QuerySimilarityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from flowhunt.models.query_similarity_request import QuerySimilarityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySimilarityRequest from a JSON string
query_similarity_request_instance = QuerySimilarityRequest.from_json(json)
# print the JSON string representation of the object
print(QuerySimilarityRequest.to_json())

# convert the object into a dict
query_similarity_request_dict = query_similarity_request_instance.to_dict()
# create an instance of QuerySimilarityRequest from a dict
query_similarity_request_from_dict = QuerySimilarityRequest.from_dict(query_similarity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


