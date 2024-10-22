# FaqCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cat_id** | **str** | Category ID | 
**primary_question** | **str** | Question | 
**answer** | **str** |  | [optional] 
**secondary_questions** | **List[str]** | Parent FAQ ID if current question points to other answer | [optional] [default to []]

## Example

```python
from flowhunt-python-sdk.models.faq_create_request import FaqCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FaqCreateRequest from a JSON string
faq_create_request_instance = FaqCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FaqCreateRequest.to_json())

# convert the object into a dict
faq_create_request_dict = faq_create_request_instance.to_dict()
# create an instance of FaqCreateRequest from a dict
faq_create_request_from_dict = FaqCreateRequest.from_dict(faq_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


