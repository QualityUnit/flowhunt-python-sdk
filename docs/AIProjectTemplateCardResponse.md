# AIProjectTemplateCardResponse

Slim shape used on the library catalog grid.

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
from flowhunt.models.ai_project_template_card_response import AIProjectTemplateCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIProjectTemplateCardResponse from a JSON string
ai_project_template_card_response_instance = AIProjectTemplateCardResponse.from_json(json)
# print the JSON string representation of the object
print(AIProjectTemplateCardResponse.to_json())

# convert the object into a dict
ai_project_template_card_response_dict = ai_project_template_card_response_instance.to_dict()
# create an instance of AIProjectTemplateCardResponse from a dict
ai_project_template_card_response_from_dict = AIProjectTemplateCardResponse.from_dict(ai_project_template_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


