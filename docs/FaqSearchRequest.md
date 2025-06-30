# FaqSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faq_id** | **str** |  | [optional] 
**status** | [**FaqStatus**](FaqStatus.md) |  | [optional] 
**cat_id** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**answer** | **str** |  | [optional] 
**parent_faq_id** | **str** |  | [optional] 
**faq_type** | [**FaqType**](FaqType.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

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


