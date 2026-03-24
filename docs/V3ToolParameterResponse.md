# V3ToolParameterResponse

Response schema for a tool parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name | 
**display_name** | **str** | Display name for UI | 
**description** | **str** | Parameter description | [optional] [default to '']
**field_type** | **str** | V3 field type (e.g., &#39;str&#39;, &#39;int&#39;, &#39;dict&#39;) | 
**required** | **bool** | Whether the parameter is required | [optional] [default to False]
**default** | **object** |  | [optional] 
**options** | **List[str]** | Options for dropdown/select fields | [optional] 
**range_spec** | **Dict[str, object]** | Range spec for numeric inputs (min, max, step) | [optional] 
**multiline** | **bool** | Whether input is multiline | [optional] 
**input_type** | **str** | Input type class name (e.g., &#39;V3MultiselectInput&#39;) | [optional] 
**advanced** | **bool** | Whether this is an advanced parameter | [optional] 
**user_specified_param** | **bool** | If True, parameter must be set by user, not AI agent | [optional] [default to False]
**loading_options_api** | **str** | API endpoint for dynamic dropdown options | [optional] 
**grouped_options** | **Dict[str, List[str]]** | Grouped options for AI model dropdown fields | [optional] 
**exclusive_group** | **str** | Name of exclusive group this parameter belongs to | [optional] 
**exclusive_label** | **str** | Label shown in exclusive group selector | [optional] 
**exclusive_order** | **int** | Order within exclusive group | [optional] 
**exclusive_default** | **bool** | Whether this is the default option in exclusive group | [optional] 

## Example

```python
from flowhunt.models.v3_tool_parameter_response import V3ToolParameterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V3ToolParameterResponse from a JSON string
v3_tool_parameter_response_instance = V3ToolParameterResponse.from_json(json)
# print the JSON string representation of the object
print(V3ToolParameterResponse.to_json())

# convert the object into a dict
v3_tool_parameter_response_dict = v3_tool_parameter_response_instance.to_dict()
# create an instance of V3ToolParameterResponse from a dict
v3_tool_parameter_response_from_dict = V3ToolParameterResponse.from_dict(v3_tool_parameter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


