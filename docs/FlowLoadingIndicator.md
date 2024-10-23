# FlowLoadingIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name | 
**loading_desc** | **str** | Loading description | 
**icon** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.flow_loading_indicator import FlowLoadingIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of FlowLoadingIndicator from a JSON string
flow_loading_indicator_instance = FlowLoadingIndicator.from_json(json)
# print the JSON string representation of the object
print(FlowLoadingIndicator.to_json())

# convert the object into a dict
flow_loading_indicator_dict = flow_loading_indicator_instance.to_dict()
# create an instance of FlowLoadingIndicator from a dict
flow_loading_indicator_from_dict = FlowLoadingIndicator.from_dict(flow_loading_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


