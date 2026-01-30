# ConfluencePageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**space_key** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.confluence_page_response import ConfluencePageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfluencePageResponse from a JSON string
confluence_page_response_instance = ConfluencePageResponse.from_json(json)
# print the JSON string representation of the object
print(ConfluencePageResponse.to_json())

# convert the object into a dict
confluence_page_response_dict = confluence_page_response_instance.to_dict()
# create an instance of ConfluencePageResponse from a dict
confluence_page_response_from_dict = ConfluencePageResponse.from_dict(confluence_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


