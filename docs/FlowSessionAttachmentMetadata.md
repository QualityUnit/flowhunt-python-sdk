# FlowSessionAttachmentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | File ID | 
**file_name** | **str** | File name | 
**file_type** | **str** | File type | [optional] 
**document_type** | [**DocumentType**](DocumentType.md) | Document Type | [optional] 

## Example

```python
from flowhunt.models.flow_session_attachment_metadata import FlowSessionAttachmentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionAttachmentMetadata from a JSON string
flow_session_attachment_metadata_instance = FlowSessionAttachmentMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionAttachmentMetadata.to_json())

# convert the object into a dict
flow_session_attachment_metadata_dict = flow_session_attachment_metadata_instance.to_dict()
# create an instance of FlowSessionAttachmentMetadata from a dict
flow_session_attachment_metadata_from_dict = FlowSessionAttachmentMetadata.from_dict(flow_session_attachment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


