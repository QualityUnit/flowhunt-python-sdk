# FlowSessionFileAccessRequiredMetadata

Metadata for file access required events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document requiring access | 
**document_type** | **str** | Type of document (e.g., google_sheets) | 
**message** | **str** | User-facing message explaining why access is needed | [optional] [default to '']

## Example

```python
from flowhunt.models.flow_session_file_access_required_metadata import FlowSessionFileAccessRequiredMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionFileAccessRequiredMetadata from a JSON string
flow_session_file_access_required_metadata_instance = FlowSessionFileAccessRequiredMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionFileAccessRequiredMetadata.to_json())

# convert the object into a dict
flow_session_file_access_required_metadata_dict = flow_session_file_access_required_metadata_instance.to_dict()
# create an instance of FlowSessionFileAccessRequiredMetadata from a dict
flow_session_file_access_required_metadata_from_dict = FlowSessionFileAccessRequiredMetadata.from_dict(flow_session_file_access_required_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


