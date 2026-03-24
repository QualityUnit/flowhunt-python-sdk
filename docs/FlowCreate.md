# FlowCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The agent name | 
**description** | **str** | The agent description | 
**detailed_description** | **str** | The agent detailed description | [optional] 
**config** | [**FlowConfig**](FlowConfig.md) | The agent configuration | 
**category_id** | **str** | The category ID | [optional] 
**engine_version** | [**FlowEngineVersion**](FlowEngineVersion.md) | The flow engine version (v2 or v3) | [optional] 
**try_flow_input_placeholder** | **str** | Custom placeholder text for the try_flow chat input | [optional] 
**disable_text_input** | **bool** | Disable the text input area in the chatbot for this flow | [optional] [default to False]

## Example

```python
from flowhunt.models.flow_create import FlowCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCreate from a JSON string
flow_create_instance = FlowCreate.from_json(json)
# print the JSON string representation of the object
print(FlowCreate.to_json())

# convert the object into a dict
flow_create_dict = flow_create_instance.to_dict()
# create an instance of FlowCreate from a dict
flow_create_from_dict = FlowCreate.from_dict(flow_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


