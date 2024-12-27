# Metadata

Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | Message | 
**tool_name** | **str** | Tool name | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**detailed_description** | **str** |  | [optional] 
**agent_query** | **str** | Search query | 
**tool_response** | **str** | Tool response | 
**task_name** | **str** |  | 
**task_input** | **str** |  | 
**agent** | **str** |  | 
**task_response** | **str** |  | 

## Example

```python
from flowhunt.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


