# VectorDocumentsTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task ID | 
**status** | [**TaskStatus**](TaskStatus.md) | Task status | 
**result** | [**List[VectorDocumentResponse]**](VectorDocumentResponse.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.vector_documents_task_response import VectorDocumentsTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VectorDocumentsTaskResponse from a JSON string
vector_documents_task_response_instance = VectorDocumentsTaskResponse.from_json(json)
# print the JSON string representation of the object
print(VectorDocumentsTaskResponse.to_json())

# convert the object into a dict
vector_documents_task_response_dict = vector_documents_task_response_instance.to_dict()
# create an instance of VectorDocumentsTaskResponse from a dict
vector_documents_task_response_from_dict = VectorDocumentsTaskResponse.from_dict(vector_documents_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


