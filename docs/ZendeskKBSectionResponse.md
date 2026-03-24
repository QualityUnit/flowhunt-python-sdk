# ZendeskKBSectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**locale** | **str** |  | 
**category_id** | **int** |  | [optional] 
**html_url** | **str** |  | 

## Example

```python
from flowhunt.models.zendesk_kb_section_response import ZendeskKBSectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZendeskKBSectionResponse from a JSON string
zendesk_kb_section_response_instance = ZendeskKBSectionResponse.from_json(json)
# print the JSON string representation of the object
print(ZendeskKBSectionResponse.to_json())

# convert the object into a dict
zendesk_kb_section_response_dict = zendesk_kb_section_response_instance.to_dict()
# create an instance of ZendeskKBSectionResponse from a dict
zendesk_kb_section_response_from_dict = ZendeskKBSectionResponse.from_dict(zendesk_kb_section_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


