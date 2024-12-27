# FlowSessionLoadingMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**tool_name** | **str** | Tool name | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**detailed_description** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_session_loading_metadata import FlowSessionLoadingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionLoadingMetadata from a JSON string
flow_session_loading_metadata_instance = FlowSessionLoadingMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionLoadingMetadata.to_json())

# convert the object into a dict
flow_session_loading_metadata_dict = flow_session_loading_metadata_instance.to_dict()
# create an instance of FlowSessionLoadingMetadata from a dict
flow_session_loading_metadata_from_dict = FlowSessionLoadingMetadata.from_dict(flow_session_loading_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


