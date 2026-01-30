# V3ToolResponse

Response schema for a single tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | **str** | Internal step name (e.g., &#39;Separator&#39;) | 
**tool_name** | **str** | Tool name for AI agents (e.g., &#39;split_text&#39;) | 
**tool_description** | **str** | Tool description for AI agents | 
**display_name** | **str** | Display name for UI | 
**category** | **str** | Tool category (e.g., &#39;data_processing&#39;, &#39;airtable&#39;) | 
**icon** | **str** | Icon identifier | 
**beta** | **bool** | Whether this tool is in beta | [optional] [default to False]
**least_available_plan** | **str** | Minimum subscription plan: T/S/P/E | [optional] [default to 'T']
**is_hitl** | **bool** | Whether this tool requires human-in-the-loop approval | [optional] [default to False]
**parameters** | [**List[V3ToolParameterResponse]**](V3ToolParameterResponse.md) | Tool parameters | [optional] 
**exclusive_groups** | [**Dict[str, V3ExclusiveGroupResponse]**](V3ExclusiveGroupResponse.md) | Exclusive group definitions for this tool | [optional] 

## Example

```python
from flowhunt.models.v3_tool_response import V3ToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3ToolResponse from a JSON string
v3_tool_response_instance = V3ToolResponse.from_json(json)
# print the JSON string representation of the object
print(V3ToolResponse.to_json())

# convert the object into a dict
v3_tool_response_dict = v3_tool_response_instance.to_dict()
# create an instance of V3ToolResponse from a dict
v3_tool_response_from_dict = V3ToolResponse.from_dict(v3_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


