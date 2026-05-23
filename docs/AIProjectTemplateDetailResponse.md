# AIProjectTemplateDetailResponse

Detail shape — adds required-integration hints. Intentionally omits agents_spec and initial_issues to keep the payload small and avoid leaking the full team graph to clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 
**role** | **str** |  | 
**team_size_bucket** | **str** |  | 
**integrations_for_card** | **List[str]** |  | 
**tags** | **List[str]** |  | 
**aha_pick** | **bool** |  | 
**popular** | **bool** |  | 
**setup_time_label** | **str** |  | 
**hire_count** | **int** |  | 
**rating** | **float** |  | 
**name** | **str** |  | 
**tagline** | **str** |  | 
**description** | **str** |  | 
**icon_emoji** | **str** |  | 
**icon_color_class** | **str** |  | 
**banner_style** | **str** |  | 
**team_preview** | [**TeamPreview**](TeamPreview.md) |  | 
**required_integrations** | [**List[RequiredIntegration]**](RequiredIntegration.md) |  | 
**initial_periodic_issue** | [**InitialIssueSeed**](InitialIssueSeed.md) |  | 

## Example

```python
from flowhunt.models.ai_project_template_detail_response import AIProjectTemplateDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIProjectTemplateDetailResponse from a JSON string
ai_project_template_detail_response_instance = AIProjectTemplateDetailResponse.from_json(json)
# print the JSON string representation of the object
print(AIProjectTemplateDetailResponse.to_json())

# convert the object into a dict
ai_project_template_detail_response_dict = ai_project_template_detail_response_instance.to_dict()
# create an instance of AIProjectTemplateDetailResponse from a dict
ai_project_template_detail_response_from_dict = AIProjectTemplateDetailResponse.from_dict(ai_project_template_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


