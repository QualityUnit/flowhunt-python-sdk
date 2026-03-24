# FlowSessionTaskResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** | Task name | 
**task_input** | **str** | Task input | 
**agent** | **str** | Agent that executed the task | 
**task_response** | **str** | Task response | 

## Example

```python
from flowhunt.models.flow_session_task_response_metadata import FlowSessionTaskResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionTaskResponseMetadata from a JSON string
flow_session_task_response_metadata_instance = FlowSessionTaskResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionTaskResponseMetadata.to_json())

# convert the object into a dict
flow_session_task_response_metadata_dict = flow_session_task_response_metadata_instance.to_dict()
# create an instance of FlowSessionTaskResponseMetadata from a dict
flow_session_task_response_metadata_from_dict = FlowSessionTaskResponseMetadata.from_dict(flow_session_task_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


