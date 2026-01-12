# FlowSessionArtefactInfo

Information about a single artefact file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique artefact identifier | 
**name** | **str** | File name | 
**path** | **str** | Relative path within workspace | 
**size** | **int** | File size in bytes | 
**modified_at** | **str** | Last modification timestamp (ISO format) | 

## Example

```python
from flowhunt.models.flow_session_artefact_info import FlowSessionArtefactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionArtefactInfo from a JSON string
flow_session_artefact_info_instance = FlowSessionArtefactInfo.from_json(json)
# print the JSON string representation of the object
print(FlowSessionArtefactInfo.to_json())

# convert the object into a dict
flow_session_artefact_info_dict = flow_session_artefact_info_instance.to_dict()
# create an instance of FlowSessionArtefactInfo from a dict
flow_session_artefact_info_from_dict = FlowSessionArtefactInfo.from_dict(flow_session_artefact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


