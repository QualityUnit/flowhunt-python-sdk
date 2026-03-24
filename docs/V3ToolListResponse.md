# V3ToolListResponse

Response schema for list of tools grouped by category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | **Dict[str, Dict[str, V3ToolResponse]]** | Tools grouped by category: {category: {step_name: tool}} | [optional] 
**count** | **int** | Total number of tools | 

## Example

```python
from flowhunt.models.v3_tool_list_response import V3ToolListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3ToolListResponse from a JSON string
v3_tool_list_response_instance = V3ToolListResponse.from_json(json)
# print the JSON string representation of the object
print(V3ToolListResponse.to_json())

# convert the object into a dict
v3_tool_list_response_dict = v3_tool_list_response_instance.to_dict()
# create an instance of V3ToolListResponse from a dict
v3_tool_list_response_from_dict = V3ToolListResponse.from_dict(v3_tool_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


