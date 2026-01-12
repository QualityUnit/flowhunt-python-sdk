# FlowSessionArtefactContentResponse

Response containing artefact file content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique artefact identifier | 
**name** | **str** | File name | 
**path** | **str** | Relative path within workspace | 
**size** | **int** | File size in bytes | 
**modified_at** | **str** | Last modification timestamp (ISO format) | 
**content** | **str** | File content | 

## Example

```python
from flowhunt.models.flow_session_artefact_content_response import FlowSessionArtefactContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionArtefactContentResponse from a JSON string
flow_session_artefact_content_response_instance = FlowSessionArtefactContentResponse.from_json(json)
# print the JSON string representation of the object
print(FlowSessionArtefactContentResponse.to_json())

# convert the object into a dict
flow_session_artefact_content_response_dict = flow_session_artefact_content_response_instance.to_dict()
# create an instance of FlowSessionArtefactContentResponse from a dict
flow_session_artefact_content_response_from_dict = FlowSessionArtefactContentResponse.from_dict(flow_session_artefact_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


