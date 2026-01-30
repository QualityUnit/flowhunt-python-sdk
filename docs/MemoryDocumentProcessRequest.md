# MemoryDocumentProcessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | 
**flow_id** | **str** | Flow ID to process the documents | 
**doc_ids** | **List[str]** | List of document IDs to process | 
**parent_node_id** | **str** | Parent node ID to attach documents | [optional] 

## Example

```python
from flowhunt.models.memory_document_process_request import MemoryDocumentProcessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryDocumentProcessRequest from a JSON string
memory_document_process_request_instance = MemoryDocumentProcessRequest.from_json(json)
# print the JSON string representation of the object
print(MemoryDocumentProcessRequest.to_json())

# convert the object into a dict
memory_document_process_request_dict = memory_document_process_request_instance.to_dict()
# create an instance of MemoryDocumentProcessRequest from a dict
memory_document_process_request_from_dict = MemoryDocumentProcessRequest.from_dict(memory_document_process_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


