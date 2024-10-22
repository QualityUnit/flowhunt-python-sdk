# FlowSessionAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name | 
**file_type** | **str** | File type | 
**file_id** | **str** | File ID | 
**type** | [**DocumentType**](DocumentType.md) | Document type | 

## Example

```python
from flowhunt-python-sdk.models.flow_session_attachment_response import FlowSessionAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionAttachmentResponse from a JSON string
flow_session_attachment_response_instance = FlowSessionAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionAttachmentResponse.to_json())

# convert the object into a dict
flow_session_attachment_response_dict = flow_session_attachment_response_instance.to_dict()
# create an instance of FlowSessionAttachmentResponse from a dict
flow_session_attachment_response_from_dict = FlowSessionAttachmentResponse.from_dict(flow_session_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


