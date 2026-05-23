# AIStudioFlowTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 
**flow_id** | **str** |  | 
**engine_version** | **str** |  | 
**category** | **str** |  | 
**tags** | **List[str]** |  | 
**aha_pick** | **bool** |  | 
**popular** | **bool** |  | 
**hire_count** | **int** |  | 
**rating** | **float** |  | 
**estimated_run_time_label** | **str** |  | 
**name** | **str** |  | 
**tagline** | **str** |  | 
**description** | **str** |  | 
**icon_emoji** | **str** |  | 
**icon_color_class** | **str** |  | 
**banner_style** | **str** |  | 
**inputs_summary** | **str** |  | 
**outputs_summary** | **str** |  | 
**integrations_for_card** | **List[str]** |  | 

## Example

```python
from flowhunt.models.ai_studio_flow_template_response import AIStudioFlowTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIStudioFlowTemplateResponse from a JSON string
ai_studio_flow_template_response_instance = AIStudioFlowTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(AIStudioFlowTemplateResponse.to_json())

# convert the object into a dict
ai_studio_flow_template_response_dict = ai_studio_flow_template_response_instance.to_dict()
# create an instance of AIStudioFlowTemplateResponse from a dict
ai_studio_flow_template_response_from_dict = AIStudioFlowTemplateResponse.from_dict(ai_studio_flow_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


