# ConfluencePagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[ConfluencePageResponse]**](ConfluencePageResponse.md) |  | 

## Example

```python
from flowhunt.models.confluence_pages_response import ConfluencePagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfluencePagesResponse from a JSON string
confluence_pages_response_instance = ConfluencePagesResponse.from_json(json)
# print the JSON string representation of the object
print(ConfluencePagesResponse.to_json())

# convert the object into a dict
confluence_pages_response_dict = confluence_pages_response_instance.to_dict()
# create an instance of ConfluencePagesResponse from a dict
confluence_pages_response_from_dict = ConfluencePagesResponse.from_dict(confluence_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


