# SerpClusterAddQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** | The post back URL where to send the response in body | [optional] 
**queries** | [**List[SerpKeyword]**](SerpKeyword.md) | List of queries | 
**customer_id** | **str** | Customer ID of cluster | [optional] 
**campaign_id** | **str** | Campaign ID of cluster | [optional] 
**group_id** | **str** | Group ID of cluster - will be generated if not provided | [optional] 
**group_name** | **str** | Group name of cluster | [optional] [default to '']

## Example

```python
from flowhunt.models.serp_cluster_add_query_request import SerpClusterAddQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SerpClusterAddQueryRequest from a JSON string
serp_cluster_add_query_request_instance = SerpClusterAddQueryRequest.from_json(json)
# print the JSON string representation of the object
print(SerpClusterAddQueryRequest.to_json())

# convert the object into a dict
serp_cluster_add_query_request_dict = serp_cluster_add_query_request_instance.to_dict()
# create an instance of SerpClusterAddQueryRequest from a dict
serp_cluster_add_query_request_from_dict = SerpClusterAddQueryRequest.from_dict(serp_cluster_add_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


