# FlowSessionArtefactsMetadata

Metadata for artefacts created by Deep Agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artefacts** | [**List[FlowSessionArtefactInfo]**](FlowSessionArtefactInfo.md) | List of artefact files created by agent | 

## Example

```python
from flowhunt.models.flow_session_artefacts_metadata import FlowSessionArtefactsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionArtefactsMetadata from a JSON string
flow_session_artefacts_metadata_instance = FlowSessionArtefactsMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionArtefactsMetadata.to_json())

# convert the object into a dict
flow_session_artefacts_metadata_dict = flow_session_artefacts_metadata_instance.to_dict()
# create an instance of FlowSessionArtefactsMetadata from a dict
flow_session_artefacts_metadata_from_dict = FlowSessionArtefactsMetadata.from_dict(flow_session_artefacts_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


