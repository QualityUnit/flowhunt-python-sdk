# MemoryDocumentUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **str** | Document ID | 
**doc_name** | **str** | Document name | 
**message** | **str** | Upload status message | 

## Example

```python
from flowhunt.models.memory_document_upload_response import MemoryDocumentUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryDocumentUploadResponse from a JSON string
memory_document_upload_response_instance = MemoryDocumentUploadResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryDocumentUploadResponse.to_json())

# convert the object into a dict
memory_document_upload_response_dict = memory_document_upload_response_instance.to_dict()
# create an instance of MemoryDocumentUploadResponse from a dict
memory_document_upload_response_from_dict = MemoryDocumentUploadResponse.from_dict(memory_document_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


