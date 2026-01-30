# SerpSearchRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[SerpSearchRequest]**](SerpSearchRequest.md) | List of serp requests | 
**live_mode** | **bool** | Live mode | [optional] 

## Example

```python
from flowhunt.models.serp_search_requests import SerpSearchRequests

# TODO update the JSON string below
json = "{}"
# create an instance of SerpSearchRequests from a JSON string
serp_search_requests_instance = SerpSearchRequests.from_json(json)
# print the JSON string representation of the object
print(SerpSearchRequests.to_json())

# convert the object into a dict
serp_search_requests_dict = serp_search_requests_instance.to_dict()
# create an instance of SerpSearchRequests from a dict
serp_search_requests_from_dict = SerpSearchRequests.from_dict(serp_search_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


