# FaqUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | [optional] 
**primary_question** | **str** | Question | [optional] 
**answer** | **str** | Answer formatted as markdow | [optional] 
**secondary_questions** | **List[str]** | Parent FAQ ID if current question points to other answer | [optional] [default to []]

## Example

```python
from flowhunt-python-sdk.models.faq_update_request import FaqUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FaqUpdateRequest from a JSON string
faq_update_request_instance = FaqUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FaqUpdateRequest.to_json())

# convert the object into a dict
faq_update_request_dict = faq_update_request_instance.to_dict()
# create an instance of FaqUpdateRequest from a dict
faq_update_request_from_dict = FaqUpdateRequest.from_dict(faq_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


