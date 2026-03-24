# SerpClusterAddQueryRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[SerpClusterAddQueryRequest]**](SerpClusterAddQueryRequest.md) | List of serp requests | 

## Example

```python
from flowhunt.models.serp_cluster_add_query_requests import SerpClusterAddQueryRequests

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterAddQueryRequests from a JSON string
serp_cluster_add_query_requests_instance = SerpClusterAddQueryRequests.from_json(json)
# print the JSON string representation of the object
print(SerpClusterAddQueryRequests.to_json())

# convert the object into a dict
serp_cluster_add_query_requests_dict = serp_cluster_add_query_requests_instance.to_dict()
# create an instance of SerpClusterAddQueryRequests from a dict
serp_cluster_add_query_requests_from_dict = SerpClusterAddQueryRequests.from_dict(serp_cluster_add_query_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


