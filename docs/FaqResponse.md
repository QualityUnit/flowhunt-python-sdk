# FaqResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faq_id** | **str** | FAQ ID | 
**workspace_id** | **str** | Workspace ID | 
**cat_id** | **str** | Category ID | 
**question** | **str** | Question | 
**answer** | **str** | Answer formatted as markdown | [optional] 
**parent_faq_id** | **str** | Parent FAQ ID if current question points to other answer | [optional] 
**status** | [**FaqStatus**](FaqStatus.md) | FAQ status | 
**updated_at** | **datetime** | FAQ updated at | 
**indexed_at** | **datetime** | FAQ indexed at | [optional] 

## Example

```python
from flowhunt.models.faq_response import FaqResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FaqResponse from a JSON string
faq_response_instance = FaqResponse.from_json(json)
# print the JSON string representation of the object
print(FaqResponse.to_json())

# convert the object into a dict
faq_response_dict = faq_response_instance.to_dict()
# create an instance of FaqResponse from a dict
faq_response_from_dict = FaqResponse.from_dict(faq_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


