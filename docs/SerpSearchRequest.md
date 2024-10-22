# SerpSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**query** | **str** | Query to search | 
**country** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**count_urls** | **int** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.serp_search_request import SerpSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpSearchRequest from a JSON string
serp_search_request_instance = SerpSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SerpSearchRequest.to_json())

# convert the object into a dict
serp_search_request_dict = serp_search_request_instance.to_dict()
# create an instance of SerpSearchRequest from a dict
serp_search_request_from_dict = SerpSearchRequest.from_dict(serp_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


