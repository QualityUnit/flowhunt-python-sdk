# FlowBatchArtefactInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique artefact identifier | 
**name** | **str** | File name | 
**size** | **int** | File size in bytes | [optional] [default to 0]
**mime_type** | **str** | MIME type | [optional] 
**download_url** | **str** | Download URL | [optional] [default to '']

## Example

```python
from flowhunt.models.flow_batch_artefact_info import FlowBatchArtefactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBatchArtefactInfo from a JSON string
flow_batch_artefact_info_instance = FlowBatchArtefactInfo.from_json(json)
# print the JSON string representation of the object
print(FlowBatchArtefactInfo.to_json())

# convert the object into a dict
flow_batch_artefact_info_dict = flow_batch_artefact_info_instance.to_dict()
# create an instance of FlowBatchArtefactInfo from a dict
flow_batch_artefact_info_from_dict = FlowBatchArtefactInfo.from_dict(flow_batch_artefact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


