# ZendeskKBCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**locale** | **str** |  | 
**html_url** | **str** |  | 

## Example

```python
from flowhunt.models.zendesk_kb_category_response import ZendeskKBCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZendeskKBCategoryResponse from a JSON string
zendesk_kb_category_response_instance = ZendeskKBCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(ZendeskKBCategoryResponse.to_json())

# convert the object into a dict
zendesk_kb_category_response_dict = zendesk_kb_category_response_instance.to_dict()
# create an instance of ZendeskKBCategoryResponse from a dict
zendesk_kb_category_response_from_dict = ZendeskKBCategoryResponse.from_dict(zendesk_kb_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


