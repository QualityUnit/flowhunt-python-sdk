# FaqSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faq_id** | **str** | FAQ ID | [optional] 
**status** | [**FaqStatus**](FaqStatus.md) | Status | [optional] 
**cat_id** | **str** | Category ID | [optional] 
**question** | **str** | Question | [optional] 
**answer** | **str** | Answer | [optional] 
**parent_faq_id** | **str** | Parent FAQ ID | [optional] 
**faq_type** | [**FaqType**](FaqType.md) | FAQ Type | [optional] 
**limit** | **int** | Limit rows in result set | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.faq_search_request import FaqSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FaqSearchRequest from a JSON string
faq_search_request_instance = FaqSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FaqSearchRequest.to_json())

# convert the object into a dict
faq_search_request_dict = faq_search_request_instance.to_dict()
# create an instance of FaqSearchRequest from a dict
faq_search_request_from_dict = FaqSearchRequest.from_dict(faq_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


